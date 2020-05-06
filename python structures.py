#assigning elements to lists
mylist1= [1,2,"one",0.5]
mylist2=["one","two","three"]
mylist1.append("hi")#.append() function adds the new element at the end of list
                    # it takes exactly one argument at a time.
print(mylist1)
mylist2[2]="THREE"#in this the element "THREE" is assigned to the element with
                  # index number 2 that is mentioned in the square brackets.
                  #indexing starts with number "0"
print(mylist2)



#accessing elements from tuple
Tuple1=("one", "two", "three")
print(Tuple1)# prints all the elements of tuple
print(len(Tuple1))# prints the number of elements the tuple
print(Tuple1[2])# prints the element of tuple with index number "2"
print(Tuple1[0])# prints the element of tuple with index number "0"




#Deleting different dictionary elements
Dict1={"1":"very unfavourable","2":"unfavourable","3":"neither/nor","4":"favourable","5":"very favourable"}
print(Dict1)
Dict1.pop("3")#indexing in dictionary is done with a "key element"
              # .pop() function is used to delete paticular pair with key element "3"
