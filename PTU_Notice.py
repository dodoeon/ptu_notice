from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.ptu.ac.kr/index.do')
FrontUrl=('https://www.ptu.ac.kr')
data = BeautifulSoup(response.content,"html.parser",from_encoding="utf-8")

def GETNOTICE(nth):
    nth -= 1
    Data_Tag = data.select('#body > div > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(n) > a > span:nth-child(1)')[nth]['class'][1]
    Data_Title = data.select('#body > div > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(n) > a > span:nth-child(2)')[nth].get_text()
    Data_Link = data.select('#body > div > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(n) > a')[nth]['href']
    Data_Date = data.select('#body > div > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(n) > div')[nth].get_text()
    if Data_Tag != '취업' :
        Data_Link = FrontUrl+Data_Link

    return (Data_Tag, Data_Title, Data_Link, Data_Date)

nth = int(input("1~7번째중 공지글 번호 선택 : "))
print(GETNOTICE(nth))
