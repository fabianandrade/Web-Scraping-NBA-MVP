Cleaning NBA Stats Data With Python And Pandas: Data Project [part 2 of 3]

* Overview of the NBA data


```python
import pandas as pd
```


```python
mvps = pd.read_csv("mvps.csv")
```


```python
mvps
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
      <th>Unnamed: 0</th>
      <th>Rank</th>
      <th>Player</th>
      <th>Age</th>
      <th>Tm</th>
      <th>First</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>G</th>
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
      <td>0</td>
      <td>1</td>
      <td>Michael Jordan</td>
      <td>27</td>
      <td>CHI</td>
      <td>77.0</td>
      <td>891.0</td>
      <td>960</td>
      <td>0.928</td>
      <td>82</td>
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
      <td>1</td>
      <td>2</td>
      <td>Magic Johnson</td>
      <td>31</td>
      <td>LAL</td>
      <td>10.0</td>
      <td>497.0</td>
      <td>960</td>
      <td>0.518</td>
      <td>79</td>
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
      <td>2</td>
      <td>3</td>
      <td>David Robinson</td>
      <td>25</td>
      <td>SAS</td>
      <td>6.0</td>
      <td>476.0</td>
      <td>960</td>
      <td>0.496</td>
      <td>82</td>
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
      <td>3</td>
      <td>4</td>
      <td>Charles Barkley</td>
      <td>27</td>
      <td>PHI</td>
      <td>2.0</td>
      <td>222.0</td>
      <td>960</td>
      <td>0.231</td>
      <td>67</td>
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
      <td>4</td>
      <td>5</td>
      <td>Karl Malone</td>
      <td>27</td>
      <td>UTA</td>
      <td>0.0</td>
      <td>142.0</td>
      <td>960</td>
      <td>0.148</td>
      <td>82</td>
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
      <th>469</th>
      <td>10</td>
      <td>11</td>
      <td>Russell Westbrook</td>
      <td>32</td>
      <td>WAS</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1010</td>
      <td>0.005</td>
      <td>65</td>
      <td>...</td>
      <td>11.5</td>
      <td>11.7</td>
      <td>1.4</td>
      <td>0.4</td>
      <td>0.439</td>
      <td>0.315</td>
      <td>0.656</td>
      <td>3.7</td>
      <td>0.075</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>470</th>
      <td>11</td>
      <td>12</td>
      <td>Ben Simmons</td>
      <td>24</td>
      <td>PHI</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>1010</td>
      <td>0.003</td>
      <td>58</td>
      <td>...</td>
      <td>7.2</td>
      <td>6.9</td>
      <td>1.6</td>
      <td>0.6</td>
      <td>0.557</td>
      <td>0.300</td>
      <td>0.613</td>
      <td>6.0</td>
      <td>0.153</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>471</th>
      <td>12</td>
      <td>13T</td>
      <td>James Harden</td>
      <td>31</td>
      <td>TOT</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1010</td>
      <td>0.001</td>
      <td>44</td>
      <td>...</td>
      <td>7.9</td>
      <td>10.8</td>
      <td>1.2</td>
      <td>0.8</td>
      <td>0.466</td>
      <td>0.362</td>
      <td>0.861</td>
      <td>7.0</td>
      <td>0.208</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>472</th>
      <td>13</td>
      <td>13T</td>
      <td>LeBron James</td>
      <td>36</td>
      <td>LAL</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1010</td>
      <td>0.001</td>
      <td>45</td>
      <td>...</td>
      <td>7.7</td>
      <td>7.8</td>
      <td>1.1</td>
      <td>0.6</td>
      <td>0.513</td>
      <td>0.365</td>
      <td>0.698</td>
      <td>5.6</td>
      <td>0.179</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>473</th>
      <td>14</td>
      <td>13T</td>
      <td>Kawhi Leonard</td>
      <td>29</td>
      <td>LAC</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1010</td>
      <td>0.001</td>
      <td>52</td>
      <td>...</td>
      <td>6.5</td>
      <td>5.2</td>
      <td>1.6</td>
      <td>0.4</td>
      <td>0.512</td>
      <td>0.398</td>
      <td>0.885</td>
      <td>8.8</td>
      <td>0.238</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
<p>474 rows × 22 columns</p>
</div>



* Cleaning the MVP vote data



```python
mvps = mvps[["Player", "Year", "Pts Won", "Pts Max", "Share"]]
```


```python
mvps
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
      <th>Player</th>
      <th>Year</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Michael Jordan</td>
      <td>1991</td>
      <td>891.0</td>
      <td>960</td>
      <td>0.928</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Magic Johnson</td>
      <td>1991</td>
      <td>497.0</td>
      <td>960</td>
      <td>0.518</td>
    </tr>
    <tr>
      <th>2</th>
      <td>David Robinson</td>
      <td>1991</td>
      <td>476.0</td>
      <td>960</td>
      <td>0.496</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Charles Barkley</td>
      <td>1991</td>
      <td>222.0</td>
      <td>960</td>
      <td>0.231</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Karl Malone</td>
      <td>1991</td>
      <td>142.0</td>
      <td>960</td>
      <td>0.148</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>469</th>
      <td>Russell Westbrook</td>
      <td>2021</td>
      <td>5.0</td>
      <td>1010</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>470</th>
      <td>Ben Simmons</td>
      <td>2021</td>
      <td>3.0</td>
      <td>1010</td>
      <td>0.003</td>
    </tr>
    <tr>
      <th>471</th>
      <td>James Harden</td>
      <td>2021</td>
      <td>1.0</td>
      <td>1010</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>472</th>
      <td>LeBron James</td>
      <td>2021</td>
      <td>1.0</td>
      <td>1010</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>473</th>
      <td>Kawhi Leonard</td>
      <td>2021</td>
      <td>1.0</td>
      <td>1010</td>
      <td>0.001</td>
    </tr>
  </tbody>
</table>
<p>474 rows × 5 columns</p>
</div>




```python
players = pd.read_csv("players.csv")
```


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
      <th>Unnamed: 0</th>
      <th>Rk</th>
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>...</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>Alaa Abdelnaby</td>
      <td>PF</td>
      <td>22</td>
      <td>POR</td>
      <td>43</td>
      <td>0</td>
      <td>6.7</td>
      <td>1.3</td>
      <td>...</td>
      <td>0.6</td>
      <td>1.4</td>
      <td>2.1</td>
      <td>0.3</td>
      <td>0.1</td>
      <td>0.3</td>
      <td>0.5</td>
      <td>0.9</td>
      <td>3.1</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>Mahmoud Abdul-Rauf</td>
      <td>PG</td>
      <td>21</td>
      <td>DEN</td>
      <td>67</td>
      <td>19</td>
      <td>22.5</td>
      <td>6.2</td>
      <td>...</td>
      <td>0.5</td>
      <td>1.3</td>
      <td>1.8</td>
      <td>3.1</td>
      <td>0.8</td>
      <td>0.1</td>
      <td>1.6</td>
      <td>2.2</td>
      <td>14.1</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>Mark Acres</td>
      <td>C</td>
      <td>28</td>
      <td>ORL</td>
      <td>68</td>
      <td>0</td>
      <td>19.3</td>
      <td>1.6</td>
      <td>...</td>
      <td>2.1</td>
      <td>3.2</td>
      <td>5.3</td>
      <td>0.4</td>
      <td>0.4</td>
      <td>0.4</td>
      <td>0.6</td>
      <td>3.2</td>
      <td>4.2</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>Michael Adams</td>
      <td>PG</td>
      <td>28</td>
      <td>DEN</td>
      <td>66</td>
      <td>66</td>
      <td>35.5</td>
      <td>8.5</td>
      <td>...</td>
      <td>0.9</td>
      <td>3.0</td>
      <td>3.9</td>
      <td>10.5</td>
      <td>2.2</td>
      <td>0.1</td>
      <td>3.6</td>
      <td>2.5</td>
      <td>26.5</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>Mark Aguirre</td>
      <td>SF</td>
      <td>31</td>
      <td>DET</td>
      <td>78</td>
      <td>13</td>
      <td>25.7</td>
      <td>5.4</td>
      <td>...</td>
      <td>1.7</td>
      <td>3.1</td>
      <td>4.8</td>
      <td>1.8</td>
      <td>0.6</td>
      <td>0.3</td>
      <td>1.6</td>
      <td>2.7</td>
      <td>14.2</td>
      <td>1991</td>
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
      <th>18039</th>
      <td>725</td>
      <td>536</td>
      <td>Delon Wright</td>
      <td>PG</td>
      <td>28</td>
      <td>SAC</td>
      <td>27</td>
      <td>8</td>
      <td>25.8</td>
      <td>3.9</td>
      <td>...</td>
      <td>1.0</td>
      <td>2.9</td>
      <td>3.9</td>
      <td>3.6</td>
      <td>1.6</td>
      <td>0.4</td>
      <td>1.3</td>
      <td>1.1</td>
      <td>10.0</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>18040</th>
      <td>726</td>
      <td>537</td>
      <td>Thaddeus Young</td>
      <td>PF</td>
      <td>32</td>
      <td>CHI</td>
      <td>68</td>
      <td>23</td>
      <td>24.3</td>
      <td>5.4</td>
      <td>...</td>
      <td>2.5</td>
      <td>3.8</td>
      <td>6.2</td>
      <td>4.3</td>
      <td>1.1</td>
      <td>0.6</td>
      <td>2.0</td>
      <td>2.2</td>
      <td>12.1</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>18041</th>
      <td>727</td>
      <td>538</td>
      <td>Trae Young</td>
      <td>PG</td>
      <td>22</td>
      <td>ATL</td>
      <td>63</td>
      <td>63</td>
      <td>33.7</td>
      <td>7.7</td>
      <td>...</td>
      <td>0.6</td>
      <td>3.3</td>
      <td>3.9</td>
      <td>9.4</td>
      <td>0.8</td>
      <td>0.2</td>
      <td>4.1</td>
      <td>1.8</td>
      <td>25.3</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>18042</th>
      <td>728</td>
      <td>539</td>
      <td>Cody Zeller</td>
      <td>C</td>
      <td>28</td>
      <td>CHO</td>
      <td>48</td>
      <td>21</td>
      <td>20.9</td>
      <td>3.8</td>
      <td>...</td>
      <td>2.5</td>
      <td>4.4</td>
      <td>6.8</td>
      <td>1.8</td>
      <td>0.6</td>
      <td>0.4</td>
      <td>1.1</td>
      <td>2.5</td>
      <td>9.4</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>18043</th>
      <td>729</td>
      <td>540</td>
      <td>Ivica Zubac</td>
      <td>C</td>
      <td>23</td>
      <td>LAC</td>
      <td>72</td>
      <td>33</td>
      <td>22.3</td>
      <td>3.6</td>
      <td>...</td>
      <td>2.6</td>
      <td>4.6</td>
      <td>7.2</td>
      <td>1.3</td>
      <td>0.3</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>2.6</td>
      <td>9.0</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
