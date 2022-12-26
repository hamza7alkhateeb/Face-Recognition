from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.by import By
import time
import pyrebase
start=time.time()
import  numpy as np
class x :
  def __init__(self):
    self.y=[]
    self.loop()


  def loop(self):
    for i in range(5):

      self.y.append(i)
  def print(self):
    print(self.y)


#main
xv=x()
xv.print()
end=time.time()
print("time taken using class",end-start)

list1=[]
start1= time.time()
for i in range (10):
  list1.append(i)
print(list1)
end1=time.time()
print("time taken without class ", end1-start1)


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


