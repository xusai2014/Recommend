import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import bs4
import lxml


class crawl:
    def page_kuai(self):
        page = 1
        ua = UserAgent()
        headers = { 'UserAgent': ua.random }
        html = requests.get('https://www.kuaidaili.com/free/inha/'+ str(page), headers = headers)
        if html.status_code == 200:
            Soup = BeautifulSoup(html.text,'lxml')
            tbody = Soup.find('tbody')
            if isinstance(tbody, bs4.element.Tag):
                tr_list = tbody.find_all('tr')
                for tr in tr_list:
                    try:
                        IP_adress = tr.find('td').get_text()
                        Ip_port = tr.find('td', attrs={'data-title':"PORT"}).get_text()
                        IP = "http://"+IP_adress + ":" + Ip_port
                        proxies = {'http':IP}
                        try:
                            response = requests.get('http://baidu.com', proxies, timeout = 6)
                            print('available ' + IP)
                        except:
                            print('error')
                    except Exception:
                        pass
            else:
                print('*******************')
                       