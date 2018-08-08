#coding:utf-8
from Tkinter import *
from tkMessageBox import *
import tkFont
import os
import sys
import shutil
import time
from PIL import Image,ImageTk

def label(text='label',image=None):
    global root
    lab1=Label(root,text=text,image=image)
    lab1.grid(row=1,column=0,columnspan=20,rowspan=20)
    return lab1

def button(text='button',command=None,column=0,row=0,sticky=None):
    global root
    butt1=Button(root,text=text,bg='green',height=5,width=10,bd='3',command=command,font=ft)
    butt1.grid(row=row,column=column,sticky=sticky)
    return butt1

def previous():
    global now_num
    impath=os.path.join(path,jpg_dict[now_num])
    print os.path.basename(impath)
    im=ImageTk.PhotoImage(Image.open(impath).resize((1024,768)))
    lab1['image']=im
    lab1.image=im
    now_num-=1
    if now_num==-1:
        now_num=0
    return now_num

def next_one(dst):
    def child_next():
        global now_num
        print 'now',now_num
        impath=os.path.join(path,jpg_dict[now_num])
        im=ImageTk.PhotoImage(Image.open(impath).resize((1024,768)))
        lab1['image']=im
        lab1.image=im
        # lab1.update()
        shutil.move(impath,dst)
        now_num+=1
        if now_num == length:
            lab1['image']=''
            lab1.image=''
            lab1.update()
            showinfo('Message','All Done')
            sys.exit(0)
        impath=os.path.join(path,jpg_dict[now_num])
        im=ImageTk.PhotoImage(Image.open(impath).resize((1024,768)))
        lab1['image']=im
        lab1.image=im
        lab1.update()
    return child_next
def gen_dict(path,suffix):
    jpglist=[i for i in os.listdir(path) if i.endswith(suffix)]
    jpg_dict=dict(enumerate(jpglist))
    return jpg_dict

def callback(event):
    global now_num
    num=int(event.char)-1
    if num in range(len(fun_next_list)):
        fun_next_list[num]()




if __name__=='__main__':

    path='./jpg/'
    suffix=('.jpg')
    select_list=['高速-1','乡村-2','城市-3','一般-4','待定-5']

    root=Tk()
    root.geometry('1524x1268')
    for p in select_list:
        try:
            os.makedirs(os.path.join(path,p))
        except Exception as err:
            print err
            continue
    now_num=0
    jpg_dict=gen_dict(path,suffix)
    length=len(jpg_dict)
    im1path=os.path.join(path,jpg_dict[0])
    im1=ImageTk.PhotoImage(Image.open(im1path).resize((1000,768)))
    lab1=label(text=None,image=im1)
    ft = tkFont.Font(family='Arial', size=10, weight='bold')
    #button0=button(text='previous',command=previous,row=0,column=0,sticky=W)
    #button1=button(text='next',command=next_one,row=0,column=19,sticky=E)
    column=2
    fun_next_list=[]
    for d in select_list:
        dst=os.path.join(path,d)
        fun_next_list.append(next_one(dst=dst))
        Button(text='%s'%(d),bd=3,bg='orange',font=ft,height=1,width=10,command=next_one(dst)).grid(row=0,column=column)
        column+=1
    root.bind('<KeyPress>',callback)
    root.focus_set()

    root.mainloop()
