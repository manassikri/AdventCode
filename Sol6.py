# file = open("text6.txt", "r")



with open("D:\\DownloadsD\\PythonPrograms\\AdventCode\\text6.txt") as f:
    lines = f.read()


test=lines.split("\n\n")
print(test)
res=[]
for st in test: 
	res.append(st.replace("\n", ""))

print(res)


sum=0
for ele in res:
	sum+=len(set(ele))


print(sum)

