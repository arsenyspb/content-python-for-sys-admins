# Databricks notebook source
# MAGIC %md 
# MAGIC dbutils.fs.put("/FileStore/arseny/blah.txt", "blah")
# MAGIC https://docs.azuredatabricks.net/user-guide/advanced/filestore.html

# COMMAND ----------

spark.sparkContext

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended default.house_power_consumption