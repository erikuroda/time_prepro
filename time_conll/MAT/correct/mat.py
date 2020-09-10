# -*- coding: UTF-8 -*-

# モジュールのインポート
import xml.etree.ElementTree as ET
import glob

# ディレクトリ内のxmlファイルリストを作成
path = '../../BCCWJ-TIMEX/00054_A_PN3b_00004.xml'
file_list = []
file_list = glob.glob(path)
file_list.sort()
file = open('./mat_54.tsv', 'w')
line = 'event1_id' + '\t' + 'event2_id' + '\t' + 'reltype' + '\n'
for xml in file_list:
	tree = ET.parse(xml)
	root = tree.getroot()
	es1 = root.findall('.//EVENT')
	es2  = root.findall('.//TLINK')
	text = ''
	for e2 in es2:
		ev = str(e2.get('task'))
		if ev == 'MAT':
			reltypeA = str(e2.get('relTypeA'))
			reltypeB = str(e2.get('relTypeB'))
			reltypeC = str(e2.get('relTypeC'))
			eve1 = str(e2.get('eventInstanceID')).replace('ei','e')
			eve2 = str(e2.get('relatedToEventInstance')).replace('ei','e')
			if reltypeA == reltypeB:
				line += eve1 + '\t' + eve2 + '\t' + reltypeA + '\n'
			elif reltypeA == reltypeC:
				line += eve1 + '\t' + eve2 + '\t' + reltypeA + '\n'
			elif reltypeB == reltypeC:
				line += eve1 + '\t' + eve2 + '\t' + reltypeB + '\n'
		else:
			continue
	#print(line)
	file.write(line)
file.close()
