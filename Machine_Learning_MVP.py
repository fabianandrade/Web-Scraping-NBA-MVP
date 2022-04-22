#!/usr/bin/env python
# coding: utf-8

# Predicting the NBA MVP: Machine Learning Project [part 3 of 3]
# 
# * Reading the data into Pandas and cleaning it

# In[1]:


import pandas as pd


# In[2]:


stats = pd.read_csv("player_mvp_stats.csv")


# In[3]:


stats


# Column deletion Unnamed: 0

# In[4]:


del stats["Unnamed: 0"]


# Machine learning algorithms don't like to use null or missing values

# In[5]:


pd.isnull(stats)


# The SUM() will show the number of nulls in each column

# In[6]:


pd.isnull(stats).sum()


# Selection in the row statistic of columns with percentage of three null points, it probably means that the player did not try

# In[7]:


stats[pd.isnull(stats["3P%"])]


# Players with 3 point attempts at 0

# In[8]:


stats[pd.isnull(stats["3P%"])][["Player", "3PA"]]


# In[9]:


stats[pd.isnull(stats["FT%"])][["Player", "FTA"]]


# This shows us that all those players who had undefined or missing values in free throw percentage, had zero bid attempts.
# So let's replace all these percentages with zero, it's not technically correct, but in this case, if the player has zero percentage on three-point shots, he's not in the race for MVP.

# * Training a Machine Learning Model

# In[10]:


stats = stats.fillna(0)


# In[11]:


stats.columns


# All numeric columns will be used in the prediction, except 'Pts Won', 'Pts Max', 'Share', otherwise the algorithm will know what it is trying to predict.
# 'Share' is the percentage of votes the player has won.
# 'Pts Won' is correlated with 'Share', it's just the points earned divided by 'Pts Max'.
# 
# - PREDICTORS = Predicted percentage of MVP votes that someone got in a given year.

# In[12]:


predictors = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year','W', 'L', 'W/L%', 'GB', 'PS/G',
       'PA/G', 'SRS']


# Test to train data only from before 2021, this gives us MVP data and all player data before year 2021.

# In[13]:


train = stats[stats["Year"] < 2021]


# In[14]:


test = stats[stats["Year"] == 2021]


# Building the first machine learning using ridge regression, a form of linear regression designed to avoid overfitting

# In[15]:


from sklearn.linear_model import Ridge

reg = Ridge(alpha=.1)


# First ML model, using the PREDICTORS columns in the training datasets, to try to predict the share of an MVP vote that someone got and then we actually go ahead and make the predictions.

# reg.fit(train[predictors], train["Share"])

# In[16]:


reg.fit(train[predictors], train["Share"])


# In[17]:


predictions = reg.predict(test[predictors])


# In[18]:


predictions


# This is a Numpy array, so converted to a data frame in Pandas so it's easier to work with.

# In[19]:


predictions = pd.DataFrame(predictions, columns=["predictions"], index=test.index)


# In[20]:


predictions


# Comparing actual values with forecasts, combining "Player", "Share" and concatenating with current forecasts.

# In[21]:


combination = pd.concat([test[["Player", "Share"]], predictions], axis=1)


# In[22]:


combination


# Adjusting dataframe to only see players who actually won the MVP.

# In[23]:


combination.sort_values("Share", ascending=False).head(10)


# * Indentifying an error metric
# 
# Basically this functions equation value take the actual values and the predicted values of an average error metric.

# In[24]:


from sklearn.metrics import mean_squared_error

mean_squared_error(combination["Share"], combination["predictions"])


# But in this case it's not important because I don't need the actual values and 525 of the values are actually just zero because these players didn't get any MVP votes.
# So in this case this error metric doesn't make sense, because I'm just looking for the top five and best players in the ranking.

# In[25]:


combination["Share"].value_counts()


# In[26]:


actual = combination.sort_values("Share", ascending=False)
predicted = combination.sort_values("predictions", ascending=False)
actual["Rk"] = list(range(1,actual.shape[0]+1))
predicted["Predicted_Rk"] = list(range(1,predicted.shape[0]+1))


# In[27]:


combination.head(10)


# In[28]:


actual.merge(predicted, on="Player").head(5)


# There are large discrepancies in the difference between the predicted rating and the actual rating.
# It uses the error metric called average precision, it is not used much for regression ML because it deals with classification

# Trying to find out the top five players in MPV VOTING and how far you need to go in predictions to find them, so following the "Predicted_RK" column, Nikola Jokic needs to go down 3 predictions, Joel Embiid needs to go down 2, Stephen Curry needs to go down 6 and so on against.
# So, the logic would be to go through all the prediction lines and if the player in this line is in the top five we will give a credit of 1 for finding them, and if we don't find them a scene counter will be incremented.

# In[29]:


