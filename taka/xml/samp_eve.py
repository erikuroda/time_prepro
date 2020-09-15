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
file = open('n1.txt', 'w')

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
			reltypeA = str(e2.get('relTypeA'))
			reltypeB = str(e2.get('relTypeB'))
			reltypeC = str(e2.get('relTypeC'))
			if str(e2.get('task')) == 'DCT':
				if id1 == id2:
					if reltypeA == reltypeB:
						line += '\t|reltype=' + reltypeA
						reltype = ''
						break;
					elif reltypeA == reltypeC:
						line += '\t|reltype=' + reltypeA
						reltype = ''
						break;
					elif reltypeB == reltypeC:
						line += '\t|reltype=' + reltypeB
						reltype = ''
						break;
		# print(line)
		text += line + '\n'

	# ファイルに書き込み
	file.write(text)

# ファイルクローズ
file.close()
