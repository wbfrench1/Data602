### Overview:
<p>This is a linear regression project that seeks to predict the cancer deathrate per 100,000 people in United States counties.  The project trains least squares models from both statsmodels and sklearn on a data set from data.world that includes 3047 county level observations and 31 numeric predictors.  The project steps through the process of creating a linear regression model. The Technical Notebook begins with an introduction to the project and steps through Exploratory Analysis, Data Cleaning, Feature Engineering, Modeling, and Results and Discussion.  The Technical Notebook hides much of the code through the use of a Utils.py file.  After training several models, the Best Fit Linear Regression Model is identified as using a subset of predictors that were identified as significant by the statsmodels linear regression model.  The final test model has a mean squared error of 17.75 as compared to a average deathrate of 178 and an R^2 of 0.46.  Given that cancer is a disease that the world has been fighting for years, a model with this level of prediction seems reasonable.</p>

### Goals:
<ol>
<li>Create a linear regression model that has significant coefficients</li>
<li>Identify the socio-economic variables that contributed most to the final model</li>
<li>Identify the socio-economic variables that were positively and negatively related to cancer deathrates</li>
<li>Learn how to correctly run and interpret a linear regression model</li>
<li>Identify potential problems with the linear regression model</li></ol>

### Motivation and Background
<p>Cancer is a disease that affects many people.  According to the American Cancer Society, 1.8 million people will be diagnosed with cancer in 2020 and 600,000 will die from the disease.  I was curious to discover if socio-economic factors could be used to identify communities at risk.</p>

### Data
<p><b>Data Source:</b> https://data.world/nrippner/ols-regression-challenge</p>
<p>The data consisted of 3047 observations; 33 predictors: 31 numeric predictors and 2 non-numeric predictors; and 1 response variable.  The data set was mostly clean but did contain some 'bad' data, including median ages in excess of 100 years and average household sizes less than 1.  The target variable had one outlier.  The variables themselves were socio-economic.  There were several 'disease' variables relating to cancer rates in the dataset, and I realized late in the process that they would distort my efforts to find significant non-disease related socio-economic factors.  That is to say the 'disease' variables had the largest coefficients in the model.</p>

### Table of Contents
<ol>
<li>Technical Notebook</li>
<li>Data Set</li>
<li>ReadMe</li>
<li>Power Point Presentation</li>
<li>YouTube Presentation: https://youtu.be/F2165qdX5SA</li>
<li>Utils.py</li>
<li>Miscellaneous</li>
<ol><li>Exploratory Data Analysis Notebook</li>
<li>Linear Model Notebook</li>
<li>Research Questions</li></ol></ol>

### Software Requirements
<ol>
<li>jupyter notebooks</li>
<li>pandas</li>
<li>matplotlib.pyplot</li>
<li>sklearn</li>
<li>statsmodels</li>
<li>numpy</li></ol>