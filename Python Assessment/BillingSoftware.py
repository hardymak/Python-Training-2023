from tkinter import *
from tkinter import messagebox
import random,os



# coding AREA


def total():
    global bathsoaptotal,facecreamtotal,facewashtotal,hairsparytotal,bodylotiontotal,risetotal,foodoiltotal,daaltotal,wheattotal,sugartotal,mazatotal,coketotal,frootitotal,namkeenstotal,biscuitstotal,entry_Otherstax,entry_Grocerystax,entry_Cosmeticstotal,total,billno

    billno=random.randint(1,99999)
    bathsoaptotal = 40 * int(entry_Bathsoap.get())
    facecreamtotal = 200 * int(entry_Facecream.get())
    facewashtotal = 180 * int(entry_Facewash.get())
    hairsparytotal = 100 * int(entry_Hairspary.get())
    bodylotiontotal = 90 * int(entry_Bodylotion.get())

    cosmetictotal = bathsoaptotal+facecreamtotal+facewashtotal+hairsparytotal+bodylotiontotal
    cosmetictax = cosmetictotal * 0.05
    
    entry_Cosmeticstotal.delete(0,END)
    entry_Cosmeticstotal.insert(0,str(cosmetictotal)+' Rs.')
    entry_Cosmeticstax.delete(0,END)
    entry_Cosmeticstax.insert(0,str(cosmetictax)+' Rs.')

    risetotal = 80 * int(entry_Rise.get())
    foodoiltotal = 120 * int(entry_Foodoil.get())
    daaltotal = 50 * int(entry_Daal.get())
    wheattotal = 60 * int(entry_Wheat.get())
    sugartotal = 40 * int(entry_Sugar.get())

    grocerytotal = risetotal+foodoiltotal+daaltotal+wheattotal+sugartotal
    grocerytax = grocerytotal * 0.05
    
    entry_Grocerystotal.delete(0,END)
    entry_Grocerystotal.insert(0,str(grocerytotal)+' Rs.')
    entry_Grocerystax.delete(0,END)
    entry_Grocerystax.insert(0,str(grocerytax)+' Rs.')

    mazatotal = 20 * int(entry_Maza.get())
    coketotal = 40 * int(entry_Coke.get())
    frootitotal = 20 * int(entry_Frooti.get())
    namkeenstotal = 10 * int(entry_Namkeens.get())
    biscuitstotal = 20 * int(entry_Biscuits.get())

    otherstotal = mazatotal+coketotal+frootitotal+namkeenstotal+biscuitstotal
    otherstax = otherstotal * 0.05
    
    entry_Otherstotal.delete(0,END)
    entry_Otherstotal.insert(0,str(otherstotal)+' Rs.')
    entry_Otherstax.delete(0,END)
    entry_Otherstax.insert(0,str(otherstax)+' Rs.')

    total = cosmetictotal + grocerytax + grocerytotal + grocerytax + otherstotal + otherstax
    entry_Billno.delete(0,END)
    entry_Billno.insert(0,billno)

def save():
    if not os.path.exists('Bills'):
        os.mkdir('Bills')
    savebill=messagebox.askyesno('Confirm','Want to Save Bill ?')
    if savebill :
        bill_save = bill_Viwes.get(1.0,END)
        file=open(f"Bills/{billno}.txt","w")
        file.write(bill_save)
        file.close()
        messagebox.showinfo("Success",f"Bill No :{billno} is Saved Successfully")

