# -*- coding: UTF-8 -*-

# モジュールのインポート
import xml.etree.ElementTree as ET
import glob

# ディレクトリ内のxmlファイルリストを作成
path = '../BCCWJ-TIMEX/00054_A_PN3b_00004.xml'
file_list = []
file_list = glob.glob(path)

# 昇順にソート
file_list.sort()

# ファイルオープン
file = open('./correct/e2e_54.tsv', 'w')
line = 'event1_id' + '\t' + 'event2_id' + '\t' + 'reltype' + '\n'

# ディレクトリ内のすべてのxmlファイルの読み込み
for xml in file_list:
	#file = open('./correct/t2e_1.tsv', 'w')
	#line = 'time_id' + '\t' + 'event_id' + '\t' + 'reltype' + '\n'
	tree = ET.parse(xml)
	root = tree.getroot()
	es1 = root.findall('.//EVENT')
	es2  = root.findall('.//TLINK')
	text = ''
	i = 0

	#for e1 in es1:
	for e2 in es2:
		#id1 = str(e1.get('eid')).replace('e', 'ei')
		#id2 = str(e2.get('relatedToEventInstance'))
		ev = str(e2.get('task'))
		if ev == 'E2E':
			reltypeA = str(e2.get('relTypeA'))
			reltypeB = str(e2.get('relTypeB'))
			reltypeC = str(e2.get('relTypeC'))
			eve1 = str(e2.get('eventInstanceID')).replace('ei','e')
			eve2 = str(e2.get('relatedToEventInstance')).replace('ei','e')
			if reltypeA == reltypeB:
				line += eve1 + '\t' + eve2 + '\t' + reltypeA + '\n'
				#reltypeA = ''
				#break
			elif reltypeA == reltypeC:
				line += eve1 + '\t' + eve2 + '\t' + reltypeA + '\n'
				#reltypeA = ''
				#break
			elif reltypeB == reltypeC:
				#reltypeB = ''
				line += eve1 + '\t' + eve2 + '\t' + reltypeB + '\n'
				#break
		else:
			continue
	#print(line)
	file.write(line)
	        # ファイルに書き込み
	        #file.write(text)

# ファイルクローズ
file.close()
