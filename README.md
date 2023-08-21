# FoodHub
Food Aggregator Platform

Developer: David Holtkamp

Date: 08/20/2023

 ## **Summary** 

Provided a JSON document with data about the American restaurant industry. There are restaurants, cuisines offered by the restaurant, and menu/menu items for the restaurant. 

Tasked with building an ETL pipeline, and performing analysis on the resulting tables. 

Included here is:
- processor.py, the python script that loaded the data, made necessary transformations, and loaded the data into two separate csv's. 
- Two csv's, a restaurants table, and a menu_items table.
- SQL file where I did the analysis to return those Mediterranean restaurants that have dishes under $15.

## **Setup and Usage:** 
- Clone the repo onto your machine `git@github.com:david-holtkamp/FoodHub.git`
- Navigate to that repo
- Run the script by executing `python processor.py`

## **Notes:**
- Python Version 3.9.6
- Tested the SQL query by deploying a local Postgres instance and importing the csv's

## **TO-DO:**
- Given more time, I may have done some slight refactoring and further tested scalability of both script and SQL query. 
- Add unit testing
- Better documentation for methods
- Add logging statements

