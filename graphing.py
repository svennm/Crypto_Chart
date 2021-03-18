import matplotlib.pyplot as plt
import numpy as np



def pvt_plt(price_array, time_array):
	""" First parameter is for the price array and the second is for the time array"""
	plt.figure("Price of asset over time")
	plt.title("Price of asset over time")
	plt.plot(price_array, time_array)
	plt.ylabel("USD")
	plt.xlabel("DATES")
	plt.show()

def compare_pvt(*create_asset):
	"""Compares multiple assets in a price over time graph"""
	num = len(create_asset)
	title = "Comparing the prices over time of "  #+ create_asset[0]
	plt.figure(title)
	plt.title(title)
	plt.plot(create_asset[1], create_asset[2])
	plt.show()
	print(num)


x = [3,4,4,5,5,5,9,5,5,9,6,6,6,6]
y = np.sin(x)
asset_array = ["BTC" , x , y]
#pvt_plt(x,y)
#compare_pvt(BTC)
print(asset_array[0])
print(asset_array[1])
print(asset_array[2])
