Web Scraping NBA Stats With Python: Data Project [Part 1 of 3]

* 3 part Machine Learning project, to try to predict who will be the MVP in a given MBA season and for that we need a lot of data about the players and their statistics.
So in this first part of the project, Web Sraping will be done to collect the various types of data and load them into Pandas to facilitate analysis.

Downloading MVP votes with requests


```python
years = list(range(1991,2022))
```


```python
url_start = "https://www.basketball-reference.com/awards/awards_{}.html"
```


```python
import requests

for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    
    with open("mvp/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(data.text)

```

Parsing the votes table with BeautifulSoup


```python
from bs4 import BeautifulSoup
```


```python
with open("mvp/1991.html", encoding="utf-8") as f:
    page = f.read()
```


```python
soup = BeautifulSoup(page, "html.parser")
```

BeautifulSoup found and remove header


```python
soup.find('tr', class_="over_header").decompose()
```

MVP table


```python
mvp_table = soup.find(id="mvp")
```


```python
import pandas as pd
```


```python
mvp_1991 = pd.read_html(str(mvp_table))[0]
```


```python
mvp_1991
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Player</th>
      <th>Age</th>
      <th>Tm</th>
      <th>First</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>G</th>
      <th>MP</th>
      <th>PTS</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>FG%</th>
      <th>3P%</th>
      <th>FT%</th>
      <th>WS</th>
      <th>WS/48</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Michael Jordan</td>
      <td>27</td>
      <td>CHI</td>
      <td>77.0</td>
      <td>891.0</td>
      <td>960</td>
      <td>0.928</td>
      <td>82</td>
      <td>37.0</td>
      <td>31.5</td>
      <td>6.0</td>
      <td>5.5</td>
      <td>2.7</td>
      <td>1.0</td>
      <td>0.539</td>
      <td>0.312</td>
      <td>0.851</td>
      <td>20.3</td>
      <td>0.321</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Magic Johnson</td>
      <td>31</td>
      <td>LAL</td>
      <td>10.0</td>
      <td>497.0</td>
      <td>960</td>
      <td>0.518</td>
      <td>79</td>
      <td>37.1</td>
      <td>19.4</td>
      <td>7.0</td>
      <td>12.5</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>0.477</td>
      <td>0.320</td>
      <td>0.906</td>
      <td>15.4</td>
      <td>0.251</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>David Robinson</td>
      <td>25</td>
      <td>SAS</td>
      <td>6.0</td>
      <td>476.0</td>
      <td>960</td>
      <td>0.496</td>
      <td>82</td>
      <td>37.7</td>
      <td>25.6</td>
      <td>13.0</td>
      <td>2.5</td>
      <td>1.5</td>
      <td>3.9</td>
      <td>0.552</td>
      <td>0.143</td>
      <td>0.762</td>
      <td>17.0</td>
      <td>0.264</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Charles Barkley</td>
      <td>27</td>
      <td>PHI</td>
      <td>2.0</td>
      <td>222.0</td>
      <td>960</td>
      <td>0.231</td>
      <td>67</td>
      <td>37.3</td>
      <td>27.6</td>
      <td>10.1</td>
      <td>4.2</td>
      <td>1.6</td>
      <td>0.5</td>
      <td>0.570</td>
      <td>0.284</td>
      <td>0.722</td>
      <td>13.4</td>
      <td>0.258</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Karl Malone</td>
      <td>27</td>
      <td>UTA</td>
      <td>0.0</td>
      <td>142.0</td>
      <td>960</td>
      <td>0.148</td>
      <td>82</td>
      <td>40.3</td>
      <td>29.0</td>
      <td>11.8</td>
      <td>3.3</td>
      <td>1.1</td>
      <td>1.0</td>
      <td>0.527</td>
      <td>0.286</td>
      <td>0.770</td>
      <td>15.5</td>
      <td>0.225</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Clyde Drexler</td>
      <td>28</td>
      <td>POR</td>
      <td>1.0</td>
      <td>75.0</td>
      <td>960</td>
      <td>0.078</td>
      <td>82</td>
      <td>34.8</td>
      <td>21.5</td>
      <td>6.7</td>
      <td>6.0</td>
      <td>1.8</td>
      <td>0.7</td>
      <td>0.482</td>
      <td>0.319</td>
      <td>0.794</td>
      <td>12.4</td>
      <td>0.209</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Kevin Johnson</td>
      <td>24</td>
      <td>PHO</td>
      <td>0.0</td>
      <td>32.0</td>
      <td>960</td>
      <td>0.033</td>
      <td>77</td>
      <td>36.0</td>
      <td>22.2</td>
      <td>3.5</td>
      <td>10.1</td>
      <td>2.1</td>
      <td>0.1</td>
      <td>0.516</td>
      <td>0.205</td>
      <td>0.843</td>
      <td>12.7</td>
      <td>0.220</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Dominique Wilkins</td>
      <td>31</td>
      <td>ATL</td>
      <td>0.0</td>
      <td>29.0</td>
      <td>960</td>
      <td>0.030</td>
      <td>81</td>
      <td>38.0</td>
      <td>25.9</td>
      <td>9.0</td>
      <td>3.3</td>
      <td>1.5</td>
      <td>0.8</td>
      <td>0.470</td>
      <td>0.341</td>
      <td>0.829</td>
      <td>11.4</td>
      <td>0.177</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9T</td>
      <td>Larry Bird</td>
      <td>34</td>
      <td>BOS</td>
      <td>0.0</td>
      <td>25.0</td>
      <td>960</td>
      <td>0.026</td>
      <td>60</td>
      <td>38.0</td>
      <td>19.4</td>
      <td>8.5</td>
      <td>7.2</td>
      <td>1.8</td>
      <td>1.0</td>
      <td>0.454</td>
      <td>0.389</td>
      <td>0.891</td>
      <td>6.6</td>
      <td>0.140</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9T</td>
      <td>Terry Porter</td>
      <td>27</td>
      <td>POR</td>
      <td>0.0</td>
      <td>25.0</td>
      <td>960</td>
      <td>0.026</td>
      <td>81</td>
      <td>32.9</td>
      <td>17.0</td>
      <td>3.5</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>0.1</td>
      <td>0.515</td>
      <td>0.415</td>
      <td>0.823</td>
      <td>13.0</td>
      <td>0.235</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Patrick Ewing</td>
      <td>28</td>
      <td>NYK</td>
      <td>0.0</td>
      <td>20.0</td>
      <td>960</td>
      <td>0.021</td>
      <td>81</td>
      <td>38.3</td>
      <td>26.6</td>
      <td>11.2</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>3.2</td>
      <td>0.514</td>
      <td>0.000</td>
      <td>0.745</td>
      <td>10.0</td>
      <td>0.155</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>John Stockton</td>
      <td>28</td>
      <td>UTA</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>960</td>
      <td>0.016</td>
      <td>82</td>
      <td>37.8</td>
      <td>17.2</td>
      <td>2.9</td>
      <td>14.2</td>
      <td>2.9</td>
      <td>0.2</td>
      <td>0.507</td>
      <td>0.345</td>
      <td>0.836</td>
      <td>14.0</td>
      <td>0.217</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Isiah Thomas</td>
      <td>29</td>
      <td>DET</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>960</td>
      <td>0.011</td>
      <td>48</td>
      <td>34.5</td>
      <td>16.2</td>
      <td>3.3</td>
      <td>9.3</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>0.435</td>
      <td>0.292</td>
      <td>0.782</td>
      <td>3.4</td>
      <td>0.098</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Robert Parish</td>
      <td>37</td>
      <td>BOS</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>960</td>
      <td>0.010</td>
      <td>81</td>
      <td>30.1</td>
      <td>14.9</td>
      <td>10.6</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>1.3</td>
      <td>0.598</td>
      <td>0.000</td>
      <td>0.767</td>
      <td>10.0</td>
      <td>0.198</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Joe Dumars</td>
      <td>27</td>
      <td>DET</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>960</td>
      <td>0.008</td>
      <td>80</td>
      <td>38.1</td>
      <td>20.4</td>
      <td>2.3</td>
      <td>5.5</td>
      <td>1.1</td>
      <td>0.1</td>
      <td>0.481</td>
      <td>0.311</td>
      <td>0.890</td>
      <td>9.9</td>
      <td>0.155</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>Bernard King</td>
      <td>34</td>
      <td>WSB</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>960</td>
      <td>0.007</td>
      <td>64</td>
      <td>37.5</td>
      <td>28.4</td>
      <td>5.0</td>
      <td>4.6</td>
      <td>0.9</td>
      <td>0.3</td>
      <td>0.472</td>
      <td>0.216</td>
      <td>0.790</td>
      <td>3.5</td>
      <td>0.070</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>Kenny Smith</td>
      <td>25</td>
      <td>HOU</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>960</td>
      <td>0.005</td>
      <td>78</td>
      <td>34.6</td>
      <td>17.7</td>
      <td>2.1</td>
      <td>7.1</td>
      <td>1.4</td>
      <td>0.1</td>
      <td>0.520</td>
      <td>0.363</td>
      <td>0.844</td>
      <td>9.0</td>
      <td>0.161</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>Hakeem Olajuwon</td>
      <td>28</td>
      <td>HOU</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>960</td>
      <td>0.004</td>
      <td>56</td>
      <td>36.8</td>
      <td>21.2</td>
      <td>13.8</td>
      <td>2.3</td>
      <td>2.2</td>
      <td>3.9</td>
      <td>0.508</td>
      <td>0.000</td>
      <td>0.769</td>
      <td>8.6</td>
      <td>0.201</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19T</td>
      <td>Tim Hardaway</td>
      <td>24</td>
      <td>GSW</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>960</td>
      <td>0.001</td>
      <td>82</td>
      <td>39.2</td>
      <td>22.9</td>
      <td>4.0</td>
      <td>9.7</td>
      <td>2.6</td>
      <td>0.1</td>
      <td>0.476</td>
      <td>0.385</td>
      <td>0.803</td>
      <td>9.9</td>
      <td>0.148</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19T</td>
      <td>Kevin McHale</td>
      <td>33</td>
      <td>BOS</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>960</td>
      <td>0.001</td>
      <td>68</td>
      <td>30.4</td>
      <td>18.4</td>
      <td>7.1</td>
      <td>1.9</td>
      <td>0.4</td>
      <td>2.1</td>
      <td>0.553</td>
      <td>0.405</td>
      <td>0.829</td>
      <td>7.9</td>
      <td>0.182</td>
    </tr>
  </tbody>
</table>
</div>



A look at the pages we'll scrape


```python
dfs = []
for year in years:
    with open("mvp/1991.html", encoding="utf-8".format(year)) as f:
        page = f.read()
    
    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="over_header").decompose()
    mvp_table = soup.find(id="mvp")
    mvp = pd.read_html(str(mvp_table))[0]
    mvp["Year"] = year
    
    dfs.append(mvp)
   
    
   
