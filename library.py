from xml.etree.ElementTree import ElementTree


library=[{"title":"maths","author":"ahmed" ,"copies":3,"status":"available","price":200,"pages":222,"borrow":1},
{"title":"5am club ","author":"robin","copies":2,"status":"available","price":250,"pages":300,"borrow":0}]

def menu():
    choice=input("""       Welcome to Library       
    1-add book
    2-update book
    3-read book 
    4-delete
    5-borrow book
    6-return book
    7-view status
    8-view book copies
    ********************    """)
    return choice

def exit():
    op=int(input(""" thank you 
     if you want return to main menu enter 0 if not any other """))
    return op 

def Add(library,title,author,copies,price,pages):
    z=0
    for i in library:
        if i["title"]==title:
            print("this book is already present")
            z+=1
    if copies ==0:
        status="not available"
    else: status="available"
    if z==0:
        print("the book has been added successfully ")
        library.append({"title":title,"author":author,"copies":int(copies),"sataue":status,"price":price,"pages":int(pages),"borrow":0})
        print(library[-1])
    else: print("this book is alraedy present ")


def update(library,title):
    z=0
    for i in library:
        if i["title"]==title:
            z+=1
    if not z==0:
        inp=input("""choose the item you want to update 
        1- title 
        2-author 
        3- price 
        4- copies """)
        if inp.isdigit()and int(inp) in  range (1,5):
            inp=int(inp)
            if inp==1:
                title=input("enter the new title ")
                for i in library:
                    if i["title"]==title:
                        i.update({"title":title})
            if inp==2:
                author=input("enter the new author ")
                for i in library:
                    if i["title"]==title:
                        i.update({"author":author})
            if inp==3:
                price=int(input("enter the new price "))
                for i in library:
                    if i["title"]==title:
                        i.update({"price":price})
            if inp==4:
                copies=input("enter the copies ")
                for i in library:
                    if i["title"]==title:
                        i.update({"copies":copies})
                        if copies==0:
                            i.update({"status":"unavailable"})
                        else:i.update({"status":"available"})
            else:print("enter number from 1 to 4 ")
    if z==0:print("this book can not be found ")


def read(library,title):
    z=0
    for i in library:
        if i["title"]==title:
            z+=1
            if i["copies"]==0:
                print("this book is not avialable right know")
            else:
                print(f'-the book title:- {i["title"]}')
                print(f'-the book status:- {i["status"]}')
                print(f'-the book author is {i["author"]}')
                print(f'the book has {i["pages"]} page')
                print(f'the book price is {i["price"]} ')
    if z==0:print("this book can not be found ")


def delete(library,title ):
    z=0
    for i in library:
        if i["title"]==title:
            z+=1
            del(i)
            print("the book was deleted successfully ")
    if z==0:print("this book is not found ")


def borrow(library,title):
    z=0
    for i in library:
        if i["title"]==title:
            z+=1
            if i["copies"]>0:
                i["copies"]-=1
                i["borrow"]+=1
                print(f'-the book title {i["title"]}')
                print(f'-the book status')
                print(f'-the book author is {i["author"]}')
                print(f'the book has {i["pages"]} page')
                print(f'the book price is {i["price"]} ')
                print("the book has been borrowed successfully")
            else:print(f'there are {i["copies"]} left  ')
    if z==0:print("this book can not be found ")
    

def returnbook(library,title):
    z=0
    for i in library:
        if i["title"]==title:
            z+=1
            if i["borrow"]==0:
                print("this book is not borrowed to be returned  ")
            else:
                print("the book returned successfully")
                i["copies"]+=1
                i["borrow"]-=1
                print(f'there are {i["copies"]} copy of the {i["title"]} now')
    if z==0:print("this book is not present ")


def view(library,title):
    z=0
    for i in library:
        if i["title"]==title:
            z+=1
            if i["copies"]>0:
                print(f' {i["title"]} book is available with {i["copies"]} copy  ')
                print(f'the book is borrowed {i["borrow"]} times now')
            else:
                print("this book is not available there is 0 copy ")
    if z==0:print("thuis book can not be found ")


while True:
    m=menu()
    if  not m.isdigit():
        q=exit()
        if q==0:
            continue
        else:break
    else:
       m=int(m)
       if m not in range (1,9):
           print("enter number from 1 to 9 ")
           continue
       else:
            if m==1:
               title=input("Enter the book title ").lower()
               author=input("enter the book writer ").lower()
               pages=input("enter the book pages ")
               copies=input("enter the number of copies ")
               price=input("enter the book price ")
               if not pages.isdigit() and copies.isdigit() and price.isdigit():
                   print("please enter a whole number in the copies price and pages ")
               else:
                   Add(library,title,author,copies,price,pages)
                   q=exit()
                   if q==0:
                       continue
                   else: break
            elif m==2:
                title=input("Enter the book title ").lower()
                update(library,title)
                q=exit()
                if q==0:
                       continue
                else: break
            elif m==3:
                title=input("Enter the book title ").lower()
                read(library,title)
                q=exit()
                if q==0:
                       continue
                else: break
            elif m==4:
                title=input("Enter the book title ").lower()
                delete(library,title)
                q=exit()
                if q==0:
                       continue
                else: break
            elif m==5:
                title=input("Enter the book title ").lower()
                borrow(library,title)
                q=exit()
                if q==0:
                       continue
                else: break
            elif m==6:
                title=input("Enter the book title ").lower()
                returnbook(library,title)
                q=exit()
                if q==0:
                       continue
                else: break
            elif m==7 or m==8 :
                title=input("Enter the book title").lower()
                view(library,title)
                q=exit()
                if q==0:
                       continue
                else: break




                

            


            



     

            


    


