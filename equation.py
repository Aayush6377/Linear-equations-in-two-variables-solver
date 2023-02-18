print("About the program:-")
print("This program can only solve pair of linear equations in two variables")
print("Both the equations must be in ax+by=c format")
print("where a,b,c are any integer")
print("You can use +/- operator only")

equ1=str(input('Enter first equation:'))  #Equation 1
a=''
for i in range(len(equ1)):
    if equ1[i].isspace()==False:
        a+=equ1[i]

equ1=a

num=[]
b=''
for i in range(len(a)):
    if a[i].isdigit()==True or a[i]=='.':
        b+=a[i]
        if '.' in equ1:
            if i==len(a)-1:
                num.append(b)
                b=''

            elif a[i+1].isdigit()==False and a[i+1]!='.':
                num.append(b)
                b=''  
        
        if i==len(a)-1:
            num.append(b)
            b=''
            
        elif a[i+1].isdigit()==False and a[i+1]!='.':
            num.append(b)
            b=''

for i in range(num.count('')):
    num.remove('')
    
for i in range(len(num)):
    num[i]=float(num[i])

alpha1=[]
b=''
for i in range(len(a)):
    if a[i].isalpha()==True:
        alpha1.append(a[i])

ope=[]
for i in range(len(a)):
    if a[i].isdigit()==False and a[i].isalpha()==False and a[i]!='.':
        ope.append(a[i])
            
l1=num+alpha1+ope

    
equ2=str(input('Enter second equation:'))   #Euation 2
a=''
for i in range(len(equ2)):
    if equ2[i].isspace()==False:
        a+=equ2[i]
equ2=a

num=[]
b=''
for i in range(len(a)):
    if a[i].isdigit()==True or a[i]=='.':
        b+=a[i]
        if '.' in equ1:
            if i==len(a)-1:
                num.append(b)
                b=''

            elif a[i+1].isdigit()==False and a[i+1]!='.':
                num.append(b)
                b=''  
        
        if i==len(a)-1:
            num.append(b)
            b=''
            
        elif a[i+1].isdigit()==False and a[i+1]!='.':
            num.append(b)
            b=''

for i in range(num.count('')):
    num.remove('')
    
for i in range(len(num)):
    num[i]=float(num[i])

alpha2=[]
b=''
for i in range(len(a)):
    if a[i].isalpha()==True:
        alpha2.append(a[i])

ope=[]
for i in range(len(a)):
    if a[i].isdigit()==False and a[i].isalpha()==False and a[i]!='.':
        ope.append(a[i])
            
l2=num+alpha2+ope


if len(alpha1)<2:        #for equations like x=45 or y=98
    for x in alpha2:
        if x not in alpha1:
            a=l1.index(alpha1[0])
            l1.insert(a+1,'+')
            l1.insert(a+1,x)
            if equ1[0].isdigit()==True or equ1[0]=='-' and equ1[1].isdigit()==True:
                l1.insert(1,0.0)
            else:
                l1.insert(0,0.0)
            
if len(alpha2)<2:      #for equations like x=45 or y=98
    for x in alpha1:
        if x not in alpha2:
            a=l2.index(alpha2[0])
            l2.insert(a+1,'+')
            l2.insert(a+1,x)
            if equ2[0].isdigit()==True or equ2[0]=='-' and equ2[1].isdigit()==True:
                l2.insert(1,0.0)
            else:
                l2.insert(0,0.0)

if equ1[0]=='-':
    if equ1[1].isdigit()==False:
        l1.insert(0,1.0)
    l1[0]=-l1[0]
    l1.remove('-')

if equ2[0]=='-':
    if equ2[1].isdigit()==False:
        l2.insert(0,1.0)
    l2[0]=-l2[0]
    l2.remove('-')

                
if (type(l1[0])==type(l1[1])==type(l1[2]))==False:
    if equ1[0].isalpha()==True:
        l1.insert(0,1.0)
    if (type(l1[0])==type(l1[1])==type(l1[2]))==False:
        l1.insert(1,1.0)

if (type(l2[0])==type(l2[1])==type(l2[2]))==False:
    if equ2[0].isalpha()==True:
        l2.insert(0,1.0)
    if (type(l2[0])==type(l2[1])==type(l2[2]))==False:
        l2.insert(1,1.0)


if len(l1)>=7 and len(l2)>=7:

    if l1[-1]=='-':
        l1[2]=-l1[2]
        l1.pop(-1)
        
    if l2[-1]=='-':
        l2[2]=-l2[2]
        l2.pop(-1)


    if l1[5]=='-':
        l1[1]=-l1[1]
        
    if l2[5]=='-':
        l2[1]=-l2[1]
        
    K=0
    while l2[0]==0.0 or l2[1]==0.0:
        l1,l2=l2,l1
        K+=1
        if K>6:
            break
                  
    if l1[-4]==l2[-3] and l1[-3]==l2[-4]:  #swapping
        l2[-4],l2[-3]=l2[-3],l2[-4]
        l2[0],l2[1]=l2[1],l2[0]   

    if K==7:
        l1.remove(0.0)
        l2.remove(0.0)
        print(l2[-3],'=',l2[1]/l2[0])
        print(l1[-4],'=',l1[1]/l1[0])

    
    elif l1[0]/l2[0]!=l1[1]/l2[1] and l1[-1]==l2[-1]=='=' and l1[-4]==l2[-4] and l1[-3]==l2[-3]:
        if len(l1)==len(l2)==7:   #calculation
            con=l1[0]/l2[0]

            a=l1[2]-(con*l2[2])
            b=l1[1]-(con*l2[1])
            y=a/b
            x=(l1[2]-(l1[1]*y))/l1[0]
            print(l1[3],'=',x)
            print(l1[4],'=',y)
            
    elif l1[0]/l2[0]==l1[1]/l2[1]==l1[2]/l2[2] and l1[-1]==l2[-1]=='=' and l1[-4]==l2[-4] and l1[-3]==l2[-3]:
        print("The pair of linear equations have infinitely many solutions")

    elif l1[0]/l2[0]==l1[1]/l2[1]!=l1[2]/l2[2] and l1[-1]==l2[-1]=='=' and l1[-4]==l2[-4] and l1[-3]==l2[-3]:
        print("The pair of linear equations have no solutions")

    else:
        print("You have some mistake in your equations")
        print("Please check it again")

else:
    print("You have some mistake in your equations")
    print("Please check it again")