```

Combine MVP votes with pandas


```python
mvps = pd.concat(dfs)
```

Combining data from multiple web pages, we now have a data frame with all MVP votes from every year from 1991 to 2021


```python
mvps.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Player</th>
      <th>Age</th>
      <th>Tm</th>
      <th>First</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>G</th>
      <th>MP</th>
      <th>...</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>FG%</th>
      <th>3P%</th>
      <th>FT%</th>
      <th>WS</th>
      <th>WS/48</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Michael Jordan</td>
      <td>27</td>
      <td>CHI</td>
      <td>77.0</td>
      <td>891.0</td>
      <td>960</td>
      <td>0.928</td>
      <td>82</td>
      <td>37.0</td>
      <td>...</td>
      <td>6.0</td>
      <td>5.5</td>
      <td>2.7</td>
      <td>1.0</td>
      <td>0.539</td>
      <td>0.312</td>
      <td>0.851</td>
      <td>20.3</td>
      <td>0.321</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Magic Johnson</td>
      <td>31</td>
      <td>LAL</td>
      <td>10.0</td>
      <td>497.0</td>
      <td>960</td>
      <td>0.518</td>
      <td>79</td>
      <td>37.1</td>
      <td>...</td>
      <td>7.0</td>
      <td>12.5</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>0.477</td>
      <td>0.320</td>
      <td>0.906</td>
      <td>15.4</td>
      <td>0.251</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>David Robinson</td>
      <td>25</td>
      <td>SAS</td>
      <td>6.0</td>
      <td>476.0</td>
      <td>960</td>
      <td>0.496</td>
      <td>82</td>
      <td>37.7</td>
      <td>...</td>
      <td>13.0</td>
      <td>2.5</td>
      <td>1.5</td>
      <td>3.9</td>
      <td>0.552</td>
      <td>0.143</td>
      <td>0.762</td>
      <td>17.0</td>
      <td>0.264</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Charles Barkley</td>
      <td>27</td>
      <td>PHI</td>
      <td>2.0</td>
      <td>222.0</td>
      <td>960</td>
      <td>0.231</td>
      <td>67</td>
      <td>37.3</td>
      <td>...</td>
      <td>10.1</td>
      <td>4.2</td>
      <td>1.6</td>
      <td>0.5</td>
      <td>0.570</td>
      <td>0.284</td>
      <td>0.722</td>
      <td>13.4</td>
      <td>0.258</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Karl Malone</td>
      <td>27</td>
      <td>UTA</td>
      <td>0.0</td>
      <td>142.0</td>
      <td>960</td>
      <td>0.148</td>
      <td>82</td>
      <td>40.3</td>
      <td>...</td>
      <td>11.8</td>
      <td>3.3</td>
      <td>1.1</td>
      <td>1.0</td>
      <td>0.527</td>
      <td>0.286</td>
      <td>0.770</td>
      <td>15.5</td>
      <td>0.225</td>
      <td>1991</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
