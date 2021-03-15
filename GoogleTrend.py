from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pylab as plt
from pandas.plotting import register_matplotlib_converters

def plottrends(searchterm, tf, booRegion, booCreateCSV, secondtermforseries):

    print ('Importing data from Google Trends')
    pytrend = TrendReq()

    if booRegion or len(secondtermforseries) == 0:
        search_list = [searchterm]
    else:
        search_list = [searchterm, secondtermforseries]

    pytrend.build_payload(search_list, cat=0, timeframe=tf,geo='',gprop='')

    register_matplotlib_converters()
    plt.figure(figsize=(10, 6))
    fig = plt.figure(1)

    if booRegion:
        df = pytrend.interest_by_region()
        df.sort_values(searchterm, inplace=True, ascending=True)
        df.reset_index(level=0, inplace=True)
        df = df.tail(25)

        ax = fig.add_subplot(111)
        ax.tick_params(axis='x', which='major', labelsize=6)
        ax.tick_params(axis='x', which='minor', labelsize=6)
        ax.set_xticklabels(df['geoName'], rotation = 50, ha="right")

        plt.bar(df['geoName'],df[searchterm], color = 'grey')
        plt.title("'" + searchterm + "'" + ' google searches by country over time : ' + tf)

    else:
        df = pytrend.interest_over_time()
        df.reset_index(level=0, inplace=True)
        plt.ylabel('Index')
        plt.plot(df['date'], df[searchterm], color = 'black', label = searchterm)

        if len(secondtermforseries) > 0:
            plt.plot(df['date'], df[secondtermforseries], color = 'grey', label = secondtermforseries)
            searchterm = searchterm + ' \\ ' + secondtermforseries

        plt.legend(loc="upper left")
        plt.title("'" + searchterm + "'" + ' google searches through time : ' + tf)

    print(df.head())

    if booCreateCSV:
        print ('Creating csv file')
        df.to_csv('c:\\temp\\googletrends.csv')

    plt.show()

if __name__ == '__main__':
    plottrends('Oil Price ','today 5-y', False, False, 'OPEC')