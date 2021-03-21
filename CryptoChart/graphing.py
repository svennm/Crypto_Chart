import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graph(price_array, time_array, graphtitle = "Price of asset over time",  yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	""" First parameter is for the price array and the second is for the time array"""
	fig = plt.figure(graphtitle)
	#sets the background of the plot to trasparent
	fig.patch.set_alpha(0.0)
	ax = plt.axes()
	ax.patch.set_alpha(0.0)
	plt.title(graphtitle)
	plt.plot(price_array, time_array)
	plt.ylabel(yaxistitle)
	plt.xlabel(xaxistitle)
	plt.show()

def subcompare(assets_array, subplot_title = "The prices over time:", yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	"""Compares multiple assets in one price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_array = [subplot_title]
	for assets_name in assets_array[0]:
		title_array.append(assets_name)
	title = pd.Series(title_array)
	title = title.str.cat(sep=" ")
	
	#creates new transparent figure and inputs the title
	fig = plt.figure(title)
	fig.patch.set_alpha(0.0)
	plt.title(title)

	#dynamically determine which subplot figuration is best based on the number of assets 
	if(number_of_assets % 2 == 0 and number_of_assets >= 4):
		#dynamically subplots the data xs then ys in a nested for loop
		num_of_rows = int(number_of_assets / 2)
		num_of_cols = int(number_of_assets / 2)
		for i in range(number_of_assets):
			ax = plt.subplot(num_of_rows, num_of_cols, i + 1)
			#sets the background of the plot to trasparent
			ax.patch.set_alpha(0.0)
			plt.title(assets_array[0][i])
			plt.ylabel(yaxistitle)
			plt.xlabel(xaxistitle)
			plt.plot(assets_array[1][i], assets_array[2][i])
	else:
		#dynamically subplots the data xs then ys in a nested for loop
		num_of_rows = number_of_assets
		for i in range(number_of_assets):
			ax = plt.subplot(num_of_rows, 1, i + 1)
			#sets the background of the plot to trasparent
			ax.patch.set_alpha(0.0)
			plt.title(assets_array[0][i])
			plt.ylabel(yaxistitle)
			plt.xlabel(xaxistitle)
			plt.plot(assets_array[1][i], assets_array[2][i])

	#displays the plot
	plt.show()

def figcompare(assets_array, figure_title =  "The prices over time:\n", yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	"""Compares multiple assets in multiple price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_array = [figure_title]
	count = 0
	for assets_name in assets_array[0]:
		title = figure_title + " " + assets_name
	
		#creates new transparent figure and inputs the title
		fig = plt.figure(title)
		fig.patch.set_alpha(0.0)
		ax = plt.axes()
		ax.patch.set_alpha(0.0)
		
		plt.title(title)
		plt.ylabel(yaxistitle)
		plt.xlabel(xaxistitle)
		plt.plot(assets_array[1][count], assets_array[2][count])
		count = count + 1

	#displays the plot
	plt.show()

def graphcompare(assets_array, figure_title =  "The prices over time:\n", yaxistitle = 'Price (USD)', xaxistitle = 'Time (months)'):
	"""Compares multiple assets in one price over time graph. (Parameter: Expects a Matrix)"""
	number_of_assets = len(assets_array[0])

	#Dynamically creates the title and adds in all the assets to it
	title_array = [figure_title]
	for assets_name in assets_array[0]:
		title_array.append(assets_name)
	title = pd.Series(title_array)
	title = title.str.cat(sep=" ")

	#creates new transparent figure and inputs the title
	fig = plt.figure(title)
	fig.patch.set_alpha(0.0)
	ax = plt.axes()
	ax.patch.set_alpha(0.0)
	
	plt.title(title)
	plt.ylabel(yaxistitle)
	plt.xlabel(xaxistitle)
	
	for i in range(number_of_assets):
		asset_name = assets_array[0][i]
		plt.plot(assets_array[1][i], assets_array[2][i], label = asset_name)

	#displays the plot
	plt.legend(loc=2)
	plt.show()


""" # Testing code delete after use 
x = [3,4,4,5,5,5,9,5,5,9,6,6,6,6]
x2 = np.cos(x)
x3 = np.arctan(x)
x4 = [3,4,4,5,6,5,9,5,9,9,6,6,6,6]
y = np.sin(x)
y2 = np.tan(x)
y3 = np.sin(x)
y4 = [3,4,9,5,2,5,9,5,5,9,8,6,1,6]

xs = [x, x2, x]
ys = [y, y2, y]
names = ["BTC" , "ETC", "USD"]
assets_array = [ names , xs, ys]

names2= ["avy", "aapl"]
xs2 = [x,x2]
ys2 = [y,y2]
assets_array2 = [names2 , xs2 , ys2]

xs = [x, x2, x3, x4]
ys = [y, y2, y3, y4]
names = ["BTC" , "ETC", "USD", "USD_COIN"]
assets_array3 = [ names , xs, ys]

graph( x, y)
subcompare(assets_array2)
subcompare(assets_array3)
figcompare(assets_array)
graphcompare(assets_array3)
"""