<p>18044 rows × 32 columns</p>
</div>



* Cleaning the player data


```python
del players["Unnamed: 0"]
```


```python
del players["Rk"]
```


```python
players["Player"] = players["Player"].str.replace("*","", regex=False)
```


```python
players.head()

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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alaa Abdelnaby</td>
      <td>PF</td>
      <td>22</td>
      <td>POR</td>
      <td>43</td>
      <td>0</td>
      <td>6.7</td>
      <td>1.3</td>
      <td>2.7</td>
      <td>.474</td>
      <td>...</td>
      <td>0.6</td>
      <td>1.4</td>
      <td>2.1</td>
      <td>0.3</td>
      <td>0.1</td>
      <td>0.3</td>
      <td>0.5</td>
      <td>0.9</td>
      <td>3.1</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mahmoud Abdul-Rauf</td>
      <td>PG</td>
      <td>21</td>
      <td>DEN</td>
      <td>67</td>
      <td>19</td>
      <td>22.5</td>
      <td>6.2</td>
      <td>15.1</td>
      <td>.413</td>
      <td>...</td>
      <td>0.5</td>
      <td>1.3</td>
      <td>1.8</td>
      <td>3.1</td>
      <td>0.8</td>
      <td>0.1</td>
      <td>1.6</td>
      <td>2.2</td>
      <td>14.1</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mark Acres</td>
      <td>C</td>
      <td>28</td>
      <td>ORL</td>
      <td>68</td>
      <td>0</td>
      <td>19.3</td>
      <td>1.6</td>
      <td>3.1</td>
      <td>.509</td>
      <td>...</td>
      <td>2.1</td>
      <td>3.2</td>
      <td>5.3</td>
      <td>0.4</td>
      <td>0.4</td>
      <td>0.4</td>
      <td>0.6</td>
      <td>3.2</td>
      <td>4.2</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Michael Adams</td>
      <td>PG</td>
      <td>28</td>
      <td>DEN</td>
      <td>66</td>
      <td>66</td>
      <td>35.5</td>
      <td>8.5</td>
      <td>21.5</td>
      <td>.394</td>
      <td>...</td>
      <td>0.9</td>
      <td>3.0</td>
      <td>3.9</td>
      <td>10.5</td>
      <td>2.2</td>
      <td>0.1</td>
      <td>3.6</td>
      <td>2.5</td>
      <td>26.5</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mark Aguirre</td>
      <td>SF</td>
      <td>31</td>
      <td>DET</td>
      <td>78</td>
      <td>13</td>
      <td>25.7</td>
      <td>5.4</td>
      <td>11.7</td>
      <td>.462</td>
      <td>...</td>
      <td>1.7</td>
      <td>3.1</td>
      <td>4.8</td>
      <td>1.8</td>
      <td>0.6</td>
      <td>0.3</td>
      <td>1.6</td>
      <td>2.7</td>
      <td>14.2</td>
      <td>1991</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
players[players["Player"] == "Greg Anderson"]
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>26</td>
      <td>TOT</td>
      <td>68</td>
      <td>2</td>
      <td>13.6</td>
      <td>1.7</td>
      <td>4.0</td>
      <td>.430</td>
      <td>...</td>
      <td>1.4</td>
      <td>3.3</td>
      <td>4.7</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>1.2</td>
      <td>2.1</td>
      <td>4.3</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>26</td>
      <td>MIL</td>
      <td>26</td>
      <td>0</td>
      <td>9.5</td>
      <td>1.0</td>
      <td>2.8</td>
      <td>.370</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.9</td>
      <td>2.9</td>
      <td>0.1</td>
      <td>0.3</td>
      <td>0.3</td>
      <td>0.8</td>
      <td>1.1</td>
      <td>2.7</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>26</td>
      <td>NJN</td>
      <td>1</td>
      <td>0</td>
      <td>18.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>1.000</td>
      <td>...</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>26</td>
      <td>DEN</td>
      <td>41</td>
      <td>2</td>
      <td>16.1</td>
      <td>2.1</td>
      <td>4.7</td>
      <td>.440</td>
      <td>...</td>
      <td>1.6</td>
      <td>4.1</td>
      <td>5.8</td>
      <td>0.3</td>
      <td>0.6</td>
      <td>0.9</td>
      <td>1.5</td>
      <td>2.6</td>
      <td>5.2</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>467</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>27</td>
      <td>DEN</td>
      <td>82</td>
      <td>82</td>
      <td>34.1</td>
      <td>4.7</td>
      <td>10.4</td>
      <td>.456</td>
      <td>...</td>
      <td>4.1</td>
      <td>7.4</td>
      <td>11.5</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>2.5</td>
      <td>3.2</td>
      <td>11.5</td>
      <td>1992</td>
    </tr>
    <tr>
      <th>1412</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>29</td>
      <td>DET</td>
      <td>77</td>
      <td>47</td>
      <td>21.1</td>
      <td>2.6</td>
      <td>4.8</td>
      <td>.543</td>
      <td>...</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>7.4</td>
      <td>0.7</td>
      <td>0.7</td>
      <td>0.9</td>
      <td>1.2</td>
      <td>3.0</td>
      <td>6.4</td>
      <td>1994</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>30</td>
      <td>ATL</td>
      <td>51</td>
      <td>0</td>
      <td>12.2</td>
      <td>1.1</td>
      <td>2.0</td>
      <td>.548</td>
      <td>...</td>
      <td>1.2</td>
      <td>2.5</td>
      <td>3.7</td>
      <td>0.3</td>
      <td>0.5</td>
      <td>0.6</td>
      <td>0.6</td>
      <td>2.0</td>
      <td>2.9</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2381</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>31</td>
      <td>SAS</td>
      <td>46</td>
      <td>7</td>
      <td>7.5</td>
      <td>0.5</td>
      <td>1.0</td>
      <td>.511</td>
      <td>...</td>
      <td>0.6</td>
      <td>1.5</td>
      <td>2.2</td>
      <td>0.2</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.2</td>
      <td>1996</td>
    </tr>
    <tr>
      <th>2948</th>
      <td>Greg Anderson</td>
      <td>C</td>
      <td>32</td>
      <td>SAS</td>
      <td>82</td>
      <td>48</td>
      <td>20.2</td>
      <td>1.6</td>
      <td>3.2</td>
      <td>.496</td>
      <td>...</td>
      <td>1.9</td>
      <td>3.5</td>
      <td>5.5</td>
      <td>0.4</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>0.9</td>
      <td>2.7</td>
      <td>3.9</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>3541</th>
      <td>Greg Anderson</td>
      <td>C</td>
      <td>33</td>
      <td>ATL</td>
      <td>50</td>
      <td>0</td>
      <td>8.0</td>
      <td>0.7</td>
      <td>1.6</td>
      <td>.444</td>
      <td>...</td>
      <td>0.8</td>
      <td>1.6</td>
      <td>2.4</td>
      <td>0.3</td>
      <td>0.4</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>1.7</td>
      <td>1.8</td>
      <td>1998</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 30 columns</p>
</div>




```python
def single_team(df):
    if df.shape[0]==1:
        return df
    else:
        row = df[df["Tm"]=="TOT"]
        row["Tm"] = df.iloc[-1,:]["Tm"]
        return row

