status=True
while status:
    cust_name = input("Enter your name : ")
    Cust_gender = input("enter gender (male/female) : ")
    cust_age = int(input("entr your age : "))
    purchase_product = "ring"
    product_gram = int(input("entr gram you purchased : "))

    bill_amt=0
    get_discount=0
    netbillvalue=0
    totalgoldrate=0
    purchase_amt=0
    currentgold_prise = 5752

    purchase_amt = currentgold_prise * product_gram
    print("currentgold_prise = Rs.5752/gm")
    print("purchase amt : ",purchase_amt)

    totalmakingcharges = product_gram * 845
    print("making charges Rs.845/gm")
    print("total making charges : ",totalmakingcharges)

    bill_amt= purchase_amt + totalmakingcharges 
    print("bill amt : ",bill_amt)

    if Cust_gender == "male" or Cust_gender == "female":
        if Cust_gender == "male":
            if cust_age >0 and cust_age <65:
                if purchase_amt > 0 and purchase_amt <= 200000:
                    get_discount= 0
                elif purchase_amt > 200000 and purchase_amt <= 300000:
                    get_discount=10
                elif purchase_amt > 300000 and purchase_amt <= 500000:
                    get_discount=20
                else:
                    get_discount=25
            else:
                if purchase_amt > 0 and purchase_amt <= 200000:
                    get_discount= 0
                elif purchase_amt > 200000 and purchase_amt <= 300000:
                    get_discount=20
                elif purchase_amt > 300000 and purchase_amt <= 500000:
                    get_discount=30
                else:
                    get_discount=35
        else:
            if cust_age >0 and cust_age <65:
                if purchase_amt > 0 and purchase_amt <= 200000:
                    get_discount= 0
                elif purchase_amt > 200000 and purchase_amt <= 300000:
                    get_discount=15
                elif purchase_amt > 300000 and purchase_amt <= 500000:
                    get_discount=25
                else:
                    get_discount=30
            else:
                if purchase_amt > 0 and purchase_amt <= 200000:
                    get_discount= 0
                elif purchase_amt > 200000 and purchase_amt <= 300000:
                    get_discount=25
                elif purchase_amt > 300000 and purchase_amt <= 500000:
                    get_discount=35
                else:
                    get_discount=40
            
    else:
        print("enter valid gender")

    print("you get discount ", get_discount, " % ""and discount amt :  ", bill_amt * get_discount * 0.01 )
    print("total net amt : ", bill_amt-(bill_amt * get_discount * 0.01))

    
    check = input("Do you want to Continue ? Press Y for yes or N of no : ")
    if check == 'y' or check =="yes":
        status= True
    else:
        status= False