import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import mplfinance as mpf
from PyQt5 import QtCore


class StockInfo(QtCore.QThread):
    def __init__(self, stock_number=0, info=None):
        self.stock_number = stock_number
        self.info = info
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        pd.set_option('display.unicode.east_asian_width', True)

    def get_profile(self):
        try:
            response = requests.get(f"https://tw.stock.yahoo.com/quote/{self.stock_number}/profile", headers = self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            section = soup.find_all('section', {'class' : "Mb($m-module)"})
            info_dict = dict()
            for each_section in section:
                info_keys = each_section.find_all('span', {'class' : "As(st) Bxz(bb) Pstart(12px) Py(8px) Bgc($c-gray-hair) C($c-primary-text) Flx(n) W(104px) W(120px)--mobile W(152px)--wide Miw(u) Pend(12px) Mend(0)"})
                info_values = each_section.find_all('div', {'class' : "Py(8px) Pstart(12px) Bxz(bb)"})
                if len(info_keys) == len(info_values):
                    for index in range(len(info_keys)):
                        info_dict[info_keys[index].text] = info_values[index].text.replace("\n", "").replace("\r", "")

            return pd.DataFrame(list(info_dict.items()), columns=['',''])

        except:
            ...

    def get_technical_analysis(self):
        try:
            response = requests.get(f"https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=d&mkt=10&sym={self.stock_number}&v=1&callback=jQuery", headers = self.headers)
            response = json.loads(response.text[response.text.rfind("ta"):].replace("ta", "{\"ta").replace("(", "").replace(")", "").replace(";", ""))

            info_per_day = list()
            for data in response['ta']:
                row = list()
                row.append(f"{str(data['t'])[4:6]}/{str(data['t'])[6:8]}/{str(data['t'])[0:4]}")
                row.append(data['o'])
                row.append(data['h'])
                row.append(data['l'])
                row.append(data['c'])
                row.append(data['v'])
                info_per_day.append(tuple(row))

            df = pd.DataFrame(info_per_day, columns=["Date", "Open", "High", "Low", "Close", "Volume"])
            df_return = pd.DataFrame(info_per_day, columns=["Date", "Open", "High", "Low", "Close", "Volume"]).iloc[::-1]
            df_return.reset_index(drop=True, inplace=True)
            df.Date = pd.to_datetime(df.Date)
            df.set_index("Date", inplace=True)
            df.index.name = 'Date'

            my_color = mpf.make_marketcolors(up='r', down='g', edge='inherit', wick='inherit', volume='inherit')
            my_style = mpf.make_mpf_style(marketcolors=my_color, figcolor='(0.82,0.83,0.85)',gridcolor='(0.82,0.83,0.85)')
            mpf.plot(df, type='candle', mav=(5,10,20), volume=True, style=my_style, savefig=dict(fname='Figure/KLineFigure.jpg', dpi=100, pad_inches=0.25))

            return df_return
            
        except:
            ...

    def get_institutional_trading(self):
        try:
            response = requests.get(f"https://tw.stock.yahoo.com/quote/{self.stock_number}/institutional-trading", headers = self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            ul = soup.find_all('ul', {'class' : "M(0) P(0) List(n)"})
            li = ul[1].find_all('li', {'class' : "List(n)"})

            info_per_day = list()
            for each_li in li:
                row = list()
                row.append(each_li.find('div', {'class' : "W(96px) Ta(start)"}).text)
                for info in each_li.find_all('span'):
                    if "Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-down)" in str(info):
                        row.append(f"-{info.text}")
                    else:
                        if info.text != "":
                            row.append(info.text)
                info_per_day.append(tuple(row))

            df = pd.DataFrame(info_per_day, columns = ["日期", "外資(張)", "投信(張)", "自營商(張)", "合計(張)", "外資籌碼", "漲跌幅(%)", "成交量"])
                        
            return df

        except:
            ...

    def get_dividend(self):
        try:
            response = requests.get(f"https://tw.stock.yahoo.com/quote/{self.stock_number}/dividend", headers = self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            ul = soup.find_all('ul', {'class' : "M(0) P(0) List(n)"})
            li = ul[0].find_all('li', {'class' : "List(n)"})

            info_per_day = list()
            for each_li in li:
                row = list()
                for info in each_li.find_all('div'):
                    if ' '.join(info["class"]) == "D(f) W(98px) Ta(start)" \
                        or ' '.join(info["class"]) == "Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)" \
                        or ' '.join(info["class"]) == "Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(108px)":
                        
                        row.append(info.text)
                info_per_day.append(tuple(row))

            df = pd.DataFrame(info_per_day, columns = ["股利所屬期間", "現金股利", "股票股利", "除息日", "除權日", "現金股利發放日", "股票股利發放日", "填息天數"])
            
            return df

        except:
            ...

    def get_stock_name(self):
        try:
            response = requests.get(f"https://tw.stock.yahoo.com/quote/{self.stock_number}", headers = self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            div = soup.find_all('div', {'class' : "D(f) Ai(c) Mb(6px)"})
            stock_id = div[0].find('span', {'class' : "C($c-icon) Fz(24px) Mend(20px)"}).text
            stock_name = div[0].find('h1', {'class' : "C($c-link-text) Fw(b) Fz(24px) Mend(8px)"}).text
            
            return stock_id, stock_name

        except:
            return 0, 0