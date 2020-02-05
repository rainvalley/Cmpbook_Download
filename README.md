昨天看到机械工业出版社电子书开放在线阅读，恰巧闲来无事，于是现学现卖，欲写出一个爬虫爬取PDF。粗略统计下，一共有11951本电子书，PDF格式共有10383本。
# 使用方法
`pip3 install requests`

`pip3 install fake_useragent`

`python3 d.py`

使用本地HTTP匿名代理，随机生成UA模拟浏览器，PDF下载URL位于当前目录下的URL.txt，注意下载时需要添加HTTP referer。

~~这个d.py我自己都看不懂~~