players = players.groupby(["Player", "Year"]).apply(single_team)
```


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
      <th></th>
      <th></th>
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
    </tr>
    <tr>
      <th>Player</th>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">A.C. Green</th>
      <th>1991</th>
      <th>164</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>2.5</td>
      <td>3.8</td>
      <td>6.3</td>
      <td>0.9</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>9.1</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>1992</th>
      <th>633</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>28</td>
      <td>LAL</td>
      <td>82</td>
      <td>53</td>
      <td>35.4</td>
      <td>4.7</td>
      <td>9.8</td>
      <td>.476</td>
      <td>...</td>
      <td>3.7</td>
      <td>5.6</td>
      <td>9.3</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>13.6</td>
      <td>1992</td>
    </tr>
    <tr>
      <th>1993</th>
      <th>1092</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>55</td>
      <td>34.4</td>
      <td>4.6</td>
      <td>8.6</td>
      <td>.537</td>
      <td>...</td>
      <td>3.5</td>
      <td>5.2</td>
      <td>8.7</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>12.8</td>
      <td>1993</td>
    </tr>
    <tr>
      <th>1994</th>
      <th>1579</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>30</td>
      <td>PHO</td>
      <td>82</td>
      <td>55</td>
      <td>34.5</td>
      <td>5.7</td>
      <td>11.3</td>
      <td>.502</td>
      <td>...</td>
      <td>3.4</td>
      <td>5.8</td>
      <td>9.2</td>
      <td>1.7</td>
      <td>0.9</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>14.7</td>
      <td>1994</td>
    </tr>
    <tr>
      <th>1995</th>
      <th>2067</th>
      <td>A.C. Green</td>
      <td>SF</td>
      <td>31</td>
      <td>PHO</td>
      <td>82</td>
      <td>52</td>
      <td>32.8</td>
      <td>3.8</td>
      <td>7.5</td>
      <td>.504</td>
      <td>...</td>
      <td>2.4</td>
      <td>5.8</td>
      <td>8.2</td>
      <td>1.5</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>11.2</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
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
      <th rowspan="5" valign="top">Željko Rebrača</th>
      <th>2002</th>
      <th>6095</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>29</td>
      <td>DET</td>
      <td>74</td>
      <td>4</td>
      <td>15.9</td>
      <td>2.6</td>
      <td>5.1</td>
      <td>.505</td>
      <td>...</td>
      <td>1.1</td>
      <td>2.8</td>
      <td>3.9</td>
      <td>0.5</td>
      <td>0.4</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>2003</th>
      <th>6595</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>30</td>
      <td>DET</td>
      <td>30</td>
      <td>12</td>
      <td>16.3</td>
      <td>2.7</td>
      <td>4.8</td>
      <td>.552</td>
      <td>...</td>
      <td>0.9</td>
      <td>2.2</td>
      <td>3.1</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.6</td>
      <td>1.0</td>
      <td>2.6</td>
      <td>6.6</td>
      <td>2003</td>
    </tr>
    <tr>
      <th>2004</th>
      <th>7176</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>31</td>
      <td>ATL</td>
      <td>24</td>
      <td>2</td>
      <td>11.4</td>
      <td>1.4</td>
      <td>3.2</td>
      <td>.442</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>2.4</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>2.2</td>
      <td>3.8</td>
      <td>2004</td>
    </tr>
    <tr>
      <th>2005</th>
      <th>7776</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>32</td>
      <td>LAC</td>
      <td>58</td>
      <td>2</td>
      <td>16.0</td>
      <td>2.3</td>
      <td>4.0</td>
      <td>.568</td>
      <td>...</td>
      <td>0.8</td>
      <td>2.3</td>
      <td>3.2</td>
      <td>0.4</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>2.2</td>
      <td>5.8</td>
      <td>2005</td>
    </tr>
    <tr>
      <th>2006</th>
      <th>8370</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>33</td>
      <td>LAC</td>
      <td>29</td>
      <td>2</td>
      <td>14.2</td>
      <td>1.8</td>
      <td>3.3</td>
      <td>.542</td>
      <td>...</td>
      <td>0.4</td>
      <td>1.8</td>
      <td>2.2</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>2.0</td>
      <td>4.7</td>
      <td>2006</td>
    </tr>
  </tbody>
</table>
<p>14092 rows × 30 columns</p>
</div>




```python
players.index = players.index.droplevel()
```


```python
players.index = players.index.droplevel()
```


```python
players.head()
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>164</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>2.5</td>
      <td>3.8</td>
      <td>6.3</td>
      <td>0.9</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>9.1</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>633</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>28</td>
      <td>LAL</td>
      <td>82</td>
      <td>53</td>
      <td>35.4</td>
      <td>4.7</td>
      <td>9.8</td>
      <td>.476</td>
      <td>...</td>
      <td>3.7</td>
      <td>5.6</td>
      <td>9.3</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>13.6</td>
      <td>1992</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>55</td>
      <td>34.4</td>
      <td>4.6</td>
      <td>8.6</td>
      <td>.537</td>
      <td>...</td>
      <td>3.5</td>
      <td>5.2</td>
      <td>8.7</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>12.8</td>
      <td>1993</td>
    </tr>
    <tr>
      <th>1579</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>30</td>
      <td>PHO</td>
      <td>82</td>
      <td>55</td>
      <td>34.5</td>
      <td>5.7</td>
      <td>11.3</td>
      <td>.502</td>
      <td>...</td>
      <td>3.4</td>
      <td>5.8</td>
      <td>9.2</td>
      <td>1.7</td>
      <td>0.9</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>14.7</td>
      <td>1994</td>
    </tr>
    <tr>
      <th>2067</th>
      <td>A.C. Green</td>
      <td>SF</td>
      <td>31</td>
      <td>PHO</td>
      <td>82</td>
      <td>52</td>
      <td>32.8</td>
      <td>3.8</td>
      <td>7.5</td>
      <td>.504</td>
      <td>...</td>
      <td>2.4</td>
      <td>5.8</td>
      <td>8.2</td>
      <td>1.5</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>11.2</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
players[players["Player"] == "Greg Anderson"]
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>26</td>
      <td>DEN</td>
      <td>68</td>
      <td>2</td>
      <td>13.6</td>
      <td>1.7</td>
      <td>4.0</td>
      <td>.430</td>
      <td>...</td>
      <td>1.4</td>
      <td>3.3</td>
      <td>4.7</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>1.2</td>
      <td>2.1</td>
      <td>4.3</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>467</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>27</td>
      <td>DEN</td>
      <td>82</td>
      <td>82</td>
      <td>34.1</td>
      <td>4.7</td>
      <td>10.4</td>
      <td>.456</td>
      <td>...</td>
      <td>4.1</td>
      <td>7.4</td>
      <td>11.5</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>2.5</td>
      <td>3.2</td>
      <td>11.5</td>
      <td>1992</td>
    </tr>
    <tr>
      <th>1412</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>29</td>
      <td>DET</td>
      <td>77</td>
      <td>47</td>
      <td>21.1</td>
      <td>2.6</td>
      <td>4.8</td>
      <td>.543</td>
      <td>...</td>
      <td>2.4</td>
      <td>5.0</td>
      <td>7.4</td>
      <td>0.7</td>
      <td>0.7</td>
      <td>0.9</td>
      <td>1.2</td>
      <td>3.0</td>
      <td>6.4</td>
      <td>1994</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>30</td>
      <td>ATL</td>
      <td>51</td>
      <td>0</td>
      <td>12.2</td>
      <td>1.1</td>
      <td>2.0</td>
      <td>.548</td>
      <td>...</td>
      <td>1.2</td>
      <td>2.5</td>
      <td>3.7</td>
      <td>0.3</td>
      <td>0.5</td>
      <td>0.6</td>
      <td>0.6</td>
      <td>2.0</td>
      <td>2.9</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2381</th>
      <td>Greg Anderson</td>
      <td>PF</td>
      <td>31</td>
      <td>SAS</td>
      <td>46</td>
      <td>7</td>
      <td>7.5</td>
      <td>0.5</td>
      <td>1.0</td>
      <td>.511</td>
      <td>...</td>
      <td>0.6</td>
      <td>1.5</td>
      <td>2.2</td>
      <td>0.2</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.2</td>
      <td>1996</td>
    </tr>
    <tr>
      <th>2948</th>
      <td>Greg Anderson</td>
      <td>C</td>
      <td>32</td>
      <td>SAS</td>
      <td>82</td>
      <td>48</td>
      <td>20.2</td>
      <td>1.6</td>
      <td>3.2</td>
      <td>.496</td>
      <td>...</td>
      <td>1.9</td>
      <td>3.5</td>
      <td>5.5</td>
      <td>0.4</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>0.9</td>
      <td>2.7</td>
      <td>3.9</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>3541</th>
      <td>Greg Anderson</td>
      <td>C</td>
      <td>33</td>
      <td>ATL</td>
      <td>50</td>
      <td>0</td>
      <td>8.0</td>
      <td>0.7</td>
      <td>1.6</td>
      <td>.444</td>
      <td>...</td>
      <td>0.8</td>
      <td>1.6</td>
      <td>2.4</td>
      <td>0.3</td>
      <td>0.4</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>1.7</td>
      <td>1.8</td>
      <td>1998</td>
    </tr>
  </tbody>
</table>
<p>7 rows × 30 columns</p>
</div>




```python
combined = players.merge(mvps, how="outer", on=["Player", "Year"])
```


```python
combined.head()
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>0.9</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>9.1</td>
      <td>1991</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>28</td>
      <td>LAL</td>
      <td>82</td>
      <td>53</td>
      <td>35.4</td>
      <td>4.7</td>
      <td>9.8</td>
      <td>.476</td>
      <td>...</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>13.6</td>
      <td>1992</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>55</td>
      <td>34.4</td>
      <td>4.6</td>
      <td>8.6</td>
      <td>.537</td>
      <td>...</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>12.8</td>
      <td>1993</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>30</td>
      <td>PHO</td>
      <td>82</td>
      <td>55</td>
      <td>34.5</td>
      <td>5.7</td>
      <td>11.3</td>
      <td>.502</td>
      <td>...</td>
      <td>1.7</td>
      <td>0.9</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>14.7</td>
      <td>1994</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A.C. Green</td>
      <td>SF</td>
      <td>31</td>
      <td>PHO</td>
      <td>82</td>
      <td>52</td>
      <td>32.8</td>
      <td>3.8</td>
      <td>7.5</td>
      <td>.504</td>
      <td>...</td>
      <td>1.5</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>11.2</td>
      <td>1995</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 33 columns</p>
</div>



The combination is correct because A.C.Green was not on the MVPS list


```python
combined[combined["Pts Won"] > 0]
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>187</th>
      <td>Al Jefferson</td>
      <td>C</td>
      <td>29</td>
      <td>CHA</td>
      <td>73</td>
      <td>73</td>
      <td>35.0</td>
      <td>9.6</td>
      <td>18.8</td>
      <td>.509</td>
      <td>...</td>
      <td>2.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.7</td>
      <td>2.4</td>
      <td>21.8</td>
      <td>2014</td>
      <td>34.0</td>
      <td>1250.0</td>
      <td>0.027</td>
    </tr>
    <tr>
      <th>329</th>
      <td>Allen Iverson</td>
      <td>PG</td>
      <td>21</td>
      <td>PHI</td>
      <td>76</td>
      <td>74</td>
      <td>40.1</td>
      <td>8.2</td>
      <td>19.8</td>
      <td>.416</td>
      <td>...</td>
      <td>7.5</td>
      <td>2.1</td>
      <td>0.3</td>
      <td>4.4</td>
      <td>3.1</td>
      <td>23.5</td>
      <td>1997</td>
      <td>1.0</td>
      <td>1150.0</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>331</th>
      <td>Allen Iverson</td>
      <td>SG</td>
      <td>23</td>
      <td>PHI</td>
      <td>48</td>
      <td>48</td>
      <td>41.5</td>
      <td>9.1</td>
      <td>22.0</td>
      <td>.412</td>
      <td>...</td>
      <td>4.6</td>
      <td>2.3</td>
      <td>0.1</td>
      <td>3.5</td>
      <td>2.0</td>
      <td>26.8</td>
      <td>1999</td>
      <td>319.0</td>
      <td>1180.0</td>
      <td>0.270</td>
    </tr>
    <tr>
      <th>332</th>
      <td>Allen Iverson</td>
      <td>SG</td>
      <td>24</td>
      <td>PHI</td>
      <td>70</td>
      <td>70</td>
      <td>40.8</td>
      <td>10.4</td>
      <td>24.8</td>
      <td>.421</td>
      <td>...</td>
      <td>4.7</td>
      <td>2.1</td>
      <td>0.1</td>
      <td>3.3</td>
      <td>2.3</td>
      <td>28.4</td>
      <td>2000</td>
      <td>132.0</td>
      <td>1210.0</td>
      <td>0.109</td>
    </tr>
    <tr>
      <th>333</th>
      <td>Allen Iverson</td>
      <td>SG</td>
      <td>25</td>
      <td>PHI</td>
      <td>71</td>
      <td>71</td>
      <td>42.0</td>
      <td>10.7</td>
      <td>25.5</td>
      <td>.420</td>
      <td>...</td>
      <td>4.6</td>
      <td>2.5</td>
      <td>0.3</td>
      <td>3.3</td>
      <td>2.1</td>
      <td>31.1</td>
      <td>2001</td>
      <td>1121.0</td>
      <td>1240.0</td>
      <td>0.904</td>
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
      <th>13587</th>
      <td>Vince Carter</td>
      <td>SF</td>
      <td>23</td>
      <td>TOR</td>
      <td>82</td>
      <td>82</td>
      <td>38.1</td>
      <td>9.6</td>
      <td>20.7</td>
      <td>.465</td>
      <td>...</td>
      <td>3.9</td>
      <td>1.3</td>
      <td>1.1</td>
      <td>2.2</td>
      <td>3.2</td>
      <td>25.7</td>
      <td>2000</td>
      <td>51.0</td>
      <td>1210.0</td>
      <td>0.042</td>
    </tr>
    <tr>
      <th>13588</th>
      <td>Vince Carter</td>
      <td>SF</td>
      <td>24</td>
      <td>TOR</td>
      <td>75</td>
      <td>75</td>
      <td>39.7</td>
      <td>10.2</td>
      <td>22.1</td>
      <td>.460</td>
      <td>...</td>
      <td>3.9</td>
      <td>1.5</td>
      <td>1.1</td>
      <td>2.2</td>
      <td>2.7</td>
      <td>27.6</td>
      <td>2001</td>
      <td>7.0</td>
      <td>1240.0</td>
      <td>0.006</td>
    </tr>
    <tr>
      <th>13592</th>
      <td>Vince Carter</td>
      <td>SF-SG</td>
      <td>28</td>
      <td>NJN</td>
      <td>77</td>
      <td>76</td>
      <td>36.7</td>
      <td>9.0</td>
      <td>20.0</td>
      <td>.452</td>
      <td>...</td>
      <td>4.2</td>
      <td>1.4</td>
      <td>0.6</td>
      <td>2.2</td>
      <td>3.2</td>
      <td>24.5</td>
      <td>2005</td>
      <td>3.0</td>
      <td>1270.0</td>
      <td>0.002</td>
    </tr>
    <tr>
      <th>13952</th>
      <td>Yao Ming</td>
      <td>C</td>
      <td>23</td>
      <td>HOU</td>
      <td>82</td>
      <td>82</td>
      <td>32.8</td>
      <td>6.5</td>
      <td>12.5</td>
      <td>.522</td>
      <td>...</td>
      <td>1.5</td>
      <td>0.3</td>
      <td>1.9</td>
      <td>2.5</td>
      <td>3.3</td>
      <td>17.5</td>
      <td>2004</td>
      <td>1.0</td>
      <td>1230.0</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>13957</th>
      <td>Yao Ming</td>
      <td>C</td>
      <td>28</td>
      <td>HOU</td>
      <td>77</td>
      <td>77</td>
      <td>33.6</td>
      <td>7.4</td>
      <td>13.4</td>
      <td>.548</td>
      <td>...</td>
      <td>1.8</td>
      <td>0.4</td>
      <td>1.9</td>
      <td>3.0</td>
      <td>3.3</td>
      <td>19.7</td>
      <td>2009</td>
      <td>1.0</td>
      <td>1210.0</td>
      <td>0.001</td>
    </tr>
  </tbody>
