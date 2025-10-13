import time
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

log=logging.getLogger(__name__)

l=[1,2,3,4,5,6,7,8,9,10]
multiplaypor=115
newlist=[]
for i in range(0,multiplaypor):
 copyl=l.copy()
 newlist.extend(copyl)
# start=time.time()

# largsetvalue=newlist[0]
# indexlargsetvalue=0

# studentslist=[ 
# [87, 10001, "Fred"],
# [28, 10002, "Tom"],
# [100, 10003, "Alistair"],
# [78, 10004, "Sasha"],
# [84, 10005, "Erin"],
# [98, 10006, "Belinda"],
# [75, 10007, "Leslie"],
# [70, 10008, "Candy"],
# [81, 10009, "Aretha"],
# [68, 10010, "Veronica"]
# ]


# def sortstudents(studentslist,index=0):
#  logger=logging.getLogger(__name__)

#  for i in range(0,len(studentslist)):
#   for j in range(i,len(studentslist)):
#    if  studentslist[i][index]>studentslist[j][index]:
#     tem=studentslist[i]
#     studentslist[i]=studentslist[j]
#     studentslist[j]=tem


#  logger.info(studentslist)





# start=time.time()

# mostrepitedvalue={'indexvalue':0,'numberoftime':0}

# for i in range(0,len(newlist)):
#  number=1
#  print(time.time()-start)
#  for j in range(i+1,len(newlist)):
#   if newlist[i]==newlist[j]:
#    number+=1
#  if number>mostrepitedvalue.get('numberoftime'):
#   mostrepitedvalue['numberoftime']=number
#   mostrepitedvalue['indexvalue']=j

# print(newlist[mostrepitedvalue.get('indexvalue')],mostrepitedvalue.get('numberoftime'))

# mostfrequent=0
# highestfrequency=0
# currentfrequency=0
# for i in range(0,len(newlist)):
#  currentfrequency+=1
#  if highestfrequency<currentfrequency:
#   highestfrequency=currentfrequency
#   mostfrequent=newlist[i]

 
#   currentfrequency+=1




def getlogging(func,basicconfig={}):
 import logging

 logger=logging.getLogger(__name__) 
 logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
 def wrapper(*args,**kwargs):
#   if func.__name__ in ['find_mode']:


  result=func(*args,**kwargs)
  return result
 return wrapper

def gettime(func):
 import time
 logger=logging.getLogger(__name__)
 def wrapper(*args,**kwargs):
  
  start=time.time()
  result= func(*args,**kwargs)
  now=time.time()
  logger.info(now-start)
  return result
 return wrapper



# @getlogging
# @gettime
# def sortlist(newlist):
#  logger=logging.getLogger(__name__)
#  for i in range(0,len(newlist)): 
#   for j in range(0,len(newlist)):
#    if newlist[i]<newlist[j]:
#     tem=newlist[j]
#     newlist[j]=newlist[i]
#     newlist[i]=tem
# #  logger.info(__file__)
#  return newlist
# newlist=sortlist(newlist)

# @getlogging
# @gettime
# def find_mode(newlist,logger):
#  most_frequent=None
#  highestfrequent=0
#  currentfrequent=0
#  newlist=sortlist(newlist)
#  for i in range(0,len(newlist)):
#   currentfrequent+=1
#   if i<len(newlist)-1 and  newlist[i]!=newlist[i+1]:
#    if currentfrequent >highestfrequent:
#      highestfrequent=currentfrequent
#      most_frequent=newlist[i]
#    currentfrequent=0
#  return {"mostfrequent":most_frequent,"mode":highestfrequent}


# mode=find_mode(newlist)
# print(mode)
# @gettime
# def find_mode2(newlist):
#  logger=logging.getLogger(__name__)
#  l=[0 for x in range(0,len(newlist))]
#  for i,x in enumerate(newlist):
#   l[newlist[i]-1]+=1
#  logger.info(l)


# find_mode2(newlist)


# sortstudents(studentslist,1)


# sales = [
# [1856, 498, 30924, 87478, 328, 2653, 387, 3754, 387587, 2873, 276, 32],

