## Exercise: Python Read Write File
1. [poem.txt](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/poem.txt) contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.



2. [stocks.csv](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/stocks.csv) contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file
with financial metrics such as pe ratio and price to book ratio. These are calculated as,
```
pe ratio = price / earnings per share
price to book ratio = price / book value
```


Your input format (stocks.csv) is,

|Company Name|Price|Earnings Per Share|Book Value|
|-------|----------|-------|----------|
|Reliance|1467|66|653|
|Tata Steel|391|89|572|

Output.csv should look like this,

|Company Name|PE Ratio|PB Ratio|
|-------|----------|-------|
|Reliance|22.23|2.25|
|Tata Steel|4.39|0.68|

[Solution](https://github.com/Siva-2004/Python-Learn-and-Practice/blob/main/Basic%20Problems/Reading%20and%20Writing%20files/Solution.ipynb)
