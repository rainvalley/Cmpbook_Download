import re
import random
from urllib.request import urlopen

def getbook(Detail_ID):
    Book_link='http://ebooks.cmanuf.com/detail?id='
    list_book_link=list(Book_link)
    list_detail_ID=list(str(Detail_ID))
    list_book_link=list_book_link+list_detail_ID
    Str_link_book="".join(list_book_link)

    Book_detail = urlopen(Str_link_book).read().decode('utf-8')
    Book_ID = re.findall(r"pdfReader\?id=(.+?)\"",Book_detail)
    ID=Book_ID[0]
    #获取Reader ID

    Reader_link = 'http://ebooks.cmanuf.com/pdfReader?id='
    List_link_Reader = list(Reader_link)
    List_ID = list(ID)
    List_link_Reader=List_link_Reader+List_ID
    Str_link_Reader="".join(List_link_Reader)
    #获取Reader地址

    Reader = urlopen(Str_link_Reader).read().decode('utf-8')
    url = re.findall(r"ifm\.src=(.+?);", Reader)
    url=str(url)
    url=re.sub(r"'\"",'',url)
    url = re.sub('[\\\]','',url)
    url=re.sub('\[|/g','',url)
    url=re.sub(']','',url)
    url=url.replace("pdfReadereneric/web/viewer.html?file=../../../","")
    url=url.replace("\"'","")
    print(url)
    #获取下载地址

getbook(200)