# [23, 55, 67, 99, 265, 376, 232, 223, 4546, 564, 4544, 3434],
# [5865, 5456, 3983, 6464, 9957, 4785, 3875, 3838, 4959, 1122, 7766, 2534]
# ]
# @getlogging
# def sorte_Sales_base_on_averageSales (sales):
#  logger=logging.getLogger(__name__)
#  highestaverage=None
#  for i in range(0,len(sales)):
#   averagesum=0
#   for j in range(0,len(sales[i])):
#    averagesum+=sales[i][j]
#   averagesum=(averagesum+0.5)/len(sales[i]) 
#   if highestaverage:
#    if highestaverage> averagesum:
#      sales[i],sales[i-1]=sales[i-1],sales[i]
#   else:
#    highestaverage=averagesum
#  return sales  



# # @getlogging
# def gethighestmediansales(sales):
#  log=logging.getLogger(__name__)
#  log.info(sales)
#  sortedsales=sorte_Sales_base_on_averageSales(sales)
#  log.info(sortedsales)
#  highestmedian=None
#  for i in range(0,len(sortedsales)):
#   length=len(sortedsales[i])
#   currentmedian=0
#   if length % 2 == 0 and length > 0:
#     Start=length//2-1
#     end=length//2+1
#     l=sortedsales[i][Start:end]
#     log.info(length)
#     currentmedian=(l[0]+l[1])/2
#   else:
#    currentmedian=sortedsales[length//2]  
#   log.info('currentmedian is {0}'.format(currentmedian))

#   if highestmedian:
#      if highestmedian<currentmedian:
#       highestmedian=currentmedian
#   else:
#      highestmedian=currentmedian
#   # log.info('highestmedian is {0}'.format(highestmedian))
#  return highestmedian
# gethighestmediansales(sales)
    






# class value:
#  def __init__(self,value):
#   self.value=value
 



#  def __add__(self,secondvalue):
#   return self.value+secondvalue
 
#  def __sub__(self,secondnew):
#   return self.value-secondnew
#  def __radd__(self,second):
#   return self.value+second


# s=value(10)
# # log.info(10+s+10)
# c=[100,200,1002,200,201]
# k=iter(c)
# # c[0]=200

# # log.info(next(k))
# # c[0]=200

# # log.info(next(k))
# # log.info(next(k))
# # log.info(next(k))
# # log.info(next(k))
# # # log.info(next(k))



# # def generator(list):
# #  for k in list:
# #   if k>100:
# #    yield k-20
# #   yield k
# # result=generator(c)

# # log.info(next(result))
# # log.info(next(result))
# # log.info(next(result))



# class Range:
#  def __init__(self,start,stop=None,step=1):

#   if step==0:
#    raise ValueError('step cannot be 0')
  

#   if stop is None:
#    start,stop=0,start



#   self._length=max(0,(stop-start+step-1)//step)
#   # log.info('length is {0}'.format(self._length))


#   self._start=start
#   self._step=step

#  def __len__(self):
#   return self._length
 

#  def __getitem__(self,k):
#   if k<0:
#     k+=len(k)

#   if not 0 <= k < self._length:
#      raise IndexError('index out of range')
#   return self._start+k*self._step 







# def draw_line(tick_length,tick_label=''):
#  line='-'*tick_length
# #  log.info(tick_label) 
# #  if tick_label:
#  line+=' '+tick_label
#  log.info(line)



# def draw_interval(center_length):
#  if center_length>0:
#   draw_interval(center_length-1)
#   draw_line(center_length)
#   draw_interval(center_length-1)


# def draw_ruler(num_inches,major_length):
#  draw_line(major_length,'0')
#  for i in range(1,1+num_inches):
#   draw_interval(major_length-1)
#   draw_line(major_length,str(i))



# draw_ruler(5,4)



# def binary_search(data,target,low,high):
#  assert type(low)==int
#  assert type(high)==int
#  assert type(data)==list 
#  assert type(target)==int
#  mid=(low+high)//2
 
#  log.info((low,high,mid))
#  if low>high:
#   return -1
#  else:
#   if target==data[mid]:
#    return mid
#   elif target<data[mid]:
#    return binary_search(data,target,low,mid-1)
#   else:
#    return binary_search(data,target,mid+1,high)
  

