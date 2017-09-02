from lxml import etree
import requests


url='http://www.jianshu.com/trending/weekly?'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
html=requests.get(url,headers=headers).content




selector = etree.HTML(html)
links = selector.xpath('//li/div/a/text()|//div/div[1]/div/a/text()|//*[@id="note-14987795"]/a')
link=[]
for i in links:
    print(i)




