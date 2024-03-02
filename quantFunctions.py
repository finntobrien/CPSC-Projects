import numpy as np
import matplotlib.pyplot as plt
import math


def deleteUncommonDates(dict1, dict2):
    # Create a set of keys from dict1
    dict1_keys = set(dict1.keys())
    i = 0
    # Iterate through the keys of dict2
    for key in list(dict2.keys()):  # Using list() to create a copy of the keys for safe iteration
        # If the key from dict2 is not in dict1, remove it from dict2
        if key not in dict1_keys:
            del dict2[key]
            i= i+1
    print(i)


def parse_text_file(file_path): ##parses a file 
    data = {} #empty set of info
    # Open the file
    file = open(file_path, 'r') #open in read mode
    try:
        lines = file.readlines() 
        headers = lines[0].split() #split the first line into headers, make sure everything is split by spaces
        for header in headers: ## for each of the headers, iterate
            data[header] = {} #set to empty values
               
        for line in lines[2:]: ## starting at the third line
            if line.strip(): #strip spaces, and set eveyrthing seperated by a space into a list
                parts = line.split() #this is the list everything is seperated in to 
                i = 0 
                for header in headers: 
                    if i + 1 < len(parts):
                        date = parts[i]
                        price = parts[i+1]
                        data[header][date] = price
                        i += 2                   
    finally:
        # close file
        file.close()

    return data


def graphHeaderPrices(startDate, endDate, headerDict, Name,tickerDistance): ## data is the dictionary, header is the index, tickerDistance is how far apart to put the tickers
    allDates = list(headerDict.keys()) #all dates/keys in that dict
    startIndex1 = allDates.index(endDate) 
    endIndex1 = allDates.index(startDate)
    if(startIndex1>endIndex1):
        startIndex2 = endIndex1
        endIndex2 = startIndex1
    else:
        startIndex2 = startIndex1
        endIndex2 = endIndex1
    datesInRange = allDates[startIndex2:endIndex2 + 1] # gets dates in required range
    
    pricesList = []
    for date in allDates[startIndex2:endIndex2 + 1]:
        price = headerDict[date]
        pricesList.append(price)

    intPricesList = []
    for price in pricesList:
        strPrice = price
        floatPrice = float(strPrice)
        intPricesList.append(floatPrice)
    if(startIndex2 == startIndex1): 
        intPricesList.reverse() ## takes the prices and sorts them by earliest to latest
        datesInRange.reverse() # does the same for the dates
        
    plt.plot(datesInRange, intPricesList, marker = 'o')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.title(Name + "Date/Price Data")
    ##plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    ##plt.xticks(range(0,len(datesInRange), 7),datesInRange[::7], rotation = 45)
    plt.xticks(range(0,len(datesInRange), tickerDistance),datesInRange[::tickerDistance], rotation = 45)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()
        
def delete_column(file_path): ## this function allows me to delete collumns from a file 
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        modified_lines = []
        for line in lines[2:]:
            if line.strip():  # Ignore empty lines
                parts = line.split()
                del parts[2] # deletes item at second index, and then deletes the one to its right
                del parts[2]
            modified_line = ' '.join(parts) + '\n'
            modified_lines.append(modified_line)
            with open(file_path, 'w') as file:
                file.writelines(modified_lines)
                
def datesDictToList(startDate, endDate, headerDict):
    allDates = list(headerDict.keys()) #all dates/keys in that dict
    startIndex = allDates.index(endDate) 
    endIndex = allDates.index(startDate)
    datesInRange = allDates[startIndex:endIndex + 1] # gets dates in required range
    if(datesInRange[0] == endDate):
        datesInRange.reverse()

        
    return datesInRange

def pricesDictToList(endDate, startDate, headerDict):
    allDates = list(headerDict.keys()) #all dates/keys in that dict
    startIndex1 = allDates.index(endDate) 
    endIndex1 = allDates.index(startDate)
    if(startIndex1 > endIndex1):
        startIndex2 = endIndex1
        endIndex2 = startIndex1
    else:
        startIndex2 = startIndex1
        endIndex2 = endIndex1
    pricesList = []
    for date in allDates[startIndex2:endIndex2 + 1]:
        price = headerDict[date]
        pricesList.append(price)
    intPricesList = []
    for price in pricesList:
        strPrice = price
        floatPrice = float(strPrice)
        intPricesList.append(floatPrice)
    #print(intPricesList)
    #if(intPricesList[0] == headerDict[endDate]):
        #intPricesList.reverse() ## takes the prices and sorts them by earliest to latest
        
    return intPricesList
     
