from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests
import validators
from queue import Queue
import threading
requests.packages.urllib3.disable_warnings()


class linkfinder():
    def __init__(self,url,cookie=""):
        self.baseUrl = self.return_entire_url(url)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "cookie": cookie}
        self.q = Queue()
        self.crawed_list = set()
        self.urlList = []
        self.q.put(url)

        self.spider_status = 1

    def return_entire_url(self,url):
        if url is not None:
            if url.startswith('http') or urlparse(url).scheme:
                return url.strip()
            else:
                if self.baseUrl == "":
                    self.baseUrl = "http://" + url
                    print(self.baseUrl)
                return urljoin(self.baseUrl,url.strip())
        else:
            pass

    def spider(self):
        while(not self.q.empty() or self.spider_status):
            url = self.q.get()
            if url in self.crawed_list :
                continue
            print("requesting:",url)
            try:
                resp = requests.get(url=url, headers=self.headers, timeout=5, verify=False)
                self.htmlParse(resp)
                self.crawed_list.add(url)
            except:
                print("requests error:",url)

            if self.spider_status == 1:
                time.sleep(5)
                self.spider_status = 0

            print(self.q.qsize())

    def htmlParse(self,response):
        tempList = []
        blacklist = ['#',None,'javascript:']

        soup = BeautifulSoup(response.text.encode('utf-8'), 'html.parser')
        for href in soup.find_all('a'):
            #print(self.urlParse(href.get('href')))
            tempList.append(href.get('href'))

        for href in soup.find_all('script'):
            #print(self.urlParse(href.get('src')))
            tempList.append(href.get('src'))

        tempList = list(set(tempList)-set(blacklist))
        for i in tempList:
            url = self.return_entire_url(i)
            if validators.url(url):
                print("get:",url)
                #print(i,self.return_entire_url(i))
                if url not in self.crawed_list :
                    self.urlList.append(url)
                    if urlparse(url).netloc in self.baseUrl:
                        self.q.put(url)


if __name__ == "__main__":
    A = linkfinder("http://testphp.vulnweb.com")
    t = threading.Thread(target=A.spider)
    t.start()
    t.join()
    for i in list(set(A.urlList)):
        print(i)



