from tkinter import
class Scrapper:
    def __init__(sf, screen);
        sf.scr = screen
        
        # import from os
        # scr.main
        # protocol and body
        
        scr.title("scrapper")
        sf.img = PhotoImage(file='C:/Users/ankit/Desktop/z.png')
        f=Frame(scr,bg="green",width=2000,height=300)
        label = Label(f,image=sf.img)
        label.place(x=600,y=50)
        e=Entry(f,font=("times",20,"italic"),bg="white",width=42)
        e.place(x=300,y=260)
        b=Button(f,bd=3,relief=RIDGE,text="SEARCH",state="active",command=lambda :sf.Engine(e.get()))
        b.place(x=800,y=265)
        f.grid(row=0,column=0)
        f1=Frame(scr,bg="white",width=2000,height=6000)
        c1=Canvas(f1,width=2000,height=5000)
        f1.scrollbar = Scrollbar(f1)
        f1.scrollbar.pack(side=RIGHT, fill=Y)
        c1.pack(side=RIGHT,expand=True,fill="both")
        sf.txt = Label(f1)
        sf.txt.config(font=("times",20,"bold"))
        c1.create_window(0,0,anchor="nw",window=sf.txt)
        f1.grid(row=1,column=0)
        
        # main loop
       
       
    def Engine(sf,a):
        sf.a=a*
        import requests
        import bs4
        import sqlite3 as sl
        import time
        try:
           con=sl.connect("e:/amaz.db")
           cur=con.cursor() 
           cur.execute("create table Amazon(Date varchar(100),Product name varchar(100),Price varchar(50),Discount varchar(50),Prime varchar(10),Ratings varchar(20))")
        except:
            pass
        headers={"User-Agent":"Mozilla/5.0 (x11;Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
        dt=requests.request("get","https://www.amazon.in/s/field-keywords=%s"%(a),headers=headers)
        s=bs4.BeautifulSoup(dt.text,"html.parser")
        var=''
        for doc in s.findAll("div",{'class':'s-item-container'}):
            list=['NULL\n','NULL\n','NULL\n','NULL\n','NULL\n']
            try:
               i=doc.find("h2")
               list[0]=i.text+'\n'
               j=doc.find('span',{"class":'a-size-base a-color-price s-price a-text-bold'})
               list[1]=j.contents[-1]+'\n'
               k=doc.find('span',{"class":'a-size-small a-color-secondary a-text-strike'})
               list[2]=k.contents[-1]+'\n'
               j=3
               for l in doc.findAll('span',{"class":'a-icon-alt'}):
                   list[j]=l.contents[-1]+'\n'
                   j=j+1
               for l in list:
                    var=var+l
               cur.execute("insert into Amazon values(time.ctime(),%s,%s,%s,%s,%s)"%(list[0],list[1],list[2],list[3],list[4]))
            except:
               pass
        sf.txt.config(text=var)
        
      # scr.mainloop()
        
                
scr = Tk()


