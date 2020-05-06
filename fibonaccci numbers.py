#taking the input from user
N = int(input("how many fibonacci numbers do you want to print"))
#declaring variables
n1,n2 = 0,1
#condition statements
if N<=0:
    print("please enter positive integer greater than zero")
elif N ==1:
    print("The fibonaaci numbers upto", N, "terms are: \n", n1)
else:
    print("The fibonaaci numbers upto", N, "terms are:")
    count=0
    while count<N:
        print(n1)
        #update variable values
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
        