def calcMaximumDrawdown(endDate, startDate, headerDict):
    #if(headerDict[endDate] )
    pricesList = pricesDictToList(endDate, startDate, headerDict)
    peakValue = max(pricesList)
    bottomValue = min(pricesList)
    
    maxDrawdown = (( peakValue - bottomValue) / peakValue) * 100
    
    return maxDrawdown

def createModifiedIndexList(data, header1, header2, header1Percentage, header2Percentage, startDate, endDate):
    h1PricesList = pricesDictToList(data, startDate, endDate, header1)
    h2PricesList = pricesDictToList(data, startDate, endDate, header2)
    modIndexPrices = []

    for i in range(0, len(h1PricesList)):
        h1Price = header1Percentage * h1PricesList[i]
        h2Price = header2Percentage * h2PricesList[i]
        totalPrice = h1Price + h2Price
        modIndexPrices.append(totalPrice)
    
    return modIndexPrices

def createModifiedIndexDict(data, header1, header2, header1Percentage, header2Percentage, startDate, endDate):
    modDict = {}


    header1Dict = data[header1]
    header2Dict = data[header2]

    del header1Dict['Date']
    del header2Dict['Date']

    for key in header1Dict.keys():
        if key in header2Dict:
            modDict[key] = (float(header1Dict[key]) * header1Percentage) + (float(header2Dict[key]) * header2Percentage)
    return modDict 

'''def graphModifiedIndexPrice(data, modIndex, modIndexName, anyHeader, startDate, endDate, tickerDistance):
    headerInfo = data[anyHeader] ## gets the dictionary for header 
    allDates = list(headerInfo.keys()) #all dates/keys in that dict
    startIndex = allDates.index(endDate) 
    endIndex = allDates.index(startDate)
    datesInRange = allDates[startIndex:endIndex + 1] # gets dates in required range
        
    pricesList = modIndex
    
    datesInRange.reverse() # puts dates in correct order
        
    plt.plot(datesInRange, pricesList, marker = 'o')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.title(modIndexName + "Date/Price Data")
    ##plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    ##plt.xticks(range(0,len(datesInRange), 7),datesInRange[::7], rotation = 45)
    plt.xticks(range(0,len(datesInRange), tickerDistance),datesInRange[::tickerDistance], rotation = 45)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()'''
    
def graphMaximumDrawdown(YTDstartDate, Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate, header1Dict, header2Dict, header1Name, header2Name):
    MaximumDrawdownList = []
    
    h1YTDMaxDD = calcMaximumDrawdown(YTDstartDate, endDate, header1Dict)
    h1Y1MaxDD = calcMaximumDrawdown(Y1startDate, endDate, header1Dict)
    h1Y3MaxDD = calcMaximumDrawdown(Y3startDate, endDate, header1Dict)
    h1Y5MaxDD = calcMaximumDrawdown(Y5startDate, endDate, header1Dict)
    h1Y10MaxDD = calcMaximumDrawdown(Y10startDate, endDate, header1Dict)
    
    h2YTDMaxDD = calcMaximumDrawdown(YTDstartDate, endDate, header2Dict)
    h2Y1MaxDD = calcMaximumDrawdown(Y1startDate, endDate, header2Dict)
    h2Y3MaxDD = calcMaximumDrawdown(Y3startDate, endDate, header2Dict)
    h2Y5MaxDD = calcMaximumDrawdown(Y5startDate, endDate, header2Dict)
    h2Y10MaxDD = calcMaximumDrawdown(Y10startDate, endDate, header2Dict)
    
    MaximumDrawdownList = [h1YTDMaxDD, h2YTDMaxDD, h1Y1MaxDD, h2Y1MaxDD, h1Y3MaxDD, h2Y3MaxDD, h1Y5MaxDD, h2Y5MaxDD, h1Y10MaxDD, h2Y10MaxDD]
    
    h1Name = header1Name
    h2Name = header2Name
    
    yearsList = [h1Name + "YTD MaxDD", header2Name + "YTD MaxDD", h1Name + " 1Y MaxDD", h2Name + " 1Y MaxDD", h1Name + " 3Y MaxDD", h2Name + " 3Y MaxDD", h1Name + " 5Y MaxDD", h2Name + " 5Y MaxDD", h1Name + " 10Y MaxDD", h2Name + " 10Y MaxDD"]
    colors = ['red' if i % 2 == 0 else 'skyblue' for i in range(len(yearsList))]

    plt.bar(yearsList, MaximumDrawdownList, color=colors)
    plt.xlabel('Indexes')
    plt.ylabel('Maximum Drawdown (%)')
    plt.title(h1Name + " & " + h2Name + "Maximum Drawdowns")
    plt.xticks(rotation=45, fontsize = 6)
    plt.show()

