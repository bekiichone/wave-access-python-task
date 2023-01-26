# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import numpy as np
import pandas as pd

class StatSum:
    def __init__(self, df):
        self.__df = df

    def summary(self):
        pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Statistical Summary')
    parser.add_argument('input_filename',
                        type=str,
                        help='an input CSV file')
    parser.add_argument('output_filename',
                        type=str,
                        help='a name of file to be generated')
    parser.add_argument('--type',
                        dest='output_type',
                        type=str,
                        choices=['markdown', 'html', 'xlsx'],
                        help='an output type')
    args = parser.parse_args()
    df = pd.read_csv(args.input_filename)
    print(df.info())
    res = StatSum(df)

