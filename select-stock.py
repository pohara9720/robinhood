import json

# Only stocks with a dollar change of $1.50 or more should be considered
def dollar_change_filter(variable):
    is_high = variable > 150

# Only stocks with a percentage change of 3% or more should be considered
def dollar_change_filter(variable):
    is_high = variable > '3%'

# Only stocks with a high volume should be considered
def volume_filter(variable):
    is_high = variable > 100000

def select_stock(data):
    dollar_change_is_high = filter(dollar_change_filter,data)
    percentage_change_is_high = filter(percent_change_filter,data)
    volume_is_high = filter(volume_filter,data)
        

with open('stock_data.json') as json_file:
    data = json.load(json_file)
    stock_data = data['stocks']

    
