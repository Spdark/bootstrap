s = input()
k = ''
for i in range(len(s)):
	z = ''
	if(ord(s[i]) >= 65 and ord(s[i]) <= 90):
		z=s[i].lower()
		k = k + z
	else:
		z=s[i].upper()
		k = k + z
print(k)