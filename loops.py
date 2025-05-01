# DEFINATION : python loops help us for itteractions.ittrable obejects---->elements


# The for loop loops through a block of code a specified number of times.

# The for loop is the only loop available in Go.

# example:
    
# a = "this is"
# for i in a:  
#    print(i)

# output:t
#        h
#        i
#        s 
#        i
#        s


# zx = "this is a car"
# for i in zx:
#   print(i)

# output:

# t
# h
# i
# s
 
# i
# s
 
# a
 
# c
# a
# r

# range()---->help to genrate a serious of number from a point to another point.
#           (start,end,increment)
#           start:0
#           end:n-1
#           increment:1

# example:
# for i in range(1,11,1):
#   print(i)
  
# output:
  
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# example:
# for i in range(6):
#   print(i)
  
# output:
#     0
# 1
# 2
# 3
# 4
# 5

# for i in range(1,11):
#   print("2x",i,"=",2*i)
  

# output:
# 2x 1 = 2
# 2x 2 = 4
# 2x 3 = 6
# 2x 4 = 8
# 2x 5 = 10
# 2x 6 = 12
# 2x 7 = 14
# 2x 8 = 16
# 2x 9 = 18
# 2x 10 = 20



                          # The continue Statement

# The continue statement is used to skip one or more iterations in the loop. It then continues with the next iteration in the loop.

# for i in range(1,11):
#    if i == 8:
#      continue
#    print(i)
   
   
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 9
# 10

# for i in range(1,111):
#   if i==50:
#     continue
#   print(i)
                          
                          
                          
                          # break statement

# The break statement is used to break/terminate the loop execution.

# for i in range(1,11):
#   if i==5:
#     break
#   print(i)
  
# output:
# 1
# 2
# 3
# 4
  
