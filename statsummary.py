import numpy as np
import pandas as pd

class StatSum:
    def __init__(self, df):
        self.df = df
    
    def summary(self, output_type='markdown', filename=None):
        if output_type not in ['markdown', 'html', 'xlsx']:
            raise ValueError("Invalid output type. Please specify 'markdown', 'html' or 'xlsx'")
            
        if not filename and output_type != 'markdown':
            raise ValueError("Please specify output filename for non-markdown output types")
        
        res_num = pd.DataFrame([])
        res_cat = pd.DataFrame([])
        num = self.df.select_dtypes(include='number')
        cat = self.df.select_dtypes(include='object')
        
        if not num.empty:
            res_num['column type'] = num.dtypes
            res_num['count'] = num.count()
            res_num['null count'] = num.isna().sum()
            res_num['mean'] = num.mean()
            res_num['var'] = num.std()**2
            res_num['std'] = num.std()
            res_num['mode'] = num.mode().T[0]
            res_num['min'] = num.min()
            res_num['25%'] = num.quantile(.25)
            res_num['50%'] = num.quantile(.50)
            res_num['75%'] = num.quantile(.75)
            res_num['max'] = num.max()
            res_num['IQR'] = num.quantile(.75) - num.quantile(.25)
            res_num['CV'] = res_num['std']/res_num['mean']
            res_num = res_num.round(3).T

        if not cat.empty:
            res_cat['column type'] = cat.dtypes
            res_cat['count'] = cat.count()
            res_cat['null count'] = cat.isna().sum()
            res_cat['unique count'] = cat.nunique()
            res_cat['top'] = cat.value_counts().idxmax()
            res_cat['freq'] = cat.value_counts()[0]
            res_cat = res_cat.T
        
        
        res = pd.concat([res_cat, res_num], axis=1)
        
        if output_type == 'markdown':
            return res.to_markdown()
        elif output_type == 'html':
            res.to_html(filename)
        else:
            res.to_excel(filename)
            
        return 
        
        