'''def graphModifiedMaximumDrawdown(data, modIndex, modIndexName, header2, Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate):
    MaximumDrawdownList = []
    
    h1Y1MaxDD = calcModifiedMaximumDrawdown(data, Y1startDate, endDate, modIndex, header2)
    h1Y3MaxDD = calcModifiedMaximumDrawdown(data, Y3startDate, endDate, modIndex, header2)
    h1Y5MaxDD = calcModifiedMaximumDrawdown(data, Y5startDate, endDate, modIndex, header2)
    h1Y10MaxDD = calcModifiedMaximumDrawdown(data, Y10startDate, endDate, modIndex, header2)
    
    h2Y1MaxDD = calcMaximumDrawdown(data, Y1startDate, endDate, header2)
    h2Y3MaxDD = calcMaximumDrawdown(data, Y3startDate, endDate, header2)
    h2Y5MaxDD = calcMaximumDrawdown(data, Y5startDate, endDate, header2)
    h2Y10MaxDD = calcMaximumDrawdown(data, Y10startDate, endDate, header2)
    
    MaximumDrawdownList = [h1Y1MaxDD, h2Y1MaxDD, h1Y3MaxDD, h2Y3MaxDD, h1Y5MaxDD, h2Y5MaxDD, h1Y10MaxDD, h2Y10MaxDD]
    
    h1Name = modIndexName
    h2Name = header2[:-6]
    
    yearsList = [h1Name + " 1Y MaxDD", h2Name + " 1Y MaxDD", h1Name + " 3Y MaxDD", h2Name + " 3Y MaxDD", h1Name + " 5Y MaxDD", h2Name + " 5Y MaxDD", h1Name + " 10Y MaxDD", h2Name + " 10Y MaxDD"]
    
    
    colors = ['red' if i % 2 == 0 else 'skyblue' for i in range(len(yearsList))]
    
    plt.bar(yearsList, MaximumDrawdownList, color=colors)
    plt.xlabel('Indexes')
    plt.ylabel('Maximum Drawdown (%)')
    plt.title(h1Name + " & " + h2Name + "Maximum Drawdowns")
    plt.xticks(rotation=45, fontsize = 6)
    plt.show()'''
    
    
    

    

def calcYearlyReturn(startDate, endDate, years, headerDict):
    startValue = headerDict[startDate]   
    endValue = headerDict[endDate] 
    yearlyReturn = 100 * ((((float(endValue) / float(startValue))**(1/years)) -1))
    
    
    return yearlyReturn

'''def calcModifiedYearlyReturn(modDict, startDate, endDate, years): ## this function is messed, it works but I need to reconfigure it cause it has issues with indexing over modindex
    endValue = modDict[endDate]
    startValue = modDict[startDate]
    
    yearlyReturn = 100 * (((float(endValue) / float(startValue))**(1/years)) -1)
    
    return yearlyReturn'''



''' headerInfo = data[anyHeader] ## gets the dictionary for header 
    allDates = list(headerInfo.keys()) #all dates/keys in that dict
        
    startIndex = allDates.index(startDate)
    print("start index")
    print(startIndex)
    
    listLength = len(modIndex)
    
    newStartIndex = listLength - 1 - startIndex
    
    if years == 10:
        newStartIndex = 0

    startValue = modIndex[newStartIndex]  ##this is the most recent value  ##NEED to look into this, my start value may be off by one day
    endValue = modIndex[-1]'''

