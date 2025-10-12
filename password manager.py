#password manager project 


maaster_pwd = input("What is the master passeord:")

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if '|' in data:
                    name, pwd = data.split('|',1)
                    print(f"Account: {name}, Password: {pwd}")
                else:
                    print("Invalid line:", data)
    except FileNotFoundError:
        print("No passwords saved yet!")

def add():
     name=input("Account name:")
     pwd=input("Password:")
     with open('password.txt','a') as f:
        f.write(name + "|" +pwd)
     print("Password added succesfully")

while True:
     mode= input("Would you like to add a new password or view existing ones (view/add),press q to quit?").lower()
     if mode == "q":
        break 
     elif mode =="view":
        view()
     elif mode =="add":
        add()
     else:
        print("invalid mode.")