</table>
<p>474 rows × 33 columns</p>
</div>



Replacement of "NAN" (when the player has not received any votes by zero) by 0


```python
combined[["Pts Won", "Pts Max", "Share"]]= combined[["Pts Won", "Pts Max", "Share"]].fillna(0)
```


```python
combined
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>0.9</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>9.1</td>
      <td>1991</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>28</td>
      <td>LAL</td>
      <td>82</td>
      <td>53</td>
      <td>35.4</td>
      <td>4.7</td>
      <td>9.8</td>
      <td>.476</td>
      <td>...</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>13.6</td>
      <td>1992</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>55</td>
      <td>34.4</td>
      <td>4.6</td>
      <td>8.6</td>
      <td>.537</td>
      <td>...</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>12.8</td>
      <td>1993</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>30</td>
      <td>PHO</td>
      <td>82</td>
      <td>55</td>
      <td>34.5</td>
      <td>5.7</td>
      <td>11.3</td>
      <td>.502</td>
      <td>...</td>
      <td>1.7</td>
      <td>0.9</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>14.7</td>
      <td>1994</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A.C. Green</td>
      <td>SF</td>
      <td>31</td>
      <td>PHO</td>
      <td>82</td>
      <td>52</td>
      <td>32.8</td>
      <td>3.8</td>
      <td>7.5</td>
      <td>.504</td>
      <td>...</td>
      <td>1.5</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>11.2</td>
      <td>1995</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <th>14087</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>29</td>
      <td>DET</td>
      <td>74</td>
      <td>4</td>
      <td>15.9</td>
      <td>2.6</td>
      <td>5.1</td>
      <td>.505</td>
      <td>...</td>
      <td>0.5</td>
      <td>0.4</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2002</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14088</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>30</td>
      <td>DET</td>
      <td>30</td>
      <td>12</td>
      <td>16.3</td>
      <td>2.7</td>
      <td>4.8</td>
      <td>.552</td>
      <td>...</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.6</td>
      <td>1.0</td>
      <td>2.6</td>
      <td>6.6</td>
      <td>2003</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14089</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>31</td>
      <td>ATL</td>
      <td>24</td>
      <td>2</td>
      <td>11.4</td>
      <td>1.4</td>
      <td>3.2</td>
      <td>.442</td>
      <td>...</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>2.2</td>
      <td>3.8</td>
      <td>2004</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14090</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>32</td>
      <td>LAC</td>
      <td>58</td>
      <td>2</td>
      <td>16.0</td>
      <td>2.3</td>
      <td>4.0</td>
      <td>.568</td>
      <td>...</td>
      <td>0.4</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>2.2</td>
      <td>5.8</td>
      <td>2005</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14091</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>33</td>
      <td>LAC</td>
      <td>29</td>
      <td>2</td>
      <td>14.2</td>
      <td>1.8</td>
      <td>3.3</td>
      <td>.542</td>
      <td>...</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>2.0</td>
      <td>4.7</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>14092 rows × 33 columns</p>
</div>



* Cleaning the team data

Next step is combined the player data and mvps with the team sheet data


```python
teams = pd.read_csv("teams.csv")
```


```python
teams.head(30)
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
      <th>Unnamed: 0</th>
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
      <td>0</td>
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
      <td>1</td>
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
      <td>2</td>
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
      <td>3</td>
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
      <td>4</td>
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
    <tr>
      <th>5</th>
      <td>5</td>
      <td>24</td>
      <td>58</td>
      <td>.293</td>
      <td>32.0</td>
      <td>101.8</td>
      <td>107.8</td>
      <td>-5.91</td>
      <td>1991</td>
      <td>Miami Heat</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Central Division</td>
      <td>Central Division</td>
      <td>Central Division</td>
      <td>Central Division</td>
      <td>Central Division</td>
      <td>Central Division</td>
      <td>Central Division</td>
      <td>1991</td>
      <td>Central Division</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>61</td>
      <td>21</td>
      <td>.744</td>
      <td>—</td>
      <td>110.0</td>
      <td>101.0</td>
      <td>8.57</td>
      <td>1991</td>
      <td>Chicago Bulls*</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>50</td>
      <td>32</td>
      <td>.610</td>
      <td>11.0</td>
      <td>100.1</td>
      <td>96.8</td>
      <td>3.08</td>
      <td>1991</td>
      <td>Detroit Pistons*</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>48</td>
      <td>34</td>
      <td>.585</td>
      <td>13.0</td>
      <td>106.4</td>
      <td>104.0</td>
      <td>2.33</td>
      <td>1991</td>
      <td>Milwaukee Bucks*</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>43</td>
      <td>39</td>
      <td>.524</td>
      <td>18.0</td>
      <td>109.8</td>
      <td>109.0</td>
      <td>0.72</td>
      <td>1991</td>
      <td>Atlanta Hawks*</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>41</td>
      <td>41</td>
      <td>.500</td>
      <td>20.0</td>
      <td>111.7</td>
      <td>112.1</td>
      <td>-0.37</td>
      <td>1991</td>
      <td>Indiana Pacers*</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>33</td>
      <td>49</td>
      <td>.402</td>
      <td>28.0</td>
      <td>101.7</td>
      <td>104.2</td>
      <td>-2.33</td>
      <td>1991</td>
      <td>Cleveland Cavaliers</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>26</td>
      <td>56</td>
      <td>.317</td>
      <td>35.0</td>
      <td>102.8</td>
      <td>108.0</td>
      <td>-4.95</td>
      <td>1991</td>
      <td>Charlotte Hornets</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0</td>
      <td>Midwest Division</td>
      <td>Midwest Division</td>
      <td>Midwest Division</td>
      <td>Midwest Division</td>
      <td>Midwest Division</td>
      <td>Midwest Division</td>
      <td>Midwest Division</td>
      <td>1991</td>
      <td>Midwest Division</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1</td>
      <td>55</td>
      <td>27</td>
      <td>.671</td>
      <td>—</td>
      <td>107.1</td>
      <td>102.6</td>
      <td>4.30</td>
      <td>1991</td>
      <td>San Antonio Spurs*</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2</td>
      <td>54</td>
      <td>28</td>
      <td>.659</td>
      <td>1.0</td>
      <td>104.0</td>
      <td>100.7</td>
      <td>3.18</td>
      <td>1991</td>
      <td>Utah Jazz*</td>
    </tr>
    <tr>
      <th>17</th>
      <td>3</td>
      <td>52</td>
      <td>30</td>
      <td>.634</td>
      <td>3.0</td>
      <td>106.7</td>
      <td>103.2</td>
      <td>3.27</td>
      <td>1991</td>
      <td>Houston Rockets*</td>
    </tr>
    <tr>
      <th>18</th>
      <td>4</td>
      <td>31</td>
      <td>51</td>
      <td>.378</td>
      <td>24.0</td>
      <td>105.9</td>
      <td>109.9</td>
      <td>-3.79</td>
      <td>1991</td>
      <td>Orlando Magic</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5</td>
      <td>29</td>
      <td>53</td>
      <td>.354</td>
      <td>26.0</td>
      <td>99.6</td>
      <td>103.5</td>
      <td>-3.75</td>
      <td>1991</td>
      <td>Minnesota Timberwolves</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6</td>
      <td>28</td>
      <td>54</td>
      <td>.341</td>
      <td>27.0</td>
      <td>99.9</td>
      <td>104.5</td>
      <td>-4.27</td>
      <td>1991</td>
      <td>Dallas Mavericks</td>
    </tr>
    <tr>
      <th>21</th>
      <td>7</td>
      <td>20</td>
      <td>62</td>
      <td>.244</td>
      <td>35.0</td>
      <td>119.9</td>
      <td>130.8</td>
      <td>-10.31</td>
      <td>1991</td>
      <td>Denver Nuggets</td>
    </tr>
    <tr>
      <th>22</th>
      <td>8</td>
      <td>Pacific Division</td>
      <td>Pacific Division</td>
      <td>Pacific Division</td>
      <td>Pacific Division</td>
      <td>Pacific Division</td>
      <td>Pacific Division</td>
      <td>Pacific Division</td>
      <td>1991</td>
      <td>Pacific Division</td>
    </tr>
    <tr>
      <th>23</th>
      <td>9</td>
      <td>63</td>
      <td>19</td>
      <td>.768</td>
      <td>—</td>
      <td>114.7</td>
      <td>106.0</td>
      <td>8.47</td>
      <td>1991</td>
      <td>Portland Trail Blazers*</td>
    </tr>
    <tr>
      <th>24</th>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
      <td>1991</td>
      <td>Los Angeles Lakers*</td>
    </tr>
    <tr>
      <th>25</th>
      <td>11</td>
      <td>55</td>
      <td>27</td>
      <td>.671</td>
      <td>8.0</td>
      <td>114.0</td>
      <td>107.5</td>
      <td>6.49</td>
      <td>1991</td>
      <td>Phoenix Suns*</td>
    </tr>
    <tr>
      <th>26</th>
      <td>12</td>
      <td>44</td>
      <td>38</td>
      <td>.537</td>
      <td>19.0</td>
      <td>116.6</td>
      <td>115.0</td>
      <td>1.72</td>
      <td>1991</td>
      <td>Golden State Warriors*</td>
    </tr>
    <tr>
      <th>27</th>
      <td>13</td>
      <td>41</td>
      <td>41</td>
      <td>.500</td>
      <td>22.0</td>
      <td>106.6</td>
      <td>105.4</td>
      <td>1.31</td>
      <td>1991</td>
      <td>Seattle SuperSonics*</td>
    </tr>
    <tr>
      <th>28</th>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>.378</td>
      <td>32.0</td>
      <td>103.5</td>
      <td>107.0</td>
      <td>-3.16</td>
      <td>1991</td>
      <td>Los Angeles Clippers</td>
    </tr>
    <tr>
      <th>29</th>
      <td>15</td>
      <td>25</td>
      <td>57</td>
      <td>.305</td>
      <td>38.0</td>
      <td>96.7</td>
      <td>103.5</td>
      <td>-6.27</td>
      <td>1991</td>
      <td>Sacramento Kings</td>
    </tr>
  </tbody>
