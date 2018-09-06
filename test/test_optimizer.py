import unittest

from spark_optimizer.optimizer import calculate_spark_settings


class TestSparkSettings(unittest.TestCase):
    def test_calc_spark_settings(self):
        ret, _ = calculate_spark_settings("c4.large", 4)
        self.assertDictEqual(
            ret, {
                'spark.executor.instances': "3",
                'spark.executor.memoryOverhead': "384m",
                'spark.executor.memory': "1740m",
                'spark.driver.memoryOverhead': "384m",
                'spark.driver.memory': "1740m",
                'spark.driver.maxResultSize': '1740m',
                'spark.executor.cores': "1",
                'spark.driver.cores': "1",
                'spark.default.parallelism': "6"
            })

        ret, opt = calculate_spark_settings("c4.8xlarge", 4)
        self.assertDictEqual(
            ret, {
                'spark.executor.instances': "31",
                'spark.executor.memoryOverhead': "1075m",
                'spark.executor.memory': "6092m",
                'spark.driver.memoryOverhead': "1075m",
                'spark.driver.memory': "6092m",
                'spark.driver.maxResultSize': "6092m",
                'spark.executor.cores': "4",
                'spark.driver.cores': "4",
                'spark.default.parallelism': "248"
            })