# l=[1,2,3,4,5,10,20,3,30,40,0]

# log.info(binary_search(l,10,0,len(l)))



# import os
 
# def disk_usage(path):
#  total=os.path.getsize(path)
#  if os.path.isdir(path):
#   for filename in os.listdir(path):
#    childpath=os.path.join(path,filename)
#    total+=disk_usage(childpath)
#  log.info('{0} -path --> {1}'.format(total,path))
#  return total


# # log.info(disk_usage('/Users/ahmed/myPythonProject/gameDominos-v2'))


# def bad_fibonacci(n):
#  if n<=1:
#   log.info(n)
#   return n
#  else:
#   return bad_fibonacci(n-2)+bad_fibonacci(n-1)
 

# # log.info(bad_fibonacci(5))


# def good_fibonacci(n):
#  if n<=1:
#   return (n,0)
#  else:
#   (a,b)=good_fibonacci(n-1)
#   return (a+b,a)
 


# log.info(good_fibonacci(5))



# def binary_sum(l,start,stop):
#  if start>=stop:
#   return 0
#  elif start==stop-1:
#   return l[start]
#  else:
#   mid=(start+stop)//2
#   return binary_sum(l,start,mid)+binary_sum(l,mid,stop)
# l=[5,20,20,102,23]
# log.info(binary_sum(l,2,len(l)))



class Empty(Exception):
 pass



# class ArrayStack:
#  def __init__(self):
#   self.__data=[]
#  def __len__(self):
#   return len(self.__data)
#  def is_empty(self):
#   return len(self.__data)==0
#  def push(self,v):
#   self.__data.append(v)
#  def top(self):
#   if self.is_empty():
#    raise Empty('stack is empty')
#   return self.__data[-1]
#  def pop(self):
#   if self.is_empty():
#    raise Empty('stack is empty')
#   return self.__data.pop()
#  def __str__(self):
#   return str(self.__data)
# arraystack=ArrayStack()
# arraystack.push(1)
# arraystack.push(2)
# arraystack.push(3)

# # log.info(arraystack.__data)
# @gettime
# def reversitemslist(unreversedlist):
#  reversedlist=[]
#  arraystack=ArrayStack()
#  for i in unreversedlist:
#   arraystack.push(i)
 
#  while not arraystack.is_empty():
#   try:
#    item=arraystack.pop()
#    reversedlist.append(item)
#   except Exception as e:
#    log.exception(e)
#  return reversedlist 

# # def reverse_file(filename):
# #  s=ArrayStack()
# #  original=open(filename)
# #  for line in original:
# #   s.push(line.rstrip('\n'))
# #  original.close()
# #  log.info(s)
# #  output=open(filename,'w+')
# #  log.info(s.is_empty())
# #  while not s.is_empty():
 
# #   output.write(s.pop()+'\n')
# #  output.close()

# # reverse_file('/Users/ahmed/myPythonProject/gameDominos-v2/find')












# class ArrayQueue:
#  DEFAULT_CAPACITY=10
#  def __init__(self):
#   self.__data=[None]*ArrayQueue.DEFAULT_CAPACITY
#   self.__size=0
#   self.__front=0

#  def __len__(self):
#   return self.__size
 



#  def is_empty(self):
#   return self.__size==0
 
#  def first(self):
#   if self.is_empty():
#    raise Empty('Queue is Empty')
#   return self.__data[self.__front]
 
#  def dequeue(self):
#   if self.is_empty():
#    raise Empty('Queue is Empty')
#   answer=self.__data[self.__front]
#   self.__data[self.__front]=None
#   self.__front=(self.__front+1)%self.__size
#   self.__size-=1
#   return answer
 
 
#  def enqueue(self,item):
#   if self.__size==len(self.__data):
#    self.resize(2*len(self.__data))

#   avail=(self.__front+self.__size)%len(self.__data)
#   self.__data[avail]=item
#   self.__size+=1


#  def __resize(self,cap):
#   old=self.__data

#   self.__data=[None]*cap

#   walk=self.__front
#   for k in range(self.__size):
#    self.__data[k]=old[walk]
#    walk=(1+walk)%len(old)
#   self.__front=0


