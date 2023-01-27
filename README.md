# Statistical Summarizer
I have created a class StatSum, which allows to produce statistical summary of input Pandas DataFrame 

## Requirements
All required packages are in requirements.txt

## How to Use
In 'main.py' script you can find an example of using the module.
First you have to create instance of class StatSum with attribue Pandas DataFrame. 
As an example I am using [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).
```python
summary = StatSum(df)
```
To produce statistical summary, call 'summary' method and provide output type either 'markdown', 'html' or 'xlsx'.
For 'html' and 'xlsx' prodive output filename.
```python
# output type - markdown
print(summary.summary())

# output type - html
summary.summary('html', 'summary.html')

# output type - xlsx
summary.summary('xlsx', 'summary.xlsx')
```
Summary output:

|              | class          | sepal_length   | sepal_width   | petal_length   | petal_width   |
|:-------------|:---------------|:---------------|:--------------|:---------------|:--------------|
| column type  | object         | float64        | float64       | float64        | float64       |
| count        | 150            | 150            | 150           | 150            | 150           |
| null count   | 0              | 0              | 0             | 0              | 0             |
| unique count | 3              | nan            | nan           | nan            | nan           |
| top          | Iris-virginica | nan            | nan           | nan            | nan           |
| freq         | 50             | nan            | nan           | nan            | nan           |
| mean         | nan            | 5.843          | 3.054         | 3.759          | 1.199         |
| var          | nan            | 0.686          | 0.188         | 3.113          | 0.582         |
| std          | nan            | 0.828          | 0.434         | 1.764          | 0.763         |
| mode         | nan            | 5.0            | 3.0           | 1.5            | 0.2           |
| min          | nan            | 4.3            | 2.0           | 1.0            | 0.1           |
| 25%          | nan            | 5.1            | 2.8           | 1.6            | 0.3           |
| 50%          | nan            | 5.8            | 3.0           | 4.35           | 1.3           |
| 75%          | nan            | 6.4            | 3.3           | 5.1            | 1.8           |
| max          | nan            | 7.9            | 4.4           | 6.9            | 2.5           |
| IQR          | nan            | 1.3            | 0.5           | 3.5            | 1.5           |
| CV           | nan            | 0.142          | 0.142         | 0.469          | 0.637         |
