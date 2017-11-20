#!/usr/bin/env python

import json
import jaconv
from kana2nums import kana2nums

import os.path

dirname = os.path.dirname(__file__)
f = open(dirname + "/../data/dict/jmdict_lemma_single.json",'r',encoding="utf-8_sig")
jmdict = json.load(f)
f.close()

count = 0
for entry in jmdict:
	if("reb" in entry):
		reb = entry["reb"]
		kana = jaconv.kata2hira( reb )
		pos = entry["pos"]
		nums = kana2nums(kana)
		if(nums != None):
			print( "{" )
			if( "keb" in entry ):
				print( '"kanji": "' + entry["keb"] + '",' )
			print( '"kana": "' + reb + '",' )
			print( '"hira": "' + kana + '",' )
			print( '"pos": ' + str(pos).replace("'", '"') + ',' )
			print( '"nums": "' + nums  + '"' )
			print( "}," )
			count += 1
