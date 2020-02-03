import re
from urllib.request import urlopen

Book_detail = urlopen("http://ebooks.cmanuf.com/detail?id=3790").read().decode('utf-8')
Book_ID = re.findall(r"pdfReader\?id=(.+?)\"",Book_detail)
ID=Book_ID[0]
#获取书籍ID

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
