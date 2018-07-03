import numpy as np
import pandas as pd
import tensorflow as tf
from pandas.tseries.offsets import *

#http://pandas.pydata.org/pandas-docs/stable/timeseries.html#overview
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html
#http://pandas.pydata.org/pandas-docs/stable/timeseries.html#generating-ranges-of-timestamps
#http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects
#http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-offset-aliases

def getEmployeeData(startdatetimecheckin, startdatetimecheckout, count, employeename, label, randomCheckinMinsMean, randomCheckinMinsVariance, randomCheckoutMinsMean, randomCheckoutMinsVariance):
    "This function"
    nameColumn0 = pd.Series(np.array(employeename).repeat(count))

    startDatetimeCheckinColumn1 = pd.Series(pd.date_range(startdatetimecheckin, periods=count, freq='B'))
    randomMinsList = 10 * np.random.randn(count) + randomCheckinMinsMean
    randomMinsSeries = pd.Series(randomMinsList, dtype=int)
    for index, val in startDatetimeCheckinColumn1.iteritems():
        startDatetimeCheckinColumn1[index] = startDatetimeCheckinColumn1[index] + Minute(randomMinsSeries[index])

    startDatetimeCheckoutColumn2 = pd.Series(pd.date_range(startdatetimecheckout, periods=count, freq='B'))
    randomMinsList2 = randomCheckoutMinsVariance * np.random.randn(count) + randomCheckoutMinsMean
    randomMinsSeries2 = pd.Series(randomMinsList2, dtype=int)
    for index, val in startDatetimeCheckoutColumn2.iteritems():
        startDatetimeCheckoutColumn2[index] = startDatetimeCheckoutColumn2[index] + Minute(randomMinsSeries2[index])

    labelColumn3 = pd.Series(np.array(label).repeat(count))

    data = pd.DataFrame({'MemberID': nameColumn0, 'CheckIn': startDatetimeCheckinColumn1, 'CheckOut': startDatetimeCheckoutColumn2, 'HoursWorked': startDatetimeCheckoutColumn2 - startDatetimeCheckinColumn1, 'Class': labelColumn3})
    #print(data)
    return data


punctionalEmployeeData = getEmployeeData('2017-1-2 9:00:00', '2017-1-2 17:00:00', 25, 'Mike', 'punctual', 15, 10, 45, 10)
hardWorkerEraticEmployeeData = getEmployeeData('2017-1-2 9:00:00', '2017-1-2 17:00:00', 25, 'Tom', 'hw-eratic', 15, 100, 60, 100)
parttimerEmployeeData = getEmployeeData('2017-1-2 9:00:00', '2017-1-2 13:30:00', 25, 'Al', 'parttime', 60, 100, 60, 100)
badEmployeeData = getEmployeeData('2017-1-2 9:00:00', '2017-1-2 17:00:00', 25, 'Smith', 'bad', 200, 100, -100, 60)
learningData = pd.concat([punctionalEmployeeData, hardWorkerEraticEmployeeData, parttimerEmployeeData, badEmployeeData], ignore_index=True)
print(learningData)





