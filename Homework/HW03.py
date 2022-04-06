import numpy as np
import pandas as pd

def spring_weather(temperatures, minTemp, maxTemp):
	return np.mean(temperatures[(temperatures >= minTemp) & (temperatures < maxTemp)])

def random_sale(items, cost, tax, discount, budget):
	return items[(cost * (1 + tax) - discount) < budget]

def no_null(data):
	return np.array([(np.mean(data[~np.isnan(data)]) if np.isnan(num) else num) for num in data])

def wordle(player1, player2):
	return np.min(player1.sum(axis = 1)) < np.min(player2.sum(axis = 1))

def csv_parser(filename):
	return pd.read_csv(filename)

def add_new_col_1(df):
	df["score"] = round((-1/30000) * df["mileage"] + (df["year"] / 2022), 3)
	return df

def add_new_col_2(df):
	df["relative_price"] = [str(int(price - df["price"].mean())) if ((brand in ["chevrolet", "dodge", "ford"]) and (color in ["silver", "blue"]) and ("days" in time)) else "Not Interested" for price, brand, color, time in zip(df["price"], df["brand"], df["color"], df["bidding_time"])]
	return df

def year_data(df):
	return df.groupby(['brand', 'model']).agg({"year":"count"})

def cannot_a_ford(df):
	return df[df['brand'] == 'ford'].groupby('year').agg({'price':'mean'}).astype({'price':np.int})
	
def export_excel(df, filename, sheetname):
	writer = pd.ExcelWriter(filename)
	df.to_excel(writer, sheet_name = sheetname)
	writer.save()




if __name__ == "__main__":
	#Q1
	temperatures = np.array([[70, 85, 58, 61, 68, 80, 77],
						[68, 78, 64, 70, 43, 77, 59]])
	# print(spring_weather(temperatures, 60, 80))

	temperatures = np.array([[72, 81, 55, 56, 86, 53, 75],
						[71, 79, 79, 82, 87, 70, 69],
						[74, 49, 77, 88, 91, 76, 88]])
	# print(spring_weather(temperatures, 70, 85))

	#Q2
	items = np.array(['apple pie', 
		"ben and jerry's mint chocolate chunk", 
		'root beer float', 
		'tiramisu', 
		'cannoli',
		"trader joe's coffee ice cream", 
		'chocolate chip cookie',
		'oatmeal raisin cookie'])
	cost = np.array([15, 6, 6, 12, 7, 7, 6, 6])
	tax = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
	discount = np.array([2,3,2,1,0,1,2,3])
	# print(random_sale(items, cost, tax, discount, 5))

	#Q3
	data = np.array([92, np.nan, 99, np.nan, np.nan, 80, np.nan, 100, np.nan, 78])
	# print(no_null(data))
	data = np.array([84, 270, 94, np.nan, np.nan, 82, np.nan, 100, np.nan, 18])
	# print(no_null(data))
	
	#Q4
	player1 = np.array([[4,4,4,2,6,6,6],
					[3,2,5,5,5,2,2],
					[1,2,1,5,4,3,3]])
	player2 = np.array([[6,2,3,3,5,4,6],
						[5,3,3,2,1,4,2],
						[1,5,4,3,6,2,4]])
	# print(wordle(player1, player2))

	#Q5
	df = csv_parser("cars.csv")
	# print(df)
	# print(df.shape)


	#Q6
	df = csv_parser("cars.csv")
	df2 = add_new_col_1(df)
	# print(df2)

	#Q7
	df = csv_parser("cars.csv")
	df3 = add_new_col_2(df)
	# print(df3)
	# print(len(df3[df3["relative_price"] != "Not Interested"]) )

	#Q8
	df = csv_parser("cars.csv")
	df4 = year_data(df)
	# pd.set_option('display.max_rows', df4.shape[0]+1)
	# print(df4)
	# print(df4.shape)

	#Q9
	df = csv_parser("cars.csv")
	# print(cannot_a_ford(df))

	#Q10
	df = csv_parser("cars.csv")
	# export_excel(df, "car_stats.xlsx", "Car Stats")