##yearlyReturn = 100 * (((float(endValue) / float(startValue))**(1/years)) -1)
        

def graphAnnulizedReturns(YTDstartDate, Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate, header1Dict, header2Dict, header1Name, header2Name):
    h1YTDreturn = calcYearlyReturn(YTDstartDate, endDate, 1, header1Dict)
    h1oneYearReturn = calcYearlyReturn(Y1startDate, endDate, 1, header1Dict)
    h1threeYearReturn = calcYearlyReturn(Y3startDate, endDate, 3, header1Dict)
    h1fiveYearReturn = calcYearlyReturn(Y5startDate, endDate, 5, header1Dict)
    h1tenYearReturn = calcYearlyReturn(Y10startDate, endDate, 10, header1Dict)
    
    h2YTDreturn = calcYearlyReturn(YTDstartDate, endDate, 1, header2Dict)
    h2oneYearReturn = calcYearlyReturn(Y1startDate, endDate, 1, header2Dict)
    h2threeYearReturn = calcYearlyReturn(Y3startDate, endDate, 3, header2Dict)
    h2fiveYearReturn = calcYearlyReturn(Y5startDate, endDate, 5, header2Dict)
    h2tenYearReturn = calcYearlyReturn(Y10startDate, endDate, 10, header2Dict)    
    
    returnsList = []
    returnsList.append(h1YTDreturn)
    returnsList.append(h2YTDreturn)
    returnsList.append(h1oneYearReturn)
    returnsList.append(h2oneYearReturn)
    returnsList.append(h1threeYearReturn)
    returnsList.append(h2threeYearReturn)
    returnsList.append(h1fiveYearReturn)
    returnsList.append(h2fiveYearReturn)
    returnsList.append(h1tenYearReturn)
    returnsList.append(h2tenYearReturn)
    
    h1Name = header1Name
    h2Name = header2Name

    datesList = ["YTD" + h1Name, "YTD"+h2Name, " 1Y"+h1Name,"1Y"+h2Name," 3Y"+h1Name," 3Y"+h2Name," 5Y"+h1Name," 5Y"+h2Name, " 10Y"+h1Name," 10Y"+h2Name]
    colors = ['red' if i % 2 == 0 else 'skyblue' for i in range(len(datesList))]

    plt.bar(datesList, returnsList, color=colors)
    plt.xlabel('Years')
    plt.ylabel('Annualized Return (%)')
    plt.title("Annualized Returns: " + h1Name + " in Red & " + h2Name + " in blue")
    plt.xticks(rotation=45, fontsize = 5)
    plt.ylim(0, 30)

    plt.show()
    
    


'''def graphModifiedAnnulizedReturns(data, modIndex, modIndexName, Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate, header2, dict1, dict2):
    
    h1YTDreturn = calcTotalReturn(dict1, "1/2/2024", endDate) ## i know this line is not up to normal standards of modularity, but it would run perfectly fine for a year. I will change it in the future though
    h1oneYearReturn = calcModifiedYearlyReturn(modIndex, Y1startDate, endDate, 1)
    h1threeYearReturn = calcModifiedYearlyReturn(modIndex, Y3startDate, endDate, 3)
    h1fiveYearReturn = calcModifiedYearlyReturn(modIndex, Y5startDate, endDate, 5)
    h1tenYearReturn = calcModifiedYearlyReturn(modIndex, Y10startDate, endDate, 10)
    
    h2YTDreturn = calcTotalReturn(dict2, "1/2/2024", endDate) ## i know this line is not up to normal standards of modularity, but it would run perfectly fine for a year. I will change it in the future though
    h2oneYearReturn = calcYearlyReturn(data, Y1startDate, endDate, 1, header2)
    h2threeYearReturn = calcYearlyReturn(data,Y3startDate, endDate, 3, header2)
    h2fiveYearReturn = calcYearlyReturn(data, Y5startDate, endDate, 5, header2)
    h2tenYearReturn = calcYearlyReturn(data, Y10startDate, endDate, 10, header2)    
    
    returnsList = []
    returnsList.append(h1YTDreturn)
    returnsList.append(h2YTDreturn)
    returnsList.append(h1oneYearReturn)
    returnsList.append(h2oneYearReturn)
    returnsList.append(h1threeYearReturn)
    returnsList.append(h2threeYearReturn)
    returnsList.append(h1fiveYearReturn)
    returnsList.append(h2fiveYearReturn)
    returnsList.append(h1tenYearReturn)
    returnsList.append(h2tenYearReturn)
    
    h1Name = modIndexName[:-6]
    h2Name = header2[:-6]

    datesList = [h1Name + "YTD", h2Name + "YTD", h1Name + " 1Y", h2Name + " 1Y", h1Name + " 3Y", h2Name + " 3Y", h1Name + " 5Y", h2Name + " 5Y", h1Name + " 10Y", h2Name + " 10Y"]
    
    colors = ['red' if i % 2 == 0 else 'skyblue' for i in range(len(datesList))]
    
    plt.bar(datesList, returnsList, color=colors)
    plt.xlabel('Years')
    plt.ylabel('Annualized Return (%)')
    plt.title(h1Name + " & " + h2Name + "Annualized Returns")
    plt.xticks(rotation=45)
    plt.show()'''
    
    

