#Introduction To The Data
#Reading csv file and convert DATE column to series of datetime values:
import pandas as pd
unrate=pd.read_csv('unrate.csv')
unrate['DATE']=pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

#Introduction to Matplotlib
import matplotlib.pyplot as plt
plt.plot()
plt.show()
#Adding Data
#Generate a line chart that visualizes the unemployment rates from 1948 i.e. first 12 values
#x=unrate['DATE'].head(12)
#y=unrate['VALUE'].head(12)
plt.plot(unrate['DATE'],unrate['VALUE'])
plt.show()
#Fixing Axis Ticks
x=unrate['DATE'].head(12)
y=unrate['VALUE'].head(12)
plt.plot(x,y)
plt.xticks(rotation=90)		#rotate the x-axis tick labels by 90 degrees
plt.show()
#Adding Axis Labels And A Title
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()