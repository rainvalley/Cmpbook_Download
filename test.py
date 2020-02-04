import re
from urllib.request import urlopen
import time
import requests
from fake_useragent import UserAgent
proxy = '127.0.0.1:10809'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
ua=UserAgent()
header={'User-Agent':ua.random}


def getbook(Detail_ID):
    Book_link='http://ebooks.cmanuf.com/detail?id='
    list_book_link=list(Book_link)
    list_detail_ID=list(str(Detail_ID))#将Detail_ID转换为字符串后再转换为list
    list_book_link=list_book_link+list_detail_ID
    Str_link_book="".join(list_book_link)
    #获取Detail URL

    Book_detail = requests.get(Str_link_book, proxies=proxies,headers=header)
    Book_ID = re.findall(r"pdfReader\?id=(.+?)\"",Book_detail.text)
    ID=Book_ID[0]
    #获取Reader ID

    Reader_link = 'http://ebooks.cmanuf.com/pdfReader?id='
    List_link_Reader = list(Reader_link)
    List_ID = list(ID)
    List_link_Reader=List_link_Reader+List_ID
    Str_link_Reader="".join(List_link_Reader)
    #获取Reader地址

    Reader = requests.get(Str_link_Reader,proxies=proxies,headers=header)
    url = re.findall(r"ifm\.src=(.+?);", Reader.text)
    url=str(url)
    url=re.sub(r"'\"",'',url)
    url = re.sub('[\\\]','',url)
    url=re.sub('\[|/g','',url)
    url=re.sub(']','',url)
    url=url.replace("pdfReadereneric/web/viewer.html?file=../../../","")
    url=url.replace("\"'","")
    print(url)
    f=open("URL.txt","a+")
    f.write("\n")
    f.write(url)
    f.close()
    #获取并处理下载地址
def getID():
    Detail_ID=1
    while Detail_ID<=2:
        time.sleep(2)
        getbook(Detail_ID)
        Detail_ID=Detail_ID+1

getID()