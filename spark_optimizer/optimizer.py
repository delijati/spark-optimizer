import os
import math

import yaml


def plot(max_executor, ret):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.DataFrame(dict(x=np.arange(1, max_executor)))
    df["unused_memory_per_node"] = np.floor(45 / df.x)
    # df = df.drop(df[<some boolean condition>].index)
    df = pd.DataFrame(ret)
    df[['unused_cores', 'unused_mem']].plot()
    plt.show()
    normalized_df = (df - df.mean()) / df.std()
    # normalized_df = (df-df.min())/(df.max()-df.min())
    normalized_df[['unused_cores', 'unused_mem']].plot()
    plt.show()
    df[['sum']].plot()
    plt.show()


def calculate_spark_settings(instance_type, num_slaves, max_executor=192):
    """
    More info:

    http://c2fo.io/c2fo/spark/aws/emr/2016/07/06/apache-spark-config-cheatsheet/
    """
    root = os.path.dirname(os.path.abspath(__file__))
    FILE = os.path.join(root, "emr_instance.yaml")
    with open(FILE) as f:
        all_instances = yaml.load(f)
    inst = all_instances[instance_type]

    memory_overhead_coefficient = 0.15
    executor_memory_upper_bound = 64
    executor_core_upper_bound = 5
    available_memory = inst["memory"] - 1
    available_cpu = inst["cpu"] - 1
    parallelism_per_core = 2

    ret = []

    for x in range(1, max_executor):
        total_memory_per_executor = math.floor(available_memory / x)
        unused_memory_per_node = available_memory - (
            x * total_memory_per_executor)
        total_core_per_executor = available_cpu / x
        unused_cores_per_node = available_cpu - (
            x * math.floor(total_core_per_executor))
        overhead_mem = total_memory_per_executor * memory_overhead_coefficient
        mem_executer = total_memory_per_executor - overhead_mem
        cores_executer = math.floor(available_cpu / x)

        if (total_memory_per_executor < executor_memory_upper_bound and
                total_core_per_executor < executor_core_upper_bound):
            ret.append({
                "executor_per_node": x,
                "overhead_mem": max(overhead_mem * 1024, 384),
                "unused_cores": unused_cores_per_node,
                "mem_executer": mem_executer,
                "cores_executer": cores_executer,
                "unused_mem": unused_memory_per_node,
                "sum": unused_cores_per_node + unused_memory_per_node
            })

    val, idx = min(
        (val, idx) for (idx, val) in enumerate([x["sum"] for x in ret]))

    # plot(max_executor, ret)

    opt = ret[idx]
    executer_instances = (opt["executor_per_node"] * num_slaves) - 1
    parallelism = (
        executer_instances * opt["cores_executer"] * parallelism_per_core)

    ret = {
        "spark.executor.instances": str(executer_instances),
        "spark.executor.memoryOverhead": "%sm" % int(opt["overhead_mem"]),
        "spark.executor.memory": "%sm" % int(opt["mem_executer"] * 1024),
        "spark.driver.memoryOverhead": "%sm" % int(opt["overhead_mem"]),
        "spark.driver.memory": "%sm" % int(opt["mem_executer"] * 1024),
        "spark.driver.maxResultSize": "%sm" % int(opt["mem_executer"] * 1024),
        "spark.executor.cores": str(int(opt["cores_executer"])),
        "spark.driver.cores": str(int(opt["cores_executer"])),
        "spark.default.parallelism": str(int(parallelism)),
    }

    return ret, opt
