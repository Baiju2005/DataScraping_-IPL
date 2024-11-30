# -*- coding: utf-8 -*-
"""IPL_selenium_Scraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GlsTtuwKE1B_DoGprwdPdWwVK9-nGlmU
"""

!pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
import time

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

driver = web_driver()

driver.get("https://www.iplt20.com/stats/2024")

view_all = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/div/a")

time.sleep(7)
view_all.click()

Name = []
Team = []
Runs = []
AVG = []
SR = []
Century = []
Fifty = []
Fours = []
Six = []



for i in range(2,169):
  name = driver.find_element('xpath', '/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[2]/div/a/div[1]'.format(i)).text
  Name.append(name)


  team = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[2]/div/a/div[2]".format(i)).text
  Team.append(team)

  runs = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[3]".format(i)).text
  Runs.append(runs)


  avg = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[8]".format(i)).text
  AVG.append(avg)

  sr = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[10]".format(i)).text
  SR.append(sr)

  century = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[11]".format(i)).text
  Century.append(century)

  fifty = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[12]".format(i)).text
  Fifty.append(fifty)

  fours = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[13]".format(i)).text
  Fours.append(fours)

  six = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[{0}]/td[14]".format(i)).text
  Six.append(six)

import pandas as pd

data = pd.DataFrame({"Names": Name, "Team": Team, "Runs": Runs, "AVG": AVG, "SR": SR, "Century": Century, "Fifty": Fifty, "Fours": Fours, "Six": Six})

data

data.to_csv("IPL_2024.csv")

"""# **EDA & Visualization**"""

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

data = pd.read_csv('/content/IPL_2024.csv')

data.head(10)

"""# **Top Bstsman**"""

top_batsman_by_team = data.loc[data.groupby('Team')['Runs'].idxmax()]

plt.figure(figsize=(10, 6))

sns.barplot(x='Team', y='Runs', data=top_batsman_by_team, palette='viridis')


plt.title('Top Batsman by Team - IPL 2024', fontsize=15)
plt.xlabel('Team', fontsize=13)
plt.ylabel('Runs', fontsize=13)
plt.xticks(rotation=45, ha='right')

plt.show()

"""# **Top Runs**"""

Top_runs = data[['Names', 'Team', 'Runs']].sort_values(by=['Runs'], ascending=False).head()

plt.figure(figsize=(8, 5))

Top_runs.plot(kind='bar', x='Names', y='Runs', color='#00BFFF')
plt.xlabel('Names')
plt.ylabel('Runs')
plt.title('Top 5 Runs')
plt.xticks(rotation=45)
plt.show()

"""# **Top Sixes**"""

Top_six = data[['Names', 'Team' ,'Six']].sort_values(by=['Six'], ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.bar(Top_six['Names'], Top_six['Six'], color="#00BFFF")
plt.xlabel('Names')
plt.ylabel('Sixes')
plt.title('Top 5 Sixes')
plt.xticks(rotation=45)
plt.show()

"""# **Top Four**"""

Top_fours = data[['Names' ,'Fours']].sort_values(by=['Fours'], ascending=False).head(5)

plt.figure(figsize=(8, 5))

plt.bar(Top_fours['Names'], Top_fours['Fours'], color="#00BFFF")
plt.xlabel('Names')
plt.ylabel('Fours')
plt.title('Top 5 Fours')
plt.xticks(rotation=45)
plt.show()

"""# **Top 50**"""

Top_fifty = data[['Names', 'Fifty']].sort_values(by=['Fifty'], ascending=False).head()

plt.figure(figsize=(8, 5))

plt.bar(Top_fifty['Names'], Top_fifty['Fifty'], color="#00BFFF")
plt.xlabel('Names')
plt.ylabel('Fifty')
plt.title('Top Fifty')
plt.xticks(rotation=45)
plt.show()