# import collections
# import array
# import ctypes
# class DynamicArray:
#  def __init__(self,val=None):
#   self.__n=0
#   self.__capacity=14
#   self.__A=self.__make_array(self.__capacity)
#   self.__value=val
#  def __len__(self):
#   return self.__n

#  def __getitem__(self,k):
#   if not 0<= k <self.__n:
#    raise IndexError('invalid index')
#   return self.__A[k]
 

#  def __setitem__(self,key,value):

#   self.__A[key]=value
 
#  def append(self,obj):

#   if self.__n == self.__capacity:
#     self.__resize(2*self.__capacity)
  
#   self.__A[self.__n]=obj
#   self.__n+=1

#  def __resize(self,c):

#   B=self.__make_array(c)
#   for k in range(self.__n):
  
#    B[k]=self.__A[k]
#   self.__A=B
#   self.__capacity=c


#  def __make_array(self,c):
#   return (c*ctypes.py_object)()
 
#  def __str__(self):
  
#   return str( [self.__A[i] for i in range(self.__n)])

#  def __mul__(self,num):
#   if not isinstance(num ,int):
#    raise TypeError('Can only multiplay by integers')
  
#   if num<=0:
#    return DynamicArray()
  

#   result=DynamicArray()
#   result.__resize(2*num)

#   for i in range(num):
#    result.append(self.__value)
   

#   return result


# class Queue:
#  DEFAULT__CAPACITY=10
#  def __init__(self):
#   self.__data =DynamicArray()*Queue.DEFAULT__CAPACITY
#   log.debug(self.__data)
#   self.__front=0
#   self.__size=0


#  def first(self):
#   if self.is_empty():
#    raise Empty('Queue is empty')
#   return  self.__data[self.__front]
 
#  def dequeue(self):
#   if self.is_empty():
#    raise Empty('Queue is empty')
#   answer=self.__data[self.__front]
#   self.__data[self.__front]=None
#   self.__front=(self.__front+1)%len(self.__data)
#   self.__size-=1
#   return answer
  
 
#  def enqueue(self,obj):
#   avail=(self.__front+self.__size)%len(self.__data)
#   self.__data[avail]=obj
#   self.__size+=1

#  def __len__(self):
#   return self.__size
 
#  def is_empty(self):
#   return self.__size==0
 
#  def __str__(self):
#   return str([self.__data[i] for i in range(self.__size)])


# # queue=Queue()


# queue.enqueue(10)
# queue.enqueue(11)
# queue.enqueue(12)
# queue.enqueue(12)
# queue.enqueue(12)
# queue.enqueue(12)
# queue.enqueue(12)

# log.info(queue)
# log.info(queue.dequeue())
# log.info(queue.dequeue())
# log.info(queue.dequeue())
# log.info(queue.dequeue())



# class Deque:
#  DEFAULT_CAPACITY=10
#  def __init__(self):
#   self.__data=DynamicArray()*Deque.DEFAULT_CAPACITY
#   self.__size=0
#   self.__rear=0
#   self.__front=0

#  def __len__(self):
#   return self.__size
 
#  def first(self):
#   if self.is_empty():
#    raise Empty('Deque is Empty')
#   return  self.__data[self.__front]
 
#  def last(self):
#   if self.is_empty():
#    raise Empty('Deque is Empty')

#   return self.__data[self.__rear] 
 
#  def add_first(self,val):
#    avail=(self.__front-1)%len(self.__data)
#    self.__data[avail]=val
#    self.__front=avail

#    self.__size+=1
 


#  def add_last(self,val):
#   avail=(self.__rear+1)%len(self.__data)
#   self.__data[avail]=val
#   self.__rear=avail
#   self.__size+=1
 
#  def is_empty(self):
#   return self.__size==0

#  def delete_first(self):
#   if self.is_empty():
#    raise Empty('Deque is Empty')
#   answer=self.__data[self.__front]
#   self.__data[self.__front]=None

#   self.__front=(self.__front+1)%len(self.__data)
#   self.__size-=1
#   return answer
 
#  def delete_last(self):
#   if self.is_empty():
#    raise Empty('Deque is Empty')
  
