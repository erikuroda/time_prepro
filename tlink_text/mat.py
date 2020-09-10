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
file = open('mat.txt', 'w')

# ディレクトリ内のすべてのxmlファイルの読み込み
for xml in file_list :

	tree = ET.parse(xml)

	# rootという要素を作成
	root = tree.getroot()

	# すべての子孫要素の中からEVENT・をすべて取得
	es1 = root.findall('.//EVENT')
	es2  = root.findall('.//TLINK')

	# textを定義
	text = ''

	i = 0
	# 出力
	for e2 in es2:
		ev = str(e2.get('task'))
		if ev == 'MAT':
			reltypeA = str(e2.get('relTypeA'))
			reltypeB = str(e2.get('relTypeB'))
			reltypeC = str(e2.get('relTypeC'))
			f_event = str(e2.get('eventInstanceID')).replace('ei','e')
			s_event = str(e2.get('relatedToEventInstance')).replace('ei','e')
			line = f_event + '\t' + s_event + '\t' + reltypeA
			text = line + '\n'
			file.write(text)
		else:
			continue
	#print(line)
	# ファイルに書き込み
	#file.write(text)
	# ファイルクローズ
file.close()