</table>
</div>




```python
teams = teams[~teams["W"].str.contains("Division")]
```


```python
teams.head(30)
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
      <th>Unnamed: 0</th>
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
      <td>0</td>
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
      <td>1</td>
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
      <td>2</td>
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
      <td>3</td>
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
      <td>4</td>
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
    <tr>
      <th>5</th>
      <td>5</td>
      <td>24</td>
      <td>58</td>
      <td>.293</td>
      <td>32.0</td>
      <td>101.8</td>
      <td>107.8</td>
      <td>-5.91</td>
      <td>1991</td>
      <td>Miami Heat</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>61</td>
      <td>21</td>
      <td>.744</td>
      <td>—</td>
      <td>110.0</td>
      <td>101.0</td>
      <td>8.57</td>
      <td>1991</td>
      <td>Chicago Bulls*</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>50</td>
      <td>32</td>
      <td>.610</td>
      <td>11.0</td>
      <td>100.1</td>
      <td>96.8</td>
      <td>3.08</td>
      <td>1991</td>
      <td>Detroit Pistons*</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>48</td>
      <td>34</td>
      <td>.585</td>
      <td>13.0</td>
      <td>106.4</td>
      <td>104.0</td>
      <td>2.33</td>
      <td>1991</td>
      <td>Milwaukee Bucks*</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>43</td>
      <td>39</td>
      <td>.524</td>
      <td>18.0</td>
      <td>109.8</td>
      <td>109.0</td>
      <td>0.72</td>
      <td>1991</td>
      <td>Atlanta Hawks*</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>41</td>
      <td>41</td>
      <td>.500</td>
      <td>20.0</td>
      <td>111.7</td>
      <td>112.1</td>
      <td>-0.37</td>
      <td>1991</td>
      <td>Indiana Pacers*</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>33</td>
      <td>49</td>
      <td>.402</td>
      <td>28.0</td>
      <td>101.7</td>
      <td>104.2</td>
      <td>-2.33</td>
      <td>1991</td>
      <td>Cleveland Cavaliers</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>26</td>
      <td>56</td>
      <td>.317</td>
      <td>35.0</td>
      <td>102.8</td>
      <td>108.0</td>
      <td>-4.95</td>
      <td>1991</td>
      <td>Charlotte Hornets</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1</td>
      <td>55</td>
      <td>27</td>
      <td>.671</td>
      <td>—</td>
      <td>107.1</td>
      <td>102.6</td>
      <td>4.30</td>
      <td>1991</td>
      <td>San Antonio Spurs*</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2</td>
      <td>54</td>
      <td>28</td>
      <td>.659</td>
      <td>1.0</td>
      <td>104.0</td>
      <td>100.7</td>
      <td>3.18</td>
      <td>1991</td>
      <td>Utah Jazz*</td>
    </tr>
    <tr>
      <th>17</th>
      <td>3</td>
      <td>52</td>
      <td>30</td>
      <td>.634</td>
      <td>3.0</td>
      <td>106.7</td>
      <td>103.2</td>
      <td>3.27</td>
      <td>1991</td>
      <td>Houston Rockets*</td>
    </tr>
    <tr>
      <th>18</th>
      <td>4</td>
      <td>31</td>
      <td>51</td>
      <td>.378</td>
      <td>24.0</td>
      <td>105.9</td>
      <td>109.9</td>
      <td>-3.79</td>
      <td>1991</td>
      <td>Orlando Magic</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5</td>
      <td>29</td>
      <td>53</td>
      <td>.354</td>
      <td>26.0</td>
      <td>99.6</td>
      <td>103.5</td>
      <td>-3.75</td>
      <td>1991</td>
      <td>Minnesota Timberwolves</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6</td>
      <td>28</td>
      <td>54</td>
      <td>.341</td>
      <td>27.0</td>
      <td>99.9</td>
      <td>104.5</td>
      <td>-4.27</td>
      <td>1991</td>
      <td>Dallas Mavericks</td>
    </tr>
    <tr>
      <th>21</th>
      <td>7</td>
      <td>20</td>
      <td>62</td>
      <td>.244</td>
      <td>35.0</td>
      <td>119.9</td>
      <td>130.8</td>
      <td>-10.31</td>
      <td>1991</td>
      <td>Denver Nuggets</td>
    </tr>
    <tr>
      <th>23</th>
      <td>9</td>
      <td>63</td>
      <td>19</td>
      <td>.768</td>
      <td>—</td>
      <td>114.7</td>
      <td>106.0</td>
      <td>8.47</td>
      <td>1991</td>
      <td>Portland Trail Blazers*</td>
    </tr>
    <tr>
      <th>24</th>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
      <td>1991</td>
      <td>Los Angeles Lakers*</td>
    </tr>
    <tr>
      <th>25</th>
      <td>11</td>
      <td>55</td>
      <td>27</td>
      <td>.671</td>
      <td>8.0</td>
      <td>114.0</td>
      <td>107.5</td>
      <td>6.49</td>
      <td>1991</td>
      <td>Phoenix Suns*</td>
    </tr>
    <tr>
      <th>26</th>
      <td>12</td>
      <td>44</td>
      <td>38</td>
      <td>.537</td>
      <td>19.0</td>
      <td>116.6</td>
      <td>115.0</td>
      <td>1.72</td>
      <td>1991</td>
      <td>Golden State Warriors*</td>
    </tr>
    <tr>
      <th>27</th>
      <td>13</td>
      <td>41</td>
      <td>41</td>
      <td>.500</td>
      <td>22.0</td>
      <td>106.6</td>
      <td>105.4</td>
      <td>1.31</td>
      <td>1991</td>
      <td>Seattle SuperSonics*</td>
    </tr>
    <tr>
      <th>28</th>
      <td>14</td>
      <td>31</td>
      <td>51</td>
      <td>.378</td>
      <td>32.0</td>
      <td>103.5</td>
      <td>107.0</td>
      <td>-3.16</td>
      <td>1991</td>
      <td>Los Angeles Clippers</td>
    </tr>
    <tr>
      <th>29</th>
      <td>15</td>
      <td>25</td>
      <td>57</td>
      <td>.305</td>
      <td>38.0</td>
      <td>96.7</td>
      <td>103.5</td>
      <td>-6.27</td>
      <td>1991</td>
      <td>Sacramento Kings</td>
    </tr>
    <tr>
      <th>30</th>
      <td>0</td>
      <td>51</td>
      <td>31</td>
      <td>.622</td>
      <td>—</td>
      <td>106.6</td>
      <td>103.0</td>
      <td>3.41</td>
      <td>1992</td>
      <td>Boston Celtics*</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1</td>
      <td>51</td>
      <td>31</td>
      <td>.622</td>
      <td>—</td>
      <td>101.6</td>
      <td>97.7</td>
      <td>3.67</td>
      <td>1992</td>
      <td>New York Knicks*</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2</td>
      <td>40</td>
      <td>42</td>
      <td>.488</td>
      <td>11.0</td>
      <td>105.4</td>
      <td>107.1</td>
      <td>-1.54</td>
      <td>1992</td>
      <td>New Jersey Nets*</td>
    </tr>
  </tbody>
</table>
</div>




```python
teams["Team"] = teams["Team"].str.replace("*", "", regex=False)
```


```python
teams.head(5)
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
      <th>Unnamed: 0</th>
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
      <td>0</td>
      <td>56</td>
      <td>26</td>
      <td>.683</td>
      <td>—</td>
      <td>111.5</td>
      <td>105.7</td>
      <td>5.22</td>
      <td>1991</td>
      <td>Boston Celtics</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>44</td>
      <td>38</td>
      <td>.537</td>
      <td>12.0</td>
      <td>105.4</td>
      <td>105.6</td>
      <td>-0.39</td>
      <td>1991</td>
      <td>Philadelphia 76ers</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>39</td>
      <td>43</td>
      <td>.476</td>
      <td>17.0</td>
      <td>103.1</td>
      <td>103.3</td>
      <td>-0.43</td>
      <td>1991</td>
      <td>New York Knicks</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
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
      <td>4</td>
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
teams["Team"].unique()
```




    array(['Boston Celtics', 'Philadelphia 76ers', 'New York Knicks',
           'Washington Bullets', 'New Jersey Nets', 'Miami Heat',
           'Chicago Bulls', 'Detroit Pistons', 'Milwaukee Bucks',
           'Atlanta Hawks', 'Indiana Pacers', 'Cleveland Cavaliers',
           'Charlotte Hornets', 'San Antonio Spurs', 'Utah Jazz',
           'Houston Rockets', 'Orlando Magic', 'Minnesota Timberwolves',
           'Dallas Mavericks', 'Denver Nuggets', 'Portland Trail Blazers',
           'Los Angeles Lakers', 'Phoenix Suns', 'Golden State Warriors',
           'Seattle SuperSonics', 'Los Angeles Clippers', 'Sacramento Kings',
           'Toronto Raptors', 'Vancouver Grizzlies', 'Washington Wizards',
           'Memphis Grizzlies', 'New Orleans Hornets', 'Charlotte Bobcats',
           'New Orleans/Oklahoma City Hornets', 'Oklahoma City Thunder',
           'Brooklyn Nets', 'New Orleans Pelicans'], dtype=object)




```python
combined["Tm"].unique()
```




    array(['LAL', 'PHO', 'DAL', 'MIA', 'CLE', 'WSB', 'CHI', 'GSW', 'IND',
           'WAS', 'MIN', 'BOS', 'HOU', 'DEN', 'ORL', 'NOH', 'TOR', 'SAC',
           'CHO', 'POR', 'DET', 'PHI', 'UTA', 'MIL', 'VAN', 'SEA', 'NJN',
           'NOK', 'LAC', 'OKC', 'ATL', 'CHA', 'MEM', 'NYK', 'NOP', 'BRK',
           'SAS', 'CHH'], dtype=object)



The team names in the COMBINED and TEAM data sheet are different (nickname and team name), the NICKNAME.TXTfile was used to adjust this error and not harm the merge.


```python
nicknames = {}

