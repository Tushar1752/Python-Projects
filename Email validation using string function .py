#Email validation using string function project

# Email validation using string functions


email = input("Enter Your Email = ")

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                if " " in email:
                    print(" Email ID should not contain spaces")
                elif email.index("@") > email.index("."):
                    print(" Invalid position: '.' should come after '@'")
                elif any (ch.isupper() for ch in email):
                    print(" Email ID should not be in capital letters")
                else:
                    print(" Email ID is valid so far")
            else:
                print(" Invalid position or missing '.' in domain")
        else:
            print(" Invalid '@' position, missing '@', or multiple '@' symbols")
    else:
        print(" First character should be an alphabet")
else:
    print(" Email length should be at least 6 characters")