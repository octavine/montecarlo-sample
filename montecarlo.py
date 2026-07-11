import yfinance
import random
import math
import matplotlib.pyplot as plt

def main():
    #cfg
    lookback="5y" # Use prefix d for day,m for month, y for year
    interval="1d" # Use prefix d for day, h for hour
    runs = 100 # how many times is it running monte carlo
    pred_time = 1000 # how many ticks is the monte carlo sampling
    ticker = "spy"


    pos = 0
    neg = 0

    stock=yfinance.Ticker(ticker)
    dat = stock.history(period=lookback, interval=interval)
    price = dat['Close'].tolist()
    returns = ret(price)
    a = []
    b = []
    avg = 0
    dd = 0
    for i in range(len(returns)):
        if returns[i] >= 0:
            a.append(returns[i])
        else:
            b.append(returns[i])
    for i in range(runs):
        t = montecarlo(a,b,pred_time, logs(price)[-1])
        if t[-1] >= logs(price)[-1]:
            pos += 1
        else:
            neg += 1
        avg += (price+format(t))[-1]
        dd+=max_dd(format(t))
        plt.plot(price+format(t))

    print("% positive outcomes:",(pos/(pos+neg))*100)
    print("original price", price[-1])
    print("average final price:", avg/runs)
    print("avg % change:", (((avg/runs)-price[-1])/price[-1])*100)
    print("avg max down draw:", dd/runs,"%")



    plt.show()

def logs(set = []):
    a = []
    for i in range(len(set)):
        a.append(math.log(set[i]))
    return a

def ret(set = []):
    a = [0]
    for i in range(len(set)):
        if i>0:
            a.append(math.log(set[i]/set[i-1]))
    return a

def format(set=[]):
    return [math.exp(x) for x in set]

def montecarlo(pset = [], nset = [], time =100, f = 0):
    a = [f]
    for i in range(time):
        c = random.random()
        if c<(len(pset)/(len(pset)+len(nset))):
            a.append(a[i] + (pset[random.randint(0,len(pset)-1)]))
        else:
            a.append(a[i] +nset[random.randint(0,len(nset)-1)])
    return a

def max_dd(set=[]):
    peak = set[0]
    max_dd = 0
    for price in set:
        if price > peak:
            peak = price
        dd = (peak - price) / peak
        if dd > max_dd:
            max_dd = dd
    return max_dd * 100

if __name__ == '__main__':
    main()
