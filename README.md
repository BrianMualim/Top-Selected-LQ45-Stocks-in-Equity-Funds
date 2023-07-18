# Top-Selected-LQ45-Stocks-in-Indonesian-Mutual-Funds

Needed Files:
- Stocks Nav Tables for Specified Month
- Cleaned Data from each equity fund's portfolio
- List of LQ45 stocks

Purpose:
To calculate the number of equity funds investing in a certain stock for the month

The code works by mostly implementing double for loops,
If ProductNameHeader in cleaned data and stocks nav match, then multiply % and AUM to create a new row (%*AUM)
If PortfolioCode in cleaned data and LQ45 match, then add product AUM to totalAUM and increase counter by 1

counter keeps track of how many equity funds are investing in a certain stock
totalAUM keeps track of totalAUM for that specific month
