""" example case of StatSum class usage"""

from statsummary import StatSum
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('iris.data', names=['sepal_length',
                                         'sepal_width',
                                         'petal_length',
                                         'petal_width',
                                         'class'])

    summary = StatSum(df)
    # output type - markdown
    print(summary.summary())

    # output type - html
    summary.summary('html', 'summary.html')

    # output type - xlsx
    summary.summary('xlsx', 'summary.xlsx')