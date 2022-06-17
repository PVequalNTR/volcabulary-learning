
import Cambridge
import yahoo

def GetWebData(word):
    CambridgelistEn,CambridgelistCh = Cambridge.GetWebData(word)
    yahoolistEn,yahoolistCh,Tense,Comparative,Plural,VerbChange = yahoo.GetWebData(word)
    notfind = []

    if(CambridgelistEn=="Can't find the word in Cambridge"):
        notfind.append("Cambridge")
        CambridgelistEn=[]
    if(yahoolistEn=="Can't find the word in yahoo"):
        notfind.append("yahoo")
        yahoolistEn=[]

    listEn = []
    listEn.append(CambridgelistEn)
    listEn.append(yahoolistEn)
    listCh = []
    listCh.append(CambridgelistCh)
    listCh.append(yahoolistCh)

    return listEn,listCh,Tense,Comparative,Plural,VerbChange,notfind
    # 回傳格式 
    # [ 'an _____ door/window', 'An _____ suitcase lay on her bed.'.... ]
    # ,["中文","這是中文"...]
    # ,[過去式,過去分詞,現在分詞] 動詞 (無則為[])
    # ,[比較級,最高級] 形容詞 (無則為[])
    # ,[名詞複數] 可數名詞 (無則為[])
    # ,[過去式1,過去式2,過去分詞1,過去分詞2,現在分詞] 如果過去式有兩種則有值 (無則為[])
    # 相對的中英文有同個index
    # 如果找不到單字，notfind = [Cambridge,yahoo] *也可能出現一個找到一個找不到的情況
    # 當yahoo找不到 Tense,Comparative,Plural,VerbChange 皆為0
    # 當兩者都找不到 listEn,listCh 為 []


if __name__ == '__main__':
    word = input("輸入 ")
    print(GetWebData(word))