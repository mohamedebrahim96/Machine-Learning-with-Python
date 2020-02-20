import pandas as pd 

# Load data
melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)

# print("Making predictions for the following 5 houses:")
# print(X.head())
# print("The predictions are")
# print(melbourne_model.predict(X.head()))


#==========================================================
#how to get absolute error 
from sklearn.metrics import mean_absolute_error
predicted_home_prices = melbourne_model.predict(X)
print("absolute error")
print(mean_absolute_error(y, predicted_home_prices))
#==========================================================
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)
# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print("validation data")
print(mean_absolute_error(val_y, val_predictions))



