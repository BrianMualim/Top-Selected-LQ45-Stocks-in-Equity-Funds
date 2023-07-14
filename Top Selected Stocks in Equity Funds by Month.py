import csv
import pandas as pd

# Must be in Month[:3]-Year Format
month = "May-2023"

stocksNAVcsv = pd.read_csv("C:\\Users\\brian\\Downloads\\Stocks NAV Tables " + month + ".csv")
cleanDataNAVcsv = pd.read_csv("C:\\Users\\brian\\Downloads\\Clean Data for Stocks\\CleanData " + month + ".csv")
lq45ListofStocksNAVcsv = pd.read_csv("C:\\Users\\brian\\Downloads\\HPAM\\LQ45.csv")

# Headers I need from stocks file
# stocks NAV has header name and aum
productNameNAVHeader = stocksNAVcsv['Nama Produk']
aumProductNAVHeader = stocksNAVcsv['AUM']

# Headers I need from clean data file
# Clean data has header name, portfolio code, and percentage
productNameCleanHeader = cleanDataNAVcsv['Nama Produk']
portfolioCodeCleanHeader = cleanDataNAVcsv['Portfolio Code']
percentageCleanHeader = cleanDataNAVcsv['Percentage']

# Header for list of stock codes from LQ45
portfolioCodeLQ45 = lq45ListofStocksNAVcsv['Portfolio Code']

aumProductColumn = []
aumPerStockColumn = []

for i in range(len(productNameCleanHeader)):
    k = 0
    for j in range(len(productNameNAVHeader)):
        if productNameCleanHeader[i] == productNameNAVHeader[j]:
            aumProductColumn.append(aumProductNAVHeader[j])
            aumPerStockColumn.append((aumProductNAVHeader[j] * percentageCleanHeader[i]) / 100)
            k = 1
            break

    if k == 0:
        aumProductColumn.append("null")
        aumPerStockColumn.append("null")

cleanDataNAVcsv['AUM'] = aumProductColumn
cleanDataNAVcsv['Percent * AUM'] = aumPerStockColumn

data = []
counter = 0
totalAUM = 0

for i in range(len(portfolioCodeLQ45)):
    counter = 0
    for j in range(len(portfolioCodeCleanHeader)):
        if portfolioCodeLQ45[i] == portfolioCodeCleanHeader[j].upper():
            counter += 1
            if aumPerStockColumn[j] != "null":
                totalAUM += aumPerStockColumn[j]

    dictionary = {
        "Portfolio Code": portfolioCodeLQ45[i],
        "Counter of MIs": counter
    }
    data.append(dictionary.values())

column0 = ["Date", month]
column1 = ["Total AUM", totalAUM]
data.insert(0, column0)
data.insert(1, column1)
filename = "C:\\Users\\brian\\Downloads\\Top Selected Stocks in Equity Funds " + month + ".csv"

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
