# let's Play a number guessing game : 
import random 

# there we will make the choices hints,  or not hints :
def guess():
    n= 0 
    m= int(input('enter your level , to 0-6 , 0-10 , 0=20 '))
    if m == 6 :
        print('prettry basic  ')
        a= random.randint(n,m)
        point=  []
        s=int(input('enter your guess : '))
        if s==a :
            point('you win : ')
            print(point.append(10))
            
            
        
        else:
            print('not matched try another time : ')
        
    elif m== 10 :
        print('intermidiate level : ')
        a=  random.randint(n, m )
        point=  []
        s=int(input('enter your guess : '))
        if s==a :
            print('win ')
            print(point.append(10))
            
        else:
            print('not matched try another time : ')
        
    elif m==20 :
        print('oh, you chose the hard core  level : ')
        a=  random.randint(n,m )
        point=  []
        s=int(input('enter your guess : '))
        if s==a :
            print('win ')
            print(point.append(10))
                
        else:
            print('not matched try another time : ')
    else:
        print('invalid input  ')

def guess_with_hints(): 
    n= 0 
        
    m= int(input('enter your level , to 0-6 , 0-10 , 0=20 '))
    if m == 6 :
        print('prettry basic  ')
        r=[ 2, 4, 6]
        print('hints : 1. even number ')
        a=  random.choice(r)
        
        
        point=  []
        s=int(input('enter your guess : '))
        if s==a :
            print(point.append(10))
                    
        else:
            print('not matched try another time : ')
        
    elif m== 10 :
        print('intermidiate level : ')
        
        r=[ 3,9 ]
        print('hints : 1.odd number ,  2. divided by 3 ')
        a=  random.choice(r)
        
        point=  []
        s=int(input('enter your guess : '))
        if s==a :
            print(point.append(10))
            
        else:
            print('not matched try another time : ')
        
    elif m==20 :
        print('oh, you chose the hard core  level : ')
        r=[ 12, 13, 16 , 10 , 18 , 5 ]
        print('hints : 1. even number   and odd number ')
        a=  random.choice(r)
        
        point=  []
        s=int(input('enter your guess : '))
        if s==a :
            print(point.append(10))

        else:
            print('not matched try another time : ')
    else:
        print('invalid input  ')
print('-=-- hi this is number guessing game ,')
print('would you like to get hints or not : ')
res= str(input('enter your response ; if yes press y or yes or no press n or no '))

if res==  'y' or res==  'yes':
    
    print(guess())
else:
    
    print(guess_with_hints())
    
    
    
    