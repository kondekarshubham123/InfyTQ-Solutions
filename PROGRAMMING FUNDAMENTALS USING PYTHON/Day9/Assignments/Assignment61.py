#PF-Assgn-61
import re
def validate_name(name):
    return str.isalpha(name) and len(name)<16
    #Start writing your code here

def validate_phone_no(phno):
    return (str.isdigit(phno) and len(phno)==10) and (not len(list(set(list(phno)))) == 1)
    

def validate_email_id(email_id):
    return (re.search('@gmail.com$|@yahoo.com$|@hotmail.com$',email_id)) != None and (email_id.count('@')==1) and (email_id.count('.com')==1)
    #Start writing your code here

def validate_all(name,phone_no,email_id):
    if validate_name(name) is False:
        print("Invalid Name")
    elif validate_phone_no(phone_no) is False:
        print("Invalid phone number")
    elif validate_email_id(email_id) is False:
        print("Invalid email id")
    else:
        print("All the details are valid")
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9999999991", "harry@gmail.com")