with open ("nicknames.txt") as f:
    lines = f.readlines()
```


```python
lines
```




    ['Abbreviation,Name\n',
     'ATL,Atlanta Hawks\n',
     'BRK,Brooklyn Nets\n',
     'BKN,Brooklyn Nets\n',
     'BOS,Boston Celtics\n',
     'CHA,Charlotte Bobcats\n',
     'CHH,Charlotte Hornets\n',
     'CHO,Charlotte Hornets\n',
     'CHI,Chicago Bulls\n',
     'CLE,Cleveland Cavaliers\n',
     'DAL,Dallas Mavericks\n',
     'DEN,Denver Nuggets\n',
     'DET,Detroit Pistons\n',
     'GSW,Golden State Warriors\n',
     'HOU,Houston Rockets\n',
     'IND,Indiana Pacers\n',
     'LAC,Los Angeles Clippers\n',
     'LAL,Los Angeles Lakers\n',
     'MEM,Memphis Grizzlies\n',
     'MIA,Miami Heat\n',
     'MIL,Milwaukee Bucks\n',
     'MIN,Minnesota Timberwolves\n',
     'NJN,New Jersey Nets\n',
     'NOH,New Orleans Hornets\n',
     'NOP,New Orleans Pelicans\n',
     'NOK,New Orleans/Oklahoma City Hornets\n',
     'NYK,New York Knicks\n',
     'OKC,Oklahoma City Thunder\n',
     'ORL,Orlando Magic\n',
     'PHI,Philadelphia 76ers\n',
     'PHX,Phoenix Suns\n',
     'PHO,Phoenix Suns\n',
     'POR,Portland Trail Blazers\n',
     'SEA,Seattle SuperSonics\n',
     'SAC,Sacramento Kings\n',
     'SAS,San Antonio Spurs\n',
     'TOR,Toronto Raptors\n',
     'UTA,Utah Jazz\n',
     'VAN,Vancouver Grizzlies\n',
     'WAS,Washington Wizards\n',
     'WSB,Washington Bullets']



Removal of the first line (header), and the strings "\n", ",".


```python
nicknames = {}

with open ("nicknames.txt") as f:
    lines = f.readlines()
    for line in lines[1:]:
        abbrev, name = line.replace("\n","").split(",")
        nicknames[abbrev] = name
```

Dictionary that maps between abbreviations (KEY) and full names (VALOR).


```python
nicknames
```




    {'ATL': 'Atlanta Hawks',
     'BRK': 'Brooklyn Nets',
     'BKN': 'Brooklyn Nets',
     'BOS': 'Boston Celtics',
     'CHA': 'Charlotte Bobcats',
     'CHH': 'Charlotte Hornets',
     'CHO': 'Charlotte Hornets',
     'CHI': 'Chicago Bulls',
     'CLE': 'Cleveland Cavaliers',
     'DAL': 'Dallas Mavericks',
     'DEN': 'Denver Nuggets',
     'DET': 'Detroit Pistons',
     'GSW': 'Golden State Warriors',
     'HOU': 'Houston Rockets',
     'IND': 'Indiana Pacers',
     'LAC': 'Los Angeles Clippers',
     'LAL': 'Los Angeles Lakers',
     'MEM': 'Memphis Grizzlies',
     'MIA': 'Miami Heat',
     'MIL': 'Milwaukee Bucks',
     'MIN': 'Minnesota Timberwolves',
     'NJN': 'New Jersey Nets',
     'NOH': 'New Orleans Hornets',
     'NOP': 'New Orleans Pelicans',
     'NOK': 'New Orleans/Oklahoma City Hornets',
     'NYK': 'New York Knicks',
     'OKC': 'Oklahoma City Thunder',
     'ORL': 'Orlando Magic',
     'PHI': 'Philadelphia 76ers',
     'PHX': 'Phoenix Suns',
     'PHO': 'Phoenix Suns',
     'POR': 'Portland Trail Blazers',
     'SEA': 'Seattle SuperSonics',
     'SAC': 'Sacramento Kings',
     'SAS': 'San Antonio Spurs',
     'TOR': 'Toronto Raptors',
     'UTA': 'Utah Jazz',
     'VAN': 'Vancouver Grizzlies',
     'WAS': 'Washington Wizards',
     'WSB': 'Washington Bullets'}



MAP function to convert and create a full name column


```python
combined["Tm"].map(nicknames)
```




    0          Los Angeles Lakers
    1          Los Angeles Lakers
    2          Los Angeles Lakers
    3                Phoenix Suns
    4                Phoenix Suns
                     ...         
    14087         Detroit Pistons
    14088         Detroit Pistons
    14089           Atlanta Hawks
    14090    Los Angeles Clippers
    14091    Los Angeles Clippers
    Name: Tm, Length: 14092, dtype: object




```python
combined["Team"] = combined["Tm"].map(nicknames)
```


```python
combined.head(5)
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>9.1</td>
      <td>1991</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>28</td>
      <td>LAL</td>
      <td>82</td>
      <td>53</td>
      <td>35.4</td>
      <td>4.7</td>
      <td>9.8</td>
      <td>.476</td>
      <td>...</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>13.6</td>
      <td>1992</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>55</td>
      <td>34.4</td>
      <td>4.6</td>
      <td>8.6</td>
      <td>.537</td>
      <td>...</td>
      <td>1.1</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>12.8</td>
      <td>1993</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>30</td>
      <td>PHO</td>
      <td>82</td>
      <td>55</td>
      <td>34.5</td>
      <td>5.7</td>
      <td>11.3</td>
      <td>.502</td>
      <td>...</td>
      <td>0.9</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>14.7</td>
      <td>1994</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Phoenix Suns</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A.C. Green</td>
      <td>SF</td>
      <td>31</td>
      <td>PHO</td>
      <td>82</td>
      <td>52</td>
      <td>32.8</td>
      <td>3.8</td>
      <td>7.5</td>
      <td>.504</td>
      <td>...</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>11.2</td>
      <td>1995</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Phoenix Suns</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>



Merge of the "team" and combined table, external and for each combined row, a new row of teams will be added that corresponds to the record of losses and wins


```python
stats = combined.merge(teams, how="outer", on=["Team", "Year"])
```


