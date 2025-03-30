from tkinter import *   #importing tkinter library 
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw
import mysql.connector
from tkinter import messagebox
import datetime




class Lib_Mang:
    def __init__(self,root):
        self.root= root 
        self.root.title("Readobrite")
        self.root.geometry("1550x900+0+0")
    
#==========variables=========================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()




#==========label===================
        img1=Image.open(r"C:\Users\anujs\OneDrive\Desktop\harsh\bg.jpg")
        img1=img1.resize((1450,180))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=160)
        
        lbl_title=Label(self.root,text="READOBRITE",font=("times new roman",40,"bold"),bg="DeepSkyBlue4",fg="white",bd=8,relief=RIDGE)
        lbl_title.place(x=580,y=50,width=380,height=100)
        
#============logo ===================
#1
        img2=Image.open(r"C:\Users\anujs\OneDrive\Desktop\harsh\logo.jpg")
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
#2
        img3=Image.open(r"C:\Users\anujs\OneDrive\Desktop\harsh\logo.jpg")
        img3=img3.resize((230,140))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=1280,y=0,width=230,height=140)
        
#==========frame===================
        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="DeepSkyBlue4")
        frame.place(x=0,y=130,width=1530,height=400)
        
#==========Data-Frame==============
        DataFrameLeft=LabelFrame(frame,text="Library Info",bg="DeepSkyBlue4",fg="light grey",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMem_type=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Member Type:",font=("arial",12,"bold"),padx=2)
        lblMem_type.grid(row=0,column=0,sticky=W)
        txtMem_type=Entry(DataFrameLeft,textvariable=self.member_var,font=("arial",13,"bold"),width=29)
        txtMem_type.grid(row=0,column=1)

#1        
        lblPRN_No=Label(DataFrameLeft,bg="DeepSkyBlue4",text="PRN No",font=("arial",12,"bold"),padx=2)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)
#2       
        lblTitle=Label(DataFrameLeft,bg="DeepSkyBlue4",text="ID No.",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)
#3        
        lblFirstName=Label(DataFrameLeft,bg="DeepSkyBlue4",text="First Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)
#4
        lblLastName=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Last Name",font=("arial",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)
#5
        lblAddress1=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Address 1",font=("arial",12,"bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)
#6       
        lblAddress2=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Address 2",font=("arial",12,"bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)
#7       
        lblPostCode=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Post Code",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)
#8        
        lblMobile=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Mobile",font=("arial",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)
#9        
        lblBookId=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Book ID",font=("arial",12,"bold"),padx=2,pady=4)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)
#10        
        lblBookTitle=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Book Title",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)
#11        
        lblAuthor=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Author Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",13,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)
#12
        lblDateBorrowed=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Date Borrowed",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)
#13
        lblDateDue=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Date Due",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)
#14
        lblDaysOnBook=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Days on Book: ",font=("arial",12,"bold"),padx=2,pady=4)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)
#15
        lblLateReturnFine=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Late Return Fine",font=("arial",12,"bold"),padx=2,pady=4)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.lateratefine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)
#16
        lblDateOverdate=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Date Over Due",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,textvariable=self.dateoverdue,font=("arial",13,"bold"),width=29)
        txtDateOverdate.grid(row=7,column=3)
#17
        lblActualPrice=Label(DataFrameLeft,bg="DeepSkyBlue4",text="Actual Price: ",font=("arial",12,"bold"),padx=2,pady=4)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finallprice,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

