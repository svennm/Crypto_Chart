import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pvt(price_array, time_array):
	""" First parameter is for the price array and the second is for the time array"""
	plt.figure("Price of asset over time")
	plt.title("Price of asset over time")
	plt.plot(price_array, time_array)
	plt.ylabel("USD")
	plt.xlabel("DATES")
	plt.show()

def pvt_subcompare(assets_array):
	"""Compares multiple assets in one price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_begin = "The prices over time:"
	title_array = [title_begin]
	for assets_name in assets_array[0]:
		title_array.append(assets_name)
	title = pd.Series(title_array)
	title = title.str.cat(sep=" ")
	
	#creates new figure and inputs the title
	plt.figure(title)
	plt.title(title)

	#dynamically subplots the data xs then ys in a nested for loop
	for i in range(number_of_assets):
		plt.subplot(number_of_assets, 1, i + 1)
		plt.title(assets_array[0][i])
		plt.ylabel('Price (USD)')
		plt.xlabel('Time (months)')
		plt.plot(assets_array[1][i], assets_array[2][i])

	#displays the plot
	plt.show()

def pvt_figcompare(assets_array):
	"""Compares multiple assets in multiple price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_begin = "The prices over time:"
	title_array = [title_begin]
	count = 0
	for assets_name in assets_array[0]:
		title = title_begin + " " + assets_name
	
		#creates new figure and inputs the title
		plt.figure(title)
		plt.title(title)
		plt.ylabel('Price (USD)')
		plt.xlabel('Time (months)')
		plt.plot(assets_array[1][count], assets_array[2][count])
		count = count + 1

	#displays the plot
	plt.show()

x = [3,4,4,5,5,5,9,5,5,9,6,6,6,6]
x2 = np.cos(x)
y = np.sin(x)
y2 = np.tan(x)

xs = [x, x2, x]
ys = [y, y2, y]
names = ["BTC" , "ETC", "USD"]
assets_array = [ names , xs, ys]

pvt( x, y)
pvt_subcompare(assets_array)
pvt_figcompare(assets_array)