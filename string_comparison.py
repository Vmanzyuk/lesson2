def string_comparison(str1,str2):
	if isinstance(str1,str) and isinstance(str2,str):
		if str1==str2:
			return 1
		elif str1!=str2 and str2=='learn':
			return 3
		elif str1!=str2 and len(str1)>len(str2):
			return 2
	else:
		return 0

print(string_comparison(1,'2'))
print(string_comparison('1','1'))
print(string_comparison('33','2'))
print(string_comparison('learn22','learn'))
print(string_comparison('1','2'))
