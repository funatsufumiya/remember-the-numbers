#!/usr/bin/env python

import json
import jaconv
from kana2nums import kana2nums

import os.path

dirname = os.path.dirname(__file__)
f = open(dirname + "/../data/dict/jmdict_lemma_single.json",'r',encoding="utf-8_sig")
jmdict = json.load(f)
f.close()

def print_json_element(dic):
	d = dic
	print( "{" )
	if( d["kanji"] != None ):
		print( '"kanji": "' + d["kanji"] + '",' )
	print( '"nums": "' + d["nums"]  + '",' )
	print( '"kana": "' + d["kana"] + '",' )
	print( '"hira": "' + d["hira"] + '",' )
	print( '"pos": ' + str(d["pos"]).replace("'", '"') + ',' )
	if( "vari" in d ):
		print( '"vari": "' + d["vari"] + '"' )
	print( "}," )

print("[")

count = 0
for entry in jmdict:
	if("reb" in entry):
		kanji = None
		if( "keb" in entry ):
			kanji = entry["keb"]
		kana = entry["reb"]
		hira = jaconv.kata2hira( kana )
		pos = entry["pos"]
		nums = kana2nums(hira)
		if(nums != None):
			e = {
				"kanji": kanji,
				"kana": kana,
				"hira": hira,
				"pos": pos,
				"nums": nums
			}

			print_json_element(e)
			count += 1

			if "n" in pos:
				e["vari"] = "1"
				if( kanji != None ):
					e["kanji"] = e["kanji"] + "に"
				e["hira"] += "に"
				e["kana"] += "に"
				e["nums"] += "2"
				print_json_element(e)

print("]")
