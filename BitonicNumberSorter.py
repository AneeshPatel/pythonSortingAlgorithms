listofval=[]
endGame=False

def checkInteger(inputx):
    try:
        int(inputx)
        return True
    except ValueError:
        return False
    
def compareStep1(listx):
    x=0
    while x<(len(listx)-1):
        first=listx[x]
        adjacent=listx[x+1]
        if x%4==0 or x==0:
            if first>=adjacent:
                listx[x+1],listx[x]=listx[x],listx[x+1]
        else:
            if first<=adjacent:
                listx[x+1],listx[x]=listx[x],listx[x+1]
        x+=2
    print(listx)

def compareStep2(listx):
    x=0
    while x<(len(listx)-2):
        first=listx[x]
        other=listx[x+2]
        if x==0 or x==1 or x==8 or x==9:
            if first>=other:
                listx[x+2],listx[x]=listx[x],listx[x+2]
        elif x==4 or x==5 or x==12 or x==13:
            if first<=other:
                listx[x+2],listx[x]=listx[x],listx[x+2]
        x+=1
    print(listx)

def compareStep3(listx):
    x=0
    while x<(len(listx)-1):
        first=listx[x]
        adjacent=listx[x+1]
        if x==0 or x==2 or x==8 or x==10:
            if first>=adjacent:
                listx[x+1],listx[x]=listx[x],listx[x+1]
        elif x==4 or x==6 or x==12 or x==14:
            if first<=adjacent:
                listx[x+1],listx[x]=listx[x],listx[x+1]
        x+=1
    print(listx)

def compareStep4(listx):
    x=0
    while x<=((len(listx))-((len(listx)/4)+1)):
        first=listx[x]
        other=listx[x+int((len(listx)/4))]
        if x<=((len(listx)/4)-1):
            if first>=other:
                listx[x+int((len(listx)/4))],listx[x]=listx[x],listx[x+int((len(listx)/4))]
        elif x>=(len(listx)/2):
            if first<=other:
                listx[x+int((len(listx)/4))],listx[x]=listx[x],listx[x+int((len(listx)/4))]
        x+=1
    print(listx)

def compareStep5(listx):
    x=0
    while x<=(len(listx)-3):
        first=listx[x]
        other=listx[x+2]
        if x==0 or x==1 or x==(len(listx)/4) or x==((len(listx)/4)+1):
            if first>=other:
                listx[x+2],listx[x]=listx[x],listx[x+2]
        elif x==(len(listx)/2) or x==((len(listx)/2)+1) or x==(((len(listx))*3)/4) or x==((((len(listx))*3)/4)+1):
            if first<=other:
                listx[x+2],listx[x]=listx[x],listx[x+2]
        x+=1
    print(listx)

def compareStep6(listx):
    x=0
    while x<=(len(listx)-2):
        first=listx[x]
        adjacent=listx[x+1]
        if x%2==0:
            if x<(len(listx)/2):
                if first>=adjacent:
                    listx[x+1],listx[x]=listx[x],listx[x+1]
            else:
                if first<=adjacent:
                    listx[x+1],listx[x]=listx[x],listx[x+1]
        x+=1
    print(listx)

def compareStep7(listx):
    x=0
    while x<(len(listx)/2):
        first=listx[x]
        other=listx[x+int((len(listx)/2))]
        if first>=other:
            listx[x+int((len(listx)/2))],listx[x]=listx[x],listx[x+int((len(listx)/2))]
        x+=1
    print(listx)

def compareStep8(listx):
    x=0
    y=int(len(listx)/2)
    while x<=((len(listx)/4)-1):
        first=listx[x]
        other=listx[x+int((len(listx)/4))]
        if first>=other:
            listx[x+int((len(listx)/4))],listx[x]=listx[x],listx[x+int((len(listx)/4))]
        x+=1
    while y>=(len(listx)/2) and y<=(((len(listx)*3)/4)-1):
        first=listx[y]
        other=listx[y+int((len(listx)/4))]
        if first>=other:
            listx[y+int((len(listx)/4))],listx[y]=listx[y],listx[y+int((len(listx)/4))]
        y+=1
    print(listx)

def compareStep9(listx):
    x=0
    while x<=(len(listx)-3):
        first=listx[x]
        other=listx[x+2]
        if x==0 or x==1 or x==(len(listx)/4) or x==((len(listx)/4)+1) or x==(len(listx)/2) or x==((len(listx)/2)+1) or x==((len(listx)*3)/4) or x==(((len(listx)*3)/4)+1):
            if first>=other:
                listx[x+2],listx[x]=listx[x],listx[x+2]
        x+=1
    print(listx)

def compareStep10(listx):
    x=0
    while x<=(len(listx)-2):
        first=listx[x]
        adjacent=listx[x+1]
        if x%2==0:
            if first>=adjacent:
                listx[x+1],listx[x]=listx[x],listx[x+1]
        x+=1
    print(listx)

def runSort():
    listofval=[]
    counter=1
    global endGame
    while endGame!=True:
        amount=input("How many integers would you like to have sorted? (Please choose either 4, 8 or 16)")
        if checkInteger(amount):
            if int(amount)==4 or int(amount)==8 or int(amount)==16:
                print("Please enter " + amount + " numbers")
                endGame=True
            else:
                print("Sorry, that is an invalid input. Please try again.")
        else:
            print("Sorry, that is an invalid input. Please try again.")

    endGame=False
    while endGame!=True and counter<=int(amount):
        number=input("Please enter a number")
        if checkInteger(number):
            listofval.append(int(number))
            counter+=1
        else:
            print("Sorry, that is an invalid input. Please try again.")
            
    print("Here is the list of numbers you chose :", listofval)

    compareStep1(listofval)
    compareStep2(listofval)
    compareStep3(listofval)
    compareStep4(listofval)
    compareStep5(listofval)
    compareStep6(listofval)
    compareStep7(listofval)
    compareStep8(listofval)
    compareStep9(listofval)
    compareStep10(listofval)

    again=input("Would you like to do it again?")
    if again=="yes" or again=="Yes":
        runSort()

runSort()
