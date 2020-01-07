def get_func():#calling two-dimensional 
    Is=input("Enter the type of shapes to be separated by '#':").split("#")
    return Is

def post_function(Is):#Transmits shapes into its functions to compute area
    s=[]
    for i in range (len(Is)):

        if(Is[i]=='square'):
            s.append(square())

        elif(Is[i]=='circle'):
            s.append(circle())

        elif(Is[i]=='rectangle'):
            s.append(rectangle())

        elif(Is[i]=='triangle'):
            s.append(triangle())

    return s

def square():#square area
    x=int(input('Enter the square side:'))
    a=x**2
    return a

def circle():#area of circle
    from math import pi
    r=int(input('Enter the radius of the circle:'))
    a=pi*r**2
    return a

def rectangle():#rectangle area
    x=int(input('Enter the lenghth of the rectangle:'))
    y=int(input('Enter the width of the rectangle:'))
    a=x*y
    return a

def triangle():#triangle area
    x=int(input('Enter the rule of triangle:'))
    h=int(input('Enter the height of triangle:'))
    a=(x*h)/2
    return a

Is=get_func()
s=post_function(Is)
for i in range(len(s)): #Print area of ​​shape
    print('Area',Is[i],'is',s[i])
