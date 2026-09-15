import mysql.connector

conn1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="augbatch1"
)

cursor=conn1.cursor() # cursor Object

# cursor.execute("SELECT * FROM actors")
# print(cursor.fetchall()) 

#insert,delete,update 
# try:
#     cursor.execute("UPDATE actors SET age=%s WHERE id=%s",[53,2])
#     conn1.commit()
#     print("Updation Successfull..!")    
# except Exception:
#     print("Something went Wrong...!")

# conn1.start_transaction()
# try:
#     cursor.execute("UPDATE bankacc SET balance=balance-%s WHERE accNo=%s",[50,"1234567"])
#     cursor.execute("UPDATE bankacc SET balance=balance+%s WHERE accNo=%s",[50,"2345678"])
#     conn1.commit()
# except Exception:
#     conn1.rollback()

while 1:
    inp=int(input("0--> Exit\n1--> View Contacts\n2--> Add a Contact\n3--> Update a Contact\n4 --> Delete a Contact\nChoose an Option:"))

    if inp==0:
        break 
    elif inp==1:
        pass
    elif inp==2:
        pass
    elif inp==3:
        pass
    elif inp==4:
        pass
    else:
        print("Invalid Input")