#   answer=self.__data[self.__rear]
#   self.__data[self.__rear]=None
#   self.__rear=(self.__rear-1)%len(self.__data)
#   self.__size-=1
#   return answer   
 

#  def __str__(self):
#   return str([self.__data[i] for i in range(len(self.__data)) if self.__data[i] is not None])





# deque=Deque()

# deque.add_first(10)
# deque.add_first(20)
# deque.add_first(30)
# deque.add_last(20)
# deque.add_last(40)
# deque.add_last(50)

# # deque.add_first(30)

# log.debug(deque)


# log.info(deque.delete_first())
# log.info(deque.delete_first())
# log.info(deque.delete_first())
# # log.info(deque.delete_first())
# # log.info(deque.delete_first())
# # log.info(deque.delete_first())
# # log.info(deque.delete_first())


# log.debug(deque)









# class LinkedStack:
#  class __Node:
#   __slots__='_element','_next'

#   def __init__(self,element,nextelement):
#     self._element=element
#     self._next=nextelement
  
#  def __init__(self):
#   self._head=None
#   self._size=0 

#  def __len__(self):
#   return self._size
 
#  def is_empty(self,):
#   return self._size==0
 
#  def push(self,e):
#   self._head=self.__Node(e,self._head)
#   self._size+=1

#  def top(self):
  
#   if self.is_empty():
#    raise Empty('LinkedStack is Empty')
  
#   return self._head._element



#  def pop(self):
#   if self.is_empty():
#     raise Empty('LinkedStack is Empty')
#   answer=self._head._element
#   self._head=self._head._next
#   self._size-=1
#   return answer
 
#  def __str__(self):
#   l=[]
#   for i in self:
#    l.append(i)
#   return str(l)
 
#  def __iter__(self):
#   if not self.is_empty(): 
#    element=self._head
#   while  not self.is_empty() and element is not None:
#     yield element._element
#     element=element._next  


# linkedstack=LinkedStack()

# linkedstack.push(10)
# linkedstack.push(20)
# linkedstack.push(30)
# linkedstack.push(40)
# linkedstack.push(50)
# linkedstack.push(60)

# log.info(linkedstack)



# class LinkedQueue:
#  class _Node:
#   __slots__='_element','_next'

#   def __init__(self,element,next):
#     self._element=element
#     self._next=next
#  def __init__(self):
#   self.__head=None
#   self.__tail=None
#   self._size=0
 
#  def is_empty(self):
#   return self._size==0
 
#  def enqueue(self,v):
#   node=self._Node(v,None)

#   if self.is_empty():
#    self.__head=node

#   else:
#    self.__tail._next=node
#   self.__tail=node
#   self._size+=1
  
 
#  def dequeue(self):
#   if self.is_empty():
#    raise Empty('linkedQueue is Empty')
#   answer=self.__head._element
#   self.__head=self.__head._next
#   self._size-=1
#   if self.is_empty():
#   #  self.__tail=None
#    pass
# #   return answer
 
# #  def __len__(self):
# #   return self._size

# #  def first(self):
# #   if self.is_empty():
# #    raise Empty('LinkedQueue is Empty')
# #   return self.__head._element
 
# #  def __iter__(self):
# #   head=self.__head
# #   while not self.is_empty() and head is not None:
# #    yield head._element
# #    head=head._next
# #  def __str__(self):
# #   return str([i for i in self])


# # linkedQueue=LinkedQueue()
# # linkedQueue.enqueue(10)
# # linkedQueue.enqueue(20)
# # linkedQueue.enqueue(30)
# # linkedQueue.enqueue(40)

# # log.info(linkedQueue)

# # while not linkedQueue.is_empty():
# #   element=linkedQueue.dequeue()
  
# #   log.info(element)



# class CircularQueue:
#  class _Node:
#   __slots__='_element','_next'

#   def __init__(self,element,next):
#    self._element=element
#    self._next=next

#  def __init__(self):
#   self._tail=None
#   self._size=0

#  def __len__(self):
#   return self._size

#  def is_empty(self):
#   return self._size==0
 
#  def dequeue(self):
#   if self.is_empty():
#    raise Empty('Circular is Empty')
#   oldhead=self._tail._next
#   if self._size==1:
#    self._tail=None
#   else:
#    self._tail._next=oldhead._next
#   self._size-=1
#   return oldhead._element
 

