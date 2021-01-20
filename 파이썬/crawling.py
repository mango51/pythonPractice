from urllib.request import urlopen

html = urlopen("http://www.naver.com/")
doc = html.read().decode("UTF-8")
print(doc)
