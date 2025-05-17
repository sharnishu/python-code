numpy stand for numerical python
it is creaeted in 2005 by travis oliphant
numpy is a python liabrary used for working with array



why is numpy faster than lists?

numpy array are store homoginus data(same type of data),but list is store differant type of data.


which language use in numpy-----> 
numpy----->numerical python
numpy ka 70% code sabse powerfull language se likha gya hai----->c language

30%---->pyhton
 speed or simplysity ki wajah se esko use kiya jata hai
array store homogenius data likee----> same type of data
numpy homogenious data store krta hai-----> ekk time pe
 but list es se slow hoti hai beacaus wo different type of data store krti hai like---
int,str,bollen,floate

numpy ek liabrary hai --->eske uor he pandas bna hai,sikcitlearn,matplotlib

resleas 2005 by
numpy bhott comlex hai ,yeah array ki help se bnaa hai,

ndarrys: when we create any object with the help of array method in numpy

import numpy as np

arr = np.array(10)

arr--->ndarray

# then cheak the type

type(arr)


array demensional
0d----->one element only
 1d------>one row and multiple column
 2d------> multiple row and multiple column
 3d------>3xs
 4d
 .
 .
 .

ndim----->n-deminsional

arr.ndim

x = np.array([12,23,34,44,34,44])

create numpy arry
# firstly provide only list

import numpy as np
 a = np.array([1,2,3,4])
 type(a)
 
 2d and 3d  --------> integer value only   like matrix
 
  b = np.array([[1,2,3,4],[5,6,7,8]])
c = np.array ([[[1,2],[3,4]],[[4,6],[7,8]]])
type(c)

# dtype---------->when create a arry in flote data typew
# bool -------------> non zero values is turee,complex

 a = np.array([1,0,3],dtype=int)
a = np.array([1,0,3],dtype=bool)

 # np.arange()---------->jub ek numpy chahiyee ho jo 1 to 10 tk ho--->jun 1 se 10 tk koi array bnana ho to range pass krty hai
 np.arange(1,11)
 # pass altanate numbers
 with reshape() function---------->ek given numpy array ko dusri shape mai convert krna

# two d array
 np.arange(1,11).reshape(5,2)
 np.arange(1,11).reshape(2,5)
 # np.ones() and np.zeros()---------> use for values initalize
 np.ones((3,4))
 np.zeros((3,4))
 np.random.random((3,4))
 
 
  # np.linspace --------->give stating point and last point and the distance between first range and second are same

 np.linspace(-10,10,10)
 np.linspace(-10,10,10,dtype=int)
 # np.identity--------->use in ml for make a graphs,,in whicg digonal point are 1 other is 0
 np.identity(5)
 # array attributes
 a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

  # 1.ndim------->number of deminsional
# how many dimension in array---->use ndim
  a2.ndim
  # shape---->how many items in array like row,column
  a1.shape
  a3.shape
  a3
  a2.size
  a3.size


  # dtype
  print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

 # chnaging datatype
  # astype
  a3.astype(np.int32)

  indexing/slicing

two type of indexing
1.positive indexing
2.negative indexing

  
  a1
  a1[-1]
  a1[5]

  array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])------->1d

  a2
  a2.dtype
  a2[1,2]
  a2[2,3]
  a2[1,1]


  a3
  array([[[0, 1],
        [2, 3]],

       [[4, 5],
        [6, 7]]])
  
  a3[1,1,0]---->6
  a3[0,1,0]---->2
  a3[0,0,0]------>0

  # slicing-------> use for  ectract multiple values
  a1
  a1[2:5]
  a1[2:5:2]

  # 2d slicing

  array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])
  a2
  a2[0,:] -----------> first row
  a2[:,2]---------->2,6,10
  a2[1,:]----------->4,5,6,7
  a2
  a2[1:,1:3]------>5,6
      -----------  >9,10














 




