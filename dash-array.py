from tkinter import * 
import random

import numpy as np

root = Tk()
step2 = []
i = 1

enter = False
randomize1 = False
makeIt=False


def getValue(finalresult,enter):
   
 
 while enter == True: 
   step2.append(finalresult)
   if enter == True:
    content = str(step2)
    with open('plan.txt', 'w') as f:
      f.write(content)
      break
       
      
def rando(randomize1,content):
   
 if (randomize1== True):  
    with open('plan.txt', 'w') as f:
      
     f.write("Array: "+ content)
     f.write("Random: ")
     f.write((step2[random.randint(0,len(step2)-1)]))
 
def clear(makeIt):
 if (makeIt== True):
   step2.clear()
   with open("plan.txt", 'r+') as f:
    f.truncate(0)

   
  
  


      




def gui():
 root.geometry("960x540")   
b = Button(root, text = "Upload",command= lambda: getValue(finalresult=E1.get(), enter = True))


b.grid(row=0,column=0)

b1 = Button(root, text = "Randomize",command= lambda:rando(randomize1 =  True,content=str(step2)))

b1.grid(row=5,column=0)

b2 = Button(root, text = "Clear",command= lambda:clear(makeIt=True))

b2.grid(row=7,column=0)
    



E1 = Entry(bd =5)
E1.grid(row=0, column=5)
  

root.mainloop()  

   
