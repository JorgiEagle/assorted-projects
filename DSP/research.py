import requests
from bs4 import BeautifulSoup
import pandas as pd

source = "https://dyson-sphere-program.fandom.com/wiki/Research"

page = requests.get(source)

soup = BeautifulSoup(page.text, "html.parser")

technologies_table = soup.find("table")

df = pd.read_html(technologies_table)


print(df)