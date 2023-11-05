#login
import admin_code
import user_code
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Add functions for admin and user authentication
    def admin_login(self,admin_username, admin_password):
        if self.username == admin_username and self.password == admin_password:
            return True  # Authentication successful
        else:
            return False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_login(self,username, password):
        if self.username == username and self.password == password:
            return True  # Authentication successful
        else:
            return False 
    # Implement user authentication logic here
    # Check if username and password match user credentials
    

# Modify the main program
def main():
    admin = Admin("Deepakshi","xyz")
    user = User("Aniket","sh")

    while True:
        print("\nMenu Options:")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("Enter your choice: ")
           
        if choice == '1':
            admin_username = input("Enter Admin Username: ")
            admin_password = input("Enter Admin Password: ")          
            if admin.admin_login(admin_username,admin_password):
                print("Login Successful")  # Authentication successful
                return(admin_code.main())
            else:
                print("Try again.")
                
            
        elif choice == '2':
            user_username = input("Enter User Username: ")
            user_password = input("Enter User Password: ")
            if user.user_login(user_username,user_password):
                print("User successfully logged in")
                return(user_code.main())
            else:
                print("Please Try Again !!")

        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()