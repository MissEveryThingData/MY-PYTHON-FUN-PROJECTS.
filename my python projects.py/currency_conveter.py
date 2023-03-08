def main():
    print("This program converts US dollars into Rands")
    print("")

    dollars = eval(input("Enter the amounts in dollars:  "))

    Rands = convert_to_rands(dollars)

    print("That is", Rands, "rands.")

convert_to_rands = lambda dollars: dollars * 17.6635

main()



