from urllib.request import urlopen
import re
html = urlopen("http://ebooks.cmanuf.com/pdfReader?id=19E34E52B8F4A7F96EB17EBA8AD4FD5D0D5DE1C498C55D8EC4024656B28605AB").read().decode('utf-8')
res = re.findall(r"ifm.src=(.+?);", html)
print("\n The URL is: ", res[0])