def calcTotalReturn(Dict, startDate,endDate):
    endValue = Dict[endDate]
    startValue = Dict[startDate]
    
    totalReturn = 100 * (float(endValue) - float(startValue)) / float(startValue)
    
    return totalReturn



def createTotalReturnTable(dict1, dict2,dict1Name, dict2Name, YTDstartDate ,Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate):
    h1YTDreturn = calcTotalReturn(dict1, YTDstartDate, endDate)
    h1oneYearReturn = calcTotalReturn(dict1, Y1startDate, endDate)
    h1threeYearReturn = calcTotalReturn(dict1, Y3startDate, endDate)
    h1fiveYearReturn = calcTotalReturn(dict1, Y5startDate, endDate)
    h1tenYearReturn = calcTotalReturn(dict1, Y10startDate, endDate)
    
    h2YTDreturn = calcTotalReturn(dict2, YTDstartDate, endDate)
    h2oneYearReturn = calcTotalReturn(dict2, Y1startDate, endDate)
    h2threeYearReturn = calcTotalReturn(dict2, Y3startDate, endDate)
    h2fiveYearReturn = calcTotalReturn(dict2, Y5startDate, endDate)
    h2tenYearReturn = calcTotalReturn(dict2, Y10startDate, endDate)

    table = [
        [dict1Name, h1YTDreturn, h1oneYearReturn, h1threeYearReturn, h1fiveYearReturn, h1tenYearReturn],
        [dict2Name, h2YTDreturn, h2oneYearReturn, h2threeYearReturn, h2fiveYearReturn, h2tenYearReturn]
        ]    
    table = list(map(list, zip(*table)))
    row_labels = ['Index','YTD', '1 Year', '3 Year', '5 Year', '10 Year']
    plt.figure(figsize=(8, 3))
    plt.table(cellText=table, loc='center', colLabels=['','', dict1Name, dict2Name], rowLabels=row_labels, rowColours=['skyblue'] * len(row_labels))
    plt.title("Total Returns in Percentages", pad=20)  # Add a title with some padding
    plt.axis('off')  # Turn off axis
    
    plt.show()
    

def v2normalizePrices(pricesDict): #normalize returns for stocks with different price ranges, so that their modified index can be compared to others 
    price_values = [] #prices Dict is a dictionary with a stock name, dates as keys, and prices as values
    for value in pricesDict.values(): 
        price_values.append(float(value))
    price_values.reverse()    # the pricesDict dictionary is in descending order, with the first value being the most recent price, so it has to be reversed

    returns = []
    for i in range(1, len(price_values)):
        daily_return = (price_values[i] - price_values[i-1]) / price_values[i-1] #calculate stock return daily
        daily_return = np.around(daily_return, 30)
        returns.append(daily_return)
    #return normalized_returns.tolist()
    return returns

