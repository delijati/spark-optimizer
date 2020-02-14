Try:

from https://blog.clairvoyantsoft.com/improving-your-apache-spark-application-performance-e51e06339baa

Set the spark.sql.shuffle.partitions Configuration Parameter

The default value for this is 200 which can be too high for some jobs. Set this configuration to the number of cores you have available across all your executors.

spark.conf.set("spark.sql.shuffle.partitions", 10)

Also try:

https://stackoverflow.com/questions/39381041/determining-optimal-number-of-spark-partitions-based-on-workers-cores-and-dataf

'rule of thumb' is: numPartitions = numWorkerNodes * numCpuCoresPerWorker
h
or even 

rule of thumb you could rely on the product of #executors by #executor.cores, and then multiply that by 3 or 4. Of course this is a heuristic. In pyspark it would look like this:

sc = SparkContext(appName = "smeeb-App")
total_cores = int(sc._conf.get('spark.executor.instances')) * int(sc._conf.get('spark.executor.cores'))
dataset = sc.textFile(input_path, total_cores * 3)
