import re
from urllib.request import urlopen

ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
]
ua=random.choice(ua_list)

Book_ID=list(range(10000))
Book_ID_Str=Book_ID[i]
Book_link='http://ebooks.cmanuf.com/detail?id='
List_book_link=list(Book_link)
List_book_ID=list(Book_ID_Str)
List_book_link=List_book_link+List_book_ID
Str_book_link="".join(List_book_link)
Book_detail = urlopen(Str_book_link).read().decode('utf-8')
Reader_ID = re.findall(r"pdfReader\?id=(.+?)\"",Book_detail)
ID=Reader_ID[0]
#获取Reader ID

Reader_link = 'http://ebooks.cmanuf.com/pdfReader?id='
List_link_Reader = list(Reader_link)
List_ID = list(ID)
List_link_Reader=List_link_Reader+List_ID
Str_link_Reader="".join(List_link_Reader)
#获取Reader地址

Reader = urlopen(Str_link_Reader).read().decode('utf-8')
url = re.findall(r"ifm\.src=(.+?);", Reader)
url=re.sub('[\\\]','',url)
url=re.sub('\[|/g','',url)
url=re.sub(']','',url)
url=url.replace("pdfReadereneric/web/viewer.html?file=../../../","")
print(url)
#获取下载地址