#  def enqueue(self,e):
#   newnode=self._Node(e,None)
#   if self.is_empty():
#    newnode._next=newnode
#   else:
#    newnode._next=self._tail._next
#    self._tail._next=newnode
#   self._tail=newnode
#   self._size+=1

#  def first(self):
#   if self.is_empty():
#    raise Empty('Circular is Empty')
#   head=self._tail._next
#   return head._element
 
#  def rotate(self):
#   if self._size>0:
#    self._tail=self._tail._next
  
#  def __iter__(self):
#   current=self._tail._next
#   for i in range(self._size):
#    yield current._element
#    current=current._next

#  def __str__(self):
#   return str([i for i in self])
 

# circularQueue=CircularQueue()
 
# circularQueue.enqueue(10)
# circularQueue.enqueue(20)
# circularQueue.enqueue(30)
# circularQueue.enqueue(40)
# log.info(circularQueue)




# class _DoublyLinkedBase:
#  class _Node:
#   __slots__='_element','_prev','_next'

#   def __init__(self,element,nex,prev):
#    self._element=element
#    self._next=nex
#    self._prev=prev

#  def __init__(self):
#   self.header=self._Node(None,None,None)
#   self.trailer=self._Node(None,None,None)
#   self.header._next=self.trailer
#   self.trailer._prev=self.header
#   self._size=0

#  def __len__(self):
#   return self._size
 
#  def is_empty(self):
#   return self._size==0
 
#  def _insert_between(self,e,predecessor,successor):
#   newnode=self._Node(e,successor,predecessor)
#   successor._prev=newnode

#   predecessor._next=newnode
#   self._size+=1
#   return newnode
 
#  def _delete_node(self,node):
#    predecessor=node._prev
#    successor=node._next
#    predecessor._next=successor
#    successor._prev=predecessor
#    self._size-=1
#    element=node._element
#    node._prev=node._next=node._element=None
#    return element
   

class _DoublyLinkedBase:
 class _Node:
  __slots__='_element','_next','_prev'

  def __init__(self,element,next,prev):
   self._element=element
   self._next=next
   self._prev=prev

 def __init__(self):
  self.header=self._Node(None,None,None)
  self.trailer=self._Node(None,None,None)
  self.header._next=self.trailer
  self.trailer._prev=self.header
  self.size=0

 def is_empty(self):
  return self.size==0

 def _insert_between(self,e,predecessor,succesor):
  newnode=self._Node(e,succesor,predecessor)
  succesor._prev=newnode
  predecessor._next=newnode
  self.size+=1
  return newnode
 
 def _delete_node(self,node):
  predecessor=node._prev
  succesor=node._next
  predecessor._next=succesor
  succesor._prev=predecessor
  self.size-=1
  element=node._element
  node._prev=node._next=node._element=None
  return element








class LinkedDeque(_DoublyLinkedBase):
 
 def first(self):
  if self.is_empty():
   raise Empty('LinkedDeque is Empty')
  return self.header._next._element 

 def last(self):
  if self.is_empty():
   raise Empty('LinkedDeque is Empty')
  self.trailer._prev._element


 def insert_first(self,e):
  self._insert_between(e,self.header,self.header._next)

 def insert_last(self,e):
  self._insert_between(e,self.trailer._prev,self.trailer)

 def delete_first(self):
  if self.is_empty():
   raise Empty('LinkedDeque is Empty')
  self._delete_node(self.header._next)
 
 def delete_last(self):
  if self.is_empty():
   raise Empty('LinkedDeque is Empty')
  self._delete_node(self.trailer._prev)

 def __iter__(self):
  current=self.header._next
  while current._element is not None:
   yield current._element
   current=current._next
 def __str__(self):
  return str([i for i in self])
 
# linkedDeque=LinkedDeque()
# linkedDeque.insert_last(30)
# linkedDeque.insert_last(40)
# linkedDeque.insert_first(10)
# linkedDeque.insert_first(30)

# log.info(linkedDeque)



# class PositionalList(_DoublyLinkedBase):
#  class _Position:
#   __slots__='node','container'
#   def __init__(self,container,Node):
#    self.container=container
#    self.node=Node
  
