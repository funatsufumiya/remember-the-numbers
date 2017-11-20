#!/usr/bin/env python

dict = {
	"い": 1,
	"いっ": 1,
	"いー": 1,
	"いち": 1,
	"いん": 1,
	# "いつ": 5,
	"お": 0,
	"おお": 0,
	"おう": 0,
	"おん": 0,
	"きゅう": 9,
	"きゅー": 9,
	"く": 9,
	"ぐ": 9,
	"こ": 5,
	"こう": 5,
	"こー": 5,
	"ご": 5,
	"ごう": 5,
	"ごー": 5,
	"さ": 3,
	"さー": 3,
	"さっ": 3,
	"さん": 3,
	"ざ": 3,
	"ざー": 3,
	"ざっ": 3,
	"ざん": 3,
	"し": 4,
	"しー": 4,
	"しっ": 4,
	"しょ": 4,
	"しん": 4,
	"じ": 4,
	"じー": 4,
	"じっ": 4,
	"じん": 4,
	"じゅう": 10,
	"じゅー": 10,
	"じょ": 4,
	"す": 3,
	"すっ": 3,
	"ず": 3,
	"ずっ": 3,
	"そ": 3,
	"ぞ": 3,
	"そっ": 3,
	"ぞっ": 3,
	"そん": 30,
	"ぞん": 30,
	"つ": 2,
	"てん": 10,
	"と": 10,
	"とっ": 10,
	"とう": 10,
	"とお": 10,
	"とー": 10,
	"ど": 10,
	"どっ": 10,
	"どう": 10,
	"どー": 10,
	"な": 7,
	"なっ": 7,
	# "なな": 7,
	"なん": 7,
	"に": 2,
	"にー": 2,
	"にい": 2,
	"にっ": 2,
	"にん": 2,
	"は": 8,
	"はー": 8,
	"はっ": 8,
	"ぱ": 8,
	"ぱー": 8,
	"ぱっ": 8,
	"ぱん": 8,
	"ば": 8,
	"ばー": 8,
	"ばん": 8,
	"ひ": 1,
	"ひー": 1,
	"ひっ": 1,
	"び": 3,
	"びー": 31,
	"びっ": 3,
	"ぴ": 3,
	"ぴー": 31,
	"ぴっ": 3,
	"ひと": 1,
	"びと": 1,
	"ぴと": 1,
	"ふ": 2,
	"ぷ": 2,
	"ぶ": 2,
	"ふた": 2,
	"ぶた": 2,
	"ふだ": 2,
	"ま": 0,
	"み": 3,
	"みー": 3,
	"みい": 31,
	"みっ": 3,
	"みつ": 3,
	"みず": 3,
	"みん": 3,
	"む": 6,
	"や": 8,
	"やっ": 8,
	# "やつ": 8,
	"やー": 8,
	"よ": 4,
	"よっ": 4,
	"よん": 4,
	"る": 6,
	"れ": 0,
	# "れい": 0,
	"れー": 0,
	"れん": 0,
	"ろ": 6,
	"ろう": 6,
	"ろー": 6,
	"ろっ": 6,
	"ろく": 6,
	"わ": 8,
	"わー": 8,
	"を": 0,
	"ん": 0,
	"ー": 0,
}

def kana2nums(kana, is_ignore=False, is_strict=True):
	out = ""
	s_prev = ""
	s = kana
	succeeded = False
	index = 0

	while(True):
		s_prev = s[0:]

		if(len(s) >= 3):
			c = s[0:3]
			if(c in dict):
				out += str(dict[c])
				s = s[3:]
				index += 3
				continue

		if(len(s) >= 2):
			c = s[0:2]
			if(c in dict):
				out += str(dict[c])
				s = s[2:]
				index += 2
				continue
		
		if(len(s) >= 1):
			c = s[0]
			if(c in dict):
				out += str(dict[c])
				s = s[1:]
				index += 1

		if(len(s) == 0):
			succeeded = True
			break
		elif(is_ignore == True and s == s_prev):
			s = s[1:]
			index += 1
			continue
		elif(is_ignore == False and s == s_prev):
			break
		
	if(succeeded):
		return out
	else:
	  if(is_strict):
	  	return None
	  else:
	  	return out

if __name__ == '__main__':
	import sys

	args = sys.argv[1:]

	if(len(args) < 1 or args[0] == '-h' or args[0] == '--help'):
		sys.stderr.write("Usage: kana2nums [hiragana]");
		exit(1)

	kana = args[0]
	is_ignore = False
	is_strict = False

	if(len(args) >= 2):
		if(args[0] == '-ignore' or args[0] == '--ignore'):
			kana = args[1]
			is_ignore = True
		elif(args[1] == '-ignore' or args[1] == '--ignore'):
			kana = args[0]
			is_ignore = True
		elif(args[0] == '-strict' or args[0] == '--strict'):
			kana = args[1]
			is_strict = True
		elif(args[1] == '-strict' or args[1] == '--strict'):
			kana = args[0]
			is_strict = True
	
	print( kana2nums(kana, is_ignore, is_strict) )