def v2createNormalizedIndex(header1, header2, header3, h1Percentage, h2Percentage, h3Percentage): #headers are stock names, and percentages are what their weight in the modified index will be 
    
    h1NormalizedReturns = v2normalizePrices(header1)
    h2NormalizedReturns = v2normalizePrices(header2)
    h3NormalizedReturns = v2normalizePrices(header3)
    
    combinedPrices = [100] # when testing this function I use the starting value at the earliest date available, but I use 100 as the standard beginning value
    
    dates = header1.keys()
    datesLength = len(dates)
    
    for i in range(datesLength -1):
        growthH1 = h1NormalizedReturns[i]
        growthH2 = h2NormalizedReturns[i]
        growthH3 = h3NormalizedReturns[i]
        combinedGrowth = 1 + (h1Percentage * growthH1) + (h2Percentage * growthH2) + (h3Percentage * growthH3)
        
        combinedPrice = combinedPrices[-1] * combinedGrowth
        
        combinedPrices.append(combinedPrice)
        
    newIndexDict = {}
    for date, price in zip(reversed(dates), combinedPrices):
        newIndexDict[date] = price
        
    return newIndexDict
 


'''def v2createNormalizedIndex(header1, header2, header3, h1Percentage, h2Percentage, h3Percentage): #headers are stock names, and percentages are what their weight in the modified index will be 
    
    h1NormalizedReturns = v2normalizePrices(header1)
    h2NormalizedReturns = v2normalizePrices(header2)
    h3NormalizedReturns = v2normalizePrices(header3)
    
    combinedPrices = [100] # when testing this function I use the starting value at the earliest date available, but I use 100 as the standard beginning value
    
    dates = header1.keys()
    datesLength = len(dates)
    
    for i in range(datesLength -1):
        growthH1 = 1 + h1NormalizedReturns[i]
        growthH2 = 1 + h2NormalizedReturns[i]
        growthH3 = 1 + h3NormalizedReturns[i]
        
        combinedPriceH1 = combinedPrices[-1] * h1Percentage
        combinedPriceH2 = combinedPrices[-1] * h2Percentage
        combinedPriceH3 = combinedPrices[-1] * h3Percentage
        
        newPriceH1 = combinedPriceH1 * growthH1
        newPriceH2 = combinedPriceH2 * growthH2
        newPriceH3 = combinedPriceH3 * growthH3
        
        newPriceH1 = np.around(newPriceH1, 30)
        newPriceH2 = np.around(newPriceH2, 30)
        newPriceH3 = np.around(newPriceH3, 30)
        
        combinedPrice = (newPriceH1 + newPriceH2 + newPriceH3) 
        combinedPrices.append(combinedPrice)
        
    newIndexDict = {}
    for date, price in zip(reversed(dates), combinedPrices):
        newIndexDict[date] = price
        
    return newIndexDict'''
    
def v1normalizePrices(endDate, startDate, indexDict, indexDict2, indexDict3):
    indexPriceList = pricesDictToList(endDate, startDate, indexDict)
    priceList2 = pricesDictToList(endDate, startDate, indexDict2)
    priceList3 = pricesDictToList(endDate, startDate, indexDict3)
    indexPriceList.reverse()
    allLists = indexPriceList + priceList2 + priceList3
    
    maxValue = max(allLists)
    
    normalizedList = [math.ceil(float(i)/maxValue * 10**15) / 10**15 for i in indexPriceList]
    listScalar = math.ceil(100/normalizedList[0] * 10**15) / 10**15
    normalizedList = [math.ceil(listScalar * float(i)/maxValue * 10**15) / 10**15 for i in indexPriceList]
    #print(normalizedList)

    return normalizedList
    
    
from decimal import Decimal

'''def normalizePrices(endDate, startDate, indexDict, indexDict2, indexDict3):
    indexPriceList = pricesDictToList(endDate, startDate, indexDict)
    priceList2 = pricesDictToList(endDate, startDate, indexDict2)
    priceList3 = pricesDictToList(endDate, startDate, indexDict3)
    indexPriceList.reverse()
    allLists = indexPriceList + priceList2 + priceList3
    

    
    maxValue = max(allLists)
    normalizedList = [listScalar * Decimal(i) / maxValue * Decimal("10e15") for i in [Decimal(x) for x in indexPriceList]]
    listScalar = Decimal(100) / normalizedList[0] * Decimal("10e15")
    normalizedList = [listScalar * Decimal(i) / maxValue * Decimal("10e15") for i in indexPriceList]
    return [float(i) for i in normalizedList]  # Convert back to float for further use'''



