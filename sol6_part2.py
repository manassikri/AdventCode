# with open("D:\\DownloadsD\\PythonPrograms\\AdventCode\\text6.txt") as f:
#     lines = f.read()

file = open("text6.txt", "r")
parent={}
size=0
res=0;
no =0
for lin in file:

	# if no==6:
	# 	break

	
	if lin is '\n':
		for ele in parent:
			if parent[ele]==size:
				print(ele)
				res+=1
		parent={}
		print("Total Count")
		print(res)
		print("Corresponding size")
		print(size)
		print("------------")
		size=0
	else:
		print(lin)
		child={}
		for c in lin :
			if c is '\n':
				continue
			#print(c)
			if c not in child:
				if c not in parent:
					parent[c]=1
				else:
					parent[c]+=1
				child[c]=1

		print(parent)
		size+=1
	no+=1


for ele in parent:
	if parent[ele]==size:
		print(ele)
		res+=1
print(res)