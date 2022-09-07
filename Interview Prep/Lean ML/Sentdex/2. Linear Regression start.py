import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

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
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume', 'label']]
df.dropna(inplace = True)

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X)
# y = np.array(df['label'])  no idea why sentdex used this

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
# clf = svm.SVR() for using a diff classifier
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)