def generatebill():
    if entry_Cname.get() == "" or entry_Cmno.get() =="":
        messagebox.showerror('Error','Customer Details Required')
    elif entry_Cosmeticstotal.get() == "" and entry_Grocerystotal.get()  == "" and entry_Otherstotal.get() =="":
        messagebox.showerror('Error','Please Enter Product Qty')
    elif entry_Cosmeticstotal.get() == "0 Rs." and entry_Grocerystotal.get()  == "0 Rs." and entry_Otherstotal.get() =="0 Rs.":
        messagebox.showerror('Error','Please Enter Product Qty')
    else:
    
        bill_Viwes.insert(END,f"\t * * *  WELCOME CUSTOMER  * * * ")
        bill_Viwes.insert(END,f"\n Bill No : {billno}")
        bill_Viwes.insert(END,f"\n Customer Name : {entry_Cname.get()}")
        bill_Viwes.insert(END,f"\n Customer Number : {entry_Cmno.get()}")
        bill_Viwes.insert(END,f"\n= = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        bill_Viwes.insert(END,f"\n Product \t\t\t Qty \t\t price")
        bill_Viwes.insert(END,f"\n= = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        if entry_Bathsoap.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Bathsoap.get()} \t\t {bathsoaptotal}")
        if entry_Facecream.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Facecream.get()} \t\t {facecreamtotal}")
        if entry_Facewash.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Facewash.get()} \t\t {facewashtotal}")
        if entry_Hairspary.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Hairspary.get()} \t\t {hairsparytotal}")
        if entry_Bodylotion.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Bodylotion.get()} \t\t {bodylotiontotal}")
        if entry_Rise.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Rise.get()} \t\t {risetotal}")
        if entry_Foodoil.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Foodoil.get()} \t\t {foodoiltotal}")
        if entry_Daal.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Daal.get()} \t\t {daaltotal}")
        if entry_Wheat.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Wheat.get()} \t\t {wheattotal}")
        if entry_Sugar.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Sugar.get()} \t\t {sugartotal}")
        if entry_Maza.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Maza.get()} \t\t {mazatotal}")
        if entry_Coke.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Coke.get()} \t\t {coketotal}")
        if entry_Frooti.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Frooti.get()} \t\t {frootitotal}")
        if entry_Namkeens.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Namkeens.get()} \t\t {namkeenstotal}")
        if entry_Biscuits.get() != "0":
            bill_Viwes.insert(END,f"\n Bath Shop \t\t\t {entry_Biscuits.get()} \t\t {biscuitstotal}")
        bill_Viwes.insert(END,f"\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        bill_Viwes.insert(END,f"\n Cosmetic Tax \t\t\t {entry_Cosmeticstax.get()}")
        bill_Viwes.insert(END,f"\n Grocery Tax \t\t\t {entry_Grocerystax.get()}")
        bill_Viwes.insert(END,f"\n Others Tax \t\t\t {entry_Otherstax.get()}")
        bill_Viwes.insert(END,f"\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        bill_Viwes.insert(END,f"\n\t\t Total Bill : \t{total} ")    

        bill_Viwes.insert(END,f"\n\n= = = = = = = = = = = Thank You = = = = = = = = = = =")
        # bill_Viwes.delete(1,END)
        save()

def exit_1():
    screen.destroy()
def clear():
    entry_Bathsoap.delete(0,END)
    entry_Bathsoap.insert(0,0)

    entry_Facecream.delete(0,END)
    entry_Facecream.insert(0,0)

    entry_Facewash.delete(0,END)
    entry_Facewash.insert(0,0)

    entry_Hairspary.delete(0,END)
    entry_Hairspary.insert(0,0)

    entry_Bodylotion.delete(0,END)
    entry_Bodylotion.insert(0,0)

    entry_Rise.delete(0,END)
    entry_Rise.insert(0,0)

    entry_Foodoil.delete(0,END)
    entry_Foodoil.insert(0,0)

    entry_Daal.delete(0,END)
    entry_Daal.insert(0,0)

    entry_Wheat.delete(0,END)
    entry_Wheat.insert(0,0)

    entry_Sugar.delete(0,END)
    entry_Sugar.insert(0,0)

    entry_Maza.delete(0,END)
    entry_Maza.insert(0,0)

    entry_Coke.delete(0,END)
    entry_Coke.insert(0,0)

    entry_Frooti.delete(0,END)
    entry_Frooti.insert(0,0)

    entry_Namkeens.delete(0,END)
    entry_Namkeens.insert(0,0)

    entry_Biscuits.delete(0,END)
    entry_Biscuits.insert(0,0)

    entry_Grocerystotal.delete(0,END)
    entry_Grocerystax.delete(0,END)
    entry_Cosmeticstotal.delete(0,END)
    entry_Cosmeticstax.delete(0,END)
    entry_Otherstotal.delete(0,END)
    entry_Otherstax.delete(0,END)
    entry_Cname.delete(0,END)
    entry_Cmno.delete(0,END)
    entry_Billno.delete(0,END)


def search():
    for i in os.listdir('Bills'):
        if i.split('.') [0] == entry_Billno.get():
            f=open(f"Bills/{i}","r")
            bill_Viwes.delete(1.0,END)
            for data in f:
                bill_Viwes.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Bill No not found')


# GUI AREA

screen = Tk()
screen.title("Billing Software")
screen.geometry("1366x768")
screen.configure(bg="#ABEBC6")
screen.state('zoomed')

# HEADER

frame_header = Frame(screen,bg="#2C3E50",borderwidth=4,relief=GROOVE)
frame_header.pack(fill="x",side="top",pady=1)

lable_heading = Label(frame_header,text="Billing Software",font=("Baufra",20,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_heading.pack()

# FOOTER

frame_footer = Frame(screen,bg="#2C3E50",borderwidth=4,relief=GROOVE)
frame_footer.pack(fill="x",side="bottom")

lable_footer = Label(frame_footer,text="By : Lionize Developers LLP",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_footer.pack()

# CUSTOMER DETAILS

frame_Cdetails = LabelFrame(screen,text="Customer Details",bg="#2C3E50",borderwidth=4,relief=GROOVE,font=("Candara",14,"bold"),fg="red")
frame_Cdetails.pack(fill= "x",pady=1)

lable_Cname = Label(frame_Cdetails,text="Customer Name : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_Cname.grid(row=0,column=0)

entry_Cname = Entry( frame_Cdetails,font=("Candara",10,"bold"),borderwidth= 5,bg="white")
entry_Cname.grid(row=0,column=1,padx= 10,pady=10)

lable_Cmno = Label(frame_Cdetails,text="Mobile No. : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_Cmno.grid(row=0,column=2)

entry_Cmno = Entry( frame_Cdetails,font=("Candara",10,"bold"),borderwidth= 5,bg="white")
entry_Cmno.grid(row=0,column=3,padx= 10,pady=10)

lable_Billno = Label(frame_Cdetails,text="Bill No. : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_Billno.grid(row=0,column=4)

entry_Billno = Entry( frame_Cdetails,font=("Candara",10,"bold"),borderwidth= 5,bg="white")
entry_Billno.grid(row=0,column=5,padx= 10,pady=10)

search_button = Button(frame_Cdetails,text= "Search",font=("Candara",10,"bold"),borderwidth= 5,bg="white",activebackground="#D0D3D4",relief="raised",command=search)
search_button.grid(row=0,column=6,padx= 10,pady=10)

# BILLING VIWES

frame_BillViwe = Frame(screen,bg="#2C3E50",borderwidth=6,relief=GROOVE)
frame_BillViwe.pack(fill="y",side="right")

lable_Viwes = Label(frame_BillViwe,text="Bill Viwe",font=("Candara",14,"bold"),fg="white",borderwidth= 2,bg="#2C3E50",relief=GROOVE)
lable_Viwes.pack(side=TOP,fill="x")

bill_Viwes = Text(frame_BillViwe,height=31,width=48,relief=GROOVE,font=("time new roman",10,"bold"))
bill_Viwes.pack(pady=2)

# BILL MENU

frame_Billmenu = LabelFrame(screen,text="Bill Menu",bg="#2C3E50",borderwidth=4,relief=GROOVE,font=("Candara",14,"bold"),fg="red")
frame_Billmenu.pack(side="bottom",fill= "x",padx=2)

lable_Cosmeticstotal = Label(frame_Billmenu,text="Cosmetics Total : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Cosmeticstotal.grid(row=0,column=0)

entry_Cosmeticstotal = Entry( frame_Billmenu,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Cosmeticstotal.grid(row=0,column=1,padx= 10,pady=10)


lable_Grocerystotal = Label(frame_Billmenu,text="Grocerys Total : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Grocerystotal.grid(row=1,column=0)

entry_Grocerystotal = Entry( frame_Billmenu,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Grocerystotal.grid(row=1,column=1,padx= 10,pady=10)

lable_Otherstotal = Label(frame_Billmenu,text="Others Total : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Otherstotal.grid(row=2,column=0)

entry_Otherstotal = Entry( frame_Billmenu,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Otherstotal.grid(row=2,column=1,padx= 10,pady=10)

lable_Cosmeticstax = Label(frame_Billmenu,text="Cosmetics Tax : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Cosmeticstax.grid(row=0,column=2)

entry_Cosmeticstax = Entry( frame_Billmenu,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Cosmeticstax.grid(row=0,column=3,padx= 10,pady=10)

lable_Grocerystax = Label(frame_Billmenu,text="Grocerys Tax : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Grocerystax.grid(row=1,column=2)

entry_Grocerystax = Entry( frame_Billmenu,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Grocerystax.grid(row=1,column=3,padx= 10,pady=10)

lable_Otherstax = Label(frame_Billmenu,text="Others Tax : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Otherstax.grid(row=2,column=2)

entry_Otherstax = Entry( frame_Billmenu,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Otherstax.grid(row=2,column=3,padx= 10,pady=10)

total_button = Button(frame_Billmenu,text= "    Total       ",font=("Candara",11,"bold"),borderwidth= 5,bg="white",activebackground="#D0D3D4",relief="raised",command=total)
total_button.place(x=580,y=57)

generatebill_button = Button(frame_Billmenu,text= "Generate Bill",font=("Candara",11,"bold"),borderwidth= 5,bg="white",activebackground="#D0D3D4",relief="raised",command=generatebill)
generatebill_button.place(x=680,y=57)

clear_button = Button(frame_Billmenu,text= "      clear      ",font=("Candara",11,"bold"),borderwidth= 5,bg="white",activebackground="#D0D3D4",relief="raised",command=clear)
clear_button.place(x=800,y=57)

exit_button = Button(frame_Billmenu,text= "        exit        ",font=("Candara",11,"bold"),borderwidth= 5,bg="white",activebackground="#D0D3D4",relief="raised",command=exit_1)
exit_button.place(x=900,y=57)

# COSMETICS 

frame_Cosmetic = LabelFrame(screen,text="Cosmetic",bg="#2C3E50",borderwidth=4,relief=GROOVE,font=("Candara",14,"bold"),fg="red")
frame_Cosmetic.pack(side="left",fill="y",padx= 2)

lable_Bathsoap = Label(frame_Cosmetic,text="Bath Soap : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Bathsoap.grid(row=0 , column= 0, padx=50)

entry_Bathsoap = Entry( frame_Cosmetic,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Bathsoap.grid(row=0,column=1,padx= 10,pady=10)
entry_Bathsoap.insert(0,0)

lable_Facecream = Label(frame_Cosmetic,text="Face Cream : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Facecream.grid(row=1 , column= 0)

entry_Facecream = Entry( frame_Cosmetic,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Facecream.grid(row=1,column=1,padx= 10,pady=10)
entry_Facecream.insert(0,0)

lable_Facewash = Label(frame_Cosmetic,text="Face Wash : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Facewash.grid(row=2 , column= 0)

entry_Facewash = Entry( frame_Cosmetic,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Facewash.grid(row=2,column=1,padx= 10,pady=10)
entry_Facewash.insert(0,0)

lable_Hairspary = Label(frame_Cosmetic,text="Hair Spray : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Hairspary.grid(row=3 , column= 0)

entry_Hairspary = Entry( frame_Cosmetic,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Hairspary.grid(row=3,column=1,padx= 10,pady=10)
entry_Hairspary.insert(0,0)

lable_Bodylotion = Label(frame_Cosmetic,text="Body Lotion : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Bodylotion.grid(row=4 , column= 0)

entry_Bodylotion = Entry( frame_Cosmetic,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Bodylotion.grid(row=4,column=1,padx= 10,pady=10)
entry_Bodylotion.insert(0,0)

# GROCERY

frame_Grocery = LabelFrame(screen,text="Grocery",bg="#2C3E50",borderwidth=4,relief=GROOVE,font=("Candara",14,"bold"),fg="red")
frame_Grocery.pack(side="left",fill="y",padx= 2)

lable_Rise = Label(frame_Grocery,text="Rise : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Rise.grid(row=0, column= 0,padx=50)

entry_Rise = Entry( frame_Grocery,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Rise.grid(row=0,column=1,padx= 10,pady=10)
entry_Rise.insert(0,0)

lable_Foodoil = Label(frame_Grocery,text="Food Oil : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Foodoil.grid(row=1, column= 0)

entry_Foodoil = Entry( frame_Grocery,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Foodoil.grid(row=1,column=1,padx= 10,pady=10)
entry_Foodoil.insert(0,0)

lable_Daal = Label(frame_Grocery,text="Daal : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Daal.grid(row=2, column= 0)

entry_Daal = Entry( frame_Grocery,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Daal.grid(row=2,column=1,padx= 10,pady=10)
entry_Daal.insert(0,0)

lable_Wheat = Label(frame_Grocery,text="Wheat : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Wheat.grid(row=3, column= 0)

entry_Wheat = Entry( frame_Grocery,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Wheat.grid(row=3,column=1,padx= 10,pady=10)
entry_Wheat.insert(0,0)

lable_Sugar = Label(frame_Grocery,text="Sugar : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Sugar.grid(row=4, column= 0)

entry_Sugar = Entry( frame_Grocery,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Sugar.grid(row=4,column=1,padx= 10,pady=10)
entry_Sugar.insert(0,0)

# OTHERS

frame_Other = LabelFrame(screen,text="Others",bg="#2C3E50",borderwidth=4,relief=GROOVE,font=("Candara",14,"bold"),fg="red")
frame_Other.pack(side="left",fill="y",padx= 2)

lable_Maza = Label(frame_Other,text="Maza : ",font=("Candara",10,"bold"),fg="white",padx= 3,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Maza.grid(row=0,column=0,padx=44)

entry_Maza = Entry( frame_Other,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Maza.grid(row=0,column=1,padx= 10,pady=10)
entry_Maza.insert(0,0)

lable_Coke = Label(frame_Other,text="Coke : ",font=("Candara",10,"bold"),fg="white",padx= 3,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Coke.grid(row=1,column=0)

entry_Coke = Entry( frame_Other,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Coke.grid(row=1,column=1,padx= 10,pady=10)
entry_Coke.insert(0,0)

lable_Frooti = Label(frame_Other,text="Frooti : ",font=("Candara",10,"bold"),fg="white",padx= 3,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Frooti.grid(row=2,column=0)

entry_Frooti = Entry( frame_Other,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Frooti.grid(row=2,column=1,padx= 10,pady=10)
entry_Frooti.insert(0,0)

lable_Namkeens = Label(frame_Other,text="Namkeens : ",font=("Candara",10,"bold"),fg="white",padx= 3,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Namkeens.grid(row=3,column=0)

entry_Namkeens = Entry( frame_Other,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Namkeens.grid(row=3,column=1,padx= 10,pady=10)
entry_Namkeens.insert(0,0)

lable_Biscuits = Label(frame_Other,text="Biscuits : ",font=("Candara",10,"bold"),fg="white",padx= 3,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Biscuits.grid(row=4,column=0)

entry_Biscuits = Entry( frame_Other,font=("time new roman",10,"bold"),borderwidth= 5,bg="white")
entry_Biscuits.grid(row=4,column=1,padx= 10,pady=10)
entry_Biscuits.insert(0,0)

screen.mainloop()