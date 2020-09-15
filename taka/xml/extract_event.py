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
file = open('event.txt', 'w')

# ディレクトリ内のすべてのxmlファイルの読み込み
for xml in file_list :

	tree = ET.parse(xml)

	# rootという要素を作成
	root = tree.getroot()

	# すべての子孫要素の中からEVENT・をすべて取得
	es1 = root.findall('.//EVENT')
	es2 = root.findall('.//TLINK')

	# textを定義
	text = ''

	# 出力
	for e1 in es1:
		line = xml[2:20] + '\t' + str(e1.text) + '\t' + str(e1.get('eid'))
		for e2 in es2:
			id1 = str(e1.get('eid')).replace('e', 'ei')
			id2 = str(e2.get('relatedToEventInstance'))
			if str(e2.get('task')) == 'DCT':
				if id1 == id2:
					reltype = str(e2.get('relTypeA'))
					line += '\t|reltype=' + reltype
					reltype = ''
					break;
		# print(line)
		text += line + '\n'

	# ファイルに書き込み
	file.write(text)

# ファイルクローズ
file.close()
