#import section
import pandas as pd
import csv as csv
import random
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
        self.name = input("Please enter your name? ")
        self.user = input("Please enter your username? ")
        self.password = input("Please enter your password? (Leave blank for auto generated one) ")
        self.category = input("Please enter your category? ")
    def AppendEntry(self): #this appends it to the account list
        account.append(self.name)
        account.append(self.user)
        account.append(self.password)
        account.append(self.category)
    def CheckData(self): 
        #This is the auto password feature and is also like the one thing that Caden did
        if self.password == "":
            x = 8
            asciiText = range(33,126)
            self.password = ''.join(chr(random.choice(asciiText)) for _ in range(x))
            
        #this section will be checking the password. This section was also taken from Chatgpt because i didnt remember a whole lot of the functions for things like checking uppercase or digits
        #but i do understand the code it spat out at me quite well
        """Check if the password meets the criteria."""
        # Define the list of allowed special characters
        special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
        # Check if password is at least 8 characters long
        if len(self.password) < 8:
            print("Password must be at least 8 characters long")
            self.password = input("What is your password? (Leave blank for auto generated one) ")
        # Check if the password contains at least one capital letter
        if not any(char.isupper() for char in self.password):
            print("password must have at least one uppercase letter")
            self.password = input("What is your password? (Leave blank for auto generated one) ")
        # Check if the password contains at least one number
        if not any(char.isdigit() for char in self.password):
            print("password must have at least one digit")
            self.password = input("What is your password? (Leave blank for auto generated one) ")
        # Check if the password contains at least one special character from the allowed list
        if not any(char in special_characters for char in self.password):
            print("must have at least one special character")
            self.password = input("What is your password? (Leave blank for auto generated one) ")

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
        attempts=0
        finduser = input("What is your Username (CASE SENSITIVE) ")
        row = file.loc[file['user'] == finduser]
        password=input("Password: ")
        if password == row['password'].item():
            print(row)
        else:
            print("Access Denied!")
            attempts+=1
    def Delete(self):
        pass
    def Modify(self):
        pass
                
    def printAccount(self):
        print(f" Name:{self.name}")
        print(f" User:{self.user}")
        print(f" Password:{self.password}")
    
a1=pwmanager()
#mainloop section
#this will be the section where we ask the user if he/she/they wants to make an account or get an existing one.
while True:
    n =input("Are you a new user? (Y/N) ")
    if n == "y":
        pwmanager.NewEntry(a1)
        pwmanager.CheckData(a1)
        pwmanager.printAccount(a1)
        pwmanager.AppendEntry(a1)
        pwmanager.SaveTheData(a1)
    elif n == "n":
        pwmanager.GetAccount(a1, finduser)
        
