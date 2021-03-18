import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pvt_plt(price_array, time_array):
	""" First parameter is for the price array and the second is for the time array"""
	plt.figure("Price of asset over time")
	plt.title("Price of asset over time")
	plt.plot(price_array, time_array)
	plt.ylabel("USD")
	plt.xlabel("DATES")
	plt.show()

def compare_pvt(assets_array):
	"""Compares multiple assets in a price over time graph"""
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
	#! This is not working err=> subplot arg is a int not a list {plot_index_y}
	for	plot_index_x in assets_array[1]:
		for plot_index_y in assets_array[2]:
			plt.subplot(number_of_assets, 1 , plot_index_y)
			plt.plot(assets_array[1][plot_index_x], assets_array[2][plot_index_y])

	#displays the plot
	plt.show()


x = [3,4,4,5,5,5,9,5,5,9,6,6,6,6]
x2 = np.cos(x)
y = np.sin(x)
y2 = np.tan(x)

xs = [x, x2]
ys = [y, y2]
names = ["BTC" , "ETC"]
assets_array = [ names , xs, ys]


compare_pvt(assets_array)


