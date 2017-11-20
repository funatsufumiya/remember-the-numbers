#!/usr/bin/env python

import json
import os.path
import sys

args = sys.argv[1:]

if len(args) < 2:
	sys.stderr.write("Usage: " + sys.argv[0] + " [table_name] [goro_xxx.json]")
	exit(1)

table_name = args[0]
path = args[1]
f = open(path,'r',encoding="utf-8_sig")
goros = json.load(f)
f.close()

for e in goros:
	s = (
		"INSERT INTO "
		+ table_name
		+ " ( kanji,kana,hira,nums,pos,vari,is_vari ) "
		+ "VALUES ( '[kanji]','[kana]','[hira]','[nums]','[pos]','[vari]',[is_vari] )"
		)
	sql = s

	if 'kanji' in e:
		sql = sql.replace("[kanji]", e["kanji"])
	else:
		sql = sql.replace("[kanji]", e["kana"])

	sql = sql.replace("[kana]", e["kana"]) 
	sql = sql.replace("[hira]", e["hira"]) 
	sql = sql.replace("[nums]", e["nums"]) 
	pos_str = ",".join(e["pos"])
	sql = sql.replace("[pos]", pos_str) 
	if 'vari' in e:
		sql = sql.replace("[vari]", e["vari"]) 
		sql = sql.replace("[is_vari]", '1')
	else:
		sql = sql.replace("[vari]", "")
		sql = sql.replace("[is_vari]", '0')
	print(sql)