mvps.to_csv("mvps.csv")
```

To predict who will be the next MVP of the season, you will need data from all players from 1991 to 2021, not just the ones who won the MVP, so map the votes of and train a machine learning model.

Downloading player stats


```python
player_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

url = player_stats_url.format(1991)
data = requests.get(url)
with open("player/1991.html", "w+", encoding="utf-8") as f:
    f.write(data.text)
```

The REQUESTS brings in just the web page as it assumes the web brownser renders and runs JavaScript on the page to download all the lines. To get all the data on the page and work around this problem, a brownser using SELENIUM will be needed.

Using selenium to scrape a Javascript page

Install Selenium Chrome Driver 98.0.4758.48 will allow Python to automate the browser https://chromedriver.chromium.org/downloads


```python
from selenium import webdriver
```


```python
driver = webdriver.Chrome(executable_path="/users/super/chromedriver")
```

    C:\Users\super\AppData\Local\Temp/ipykernel_17224/1494757858.py:1: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
      driver = webdriver.Chrome(executable_path="/users/super/chromedriver")
    

A new chrome window was created that is being controlled by selenium so that it is possible to render and get all the necessary lines and the HTML of that page 


```python
import time

year = 1991
url = player_stats_url.format(year)

driver.get(url)
driver.execute_script("window.scrollTo(1,10000)")
time.sleep(2)

