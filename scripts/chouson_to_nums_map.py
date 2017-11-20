#!/usr/bin/env python

import json
import jaconv
from kana2nums import kana2nums

import os.path

dirname = os.path.dirname(__file__)
f = open(dirname + "/../data/dict/chouson/chouson_list.json",'r',encoding="utf-8_sig")
jmdict = json.load(f)
f.close()

def typ_kana(typ):
	if typ == '市':
		return 'し'
	elif typ == '村':
		return 'むら'
	elif typ == '町':
		return 'まち'

count = 0
for entry in jmdict:
	if("kana" in entry):
		typ = entry["type"]
		name = entry["name"] + typ
		kana = entry["kana"] + typ_kana(typ)
		pos = ["n"]
		nums = kana2nums(kana)
		if(nums != None):
			print( "{" )
			print( '"kanji": "' + name + '",' )
			print( '"kana": "' + kana + '",' )
			print( '"hira": "' + kana + '",' )
			print( '"pos": ' + str(pos).replace("'", '"') + ',' )
			print( '"nums": "' + nums  + '"' )
			print( "}," )
			count += 1
