wo=input("Enter the word: ")
ch=input("Enter the character: ")
i=0
count=0

while i<len(wo):
    if wo[i]==ch:
        count=count+1
    i=i+1

print(ch,"is occured",count,"times")