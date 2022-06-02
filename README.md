# Crop Recommendation Engine


## Table of Content
  * [Demo](#demo)
  * [Problem Statement](#problem-statement)
  * [Approach](#approach)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Bugs & Logs](#bugs--logs)
  * [Contributors](#contributors)

## Demo
Link: [https://agricultural-crop-selector.herokuapp.com/](https://agricultural-crop-selector.herokuapp.com/)

![crop-recommedation-engine](https://user-images.githubusercontent.com/76767335/171604913-bb38b123-7b09-424b-b466-24407d865a46.gif)


## Problem Statement
Agricultural Production Optimization Engine/Crop Recommendation Engine

Problem Statement
     Build a Predictive Model so as to suggest the most suitable crops to grow based on the available Climitic and Soil condition

Goal - 
     To Achieve Precision Farming bt Optimising the Agricultural Production

## Approach
Data Exploration : Exploring dataset using pandas, numpy.

Feature Engineering : Removed missing values and created new features as per insights.

Model Building & Testing : Tried many machine learning algorithms and checked the base accuracy to find the best fit.

Pickle File : Created pickle file as per need.

Building web app : Building web app using python.

User Interface & deployment :  Created an UI that shows the output.
                          After that I have deployed project on heroku.
## Technologies Used
 
   1. Python 
   2. Pandas
   3. Numpy
   4. Sklearn
   5. matplotlib
   6. seaborn
   7. Flask

## Dataset
[Download here](https://github.com/Shankar297/Agreecultur-Production-Engine/blob/master/data.csv)

## Installation
Click here to install [python](https://www.python.org/downloads/). To install the required packages and libraries, run this pip command in the project directory after cloning the repository:
```bash
git clone https://github.com/Shankar297/Agreecultur-Production-Engine.git
```

```bash
pip install -r requirements.txt
```
If pip is not already installed, Follow this [link](https://pip.pypa.io/en/stable/installation/)

## Deployement on Heroku
Create a virtual app on Heroku website. You can either connect your github profile or download cli to manually deploy this project.
Follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Bugs & Logs

1. If you find a bug, kindly open an issue and it will be addressed as early as possible.
2. Under localhost, logging is performed for all the actions and its stored onto logs.txt file
3. When the app is deployed on heroku, logs can be viewed on  heroku dashboard or CLI.

## Contributors
  [Shankar Wagh](https://github.com/Shankar297)
