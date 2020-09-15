# -*- coding: UTF-8 -*-
# check.py
# 目的：result.txtの内容の整合性を、何行目の情報かを見ていくことで確認する。

# 正規表現のライブラリをインポート
import re

# ファイルオープン
result = open('result_edit.txt', 'r')

# result.txtの内容を一行ずつ読み込む
lines = result.readlines()

# ファイルクローズ
result.close()

# カウント用の変数を作成
ok = 0
ng = 0

# 数字を格納するリストを作成
list1 = []
list2 = []

# result.txtの内容を一行ずつ読み込む
for line in lines:
	# 数字,数字の行を取り出してlist1に追加
	if re.search('[0-9]+,[0-9]+',line) != None:
		list1.append(line.replace('\n', ''))

	# line:数字の行を取り出してlist2に追加
	if re.match('.*line:.*',line) != None:
		list2.append(line.replace('\n', '').replace('line:', ''))
	
# デバック用
# print(list1)
# print(list2)

# リストの長さを取得
length = len(list2)
print(length)

# リストの中身を見ていく
for n in range(length):

	# a,b,cを3つ定義
	a = int(list1[n].split(',').pop(0)) # textの行
	b = int(list1[n].split(',').pop(1)) # 次のtextの行
	c = int(list2[n]) #wordの行

	print(a,b,c)

	# OK or NG 判定
	if a < c and c < b: # cがaとbの間にあったらOK
		ok += 1
		print('→OK\n')

	else: # そうでなかったらNG
		ng += 1
		print('→NG\n')

# 割合を計算
x = ok/length*100
y = ng/length*100

# カウントの結果を出力
print('~result~')
print('OK:',ok, x, '%')
print('NG:',ng, '\t', y, '%')
