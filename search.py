
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

import csv

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ",]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    cnt = 0
    list_num = len(source)
    for i in source:
        cnt+=1
        if i == word:
            print(f"{word}が見つかりました。")
            break
        if cnt == list_num:
            print("見つかりませんでした。検索ワードをリストに追加しました。")
            #検索ワードをリストに追加
            source.append(word)
            
            #csvの中身をリストに追加
            print("csvファイルからリストに追加しました。")
            f = open('listcsv.csv', 'r')
            dataReader = csv.reader(f)
            row = next(dataReader)
            source.extend(row)
            f.close()
            
            #csvに最新のリストを書き込み
            print("最新のリストをcsvに反映しました。")
            f = open('listcsv.csv', 'w', encoding='utf-8', newline='')
            dataWriter = csv.writer(f)
            dataWriter.writerow(source)
            f.close()
            break

if __name__ == "__main__":
    search()