#! /usr/bin/env python
import rospy
from time import sleep
n= 1
while n<11:
   if n==10:
      sleep(1)
      print("time is up! ! ! !  ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
      n+=1
   elif n<10:
       sleep(1)
       print(n)
       n+=1








rospy.init_node("string_python_node")
print("account:iclab_xiao_ming")
x=raw_input("password:")
if x=="aa":
   print("welcome!user iclab_xiao_ming")
else:
   print("account or password error,please again")

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
