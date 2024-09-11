
# import pandas as pd

# print(pd._version_)

#_______________________________________________________________
# Required Tasks:
# 1. Read the data from the spreadsheet
# 2. Collect all of the sales from each month into a single list
# 3. Output the total sales across all months


#C:\Repos\Code\cfg-python_Kickstarter\CFG_session_1_VScode\Project\sales.csv
#C:\Repos\Code\cfg-python_Kickstarter\CFG_session_1_VScode\Project\Final.Project.Pandas.py



# 1. Read the data from the spreadsheet

# file_path = r'C:\Repos\Code\cfg-python_Kickstarter\CFG_session_1_VScode\Project'

import os
os.chdir(r"C:\Repos\Code\cfg-python_Kickstarter\CFG_session_1_VScode\Project")

print("Directory changed")



import pandas as pd                 # pd is a Pandas package

print(os.getcwd())                  # print the current working directory

df = pd.read_csv('sales.csv')       # read_csv() function does read the file and returns DataFrame
                                    # Pandas DataFrame (df) object.
                                    

print(df)                           # display the DataFrame



# 2. Collect all of the sales from each month into a single list

# Import pandas library as 'pd'
# Read the CSV file into a DataFrame:  pd.read_csv('sales.csv') 
# Extract the sales column and convert it to a list:  tolist() method to convert the sales column to a list.
# Print the sales list.

import pandas as pd
df = pd.read_csv('sales.csv')
sales_list = df['sales'].tolist()   #extract the sales column and convert it to a list
print(sales_list)




# 3. Output the total sales across all months

#sum the values in the 'sales' column using pandas:

# Import pandas:   'pd'
# Read the CSV file into a DataFrame:   'pd.read_csv()'
# Sum the sales column:    'sum()'
# Print the total sales.

import os
os.chdir(r"C:\Repos\Code\cfg-python_Kickstarter\CFG_session_1_VScode\Project")

print("Directory changed")

import pandas as pd

df = pd.read_csv('sales.csv')

total_sales = df['sales'].sum()

print('Total sales across all months:', total_sales)
