def  highest_consonant_v1(s):
for l in s:
	if l is not in  ["a","e","o","i","u"]
		sub+=l
	else:
		sub+=" "
substrings=sub.split('')
values=[ ]
	for  sub in substrings:
		values.append(evaluate(sub))

def evaluate(string):
value=0
dictionary={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"x":22,"y":24,"z":25}
for letter in dictionary:
	value+=dictionary[letter]