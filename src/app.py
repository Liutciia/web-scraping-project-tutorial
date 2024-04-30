import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns



#Step 1: Install dependencies - pip install pandas requests

#Step 2: Download HTML 
url = 'https://es.wikipedia.org/wiki/Leucocito'  
response = requests.get(url)
html_content = response.text

# Step 3: transform the HTML
soup = BeautifulSoup(html_content, 'html.parser')

tables = soup.find_all('table')






# Step 4: Extract data from each table and store it in a DataFrame
dfs = []
for table in tables:
    # Extract data from the table rows and cells
    data = []
    rows = table.find_all('tr')
    for row in rows:
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        data.append(row_data)
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data[1:], columns=data[0])
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Display the final DataFrame
print(final_df)
