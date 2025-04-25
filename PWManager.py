#import section
import pandas as pd
import csv as csv
#functions/global variables/classes
#its recomended to use a class

'''
IMPORTANT! 
functions such as the Save and Get functions in the classes have "pass" in them. 
Once you add code DELETE THE PASS! Pass is there to break the function as to not produce any errors while still having the layout clear.
Also currently i have commented out the code in SaveTheData as it did not work, so far the only working features is our ability to add values to the list

'''
account = []
n= input("Are you a new user? (Y/N) ")
class pwmanager:
    def __init__(self): #this makes it so every time we make a new account object it will ask for name, user, pass, and category.
        #TODO Make it so the user can input something to create a randomly generated password, also check for the password criteria as described in the README.md
        self.name = input("What is your name? ")
        self.user = input("what is your username? ")
        self.password = input("What is your password? ")
        self.category = input("What is your category? ")
    def AppendEntry(self): #this appends it to the account list
        account.append(self.name)
        account.append(self.user)
        account.append(self.password)
        account.append(self.category)
        print(account)
    def SaveTheData(self): #This all saves the data to the database.csv file!! it also clears the list so we can keep using it.
        #i suck at data science and wouldnt have figured this out if it werent for bander and GeeksForGeeks https://www.geeksforgeeks.org/writing-data-from-a-python-list-to-csv-row-wise/
        file= open("database.csv","a+",newline='')
        with file:
            write= csv.writer(file)
            write.writerow(account)
            print("Uploaded info to database succesfully!")
            account.clear()
    def GetAccount(self, user): #This will use the pandas module to grab the data
        pass


#mainloop section
#this will be the section where we ask the user if he/she/they wants to make an account or get an existing one.
if n == "y":
    a1=pwmanager()
    pwmanager.AppendEntry(a1)
    pwmanager.SaveTheData(a1)
elif n == "n":
    pass
        