def v1createNormalizedIndex(header1Dict, header2Dict, header3Dict, h1Percentage, h2Percentage, h3Percentage, endDate, startDate): #headers are stock names, and percentages are what their weight in the modified index will be 

    
    h1NormalizedList = v1normalizePrices(endDate, startDate, header1Dict, header2Dict, header3Dict)
    h2NormalizedList = v1normalizePrices(endDate, startDate, header2Dict, header1Dict, header3Dict)
    h3NormalizedList = v1normalizePrices(endDate, startDate, header3Dict, header2Dict, header1Dict)

    dates = datesDictToList(startDate, endDate, header1Dict)
    datesLength = len(dates)
    '''print("dates length")
    print(datesLength)
    print("h1NormalizedList length" )
    print(len(h3NormalizedList))'''
    combinedPrices = []
    
    for i in range(datesLength):
        h1Price = (math.ceil(h1NormalizedList[i] * 10**15) / 10**15) * (math.ceil(h1Percentage * 10**15) / 10**15)
        h2Price = (math.ceil(h2NormalizedList[i] * 10**15) / 10**15) * (math.ceil(h2Percentage * 10**15) / 10**15)
        h3Price = (math.ceil(h3NormalizedList[i] * 10**15) / 10**15) * (math.ceil(h3Percentage * 10**15) / 10**15)
        
        newPrice = h1Price + h2Price + h3Price
        
        combinedPrices.append(newPrice)
    #print(combinedPrices)
    newIndexDict = {}
    for date, price in zip(dates, combinedPrices):
        newIndexDict[date] = price
        
    return newIndexDict
    
def calcVolatility(dict1, startDate, endDate, years):
    # Calculate daily returns
    prices = pricesDictToList(endDate, startDate, dict1)
    returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
    
    num_trading_days = 252 * years
    print(np.std(returns))
    # Calculate volatility (standard deviation of returns)
    volatility =  np.std(returns) * np.sqrt(num_trading_days)

    return volatility

def createVolatilityTable(dict1, dict2,dict1Name, dict2Name, YTDstartDate ,Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate):
    #h1YTDvolatility = calcTotalReturn(dict1, YTDstartDate, endDate)
    h1oneYearvolatility = calcVolatility(dict1, Y1startDate, endDate, 1)
    h1threeYearvolatility = calcVolatility(dict1, Y3startDate, endDate, 3)
    h1fiveYearvolatility = calcVolatility(dict1, Y5startDate, endDate, 5)
    h1tenYearvolatility = calcVolatility(dict1, Y10startDate, endDate, 10)
    
    #h2YTDvolatility = calcVolatility(dict2, YTDstartDate, endDate)
    h2oneYearvolatility = calcVolatility(dict2, Y1startDate, endDate, 1)
    h2threeYearvolatility = calcVolatility(dict2, Y3startDate, endDate, 3)
    h2fiveYearvolatility = calcVolatility(dict2, Y5startDate, endDate, 5)
    h2tenYearvolatility = calcVolatility(dict2, Y10startDate, endDate, 10)

    table = [
        [dict1Name, h1oneYearvolatility, h1threeYearvolatility, h1fiveYearvolatility, h1tenYearvolatility],
        [dict2Name, h2oneYearvolatility, h2threeYearvolatility, h2fiveYearvolatility, h2tenYearvolatility]
        ]    
    table = list(map(list, zip(*table)))
    row_labels = ['Index', '1 Year', '3 Year', '5 Year', '10 Year']
    plt.figure(figsize=(8, 3))
    plt.table(cellText=table, loc='center', colLabels=['','', dict1Name, dict2Name], rowLabels=row_labels, rowColours=['skyblue'] * len(row_labels))
    plt.title("Volatility", pad=20)  # Add a title with some padding
    plt.axis('off')  # Turn off axis
    
    plt.show()
    
