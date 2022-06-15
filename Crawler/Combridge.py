from urllib.request import Request,urlopen
from bs4 import *
# Request 可以幫助發出複雜的請求(帶header)，所以不直接用urlopen
def GetWebData(word): # 輸入單字
    link = "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/"+word
    request = Request(link,headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    })
    Web = urlopen(request)
    Data = Web.read().decode('utf-8') 
    # 回傳帶了很多16進制垃圾(跳脫字元)，要轉回來
    # type = str所以要解析
    bs4_Data = BeautifulSoup(Data,'html.parser')
    # BeautifulSoup解析html的str成bs4.BeautifulSoup格式，可是他很慢就是
    SetenceDatas = bs4_Data.find_all(name="div", class_="examp dexamp")
    list = []
    for SetenceData in SetenceDatas:
        Setence = SetenceData.span.text.replace(word,"_____")
        list.append(Setence)
        # 這裡不能用.string要用.text，因為span裡面還塞了不少的<a>標籤(連結到個別單字頁面)
        # 使用remove把目標單字替換掉
    return list  
    # 回傳格式 [ 'an _____ door/window', 'An _____ suitcase lay on her bed.'.... ]








