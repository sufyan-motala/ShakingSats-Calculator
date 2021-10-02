import csv
import yfinance as yf

#Function to somewhat accurately get current price
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

btc_cad = get_current_price("BTC-CAD")
total_btc_amount = 0
days_shaken = 0

#Opening CSV file
with open('transactions_summary.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    ##Intterate through each row of CSV
    for row in csv_reader:
        #Check if "Transaction Type" column contains "shakingsats"
        if ("shakingsats" in row[0]):
            #If so add column containing amount of BTC to btc_total and increase counter
            total_btc_amount += float(row[4])
            days_shaken += 1

total_cad_amount = btc_cad * total_btc_amount
daily_avg_earned = total_cad_amount / days_shaken

#Output + formatting
print("Total days shaken =", days_shaken, "days.")
print("Total BTC earned =", total_btc_amount)
print("Total amount earned in CAD =", "$" + str(round(btc_cad * total_btc_amount,2)), "|| At current BTC price of", "$" +str(round(btc_cad,2)))
print("This means you earned an average of", "$" + str(round(daily_avg_earned,2)), "per day.")