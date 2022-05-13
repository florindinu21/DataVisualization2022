!pip install pyspark
!wget -q https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

import DataInit

spark1 = SparkSession.builder.appName('Stroke').getOrCreate()

data_frame = DataInit.get_data_frame(spark1)

data_frame.count()

DataInit.data_summary_show(data_frame)

clean_data_frame = DataInit.data_cleaning(data_frame, spark1)

clean_data_frame.count()

#TODO: plot on cleaned up data