#===========Data Frame Right===================================


        DataFrameRight=LabelFrame(frame,text="Book Details",bg="DeepSkyBlue4",fg="light grey",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

#==========scrollbar================================================   
        lisrScrollbar=Scrollbar(DataFrameRight)
        lisrScrollbar.grid(row=0,column=1,sticky=NS)


        listBooks=['Pride & Prejudice', '1984', 'Hamlet', 'One Hundred Years of Solitude',
                   'Anna Karenina', 'The Odyssey', 'The Stranger', 'Atomic Habits', 'Dune', 
                   'The Da Vinci Code', 'How to Win Friends and Influence People', 'War and Peace', 
                   'Jane Eyre', "Harry Potter and the Sorcerer’s Stone", 'The Fault in Our Stars', 
                   'The Hunger Games', 'Wings of Fire']
        
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if (x=="Wings of Fire"):
                self.bookid_var.set("BKID7879")
                self.booktitle_var.set("Wings of Fire")
                self.author_var.set("A.P.J. Abdul Kalam")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#2        
        
            elif (x=="1984"):
                self.bookid_var.set("BKID7889")
                self.booktitle_var.set("1984")
                self.author_var.set("George Orwell")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#3                
        
            elif (x=="Hamlet"):
                self.bookid_var.set("BKID7881")
                self.booktitle_var.set("Hamlet")
                self.author_var.set("William Shakespeare")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#4        
            elif (x=="Pride & Prejudice"):
                self.bookid_var.set("BKID7880")
                self.booktitle_var.set("Pride and Prejudice")
                self.author_var.set("Jane Austen")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#5      
            elif (x=="One Hundred Years of Solitude"):
                self.bookid_var.set("BKID8001")
                self.booktitle_var.set("One Hundred Years of Solitude")
                self.author_var.set("Gabriel García Márquez")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#6      
            elif (x=="Anna Karenina"):
                self.bookid_var.set("BKID8002")
                self.booktitle_var.set("Anna Karenina")
                self.author_var.set("Leo Tolstoy")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#7    
            elif (x=="The Odyssey"):
                self.bookid_var.set("BKID8003")
                self.booktitle_var.set("The Odyssey")
                self.author_var.set("Homer")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#8    
            elif (x=="The Stranger"):
                self.bookid_var.set("BKID8004")
                self.booktitle_var.set("The Stranger")
                self.author_var.set("Albert Camus")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
                
#9
            elif (x=="Atomic Habits"):
                self.bookid_var.set("BKID8005")
                self.booktitle_var.set("Atomic Habits")
                self.author_var.set("James Clear")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#10
            elif (x=="Dune"):
                self.bookid_var.set("BKID8009")
                self.booktitle_var.set("Dune")
                self.author_var.set("Frank Herbert")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#11
            elif (x=="The Da Vinci Code"):
                self.bookid_var.set("BKID8011")
                self.booktitle_var.set("The Da Vinci Code")
                self.author_var.set("Dan Brown")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#12
            elif (x=="How to Win Friends and Influence People"):
                self.bookid_var.set("BKID8012")
                self.booktitle_var.set("How to Win Friends and Influence People")
                self.author_var.set("Dale Carnegie")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#13
            elif (x=="War and Peace"):
                self.bookid_var.set("BKID8013")
                self.booktitle_var.set("War and Peace")
                self.author_var.set("Leo Tolstoy")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#14
            elif (x=="The Da Vinci Code"):
                self.bookid_var.set("BKID8014")
                self.booktitle_var.set("The Da Vinci Code")
                self.author_var.set("Dan Brown")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#15
            elif (x=="Jane Eyre"):
                self.bookid_var.set("BKID8015")
                self.booktitle_var.set("Jane Eyre")
                self.author_var.set("Charlotte Brontë")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#16
            elif (x=="Harry Potter and the Sorcerer’s Stone"):
                self.bookid_var.set("BKID8016")
                self.booktitle_var.set("Harry Potter and the Sorcerer’s Stone")
                self.author_var.set("J. K. Rowlings")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#17
            elif (x=="The Fault in Our Stars"):
                self.bookid_var.set("BKID8018")
                self.booktitle_var.set("The Fault in Our Stars")
                self.author_var.set("John Green")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")
#18
            elif (x=="The Hunger Games"):
                self.bookid_var.set("BKID8019")
                self.booktitle_var.set("The Hunger Games")
                self.author_var.set("Suzanne Collins")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs. 380")

                
          
        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        lisrScrollbar.config(command=listbox.yview)


        for item in listBooks:
                listbox.insert(END,item)

        
#==========Button-frame========================================
        Framebutton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="DeepSkyBlue4")
        Framebutton.place(x=0,y=530,width=1500,height=70)
        
