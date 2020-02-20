import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
iowa_file_path = 'housesDataSet.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

iowa_model = DecisionTreeRegressor()

iowa_model.fit(X,y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())
print("==========================================================")

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
test_model = DecisionTreeRegressor()
test_model.fit(train_X,train_y)

print(test_model.predict(train_X.head()))
print(train_y.head().tolist())

print("=============================================================")
val_model = test_model.predict(val_X)
from sklearn.metrics import mean_absolute_error
print("MAE",mean_absolute_error(val_y,val_model))
print("==============================================================")
def get_min_mae(max_leaf_nodes,train_x,val_x,train_y,val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_x,train_y)
    preds_val = model.predict(val_x)
    print("MAE:",max_leaf_nodes," ",mean_absolute_error(val_y,preds_val))
for leaf_node in [5,50,500,5000]:
    get_min_mae(leaf_node,train_X,val_X,train_y,val_y)

