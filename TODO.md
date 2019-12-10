Try:
from https://blog.clairvoyantsoft.com/improving-your-apache-spark-application-performance-e51e06339baa

Set the spark.sql.shuffle.partitions Configuration Parameter

The default value for this is 200 which can be too high for some jobs. Set this configuration to the number of cores you have available across all your executors.

spark.conf.set("spark.sql.shuffle.partitions", 10)