#Buttons       
        btnAddData=Button (Framebutton,command=self.adda_data,text="Add Data", font=("arial", 12, "bold"), width=23, bg="LightBlue4", fg="white") 
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button (Framebutton,command=self.fetch_data, text="Show Data", font=("arial", 12, "bold"), width=23, bg="LightBlue4", fg="white") 
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button (Framebutton,command=self.update_data, text="Update", font=("arial", 12, "bold"), width=23, bg="LightBlue4", fg="white") 
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button (Framebutton, text="Delete", font=("arial", 12, "bold"), width=23, bg="LightBlue4", fg="white") 
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button (Framebutton, text="Exit", font=("arial", 12, "bold"), width=23,bg="LightBlue4", fg="white") 
        btnAddData.grid(row=0,column=4)
        
      
        
        
        
        
#==========Information-frame=========
        framedetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="DeepSkyBlue4")
        framedetails.place(x=0,y=600,width=1530,height=225)
        
        Table_frame=Frame(framedetails, bd=6, relief=RIDGE, bg="DeepSkyBlue4")
        Table_frame.place(x=0,y=2, width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame, column=("membertype", "prnno", 
                                                            "title", "firtname", 
                                                            "lastname", "adress1", 
                                                            "adress2", "postid", "mobile", 
                                                            "bookid", "booktitle", "auther", 
                                                            "dateborrowed", "datedue", "days", 
                                                            "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firtname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("adress1", text="Address1")
        self.library_table.heading("adress2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Auther")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")
        
        
        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firtname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)
        

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="jash12345",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook.get(),
                                                                                                            self.lateratefine_var.get(),
                                                                                                            self.dateoverdue.get(),
                                                                                                            self.finallprice.get() 
                                                                                                            ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Book has been issued successfully")
        

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="jash12345", database="library")
            my_cursor = conn.cursor() 
            my_cursor.execute("SELECT * FROM library")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                    self.library_table.delete(*self.library_table.get_children())
                    for row in rows:
                            self.library_table.insert("", END, values=row)
                            conn.close()

    def update_data(self):
            if self.id_var.get() == "":
                    messagebox.showerror("Error", "Please enter an ID to update.")
                    return
            conn = mysql.connector.connect(host="localhost", username="root", password="jash12345", database="library")
            my_cursor = conn.cursor()
            update_query = """UPDATE library SET 
                        membertype=%s, 
                        prnno=%s, 
                        firstname=%s, 
                        lastname=%s, 
                        address1=%s, 
                        address2=%s, 
                        postcode=%s, 
                        mobile=%s, 
                        bookid=%s, 
                        booktitle=%s, 
                        author=%s, 
                        dateborrowed=%s, 
                        datedue=%s, 
                        days=%s, 
                        latereturnfine=%s, 
                        dateoverdue=%s, 
                        finalprice=%s 
                      WHERE id=%s"""
            my_cursor.execute(update_query, (
                    self.member_var.get(),
        self.prn_var.get(),
        self.firstname_var.get(),
        self.lastname_var.get(),
        self.address1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.author_var.get(),
        self.dateborrowed_var.get(),
        self.datedue_var.get(),
        self.daysonbook.get(),
        self.lateratefine_var.get(),
        self.dateoverdue.get(),
        self.finallprice.get(),
        self.id_var.get()  # This is used to specify which record to update
    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data updated successfully.")



      






if __name__=="__main__":
    root = Tk()
    obj = Lib_Mang(root)
    root.mainloop() #to prevent the window from instant closing
  