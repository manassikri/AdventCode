file = open("temp3.txt", "r")
#print(file.read())
arr = ["byr", "iyr" ,"eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid" ,"cid"]
credentials = {}
count=0
ans=0
fl = 1
c=0
for line in file.readlines():

	if line == '\n':
		#print("reached deadline")
		#print(count)
		
		
		fl=1
		if count==8 or (count==7 and "cid" not in credentials ):


			for wrd in arr:
				if wrd=="byr":
					#print("byr")
					#print(credentials["byr"])
					t1 = int(credentials["byr"])
					if t1>=1920 and t1<=2002:

						pass
						
					else:
						fl=0
						#break

				elif wrd == "iyr":
					#print("iyr")
					#print(credentials["iyr"])
					t2 = int(credentials["iyr"])
					if t2>=2010 and t2<=2020:
						#print("")
						pass
					else:
						fl=0
						#break
				elif wrd == "eyr" :
					#print("eyr")
					#print(credentials["eyr"])
					t3 = int(credentials["eyr"])
					if t3>=2020 and t3<=2030:
						pass
						#print("")
					else:
						fl=0
						#break
				elif wrd == "hgt":
					#print("hgt")
					#print(credentials["hgt"])
					ht = credentials["hgt"]
					lt = len(ht);

					unit = ht[-2:]
					#print(unit)

					height = ht[0:-2]
					#print(height)
					if unit=="cm":
						if int(height)>=150 and int(height) <=193:
							pass
						else:
							fl=0

					elif unit =="in":
						if int(height)>=59 and int(height) <=76:
							pass
						else:
							fl=0

					else:
						fl=0

				elif wrd == "hcl" :
					#print("hcl")
					#print(credentials["hcl"])
					hcl_str = credentials["hcl"]
					lt = len(hcl_str)
					if(len(hcl_str)!=7 or hcl_str[0]!='#' or any(c not in "0123456789abcdef" for c in hcl_str[1:])) :

						fl=0
					else:
						# print("************************")
						# print(hcl_str)
						# print("************************")
						# print("")
						pass
				elif wrd == "ecl":
					# print("ecl")
					# print(credentials["ecl"])
					
					if credentials["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
						pass
					else:
						fl=0
				elif wrd == "pid" :
					# print("pid")
					# print(credentials["pid"])
					if(len(credentials["pid"])==9 and credentials["pid"].isnumeric()):
						pass
					else:
						fl=0
				else :
					if wrd not in arr: 
						fl=0
		
		else:
			fl=0

		ans+=fl
		if fl==1:
			c+=1
			print(credentials,"test",c)
			
		credentials = {}
		#sans=0
		count=0
	else :
		word = line.replace('\n','').split(' ')
		#print(word)
		for wrds in word :
			#print(wrds)
			uni,det = wrds.split(':')
			# if uni=="hgt":
			# 	#print(det)
				
			if uni not in credentials:
				count+=1
				credentials[uni]=det
			else :	
				credentials[uni]=det

if count==8 or (count==7 and "cid" not in credentials ):
	pass
	#ans+=1

print(ans)