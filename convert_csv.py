#Using this script to convert a CSV file into an HTML file so that I can use the HTML file as the data source for the Bootstrap "Responsive Tables" component
import pandas as pd

sourceCSV = "Resources/cities.csv"
df = pd.read_csv(sourceCSV)
df.set_index('City_ID', inplace=True)

df.to_html("Resources/cities.html")