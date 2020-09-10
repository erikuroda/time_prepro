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
file = open('t2e_sam.txt', 'w')

# ディレクトリ内のすべてのxmlファイルの読み込み
for xml in file_list :

	tree = ET.parse(xml)

	# rootという要素を作成
	root = tree.getroot()

	# すべての子孫要素の中からEVENT・をすべて取得
	es2  = root.findall('.//TLINK')

	# textを定義
	text = ''

	i = 0
	# 出力
	for e2 in es2:
		ev = str(e2.get('task'))
		if ev == 'T2E':
			reltype = str(e2.get('relTypeA'))
			time = str(e2.get('timeID'))
			event = str(e2.get('relatedToEventInstance')).replace('ei','e')
			line = ev + '\t' + time + '\t' + event + '\t' + reltype
			text = line + '\n'
			file.write(text)
		else:
			continue
	#print(line)
	# ファイルに書き込み
	#file.write(text)
	# ファイルクローズ
file.close()