html = driver.page_source
```


```python
with open("player/{}.html".format(year), "w+", encoding="utf-8") as f:
    f.write(html)
```

And now the file has all the lines and statistics from 1991, because the JavaScript was executed, you must do the same code for the rest of the seasons.


```python
for year in years:
    url = player_stats_url.format(year)

    driver.get(url)
    driver.execute_script("window.scrollTo(1,10000)")
    time.sleep(2)

    html = driver.page_source
    
    with open("player/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(html)
```

Parsing the stats with BeautifulSoup


```python
df = []
for year in years:
    with open("player/{}.html".format(year), encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="thead").decompose()
    player_table = soup.find(id="per_game_stats")
    player = pd.read_html(str(player_table))[0]
    player["Year"] = year
    
    dfs.append(player)
```

Combining player stats with pandas


```python
players = pd.concat(dfs)
```

We have all players from 1991 to 2021 in the same data table.


```python
players
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Player</th>
      <th>Age</th>
      <th>Tm</th>
      <th>First</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>G</th>
      <th>MP</th>
      <th>...</th>
      <th>2P</th>
      <th>2PA</th>
      <th>2P%</th>
      <th>eFG%</th>
      <th>FT</th>
      <th>FTA</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TOV</th>
      <th>PF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Michael Jordan</td>
      <td>27</td>
      <td>CHI</td>
      <td>77.0</td>
      <td>891.0</td>
      <td>960.0</td>
      <td>0.928</td>
      <td>82</td>
      <td>37.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Magic Johnson</td>
      <td>31</td>
      <td>LAL</td>
      <td>10.0</td>
      <td>497.0</td>
      <td>960.0</td>
      <td>0.518</td>
      <td>79</td>
      <td>37.1</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>David Robinson</td>
      <td>25</td>
      <td>SAS</td>
      <td>6.0</td>
      <td>476.0</td>
      <td>960.0</td>
      <td>0.496</td>
      <td>82</td>
      <td>37.7</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Charles Barkley</td>
      <td>27</td>
      <td>PHI</td>
      <td>2.0</td>
      <td>222.0</td>
      <td>960.0</td>
      <td>0.231</td>
      <td>67</td>
      <td>37.3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Karl Malone</td>
      <td>27</td>
      <td>UTA</td>
      <td>0.0</td>
      <td>142.0</td>
      <td>960.0</td>
      <td>0.148</td>
      <td>82</td>
      <td>40.3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>725</th>
      <td>NaN</td>
      <td>Delon Wright</td>
      <td>28</td>
      <td>SAC</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27</td>
      <td>25.8</td>
      <td>...</td>
      <td>2.6</td>
      <td>5.3</td>
      <td>.500</td>
      <td>.536</td>
      <td>1.1</td>
      <td>1.3</td>
      <td>1.0</td>
      <td>2.9</td>
      <td>1.3</td>
      <td>1.1</td>
    </tr>
    <tr>
      <th>726</th>
      <td>NaN</td>
      <td>Thaddeus Young</td>
      <td>32</td>
      <td>CHI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>68</td>
      <td>24.3</td>
      <td>...</td>
      <td>5.3</td>
      <td>9.1</td>
      <td>.580</td>
      <td>.568</td>
      <td>1.0</td>
      <td>1.7</td>
      <td>2.5</td>
      <td>3.8</td>
      <td>2.0</td>
      <td>2.2</td>
    </tr>
    <tr>
      <th>727</th>
      <td>NaN</td>
      <td>Trae Young</td>
      <td>22</td>
      <td>ATL</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>63</td>
      <td>33.7</td>
      <td>...</td>
      <td>5.6</td>
      <td>11.3</td>
      <td>.491</td>
      <td>.499</td>
      <td>7.7</td>
      <td>8.7</td>
      <td>0.6</td>
      <td>3.3</td>
      <td>4.1</td>
      <td>1.8</td>
    </tr>
    <tr>
      <th>728</th>
      <td>NaN</td>
      <td>Cody Zeller</td>
      <td>28</td>
      <td>CHO</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48</td>
      <td>20.9</td>
      <td>...</td>
      <td>3.7</td>
      <td>6.2</td>
      <td>.598</td>
      <td>.565</td>
      <td>1.8</td>
      <td>2.5</td>
      <td>2.5</td>
      <td>4.4</td>
      <td>1.1</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>729</th>
      <td>NaN</td>
      <td>Ivica Zubac</td>
      <td>23</td>
      <td>LAC</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>72</td>
      <td>22.3</td>
      <td>...</td>
      <td>3.6</td>
      <td>5.4</td>
      <td>.656</td>
      <td>.654</td>
      <td>1.9</td>
      <td>2.4</td>
      <td>2.6</td>
      <td>4.6</td>
      <td>1.1</td>
      <td>2.6</td>
    </tr>
  </tbody>
</table>
<p>18664 rows × 38 columns</p>
</div>




```python
players.to_csv("players.csv")
```

Downloading team data

The time records by year are very important so the machine learning model can use it as a predictor 


```python
team_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html"
```

Obtemos os registros por ano usando request.get é muito mais rápido


```python

for year in years:
    url = team_stats_url.format(year)

    data = requests.get(url)

    with open("team/{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(data.text)
```

Parsing the team data with BeautifulSoup


```python
dfs = []
for year in years:
    with open("team/{}.html".format(year), encoding="utf-8") as f:
        page = f.read()
    
    soup = BeautifulSoup(page, "html.parser")
    soup.find("tr", class_="thead").decompose()
    team_table = soup.find_all(id="divs_standings_E")
    team = pd.read_html(str(team_table))[0]
    team["Year"] = year
    team["Team"] = team["Eastern Conference"]
    del team["Eastern Conference"]
    dfs.append(team)

    team_table = soup.find_all(id="divs_standings_W")
    team = pd.read_html(str(team_table))[0]
    team["Year"] = year
    team["Team"] = team["Western Conference"]    
    del team["Western Conference"]
    dfs.append(team)

```

Combining team stats with pandas


```python
teams = pd.concat(dfs)
```

Analysis of all teams HTML files from 1991 to 2021 and a single table


```python
teams.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>L</th>
      <th>W/L%</th>
      <th>GB</th>
      <th>PS/G</th>
      <th>PA/G</th>
      <th>SRS</th>
      <th>Year</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>42</td>
      <td>30</td>
      <td>.583</td>
      <td>—</td>
      <td>112.4</td>
      <td>110.2</td>
      <td>2.26</td>
      <td>2021</td>
      <td>Dallas Mavericks*</td>
    </tr>
    <tr>
      <th>14</th>
      <td>38</td>
      <td>34</td>
      <td>.528</td>
      <td>4.0</td>
      <td>113.3</td>
      <td>112.3</td>
      <td>1.07</td>
      <td>2021</td>
      <td>Memphis Grizzlies*</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33</td>
      <td>39</td>
      <td>.458</td>
      <td>9.0</td>
      <td>111.1</td>
      <td>112.8</td>
      <td>-1.58</td>
      <td>2021</td>
      <td>San Antonio Spurs</td>
    </tr>
    <tr>
      <th>16</th>
      <td>31</td>
      <td>41</td>
      <td>.431</td>
      <td>11.0</td>
      <td>114.6</td>
      <td>114.9</td>
      <td>-0.20</td>
      <td>2021</td>
      <td>New Orleans Pelicans</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>55</td>
      <td>.236</td>
      <td>25.0</td>
      <td>108.8</td>
      <td>116.7</td>
      <td>-7.50</td>
      <td>2021</td>
      <td>Houston Rockets</td>
    </tr>
  </tbody>
</table>
</div>




```python
teams.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>L</th>
      <th>W/L%</th>
      <th>GB</th>
      <th>PS/G</th>
      <th>PA/G</th>
      <th>SRS</th>
      <th>Year</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>56</td>
      <td>26</td>
      <td>.683</td>
      <td>—</td>
      <td>111.5</td>
      <td>105.7</td>
      <td>5.22</td>
      <td>1991</td>
      <td>Boston Celtics*</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44</td>
      <td>38</td>
      <td>.537</td>
      <td>12.0</td>
      <td>105.4</td>
      <td>105.6</td>
      <td>-0.39</td>
      <td>1991</td>
      <td>Philadelphia 76ers*</td>
    </tr>
    <tr>
      <th>2</th>
      <td>39</td>
      <td>43</td>
      <td>.476</td>
      <td>17.0</td>
      <td>103.1</td>
      <td>103.3</td>
      <td>-0.43</td>
      <td>1991</td>
      <td>New York Knicks*</td>
    </tr>
    <tr>
      <th>3</th>
      <td>30</td>
      <td>52</td>
      <td>.366</td>
      <td>26.0</td>
      <td>101.4</td>
      <td>106.4</td>
      <td>-4.84</td>
      <td>1991</td>
      <td>Washington Bullets</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26</td>
      <td>56</td>
      <td>.317</td>
      <td>30.0</td>
      <td>102.9</td>
      <td>107.5</td>
      <td>-4.53</td>
      <td>1991</td>
      <td>New Jersey Nets</td>
    </tr>
  </tbody>
</table>
</div>




```python
teams.to_csv("teams.csv")
```

* Web Scraping with REQUESTS library;
* Analysis with BeautifulSoup and Pandas;
* Use of SELENIUM for advanced Web Scraping, initializing the Web Driver, executing the Java Script and getting the rendered HTML;
* Combining all data into a single Pandas data frame and writing it to CSV for players, teams and mvp's;
* All HTML files archived and saved (in case we want to go back and process them in a different way)

Next steps: Prepare the data for Machine Learning. So getting the predictors right and making sure you clean the data properly.
