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

is_first_print = True
def print_json_element(name, kana, nums, pos, vari=""):
	global is_first_print

	if is_first_print:
		print( "{" )
		is_first_print = False
	else:
		print( ",{" )
	print( '"kanji": "' + name + '",' )
	print( '"nums": "' + nums  + '",' )
	print( '"kana": "' + kana + '",' )
	print( '"hira": "' + kana + '",' )
	if vari != "":
		print( '"pos": ' + str(pos).replace("'", '"') + ',' )
		print( '"vari": "' + vari  + '"' )
	else:
		print( '"pos": ' + str(pos).replace("'", '"') + '' )

	print( "}" )

print("[")

count = 0
for entry in jmdict:
	if("kana" in entry):
		typ = entry["type"]
		name = entry["name"] + typ
		kana = entry["kana"] + typ_kana(typ)
		pos = ["n"]
		nums = kana2nums(kana)
		if(nums != None):
			print_json_element(name, kana, nums, pos)
			print_json_element(name+"に", kana+"に", nums+"2", pos, "ni")
			print_json_element(name+"が", kana+"が", nums+"5", pos, "ga")
			print_json_element(name+"を", kana+"を", nums+"0", pos, "wo")
			count += 1

print("]")
