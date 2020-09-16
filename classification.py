# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:48:03 2018

@author: Kaushal
"""
import numpy as np

def distance(p1,p2):
    """Finds the distance between points p1 and p2"""
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

import random

def majority_vote(votes):
    """
    Return the most common element in votes
    """
    vote_counts = {}
    for vote in votes:
        #known word
        if vote in vote_counts:
            vote_counts[vote] += 1
        #unknown word
        else:
            vote_counts[vote] = 1    
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)
    
import scipy.stats as ss
def majority_vote_short(votes):
    """
    Return the most common element in votes
    """
    mode, count = ss.mstats.mode(votes)
    return mode


#loop over all points
    #compute the distance between point p and every other point
#sort distances and return thosek points that are nearest to point p

def find_nearest_neighbors(p, points, k=5): 
    """Find the k nearest neighbors of the point p and return their indices"""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
         distances[i] = distance(p,points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    #find k nearest neighbors
    ind = find_nearest_neighbors(p, points, k)
    #predict the class or category of p based on majority vote
    return majority_vote(outcomes[ind])
    
outcomes = np.array([0,0,0,0,1,1,1,1,1])

knn_predict(np.array([2.5,2.7]), points, outcomes, k = 2)


ind = find_nearest_neighbors(p, points, 2); print(points[ind])

distances[ind]
distances[ind[0:2]]


points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])

p = np.array([2.5,2])

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])

 
p1 = np.array([1,1])
p2 = np.array([4,4])

distance(p1,p2)

votes = [1,2,3,1,2,3,1,2,3,3,3,3,3]
winner = majority_vote_short(votes)

def generate_synth_data(n=50):
    """ Create two sets of points from bivariate normal distributions; axis = 0because we are concatenating along rows (xx axis)"""
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    return (points, outcomes)

n = 20
(points, outcomes) = generate_synth_data(n = 20)

plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.savefig("bivardata.pdf")

##Meshgrid
#Meshgrid takes in two or more cordinate vectors, say one vector containg the x values
# of interest and the other containing y values of interest. It returns matrices the
# first containing the x values for each grid and the second containing the y values for each grid
# point

#Enumerate is used when we'd like to have acess simultaneously to two things-
# different elements in the seqquence as well as their index

#Enumerate example
seasons = ["spring", "summer", "fall", "winter"]
list(enumerate(seasons))

for ind, season in enumerate(seasons):
    print(ind, season)
#Example ends

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """Classify each point on the prediction grid"""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    #We next need to generate our classifiers prediction corresponding
    # to every point of the meshgrid
    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            #Note we are doing j, i here. This is because j corresponds to y values,
            #and when we specify and index using square brackets, the first value
            #the first argument corresponds to the row of the array. That's why we 
            #want to make sure that we assign y  values to the rows of the array
            #and the x values to the column of the array
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
            
    return (xx, yy, prediction_grid)

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)

(predictors, outcomes) = generate_synth_data()

k = 5; filename = "knn_synth_5.pdf"; limits = (-3, 4, -3, 4); h=0.1

(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)

plot_prediction_grid(xx, yy, prediction_grid, filename)

k = 1; filename = "knn_synth_1.pdf"; limits = (-3, 4, -3, 4); h=0.1

(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k = 1)

plot_prediction_grid(xx, yy, prediction_grid, filename)

#############
#Applying kNN method
#############

from sklearn import datasets

iris = datasets.load_iris()

predictors = iris.data[:,0:2]
outcomes = iris.target

plt.plot(predictors[outcomes ==0][:,0], predictors[outcomes ==0][:,1], "ro")
plt.plot(predictors[outcomes ==1][:,0], predictors[outcomes ==1][:,1], "go")
plt.plot(predictors[outcomes ==2][:,0], predictors[outcomes ==2][:,1], "bo")
plt.savefig("iris.pdf")

k = 5; filename = "iris_grid.pdf"; limits = (4, 8, 1.5, 4.5); h=0.1

(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)

plot_prediction_grid(xx, yy, prediction_grid, filename)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)
sk_predictions.shape
sk_predictions[0:10]


my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])

sk_predictions == my_predictions

print(100*np.mean(sk_predictions == my_predictions))

print(100*np.mean(sk_predictions == outcomes))

print(100*np.mean(outcomes == my_predictions))


{'52WeekChange': 0.5072191,
 'SandP52WeekChange': 0.13119566,
 'address1': 'One Microsoft Way',
 'algorithm': None,
 'annualHoldingsTurnover': None,
 'annualReportExpenseRatio': None,
 'ask': 0,
 'askSize': 1300,
 'averageDailyVolume10Day': 36636666,
 'averageVolume': 35006625,
 'averageVolume10days': 36636666,
 'beta': 0.893534,
 'beta3Year': None,
 'bid': 211.03,
 'bidSize': 800,
 'bookValue': 15.626,
 'category': None,
 'circulatingSupply': None,
 'city': 'Redmond',
 'companyOfficers': [],
 'country': 'United States',
 'currency': 'USD',
 'dateShortInterest': 1598832000,
 'dayHigh': 209.7799,
 'dayLow': 206.93,
 'dividendRate': 2.04,
 'dividendYield': 0.0098,
 'earningsQuarterlyGrowth': -0.151,
 'enterpriseToEbitda': 22.827,
 'enterpriseToRevenue': 10.416,
 'enterpriseValue': 1489646256128,
 'exDividendDate': 1597795200,
 'exchange': 'NMS',
 'exchangeTimezoneName': 'America/New_York',
 'exchangeTimezoneShortName': 'EDT',
 'expireDate': None,
 'fiftyDayAverage': 212.69771,
 'fiftyTwoWeekHigh': 232.86,
 'fiftyTwoWeekLow': 132.52,
 'fiveYearAverageReturn': None,
 'fiveYearAvgDividendYield': 1.83,
 'floatShares': 7455727348,
 'forwardEps': 7.34,
 'forwardPE': 28.444141,
 'fromCurrency': None,
 'fullTimeEmployees': 163000,
 'fundFamily': None,
 'fundInceptionDate': None,
 'gmtOffSetMilliseconds': '-14400000',
 'heldPercentInsiders': 0.014249999,
 'heldPercentInstitutions': 0.74093,
 'industry': 'Software—Infrastructure',
 'isEsgPopulated': False,
 'lastCapGain': None,
 'lastDividendValue': None,
 'lastFiscalYearEnd': 1593475200,
 'lastMarket': None,
 'lastSplitDate': 1045526400,
 'lastSplitFactor': '2:1',
 'legalType': None,
 'logo_url': 'https://logo.clearbit.com/microsoft.com',
 'longBusinessSummary': 'Microsoft Corporation develops, licenses, and '
                        'supports software, services, devices, and solutions '
                        'worldwide. Its Productivity and Business Processes '
                        'segment offers Office, Exchange, SharePoint, '
                        'Microsoft Teams, Office 365 Security and Compliance, '
                        'and Skype for Business, as well as related Client '
                        'Access Licenses (CAL); Skype, Outlook.com, and '
                        'OneDrive; LinkedIn that includes Talent, Learning, '
                        'Sales, and Marketing solutions, as well as premium '
                        'subscriptions; and Dynamics 365, a set of cloud-based '
                        'and on-premises business solutions for small and '
                        'medium businesses, large organizations, and divisions '
                        'of enterprises. Its Intelligent Cloud segment '
                        'licenses SQL and Windows Servers, Visual Studio, '
                        'System Center, and related CALs; GitHub that provides '
                        'a collaboration platform and code hosting service for '
                        'developers; and Azure, a cloud platform. It also '
                        'offers support services and Microsoft consulting '
                        'services to assist customers in developing, '
                        'deploying, and managing Microsoft server and desktop '
                        'solutions; and training and certification to '
                        'developers and IT professionals on various Microsoft '
                        'products. Its More Personal Computing segment '
                        'provides Windows original equipment manufacturer '
                        '(OEM) licensing and other non-volume licensing of the '
                        'Windows operating system; Windows Commercial, such as '
                        'volume licensing of the Windows operating system, '
                        'Windows cloud services, and other Windows commercial '
                        'offerings; patent licensing; Windows Internet of '
                        'Things; and MSN advertising. It also offers Surface, '
                        'PC accessories, PCs, tablets, gaming and '
                        'entertainment consoles, and other intelligent '
                        'devices; Gaming, including Xbox hardware, and Xbox '
                        'content and services; video games and third-party '
                        'video game royalties; and Search, including Bing and '
                        'Microsoft advertising. It sells its products through '
                        'OEMs, distributors, and resellers; and directly '
                        'through digital marketplaces, online stores, and '
                        'retail stores. The company was founded in 1975 and is '
                        'headquartered in Redmond, Washington.',
 'longName': 'Microsoft Corporation',
 'market': 'us_market',
 'marketCap': 1579973869568,
 'maxAge': 1,
 'maxSupply': None,
 'messageBoardId': 'finmb_21835',
 'morningStarOverallRating': None,
 'morningStarRiskRating': None,
 'mostRecentQuarter': 1593475200,
 'navPrice': None,
 'netIncomeToCommon': 44280999936,
 'nextFiscalYearEnd': 1656547200,
 'open': 208.42,
 'openInterest': None,
 'payoutRatio': 0.3455,
 'pegRatio': 2.13,
 'phone': '425-882-8080',
 'previousClose': 205.41,
 'priceHint': 2,
 'priceToBook': 13.361065,
 'priceToSalesTrailing12Months': 11.047609,
 'profitMargins': 0.30962,
 'quoteType': 'EQUITY',
 'regularMarketDayHigh': 209.7799,
 'regularMarketDayLow': 206.93,
 'regularMarketOpen': 208.42,
 'regularMarketPreviousClose': 205.41,
 'regularMarketPrice': 208.42,
 'regularMarketVolume': 21823942,
 'revenueQuarterlyGrowth': None,
 'sector': 'Technology',
 'sharesOutstanding': 7567649792,
 'sharesPercentSharesOut': 0.0047999998,
 'sharesShort': 36458662,
 'sharesShortPreviousMonthDate': 1596153600,
 'sharesShortPriorMonth': 36472205,
 'shortName': 'Microsoft Corporation',
 'shortPercentOfFloat': 0.0049,
 'shortRatio': 1.08,
 'startDate': None,
 'state': 'WA',
 'strikePrice': None,
 'symbol': 'MSFT',
 'threeYearAverageReturn': None,
 'toCurrency': None,
 'totalAssets': None,
 'tradeable': False,
 'trailingAnnualDividendRate': 2.04,
 'trailingAnnualDividendYield': 0.009931357,
 'trailingEps': 5.76,
 'trailingPE': 36.246525,
 'twoHundredDayAverage': 188.24246,
 'volume': 21823942,
 'volume24Hr': None,
 'volumeAllCurrencies': None,
 'website': 'http://www.microsoft.com',
 'yield': None,
 'ytdReturn': None,
 'zip': '98052-6399'}
