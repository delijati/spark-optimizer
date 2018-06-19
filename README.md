# Spark-optimizer

Optimize spark settings (for cluster aka yarn run)

Original source: http://c2fo.io/c2fo/spark/aws/emr/2016/07/06/apache-spark-config-cheatsheet/

## Usage

Install:

    $ virtualenv env
    $ env/bin/pip install -c req.txt

Generate settings for `c4.4xlarge` with `4` nodes:

    $ env/bin/python emr_setting.py c4.4xlarge 4
    {'spark.default.parallelism': '108',
     'spark.driver.cores': '2',
     'spark.driver.memory': '3G',
     'spark.executor.cores': '2',
     'spark.executor.instances': '27',
     'spark.executor.memory': '3G',
     'spark.yarn.driver.memoryOverhead': '1024',
     'spark.yarn.executor.memoryOverhead': '1024'}


Update instance info:

    $ env/bin/python emr_update.py
