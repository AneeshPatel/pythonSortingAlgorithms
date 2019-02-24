listofval=[]
endGame=False

def end(value, list):
    if value=='':
        return True
    else:
        list.append(value)
        return False
    
while endGame!=True:
    number=input("Please enter a number")
    if end(number, listofval)==True:
        endGame=True
    else:
        endGame=False
print(listofval)

for x in range(0,len(listofval)):
    print("x=", x)
    for y in range(x+1,len(listofval)):
        if int(listofval[x])>int(listofval[y]):
            z=listofval[x]
            listofval[x]=listofval[y]
            listofval[y]=z
            print(listofval)
        


