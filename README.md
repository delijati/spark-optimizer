
# Spark-optimizer

[![Build Status](https://api.travis-ci.org/delijati/spark-optimizer.svg?branch=master)](https://travis-ci.org/delijati/spark-optimizer)

Optimize spark settings (for cluster aka yarn run)

Original source: http://c2fo.io/c2fo/spark/aws/emr/2016/07/06/apache-spark-config-cheatsheet/

## Usage

Install:

    $ virtualenv env
    $ env/bin/pip install spark-optimizer

Dev install:

    $ virtualenv env
    $ env/bin/pip install -e .


Generate settings for `c4.4xlarge` with `4` nodes:

    $ env/bin/spark-optimizer c4.4xlarge 4
    {'spark.default.parallelism': '108',
     'spark.driver.cores': '2',
     'spark.driver.maxResultSize': '3481m',
     'spark.driver.memory': '3481m',
     'spark.driver.memoryOverhead': '614m',
     'spark.executor.cores': '2',
     'spark.executor.instances': '27',
     'spark.executor.memory': '3481m',
     'spark.executor.memoryOverhead': '614m'}

Update instance info:

    $ env/bin/python spark_optimizer/emr_update.py
