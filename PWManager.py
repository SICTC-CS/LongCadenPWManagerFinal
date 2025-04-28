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
n= ""
finduser = ""

class pwmanager:
    def NewEntry(self): #this makes it so every time we make a new account object it will ask for name, user, pass, and category.
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
    def CheckData(self): #This function will handle checking the data, this includes ensuring the selected user is unique and the password meets the critera in the README.md
        pass
    def SaveTheData(self): #This all saves the data to the database.csv file!! it also clears the list so we can keep using it.
        #i suck at data science and wouldnt have figured this out if it werent for bander and GeeksForGeeks https://www.geeksforgeeks.org/writing-data-from-a-python-list-to-csv-row-wise/
        file= open("database.csv","a+",newline='')
        with file:
            write= csv.writer(file)
            write.writerow(account)
            print("Uploaded info to database succesfully!")
            account.clear()
    def GetAccount(self, finduser):  # This will use pandas to grab data
        file= pd.read_csv("database.csv",header=0)
        finduser = input("What is your Username (CASE SENSITIVE) ")
        row = file.loc[file['user'] == finduser]
        print(row)
    # try:
    #     df = pd.read_csv("database.csv")
    #     found = df[df['Username'].str.lower() == user.lower()]
    #     if not found.empty:
    #         print("Account found:")
    #         print(found)
    #     else:
    #         print("No account found with that username.")
    # except FileNotFoundError:
    #     print("Database file not found.")
    # except Exception as e:
    #     print("An error occurred while retrieving the account:", e) #Caden asked ChatGPT to do the get function for him, this is what is spat ou
    
a1=pwmanager()
#mainloop section
#this will be the section where we ask the user if he/she/they wants to make an account or get an existing one.
while True:
    n =input("Are you a new user? (Y/N) ")
    if n == "y":
        pwmanager.NewEntry(a1)
        pwmanager.AppendEntry(a1)
        pwmanager.SaveTheData(a1)
    elif n == "n":
        pwmanager.GetAccount(a1, finduser)
        