```python
stats
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>Share</th>
      <th>Team</th>
      <th>Unnamed: 0</th>
      <th>W</th>
      <th>L</th>
      <th>W/L%</th>
      <th>GB</th>
      <th>PS/G</th>
      <th>PA/G</th>
      <th>SRS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Byron Scott</td>
      <td>SG</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>82</td>
      <td>32.1</td>
      <td>6.1</td>
      <td>12.8</td>
      <td>.477</td>
      <td>...</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Elden Campbell</td>
      <td>PF</td>
      <td>22</td>
      <td>LAL</td>
      <td>52</td>
      <td>0</td>
      <td>7.3</td>
      <td>1.1</td>
      <td>2.4</td>
      <td>.455</td>
      <td>...</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Irving Thomas</td>
      <td>PF</td>
      <td>25</td>
      <td>LAL</td>
      <td>26</td>
      <td>0</td>
      <td>4.2</td>
      <td>0.7</td>
      <td>1.9</td>
      <td>.340</td>
      <td>...</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>James Worthy</td>
      <td>SF</td>
      <td>29</td>
      <td>LAL</td>
      <td>78</td>
      <td>74</td>
      <td>38.6</td>
      <td>9.2</td>
      <td>18.7</td>
      <td>.492</td>
      <td>...</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>10</td>
      <td>58</td>
      <td>24</td>
      <td>.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
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
      <th>14087</th>
      <td>Spencer Hawes</td>
      <td>PF</td>
      <td>28</td>
      <td>MIL</td>
      <td>54</td>
      <td>1</td>
      <td>14.8</td>
      <td>2.5</td>
      <td>5.1</td>
      <td>.484</td>
      <td>...</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>7</td>
      <td>42</td>
      <td>40</td>
      <td>.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14088</th>
      <td>Steve Novak</td>
      <td>PF</td>
      <td>33</td>
      <td>MIL</td>
      <td>8</td>
      <td>0</td>
      <td>2.8</td>
      <td>0.3</td>
      <td>0.9</td>
      <td>.286</td>
      <td>...</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>7</td>
      <td>42</td>
      <td>40</td>
      <td>.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14089</th>
      <td>Terrence Jones</td>
      <td>PF</td>
      <td>25</td>
      <td>MIL</td>
      <td>54</td>
      <td>12</td>
      <td>23.5</td>
      <td>4.3</td>
      <td>9.1</td>
      <td>.470</td>
      <td>...</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>7</td>
      <td>42</td>
      <td>40</td>
      <td>.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14090</th>
      <td>Thon Maker</td>
      <td>C</td>
      <td>19</td>
      <td>MIL</td>
      <td>57</td>
      <td>34</td>
      <td>9.9</td>
      <td>1.5</td>
      <td>3.2</td>
      <td>.459</td>
      <td>...</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>7</td>
      <td>42</td>
      <td>40</td>
      <td>.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14091</th>
      <td>Tony Snell</td>
      <td>SG</td>
      <td>25</td>
      <td>MIL</td>
      <td>80</td>
      <td>80</td>
      <td>29.2</td>
      <td>3.1</td>
      <td>6.8</td>
      <td>.455</td>
      <td>...</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>7</td>
      <td>42</td>
      <td>40</td>
      <td>.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
  </tbody>
</table>
<p>14092 rows × 42 columns</p>
</div>




```python
combined
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>Year</th>
      <th>Pts Won</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>.476</td>
      <td>...</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>1.2</td>
      <td>1.4</td>
      <td>9.1</td>
      <td>1991</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>28</td>
      <td>LAL</td>
      <td>82</td>
      <td>53</td>
      <td>35.4</td>
      <td>4.7</td>
      <td>9.8</td>
      <td>.476</td>
      <td>...</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>13.6</td>
      <td>1992</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>55</td>
      <td>34.4</td>
      <td>4.6</td>
      <td>8.6</td>
      <td>.537</td>
      <td>...</td>
      <td>1.1</td>
      <td>0.5</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>12.8</td>
      <td>1993</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>30</td>
      <td>PHO</td>
      <td>82</td>
      <td>55</td>
      <td>34.5</td>
      <td>5.7</td>
      <td>11.3</td>
      <td>.502</td>
      <td>...</td>
      <td>0.9</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>14.7</td>
      <td>1994</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Phoenix Suns</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A.C. Green</td>
      <td>SF</td>
      <td>31</td>
      <td>PHO</td>
      <td>82</td>
      <td>52</td>
      <td>32.8</td>
      <td>3.8</td>
      <td>7.5</td>
      <td>.504</td>
      <td>...</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>11.2</td>
      <td>1995</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Phoenix Suns</td>
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
      <th>14087</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>29</td>
      <td>DET</td>
      <td>74</td>
      <td>4</td>
      <td>15.9</td>
      <td>2.6</td>
      <td>5.1</td>
      <td>.505</td>
      <td>...</td>
      <td>0.4</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2002</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Detroit Pistons</td>
    </tr>
    <tr>
      <th>14088</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>30</td>
      <td>DET</td>
      <td>30</td>
      <td>12</td>
      <td>16.3</td>
      <td>2.7</td>
      <td>4.8</td>
      <td>.552</td>
      <td>...</td>
      <td>0.2</td>
      <td>0.6</td>
      <td>1.0</td>
      <td>2.6</td>
      <td>6.6</td>
      <td>2003</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Detroit Pistons</td>
    </tr>
    <tr>
      <th>14089</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>31</td>
      <td>ATL</td>
      <td>24</td>
      <td>2</td>
      <td>11.4</td>
      <td>1.4</td>
      <td>3.2</td>
      <td>.442</td>
      <td>...</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>2.2</td>
      <td>3.8</td>
      <td>2004</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Atlanta Hawks</td>
    </tr>
    <tr>
      <th>14090</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>32</td>
      <td>LAC</td>
      <td>58</td>
      <td>2</td>
      <td>16.0</td>
      <td>2.3</td>
      <td>4.0</td>
      <td>.568</td>
      <td>...</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>2.2</td>
      <td>5.8</td>
      <td>2005</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Clippers</td>
    </tr>
    <tr>
      <th>14091</th>
      <td>Željko Rebrača</td>
      <td>C</td>
      <td>33</td>
      <td>LAC</td>
      <td>29</td>
      <td>2</td>
      <td>14.2</td>
      <td>1.8</td>
      <td>3.3</td>
      <td>.542</td>
      <td>...</td>
      <td>0.2</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>2.0</td>
      <td>4.7</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Clippers</td>
    </tr>
  </tbody>
</table>
<p>14092 rows × 34 columns</p>
</div>



Same number of rows, it can mean that the merge was successful, but it is necessary to observe the data to ensure.


```python
del stats["Unnamed: 0"]
```


```python
stats.dtypes
```




    Player      object
    Pos         object
    Age         object
    Tm          object
    G           object
    GS          object
    MP          object
    FG          object
    FGA         object
    FG%         object
    3P          object
    3PA         object
    3P%         object
    2P          object
    2PA         object
    2P%         object
    eFG%        object
    FT          object
    FTA         object
    FT%         object
    ORB         object
    DRB         object
    TRB         object
    AST         object
    STL         object
    BLK         object
    TOV         object
    PF          object
    PTS         object
    Year         int64
    Pts Won    float64
    Pts Max    float64
    Share      float64
    Team        object
    W           object
    L           object
    W/L%        object
    GB          object
    PS/G        object
    PA/G        object
    SRS         object
    dtype: object



TO_NUMERIC function to evaluate all columns and convert to numeric, which cannot be ignored.


```python
stats = stats.apply(pd.to_numeric, errors="ignore")
```


```python
stats.dtypes
```




    Player      object
    Pos         object
    Age          int64
    Tm          object
    G            int64
    GS           int64
    MP         float64
    FG         float64
    FGA        float64
    FG%        float64
    3P         float64
    3PA        float64
    3P%        float64
    2P         float64
    2PA        float64
    2P%        float64
    eFG%       float64
    FT         float64
    FTA        float64
    FT%        float64
    ORB        float64
    DRB        float64
    TRB        float64
    AST        float64
    STL        float64
    BLK        float64
    TOV        float64
    PF         float64
    PTS        float64
    Year         int64
    Pts Won    float64
    Pts Max    float64
    Share      float64
    Team        object
    W            int64
    L            int64
    W/L%       float64
    GB          object
    PS/G       float64
    PA/G       float64
    SRS        float64
    dtype: object




```python
stats["GB"].unique()
```




    array(['5.0', '14.0', '23.0', '7.0', '—', '40.0', '42.0', '18.0', '6.0',
           '24.0', '26.0', '37.0', '29.0', '21.0', '28.0', '25.0', '8.0',
           '19.0', '1.0', '13.0', '17.0', '3.0', '15.0', '9.0', '2.0', '35.0',
           '20.0', '11.0', '16.0', '41.0', '12.0', '50.0', '10.0', '30.0',
           '34.0', '4.0', '1.5', '22.0', '51.0', '36.0', '43.0', '39.0',
           '18.5', '48.0', '46.0', '10.5', '32.0', '38.0', '27.0', '33.0',
           '31.0', '21.5', '45.0', '22.5', '25.5', '3.5', '20.5', '11.5',
           '44.0', '52.0', '56.0', '2.5', '12.5', '47.0', '32.5', '4.5'],
          dtype=object)




```python
stats["GB"] = stats["GB"].str.replace('—', "0")
```


```python
stats["GB"].unique()
```




    array(['5.0', '14.0', '23.0', '7.0', '0', '40.0', '42.0', '18.0', '6.0',
           '24.0', '26.0', '37.0', '29.0', '21.0', '28.0', '25.0', '8.0',
           '19.0', '1.0', '13.0', '17.0', '3.0', '15.0', '9.0', '2.0', '35.0',
           '20.0', '11.0', '16.0', '41.0', '12.0', '50.0', '10.0', '30.0',
           '34.0', '4.0', '1.5', '22.0', '51.0', '36.0', '43.0', '39.0',
           '18.5', '48.0', '46.0', '10.5', '32.0', '38.0', '27.0', '33.0',
           '31.0', '21.5', '45.0', '22.5', '25.5', '3.5', '20.5', '11.5',
           '44.0', '52.0', '56.0', '2.5', '12.5', '47.0', '32.5', '4.5'],
          dtype=object)




```python
stats["GB"] = pd.to_numeric(stats["GB"])
```


