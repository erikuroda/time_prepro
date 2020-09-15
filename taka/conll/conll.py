# -*- coding: UTF-8 -*-
# conll.py
# 目的：event.txtの内容を、conllファイルに紐付ける。

# 正規表現のライブラリをインポート
import re

# ファイルオープン
event = open('event_edit.txt', 'r')
result = open('result_edit.txt', 'w')

# 変数を定義
n1 = 0 # wordが含まれるtextのline
n2 = 0 # n1の次にtextが含まれるline
n3 = 0 # wrodのline
n4 = 0 # 文字数カウント変数
xml = ''

# test.txtの内容を一行ずつ読み込む
for line1 in event:

	# textとcheckを定義
	text = ''
	check = 0

	# 行の内容をタブで分割してそれぞれ定義
	xml_new = line1.split('\t').pop(0)
	word = line1.split('\t').pop(1)
	data = line1.split('\t').pop(2)

	text += word + '\n'
	
	# もし、読み込むべきconllファイルが変わったら、
	if(xml != xml_new):

		# n1とn3とxmlを変更
		n1 = 0
		n3 = 0
		xml = xml_new

		# conllファイルの内容を一行ずつ読み込み、リストに代入
		conll = open(xml + '.conll', 'r+')
		lines = conll.readlines()
		conll.close()

	
	# 単語が含まれている文章を位置を特定

	# 同じ文章のそれより後に含まれていないか見る
	if lines[n1].rfind(word) > n4:
		n4 = lines[n1].find(word)
		line3 = lines[n1]

	# 見つからなかったら、それより後の部分を探しに行く
	else:
		for line2 in lines:

			if line2.find(word) > 0 and line2.find('# text') != -1 and lines.index(line2) > n1:
				n4 = line2.find(word)
				n1 = lines.index(line2)
				line3 = line2
				break;


	# 単語が含まれている文章の次の文章の位置を特定
	for line2 in lines:
			
		if line2.find('# text') != -1 and lines.index(line2) > n1:
			n2 = lines.index(line2)
			text += str(n1) + ',' + str(n2) + '\n' + line3
			break;

	# その文がファイルの最後だった場合、n2を10000に設定
	if n1 >= n2 or n2 == 10000:
		n2 = 10000
		text += str(n1) + ',' + str(n2) + '\n' + line3
	

	# 単語に一致する箇所を探す
	# 先頭2文字で見る
	if check == 0:
		for line2 in lines:
		
			if line2.find(word[0:2]) >= 0 and line2.find('# text') == -1 and lines.index(line2) > n3 and lines.index(line2) < n2:
				n3 = lines.index(line2)
				# text += 'line:' + str(n3) + ', place:' + str(n4) + '\n' + line2 + data +  '\n'
				text += 'line:' + str(n3) + '\n' + line2 + data +  '\n'
				check = 1
				break;

	# 見つからなかったら、先頭1文字で見る
	if check == 0:
		for line2 in lines:
		
			if line2.find(word[0:1]) >= 0 and line2.find('# text') == -1 and lines.index(line2) > n3 and lines.index(line2) < n2:
				n3 = lines.index(line2)
				# text += 'line:' + str(n3) + ', place:' + str(n4) + '\n' + line2 + data +  '\n'
				text += 'line:' + str(n3) + '\n' + line2 + data +  '\n'
				check = 1
				break;
	
	# それでも見つからなかったら、エラーとして出力
	if check == 0:
		print(line1)

	
	# ファイルにtextの情報を書き込み
	result.write(text)

# ファイルクローズ
event.close()
result.close()


'''
今後の展開
単語を1文字ずつ区切って、1文字ずつ繋げて、その繋がったものが見つかったら当てはめ、次のステップに進むという形で書く？

conllファイルの、'Bunsetu'を含む行だけとってきて、listに入れるというのはどうだろうか？
→そこでtab区切り→2番目の要素をつなげて単語を作る
3番目の要素に'為る'があったら、例外そちを行う
'''

