#import
import random

def addres(k,l): #Putting bombs in user-entered locations
    for i in range(0,k):
        n=int(input("Enter the row of the table:"))
        m=int(input("Enter the table column:"))
        l[n][m]='*'
    return l

def rand(n,m,l): #Put the number at random in the spaces in the table
    for i in range(0,n):
        for j in range(0,m):
            if l[i][j]==0:
                l[i][j]=random.randint(1,9) #Random number from 1 to 9
    return l

def printt(l): #Show table
    for i in l:
        for j in i:
            print (j,end=" ")
        print()

def main():
    n=int(input("Enter the row of the table:"))
    m=int(input("Enter the table column:"))
    l = [[0 for i in range(m)]for j in range(n)] #List with element zero at n * m
    k=int(input("Enter the number of bombs:"))
    l=addres(k,l)
    l=rand(n,m,l)
    printt (l)

main()