def find_ap(combination):
    actual = combination.sort_values("Share", ascending=False).head(5)
    predicted = combination.sort_values("predictions", ascending=False)
    ps = []
    found = 0
    seen = 1
    for index,row in predicted.iterrows():
        if row["Player"] in actual["Player"].values:
            found += 1
            ps.append(found / seen)
        seen += 1

    return sum(ps) / len(ps)


# In[30]:


find_ap(combination)


# * Implementing backtesting to predict each year

# So now there is a way to find the error.
# When running the algorithm for all years, it can be seen that it only has predictions for one year. A principle called back_testing is used to make predictions for most years.

# In[31]:


years = list(range(1991,2022))


# Training and test set: before 1997 is training set and 1997 test set

# In[32]:


aps = []
all_predictions = []
for year in years[5:]:
    train = stats[stats["Year"] < year]
    test = stats[stats["Year"] == year]
    reg.fit(train[predictors], train["Share"])
    predictions = reg.predict(test[predictors])
    predictions = pd.DataFrame(predictions, columns=["predictions"], index=test.index)
    combination = pd.concat([test[["Player", "Share"]], predictions], axis=1)
    all_predictions.append(combination)
    aps.append(find_ap(combination))
    


# In[33]:


sum(aps) / len(aps)


# In[34]:


def add_ranks(predictions):
    predictions = predictions.sort_values("predictions", ascending=False)
    predictions["Predicted_Rk"] = list(range(1,predictions.shape[0]+1))
    predictions = predictions.sort_values("Share", ascending=False)
    predictions["Rk"] = list(range(1,predictions.shape[0]+1))
    predictions["Diff"] = (predictions["Rk"] - predictions["Predicted_Rk"])
    return predictions


# In[35]:


add_ranks(all_predictions[1])


# In[36]:


def backtest(stats, model, years, predictors):
    aps = []
    all_predictions = []
    for year in years:
        train = stats[stats["Year"] < year]
        test = stats[stats["Year"] == year]
        model.fit(train[predictors],train["Share"])
        predictions = model.predict(test[predictors])
        predictions = pd.DataFrame(predictions, columns=["predictions"], index=test.index)
        combination = pd.concat([test[["Player", "Share"]], predictions], axis=1)
        combination = add_ranks(combination)
        all_predictions.append(combination)
        aps.append(find_ap(combination))
    return sum(aps) / len(aps), aps, pd.concat(all_predictions)


# In[37]:


mean_ap, aps, all_predictions = backtest(stats, reg, years[5:], predictors)


# In[38]:


mean_ap


# In[39]:


all_predictions[all_predictions["Rk"] < 5].sort_values("Diff").head(10)


# In[40]:


pd.concat([pd.Series(reg.coef_), pd.Series(predictors)], axis=1).sort_values(0, ascending=False)


# In[41]:


stat_ratios = stats[["PTS", "AST", "STL", "BLK", "3P", "Year"]].groupby("Year").apply(lambda x: x/x.mean())


# In[42]:


stats[["PTS_R", "AST_R", "STL_R", "BLK_R", "3P_R"]] = stat_ratios[["PTS", "AST", "STL", "BLK", "3P"]]


# In[43]:


predictors += ["PTS_R", "AST_R", "STL_R", "BLK_R", "3P_R"]


# In[44]:


mean_ap, aps, all_predictions = backtest(stats, reg, years[5:], predictors)


# In[45]:


mean_ap


# * Diagnosing model performance

# In[47]:


all_predictions[all_predictions["Rk"] <= 5].sort_values("Diff").head(10)


# In[50]:


pd.concat([pd.Series(reg.coef_), pd.Series(predictors)], axis=1).sort_values(0, ascending=False)


# * Adding more predictors

# In[55]:


stat_ratios = stats[["PTS", "AST", "STL", "BLK", "3P", "Year"]].groupby("Year").apply(lambda x: x/x.mean())


# In[57]:


stat_ratios


# In[58]:


stats[["PTS_T", "AST_R", "STL_R", "BLK_R", "3P_R"]] = stat_ratios[["PTS", "AST", "STL", "BLK", "3P"]]


# In[59]:


stats.head()


# In[60]:


predictors += ["PTS_R", "AST_R", "STL_R", "BLK_R", "3P_R"]


# In[61]:


mean_ap, aps, all_predictions = backtest(stats, reg, years[5:], predictors)


# In[62]:


mean_ap


# In[66]:


stats["Pos"].unique


# In[67]:


stats["NPos"] = stats["Pos"].astype("category").cat.codes
stats["NTm"] = stats["Tm"].astype("category").cat.codes


# In[69]:


stats.head(5)


# * Using a random forest model

# In[77]:


from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=50, random_state=1, min_samples_split=5)

mean_ap, aps, all_predictions = backtest(stats, rf, years[28:], predictors + ["NPos", "NTm"])


# In[78]:


mean_ap


# In[ ]:




