#!/usr/bin/env python

import json
import jaconv
from kana2nums import kana2nums

import os.path

dirname = os.path.dirname(__file__)
f = open(dirname + "/../data/dict/jmdict_lemma_single.json",'r',encoding="utf-8_sig")
jmdict = json.load(f)
f.close()

is_first_print = True

def print_json_element(dic):
	global is_first_print

	d = dic

	if is_first_print:
		print( "{" )
		is_first_print = False
	else:
		print( ",{" )

	if( d["kanji"] != None ):
		print( '"kanji": "' + d["kanji"] + '",' )
	print( '"nums": "' + d["nums"]  + '",' )
	print( '"kana": "' + d["kana"] + '",' )
	print( '"hira": "' + d["hira"] + '",' )
	if( "vari" in d ):
		print( '"pos": ' + str(d["pos"]).replace("'", '"') + ',' )
		print( '"vari": "' + d["vari"] + '"' )
	else:
		print( '"pos": ' + str(d["pos"]).replace("'", '"') + '' )
	print( "}" )

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

			# Add variations ----

			# Noun variations
			if "n" in pos or "n-adv" in pos or "n-t" in pos:
				e2 = e.copy()
				e2["vari"] = "ni"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "に"
				e2["hira"] += "に"
				e2["kana"] += "に"
				e2["nums"] += "2"
				print_json_element(e2)

				e3 = e.copy()
				e3["vari"] = "sa-noun"
				if( kanji != None ):
					e3["kanji"] = e3["kanji"] + "さ"
				e3["hira"] += "さ"
				e3["kana"] += "さ"
				e3["nums"] += "3"
				print_json_element(e3)

				e3 = e.copy()
				e3["vari"] = "yo"
				if( kanji != None ):
					e3["kanji"] = e3["kanji"] + "よ"
				e3["hira"] += "よ"
				e3["kana"] += "よ"
				e3["nums"] += "4"
				print_json_element(e3)

				if "n" in pos:
					e3 = e.copy()
					e3["vari"] = "ga"
					if( kanji != None ):
						e3["kanji"] = e3["kanji"] + "が"
					e3["hira"] += "が"
					e3["kana"] += "が"
					e3["nums"] += "5"
					print_json_element(e3)

				e3 = e.copy()
				e3["vari"] = "mo"
				if( kanji != None ):
					e3["kanji"] = e3["kanji"] + "も"
				e3["hira"] += "も"
				e3["kana"] += "も"
				e3["nums"] += "6"
				print_json_element(e3)

				e3 = e.copy()
				e3["vari"] = "ha"
				if( kanji != None ):
					e3["kanji"] = e3["kanji"] + "は"
				e3["hira"] += "は"
				e3["kana"] += "は"
				e3["nums"] += "8"
				print_json_element(e3)

				if "n" in pos:
					e3 = e.copy()
					e3["vari"] = "wo"
					if( kanji != None ):
						e3["kanji"] = e3["kanji"] + "を"
					e3["hira"] += "を"
					e3["kana"] += "を"
					e3["nums"] += "0"
					print_json_element(e3)

		 	# Verb variations
			elif "v5k" in pos or "v5r" in pos or "v5m" in pos or "vs-s" in pos:
				e2 = e.copy()
				e2["vari"] = "na-verb"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "な"
				e2["hira"] += "な"
				e2["kana"] += "な"
				e2["nums"] += "7"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "mo-verb"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "も"
				e2["hira"] += "も"
				e2["kana"] += "も"
				e2["nums"] += "6"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "yo"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "よ"
				e2["hira"] += "よ"
				e2["kana"] += "よ"
				e2["nums"] += "4"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "nayo"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "なよ"
				e2["hira"] += "なよ"
				e2["kana"] += "なよ"
				e2["nums"] += "74"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "sa-verb"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "さ"
				e2["hira"] += "さ"
				e2["kana"] += "さ"
				e2["nums"] += "3"
				print_json_element(e2)

			# Adj variations
			if "adj-na" in pos or ("adv" in pos and not ("n" in pos)):
				e2 = e.copy()
				e2["vari"] = "na"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "な"
				e2["hira"] += "な"
				e2["kana"] += "な"
				e2["nums"] += "7"
				print_json_element(e2)

			elif "adj-i" in pos:
				e2 = e.copy()
				e2["vari"] = "na"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "な"
				e2["hira"] += "な"
				e2["kana"] += "な"
				e2["nums"] += "7"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "ga-adj"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "が"
				e2["hira"] += "が"
				e2["kana"] += "が"
				e2["nums"] += "5"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "yo"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "よ"
				e2["hira"] += "よ"
				e2["kana"] += "よ"
				e2["nums"] += "4"
				print_json_element(e2)

				e2 = e.copy()
				e2["vari"] = "sa-adj"
				if( kanji != None ):
					e2["kanji"] = e2["kanji"] + "さ"
				e2["hira"] += "さ"
				e2["kana"] += "さ"
				e2["nums"] += "3"
				print_json_element(e2)


print("]")
