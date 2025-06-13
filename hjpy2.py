import threading
import time
import tkinter as tk
import numpy as np
root = tk.Tk()
root.title("wsTel hj")
enHj = tk.Text(root,width=400)
#root.geometry('600x600')
def getData():
    global text_contentall 
    global str_arr
    global str_arr2
    #获取text全部内容并去除内容中的空格,用split将内容以每一行末尾的\n分割成一个列表     
   # text_content = (enHj.get("0.0","end").replace(" ","")).split("\n")
    #text_content.pop()#列表最后一个元素是空删除它
    text_contentall=(enHj.get("0.0","end").replace(" ","")).split("\n")
   
    text_contentall[0].split('\t')[0]
    str_arr =np.array([str(element) for element in text_contentall])
   
    str_arr2='\n'.join(str_arr)
    
   # enHj.insert('1.0', 'Hello')
   # enHj.insert('insert','world')
   # text_contentALL = ['县市\t收入', 'a\t1', 'b\t2', 'c\t3', 'd\t4', 'e\t5', 'f\t6', 'g\t7', '']
       
    #print(text_contentall.__len__())
    
    enHj.delete("0.0", "end") 
        

def compDate():
    print("开始执行确认行")
    #获取text全部内容并去除内容中的空格,用split将内容以每一行末尾的\n分割成一个列表     
   # text_content = (enHj.get("0.0","end").replace(" ","")).split("\n")
    #text_content.pop()#列表最后一个元素是空删除它
    global str_arr3
    global str_arr4
    global str_arr5
    str_arr4 = [] 
    str_arr41 = [] 
    str_arr3np=(enHj.get("0.0","end").replace(" ","")).split("\n")
    str_arr3=np.array(str_arr3np)
    
    print()
    #for element in str_arr3:
    for element2 in str_arr:       
        str_arr4.append(element2.split('\t')[0])
        #time.sleep(0.00001)
        #root.update()
    str_c = np.intersect1d(str_arr3,str_arr4)
    print(str_c) 
    print(len(str_c))       
    str_arr5='\n'.join(str_arr41)
    #print(text_contentall[0])    
    #for text_conten in str_arr2:
    enHj.delete("0.0", "end") 
    #enHj.insert('0.0',str_arr2)
    enHj.insert('0.0',str_arr5)
     

   # enHj.insert('1.0', 'Hello')
   # enHj.insert('insert','world')
   # text_contentALL = ['县市\t收入', 'a\t1', 'b\t2', 'c\t3', 'd\t4', 'e\t5', 'f\t6', 'g\t7', '']
      
  
#enHj.insert('1.0', 'Hello\n')

button1=tk.Button(root,padx=40,text="导入",command=getData)
button2=tk.Button(root,text="开始对比",command=compDate)
enHj.pack(padx=0, pady=0) 
button1.pack(side="left",padx=200, pady=100) 
button2.pack(padx=50, pady=150) 
root.mainloop() 


