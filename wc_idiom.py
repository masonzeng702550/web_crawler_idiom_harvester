import requests
import re
from bs4 import BeautifulSoup
'''
f = open("20210505test.txt","w",encoding='utf-8')
f.write(apple.text)
f.close()
'''
##print(apple.text)
def clear_html_re(src_html):
  content = re.sub(r"</?(.+?)>", "", src_html) 
  dst_html = re.sub(r"\s+", "", content)
  return dst_html

def idiom(word):
  apple = requests.get("https://dict.idioms.moe.edu.tw/idiomList.jsp?idiom="+word)
  banana = requests.get("https://dict.idioms.moe.edu.tw/idiomList.jsp?idiom="+word+"&tp=9")
  soup = BeautifulSoup(apple.text, 'html.parser')
  soup1 = BeautifulSoup(banana.text, 'html.parser')
  a_tag = soup.find_all('div',role='cell')
  a_tag1 = soup1.find_all('div',role='cell')
  test=[]
  for i in a_tag:
    i=str(i) 
    if i[5]=="r":
      #soup = BeautifulSoup(i,'html.parser')
      work=clear_html_re(i)
      #test.append(soup.get_text())
      test.append(work)
  for i1 in a_tag1:
    i1=str(i1) 
    if i1[5]=="r":
      #soup1 = BeautifulSoup(i1,'html.parser')
      work1=clear_html_re(i1)
      if work1 not in test:
         test.append(work1)
  return(test)
      #print(soup.get_text())
verb=["盧","彥","垣","羹","篤","坪","遵","煉"]
for a in verb:
  check=idiom(a)
  print(check)









    