def createMaximumDrawdownTable(YTDstartDate, Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate, header1Dict, header2Dict, header1Name, header2Name):
    MaximumDrawdownList = []
    
    h1YTDMaxDD = round(calcMaximumDrawdown(YTDstartDate, endDate, header1Dict), 2)
    h1Y1MaxDD = round(calcMaximumDrawdown(Y1startDate, endDate, header1Dict),2)
    h1Y3MaxDD = round(calcMaximumDrawdown(Y3startDate, endDate, header1Dict),2)
    h1Y5MaxDD = round(calcMaximumDrawdown(Y5startDate, endDate, header1Dict),2)
    h1Y10MaxDD = round(calcMaximumDrawdown(Y10startDate, endDate, header1Dict),2)
    
    h2YTDMaxDD = round(calcMaximumDrawdown(YTDstartDate, endDate, header2Dict),2)
    h2Y1MaxDD = round(calcMaximumDrawdown(Y1startDate, endDate, header2Dict),2)
    h2Y3MaxDD = round(calcMaximumDrawdown(Y3startDate, endDate, header2Dict),2)
    h2Y5MaxDD = round(calcMaximumDrawdown(Y5startDate, endDate, header2Dict),2)
    h2Y10MaxDD = round(calcMaximumDrawdown(Y10startDate, endDate, header2Dict),2)
    
    
    table = [
    [header1Name, h1YTDMaxDD, h1Y1MaxDD,h1Y3MaxDD, h1Y5MaxDD, h1Y10MaxDD],
    [header2Name, h2YTDMaxDD, h2Y1MaxDD, h2Y3MaxDD, h2Y5MaxDD, h2Y10MaxDD]
    ]    
    
    h1Name = header1Name
    h2Name = header2Name
        
    table = list(map(list, zip(*table)))
    row_labels = ['Index', 'YTD','1 Year', '3 Year', '5 Year', '10 Year']
    plt.figure(figsize=(8, 3))
    plt.table(cellText=table, loc='center', colLabels=['','', h1Name, h2Name], rowLabels=row_labels, rowColours=['skyblue'] * len(row_labels))
    plt.title("Maximum Drawdowns", pad=1)  # Add a title with some padding
    plt.axis('off')  # Turn off axis

    plt.show()

def createYearlyReturnTable(dict1, dict2,dict1Name, dict2Name, YTDstartDate ,Y1startDate, endDate, Y3startDate, Y5startDate, Y10startDate):
    h1YTDreturn = round(calcYearlyReturn(YTDstartDate, endDate, 1, dict1),2)
    h1Y1return = round(calcYearlyReturn(Y1startDate, endDate, 1, dict1),2)
    h1Y3return = round(calcYearlyReturn(Y3startDate, endDate, 3, dict1),2)
    h1Y5return = round(calcYearlyReturn(Y5startDate, endDate, 5, dict1),2)
    h1Y10return = round(calcYearlyReturn(Y10startDate, endDate, 10, dict1),2)
    
    h2YTDreturn = round(calcYearlyReturn(YTDstartDate, endDate, 1, dict2),2)
    h2Y1return = round(calcYearlyReturn(Y1startDate, endDate, 1, dict2),2)
    h2Y3return = round(calcYearlyReturn(Y3startDate, endDate, 3, dict2),2)
    h2Y5return = round(calcYearlyReturn(Y5startDate, endDate, 5, dict2),2)
    h2Y10return = round(calcYearlyReturn(Y10startDate, endDate, 10, dict2),2)

    table = [
        [dict1Name, h1YTDreturn, h1Y1return, h1Y3return, h1Y5return, h1Y10return],
        [dict2Name, h2YTDreturn, h2Y1return, h2Y3return, h2Y5return, h2Y10return]
        ]    
    table = list(map(list, zip(*table)))
    row_labels = ['Index','YTD', '1 Year', '3 Year', '5 Year', '10 Year']
    plt.figure(figsize=(8, 3))
    plt.table(cellText=table, loc='center', colLabels=['','', dict1Name, dict2Name], rowLabels=row_labels, rowColours=['skyblue'] * len(row_labels))
    plt.title("Annualized Returns in Percentages", pad=1)  # Add a title with some padding
    plt.axis('off')  # Turn off axis
    
    plt.show()
    

    
    
    
    
                
