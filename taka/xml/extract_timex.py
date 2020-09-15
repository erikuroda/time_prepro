# -*- coding: UTF-8 -*-

# モジュールのインポート
import xml.etree.ElementTree as ET
import glob

# ディレクトリ内のxmlファイルリストを作成
path = './*.xml'
file_list = []
file_list = glob.glob(path)

# 昇順にソート
file_list.sort()

# ファイルオープン
file = open('timex.txt', 'w')

# ディレクトリ内のすべてのxmlファイルの読み込み
for xml in file_list :

	tree = ET.parse(xml)

	# rootという要素を作成
	root = tree.getroot()

	# すべての子孫要素の中からTIMEX3をすべて取得
	es = root.findall('.//TIMEX3')

	# textを定義
	text = ''

	# 出力
	for e in es:
		line = xml[2:20] + '\t' + str(e.text) + '\t|tid=' + str(e.get('tid')) + '|define=' + str(e.get('definite')) + '|type=' + str(e.get('type')) + '|value=' + str(e.get('value')) + '|functionInDocument=' + str(e.get('functionInDocument', default=None)) + '|valueFromSurface=' + str(e.get('valueFromSurface', default=None))
		print(line)
		text += line + '\n'

	# ファイルに書き込み
	file.write(text)

# ファイルクローズ
file.close()