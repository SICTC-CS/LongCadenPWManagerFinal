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
file= pd.read_csv("database.csv",header=0)
class pwmanager:
    def NewEntry(self): #this makes it so every time we make a new account object it will ask for name, user, pass, and category.
        #TODO Make it so the user can input something to create a randomly generated password, also check for the password criteria as described in the README.md
        self.name = input("What is your name? ")
        self.user = input("what is your username? ")
        self.password = input("What is your password? (Leave blank for auto generated one) ")
        self.category = input("What is your category? ")
    def AppendEntry(self): #this appends it to the account list
        account.append(self.name)
        account.append(self.user)
        account.append(self.password)
        account.append(self.category)
        print(account)
    def CheckData(self): 
        if self.password == "":
            x = int(input("How long do you want the password to be? "))
            asciiText = range(33, 126)
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
        global file
        finduser = input("What is your Username (CASE SENSITIVE) ")
        row = file.loc[file['user'] == finduser]
        print(row)
    def Modify(self):
        try:
            df = pd.read_csv("database.csv")
            user = input("Enter your current username for modification: ")

            # Check if the user exists
            if user in df['user'].values:
                print("Account found. What would you like to modify?")
                print("1. Name\n2. Username\n3. Password\n4. Category")
                choice = input("Enter the number of the field you want to modify: ")

                # Get index of the row to modify
                index = df[df['user'] == user].index[0]

                if choice == "1":
                    new_name = input("Enter new name: ")
                    df.at[index, 'name'] = new_name
                elif choice == "2":
                    new_username = input("Enter new username: ")
                    df.at[index, 'user'] = new_username
                elif choice == "3":
                    new_password = input("Enter new password: ")
                    df.at[index, 'password'] = new_password
                elif choice == "4":
                    new_category = input("Enter new category: ")
                    df.at[index, 'category'] = new_category
                else:
                    print("Invalid option.")
                    return

                # Save changes
                df.to_csv("database.csv", index=False)
                print("Account information successfully updated.")

            else:
                print(f"No account found with username '{user}'.")
        except FileNotFoundError:
            print("No database file found. Cannot modify accounts.")
        except Exception as e:
            print("An error occurred while modifying the account:", e)
    def Delete(self): #gpt assisted
        try:
            df = pd.read_csv("database.csv")
            user = input("Type in your username for deletion verification: ")

            # Check if the username exists in the 'user' column
            if user in df['user'].values:
                confirm = input(f"Are you sure you want to permanently delete the account for '{user}'? (Y/N): ").strip().lower()
                if confirm == 'y':
                    df = df[df['user'] != user]
                    df.to_csv("database.csv", index=False)
                    print(f"The account for '{user}' has been successfully deleted.")
                else:
                    print("Account deletion canceled. Your data is safe.")
            else:
                print(f"No account found with the username '{user}'. Please check for typos.")
        except FileNotFoundError:
            print("The database file doesn't exist yet. No accounts to delete.")
        except Exception as e:
            print("An error occurred while trying to delete the account:", e)
                
    
a1=pwmanager()
#mainloop section
#this will be the section where we ask the user if he/she/they wants to make an account or get an existing one.
while True:
    n =input("Are you a new user? (Y/N) ")
    if n == "y":
        pwmanager.NewEntry(a1)
        pwmanager.CheckData(a1)
        pwmanager.AppendEntry(a1)
        pwmanager.SaveTheData(a1)
    elif n == "n":
        pwmanager.GetAccount(a1, finduser)
        pwmanager.Modify(a1)
        pwmanager.Delete(a1)
              
