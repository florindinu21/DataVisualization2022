
pip install pyspark

from pyspark.sql import SparkSession

from pyspark.sql.functions import col,isnan, when, count

from pyspark.sql.types import StringType, StructField, StructType

from pyspark.ml.feature import StringIndexer, OneHotEncoder
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

!wget -q https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz

spark1 = SparkSession.builder.appName('Stroke').getOrCreate()

df = spark1.read.csv('/content/sample_data/final_dataset.csv',inferSchema=True,header=True)

df.printSchema()

df.show()

df.columns

df.count()

df.summary().show()

df.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns]
   ).show()

#string indexing

SI_gender= StringIndexer(inputCol='gender',outputCol='gender_index')
SI_ever_married= StringIndexer(inputCol='ever_married',outputCol='ever_married_index')
SI_work_type= StringIndexer(inputCol='work_type',outputCol='work_type_index')
SI_residence_type= StringIndexer(inputCol='Residence_type',outputCol='Residence_type_index')
SI_smoking_status= StringIndexer(inputCol='smoking_status',outputCol='smoking_status_index')
df= SI_gender.fit(df).transform(df)
df= SI_ever_married.fit(df).transform(df)
df= SI_work_type.fit(df).transform(df)
df= SI_residence_type.fit(df).transform(df)
df= SI_smoking_status.fit(df).transform(df)
df.select('gender', 'gender_index', 'ever_married', 'ever_married_index','work_type','work_type_index','Residence_type','Residence_type_index','smoking_status','smoking_status_index').show(10)

#classification

df= df.drop(df['gender'])
df=df.drop(df['ever_married'])
df=df.drop(df['work_type'])
df=df.drop(df['smoking_status'])
df=df.drop(df['Residence_type'])
df=df.drop(df['bmi'])

data =df.toPandas()
X = data.drop('stroke', axis=1)
y = data['stroke']
data.size

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
print(X_train.shape)

#tensorflow &neural network with 2 layers

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout

model = Sequential()
model.add(Dense(units=9, activation='relu', input_shape=(9,))) # First layer 
model.add(Dense(units=9, activation='relu')) # Second layer
model.add(Dense(units=1, activation='sigmoid')) # Output layer
model.summary()

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25)
history = model.fit(x=X_train, y=y_train,epochs=100,validation_data=(X_test, y_test), verbose=1, callbacks=[early_stop] )

print(type(history.history))

print(history.history['val_loss'][:5])
print(history.history['loss'][:5])

plt.plot(history.history['loss'], c='cornflowerblue', label='training loss')
plt.plot(history.history['val_loss'], c='goldenrod', label='validation loss')
plt.legend()
plt.xlabel('epochs')
plt.ylabel('loss');

model = Sequential()
model.add(Dense(units=9, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=9, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')
history = model.fit(x=X_train,  y=y_train,  epochs=200, validation_data=(X_test, y_test),  verbose=1, callbacks=[early_stop] )

plt.plot(history.history['loss'], c='cornflowerblue', label='training loss')
plt.plot(history.history['val_loss'], c='goldenrod', label='validation loss')
plt.legend()
plt.xlabel('epochs')
plt.ylabel('loss');