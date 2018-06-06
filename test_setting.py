import unittest
from emr_setting import calculate_spark_settings


class TestSparkSettings(unittest.TestCase):
    def test_calc_spark_settings(self):
        ret, _ = calculate_spark_settings("c4.large", 4)
        self.assertDictEqual(
            ret, {
                'spark.executor.instances': "3",
                'spark.yarn.executor.memoryOverhead': "1024",
                'spark.executor.memory': "1G",
                'spark.yarn.driver.memoryOverhead': "1024",
                'spark.driver.memory': "1G",
                'spark.executor.cores': "1",
                'spark.driver.cores': "1",
                'spark.default.parallelism': "6"
            })

        ret, opt = calculate_spark_settings("c4.8xlarge", 4)
        self.assertDictEqual(
            ret, {
                'spark.executor.instances': "31",
                'spark.yarn.executor.memoryOverhead': "1024",
                'spark.executor.memory': "6G",
                'spark.yarn.driver.memoryOverhead': "1024",
                'spark.driver.memory': "6G",
                'spark.executor.cores': "4",
                'spark.driver.cores': "4",
                'spark.default.parallelism': "248"
            })
        self.assertDictEqual(
            opt, {
                'cores_executer': 4,
                'executor_per_node': 8,
                'mem_executer': 6,
                'overhead_mem': 1024,
                'sum': 6.0,
                'unused_cores': 3,
                'unused_mem': 3.0
            })
