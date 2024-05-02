import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Step 1: Fetch the HTML content of the webpage
url = "https://es.wikipedia.org/wiki/Leucocito"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html")

# Step 3: Find a table elements in the parsed HTML
table = soup.find("table", class_= "wikitable")

# Create a DataFrame
wikitable = pd.DataFrame(columns=["Tipo", "Porcentaje aproximado en adultos"])

for row in table.find_all("tr"):
    cell = row.find_all("td")
    if (cell != []):
        Tipo = cell[0].text
        Porcentaje_aproximado_en_adultos = cell[3].text
        if "%" in Porcentaje_aproximado_en_adultos:
            wikitable = wikitable.append({"Tipo": Tipo, "Porcentaje aproximado en adultos": Porcentaje_aproximado_en_adultos}, ignore_index = True)

print(wikitable)

#Step 5: 
#Store the data in sqlite
connection = sqlite3.connect("wikitable")
connection.execute("DROP TABLE wikitable")

#Create a table
cursor = connection.cursor()
connection.execute("""CREATE TABLE wikitable (
               Tipo TEXT NOT NULL, 
               Porcentaje aproximado en adultos TEXT NOT NULL
               );""")

#Insert the values
connection.execute("""INSERT INTO wikitable VALUES ("Neutrófilo", "62%")""")
connection.execute("""INSERT INTO wikitable VALUES ("Eosinófilo", "2.3%")""")
connection.execute("""INSERT INTO wikitable VALUES ("Basófilo", "0.4%")""")
connection.execute("""INSERT INTO wikitable VALUES ("Linfocito", "30%")""")
connection.execute("""INSERT INTO wikitable VALUES ("Monocito", "5.3%")""")


#Almacena (commit) los cambios
connection.commit()

#SELECT
result_dataFrame = pd.read_sql("Select * from wikitable;", connection)
print(result_dataFrame)

#Step 6: Visualize the data
