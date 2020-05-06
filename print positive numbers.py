list1 = list(map(int, input("Enter a multiple integer values seperated by spaces ").split()))  
pos_nos = list(filter(lambda x: (x >= 0), list1)) 
  print("Positive numbers in the list: ", *pos_nos)
