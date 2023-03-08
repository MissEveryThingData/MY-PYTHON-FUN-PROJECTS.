def main():
    print("welcome to the email slicer")
    print("")

    email_input = input("input your email address: ")

    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()