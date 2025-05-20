lo=int(input("Enter the lower range: "))
up=int(input("Enter the upper range: "))
print("Prime number between",lo,"and",up,"= ")

for n in range(lo,up+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)