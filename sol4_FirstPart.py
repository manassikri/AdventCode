file = open("text3.txt", "r")
#print(file.read())
arr = {"byr", "iyr" ,"eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid" ,"cid"} 
credentials = {}
count=0
ans=0
for line in file.readlines():

	if line is '\n':
		print("reached deadline")
		print(count)
		if count==8 or (count==7 and "cid" not in credentials ):
			ans+=1
		credentials = {}
		#sans=0
		count=0
	else :
		word = line.split(' ')
		print(word)
		for wrds in word :
			print(wrds)
			uni,det = wrds.split(':')
			if uni not in credentials:
				count+=1
				credentials[uni]=det
			else :	
				credentials[uni]=det

if count==8 or (count==7 and "cid" not in credentials ):
	ans+=1

print(ans)