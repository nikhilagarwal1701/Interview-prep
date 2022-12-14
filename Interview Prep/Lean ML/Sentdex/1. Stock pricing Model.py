import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')
#df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
#high low percent
df['HL_PCT'] = ((df['Adj. High'] - df['Adj. Low']) / df['Adj. Low']) * 100
#percent change
df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']) * 100

#df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(0.001 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume', 'label']]
df.dropna(inplace = True)
print(df.head)