```python
stats
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>Team</th>
      <th>W</th>
      <th>L</th>
      <th>W/L%</th>
      <th>GB</th>
      <th>PS/G</th>
      <th>PA/G</th>
      <th>SRS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A.C. Green</td>
      <td>PF</td>
      <td>27</td>
      <td>LAL</td>
      <td>82</td>
      <td>21</td>
      <td>26.4</td>
      <td>3.1</td>
      <td>6.6</td>
      <td>0.476</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>58</td>
      <td>24</td>
      <td>0.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Byron Scott</td>
      <td>SG</td>
      <td>29</td>
      <td>LAL</td>
      <td>82</td>
      <td>82</td>
      <td>32.1</td>
      <td>6.1</td>
      <td>12.8</td>
      <td>0.477</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>58</td>
      <td>24</td>
      <td>0.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Elden Campbell</td>
      <td>PF</td>
      <td>22</td>
      <td>LAL</td>
      <td>52</td>
      <td>0</td>
      <td>7.3</td>
      <td>1.1</td>
      <td>2.4</td>
      <td>0.455</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>58</td>
      <td>24</td>
      <td>0.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Irving Thomas</td>
      <td>PF</td>
      <td>25</td>
      <td>LAL</td>
      <td>26</td>
      <td>0</td>
      <td>4.2</td>
      <td>0.7</td>
      <td>1.9</td>
      <td>0.340</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>58</td>
      <td>24</td>
      <td>0.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>James Worthy</td>
      <td>SF</td>
      <td>29</td>
      <td>LAL</td>
      <td>78</td>
      <td>74</td>
      <td>38.6</td>
      <td>9.2</td>
      <td>18.7</td>
      <td>0.492</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Los Angeles Lakers</td>
      <td>58</td>
      <td>24</td>
      <td>0.707</td>
      <td>5.0</td>
      <td>106.3</td>
      <td>99.6</td>
      <td>6.73</td>
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
      <th>14087</th>
      <td>Spencer Hawes</td>
      <td>PF</td>
      <td>28</td>
      <td>MIL</td>
      <td>54</td>
      <td>1</td>
      <td>14.8</td>
      <td>2.5</td>
      <td>5.1</td>
      <td>0.484</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14088</th>
      <td>Steve Novak</td>
      <td>PF</td>
      <td>33</td>
      <td>MIL</td>
      <td>8</td>
      <td>0</td>
      <td>2.8</td>
      <td>0.3</td>
      <td>0.9</td>
      <td>0.286</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14089</th>
      <td>Terrence Jones</td>
      <td>PF</td>
      <td>25</td>
      <td>MIL</td>
      <td>54</td>
      <td>12</td>
      <td>23.5</td>
      <td>4.3</td>
      <td>9.1</td>
      <td>0.470</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14090</th>
      <td>Thon Maker</td>
      <td>C</td>
      <td>19</td>
      <td>MIL</td>
      <td>57</td>
      <td>34</td>
      <td>9.9</td>
      <td>1.5</td>
      <td>3.2</td>
      <td>0.459</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <th>14091</th>
      <td>Tony Snell</td>
      <td>SG</td>
      <td>25</td>
      <td>MIL</td>
      <td>80</td>
      <td>80</td>
      <td>29.2</td>
      <td>3.1</td>
      <td>6.8</td>
      <td>0.455</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Milwaukee Bucks</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>9.0</td>
      <td>103.6</td>
      <td>103.8</td>
      <td>-0.45</td>
    </tr>
  </tbody>
</table>
<p>14092 rows × 41 columns</p>
</div>



* Combining the team, player and MVPs data


```python
stats.to_csv("player_mvp_stats.csv")
```

* Exploring the NBA data

Who scored the most points in the entire dataset?


```python
highest_scoring = stats[stats["G"] > 70].sort_values("PTS", ascending=False).head(10)
```


```python
highest_scoring
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
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>...</th>
      <th>Pts Max</th>
      <th>Share</th>
      <th>Team</th>
      <th>W</th>
      <th>L</th>
      <th>W/L%</th>
      <th>GB</th>
      <th>PS/G</th>
      <th>PA/G</th>
      <th>SRS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9634</th>
      <td>James Harden</td>
      <td>PG</td>
      <td>29</td>
      <td>HOU</td>
      <td>78</td>
      <td>78</td>
      <td>36.8</td>
      <td>10.8</td>
      <td>24.5</td>
      <td>0.442</td>
      <td>...</td>
      <td>1010.0</td>
      <td>0.768</td>
      <td>Houston Rockets</td>
      <td>53</td>
      <td>29</td>
      <td>0.646</td>
      <td>0.0</td>
      <td>113.9</td>
      <td>109.1</td>
      <td>4.96</td>
    </tr>
    <tr>
      <th>1051</th>
      <td>Kobe Bryant</td>
      <td>SG</td>
      <td>27</td>
      <td>LAL</td>
      <td>80</td>
      <td>80</td>
      <td>41.0</td>
      <td>12.2</td>
      <td>27.2</td>
      <td>0.450</td>
      <td>...</td>
      <td>1250.0</td>
      <td>0.386</td>
      <td>Los Angeles Lakers</td>
      <td>45</td>
      <td>37</td>
      <td>0.549</td>
      <td>9.0</td>
      <td>99.4</td>
      <td>96.9</td>
      <td>2.53</td>
    </tr>
    <tr>
      <th>4425</th>
      <td>Allen Iverson</td>
      <td>PG</td>
      <td>30</td>
      <td>PHI</td>
      <td>72</td>
      <td>72</td>
      <td>43.1</td>
      <td>11.3</td>
      <td>25.3</td>
      <td>0.447</td>
      <td>...</td>
      <td>1250.0</td>
      <td>0.001</td>
      <td>Philadelphia 76ers</td>
      <td>38</td>
      <td>44</td>
      <td>0.463</td>
      <td>11.0</td>
      <td>99.4</td>
      <td>101.3</td>
      <td>-2.10</td>
    </tr>
    <tr>
      <th>9953</th>
      <td>Michael Jordan</td>
      <td>SG</td>
      <td>29</td>
      <td>CHI</td>
      <td>78</td>
      <td>78</td>
      <td>39.3</td>
      <td>12.7</td>
      <td>25.7</td>
      <td>0.495</td>
      <td>...</td>
      <td>980.0</td>
      <td>0.577</td>
      <td>Chicago Bulls</td>
      <td>57</td>
      <td>25</td>
      <td>0.695</td>
      <td>0.0</td>
      <td>105.2</td>
      <td>98.9</td>
      <td>6.19</td>
    </tr>
    <tr>
      <th>6871</th>
      <td>Tracy McGrady</td>
      <td>SG</td>
      <td>23</td>
      <td>ORL</td>
      <td>75</td>
      <td>74</td>
      <td>39.4</td>
      <td>11.1</td>
      <td>24.2</td>
      <td>0.457</td>
      <td>...</td>
      <td>1190.0</td>
      <td>0.359</td>
      <td>Orlando Magic</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>7.0</td>
      <td>98.5</td>
      <td>98.4</td>
      <td>-0.39</td>
    </tr>
    <tr>
      <th>6300</th>
      <td>Kevin Durant</td>
      <td>SF</td>
      <td>25</td>
      <td>OKC</td>
      <td>81</td>
      <td>81</td>
      <td>38.5</td>
      <td>10.5</td>
      <td>20.8</td>
      <td>0.503</td>
      <td>...</td>
      <td>1250.0</td>
      <td>0.986</td>
      <td>Oklahoma City Thunder</td>
      <td>59</td>
      <td>23</td>
      <td>0.720</td>
      <td>0.0</td>
      <td>106.2</td>
      <td>99.8</td>
      <td>6.66</td>
    </tr>
    <tr>
      <th>6352</th>
      <td>Russell Westbrook</td>
      <td>PG</td>
      <td>28</td>
      <td>OKC</td>
      <td>81</td>
      <td>81</td>
      <td>34.6</td>
      <td>10.2</td>
      <td>24.0</td>
      <td>0.425</td>
      <td>...</td>
      <td>1010.0</td>
      <td>0.879</td>
      <td>Oklahoma City Thunder</td>
      <td>47</td>
      <td>35</td>
      <td>0.573</td>
      <td>4.0</td>
      <td>106.6</td>
      <td>105.8</td>
      <td>1.14</td>
    </tr>
    <tr>
      <th>1065</th>
      <td>Kobe Bryant</td>
      <td>SG</td>
      <td>28</td>
      <td>LAL</td>
      <td>77</td>
      <td>77</td>
      <td>40.8</td>
      <td>10.6</td>
      <td>22.8</td>
      <td>0.463</td>
      <td>...</td>
      <td>1290.0</td>
      <td>0.404</td>
      <td>Los Angeles Lakers</td>
      <td>42</td>
      <td>40</td>
      <td>0.512</td>
      <td>19.0</td>
      <td>103.3</td>
      <td>103.4</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>9927</th>
      <td>Michael Jordan</td>
      <td>SG</td>
      <td>27</td>
      <td>CHI</td>
      <td>82</td>
      <td>82</td>
      <td>37.0</td>
      <td>12.1</td>
      <td>22.4</td>
      <td>0.539</td>
      <td>...</td>
      <td>960.0</td>
      <td>0.928</td>
      <td>Chicago Bulls</td>
      <td>61</td>
      <td>21</td>
      <td>0.744</td>
      <td>0.0</td>
      <td>110.0</td>
      <td>101.0</td>
      <td>8.57</td>
    </tr>
    <tr>
      <th>3263</th>
      <td>LeBron James</td>
      <td>SF</td>
      <td>21</td>
      <td>CLE</td>
      <td>79</td>
      <td>79</td>
      <td>42.5</td>
      <td>11.1</td>
      <td>23.1</td>
      <td>0.480</td>
      <td>...</td>
      <td>1250.0</td>
      <td>0.550</td>
      <td>Cleveland Cavaliers</td>
      <td>50</td>
      <td>32</td>
      <td>0.610</td>
      <td>14.0</td>
      <td>97.6</td>
      <td>95.4</td>
      <td>2.17</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 41 columns</p>
</div>




```python
highest_scoring.plot.bar("Player", "PTS")
```




    <AxesSubplot:xlabel='Player'>




    
![png](output_70_1.png)
    


Who had the highest score per year?


```python
highest_scoring = stats.groupby("Year").apply(lambda x: x.sort_values("PTS", ascending=False).head(1))
```


```python
highest_scoring.plot.bar("Year", "PTS")
```




    <AxesSubplot:xlabel='Year'>




    
![png](output_73_1.png)
    



```python
stats.corr()["Share"]
```




    Age        0.018596
    G          0.089282
    GS         0.167476
    MP         0.162175
    FG         0.276365
    FGA        0.249254
    FG%        0.065789
    3P         0.096225
    3PA        0.096460
    3P%        0.013611
    2P         0.275976
    2PA        0.251885
    2P%        0.063240
    eFG%       0.059335
    FT         0.316392
    FTA        0.321457
    FT%        0.037875
    ORB        0.101375
    DRB        0.213241
    TRB        0.186209
    AST        0.200253
    STL        0.175041
    BLK        0.154713
    TOV        0.233015
    PF         0.071046
    PTS        0.288267
    Year      -0.008135
    Pts Won    0.995153
    Pts Max    0.521335
    Share      1.000000
    W          0.122718
    L         -0.121866
    W/L%       0.126559
    GB        -0.101014
    PS/G       0.045206
    PA/G      -0.039617
    SRS        0.122782
    Name: Share, dtype: float64




```python
stats.corr()["Share"].plot.bar()
```




    <AxesSubplot:>




    
![png](output_75_1.png)
    


Next step is Machine Learning! =)


```python

```