#   def element(self):
#    return self.node._element
  
#   def __eq__(self, other):
#    return type(other) is type(self) and other.node is self.node
  
#   def __ne__(self, other):
#    return not (self==other)
 
 
#  def _validate(self,p):
#   if not isinstance(p,self._Position):
#    raise TypeError('P must be proper Position type')
  
#   if p.container is not self:
#    raise ValueError('P does not belong to this container')
  
#   if p.node._next is None:
#    raise ValueError('p is no longer valid')
#   return p.node
 
#  def _make_position(self,node):
#   if node is self.header or node is self.trailer:
#    return None
#   else:
#    return self._Position(self,node)
  
#  def first(self):
#   return self._make_position(self.header._next)
 
#  def last(self):
#   return self._make_position(self.trailer._prev)
 
#  def before (self,p):
#   node=self._validate(p)
#   return self._make_position(node._prev)

#  def after(self,p):
#   node=self._validate(p)
#   return self._make_position(node._next)
 
#  def __iter__(self):
#   cursor=self.first()
#   while cursor is not None:
#    yield cursor.element()
#    cursor=self.after(cursor)
#  def _insert_between(self, e, predecessor, successor):
#   node= super()._insert_between(e, predecessor, successor)
#   return self._make_position(node)
 
#  def add_first(self,e):
#   return self._insert_between(e,self.header,self.header._next)
 
#  def add_last(self,e):
#   return self._insert_between(e,self.trailer._prev,self.trailer)
 
#  def add_befor(self,p,e):
#   original=self._validate(p)
#   return self._insert_between(e,original._prev,original)

#  def add_after(self,p,e):
#   original=self._validate(p)
#   return self._insert_between(e,original,original._next)

#  def delete(self,p):
#   original=self._validate(p)
#   return self._delete_node(original)

#  def replace(self,p,e):
#   original=self._validate(p)
#   old_value=original.element()
#   original.element=e
#   return old_value

#  def __str__(self):
#   return str([i for i in self])


class PositionalList(_DoublyLinkedBase):
 class _Positional:
  def __init__(self,container,node):
    self.node=node
    self.container=container
  def __eq__(self, other):
   return type (other) is type(self) and other.node is self.node
  
  def __ne__(self, other):
   return not (self==other)
  
  def element(self):
   return self.node._element
  
 def first(self):
  return self._make_position(self.header._next)
 
 def last(self):
  return self._make_position(self.trailer._prev)

 def _make_position(self,node):
  if node is self.header or node is self.trailer:
   return None
  else:
   return self._Positional(self,node)
 
 def _validate(self,p):
  if not isinstance(p,self._Positional):
   raise TypeError('P must be proper Position type')
  if p.container is not self:
   raise ValueError('p does not belong to this container')
  if p.node._next is None:
   raise ValueError('p is no longer valid') 
  return p.node

 def befor (self,p):
  node=self._validate(p)
  return self._make_position(node._prev)
 
 def after(self,p):
  node =self._validate(p)
  return self._make_position(node._next)
 
 def _insert_between(self, e, predecessor, succesor):
  node= super()._insert_between(e, predecessor, succesor)
  return self._make_position(node)
 
 def delete(self,p):
  original=self._validate(p)
  return self._delete_node(original)
 
 def add_before(self,p,e): 
  original=self._validate(p)
  return self._insert_between(e,original._prev,original)
 
 def add_after(self,p,e):
  original=self._validate(p)
  return self._insert_between(e,original,original._next)
 
 def replace(self,p,e):
  origianl=self._validate(p)
  old_Value=origianl.element()
  origianl._element=e
  return old_Value
 
 def add_first(self,e):
  return self._insert_between(e,self.header,self.header._next)
 
 def add_last(self,e):
  return self._insert_between(e,self.trailer._prev,self.trailer)
 
 def __iter__(self):
  cursor=self.first()
  while cursor is not None:
   yield cursor.element()
   cursor=self.after(cursor)
 
 def __str__(self):
  return str([i for i in self])



positionallist=PositionalList()
positionallist.add_first(10)
positionallist.add_first(20)
positionallist.add_first(30)

