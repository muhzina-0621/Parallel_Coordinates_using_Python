# import packages
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# read data from excel
file_path = 'data2.xlsx'  # replace with your Excel file path
sheet_name = 'data1'  # replace with your sheet name if necessary

try:
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # print column names to debug
    print("Columns in the dataset:", data.columns)
    
    # Assuming the Excel file has columns 'Age', 'Salary', 'Qualifications'
    # Create a new DataFrame with these columns and a category column for color coding
    df = data[['Age', 'Salary', 'Qualifications']]
    
    # Add a categorical column for parallel coordinates coloring (e.g., based on Qualifications)
    # Here we'll assume that 'Qualifications' can serve as a category
    # You may need to modify this part based on your actual data
    df['Category'] = pd.cut(df['Qualifications'], bins=3, labels=['Low', 'Medium', 'High'])

    # Plot parallel coordinates
    plt.figure(figsize=(10, 6))
    parallel_coordinates(df, 'Category', cols=['Age', 'Salary'], color=('#556270', '#4ECDC4', '#C7F464'))
    
    # Set plot title and labels
    plt.title('Parallel Coordinates Plot')
    plt.xlabel('Attributes')
    plt.ylabel('Values')
    
    # Show plot
    plt.show()

except KeyError as e:
    print(f"KeyError: {e}. Please check the column names in your Excel file.")
except Exception as e:
    print(f"An error occurred: {e}")
