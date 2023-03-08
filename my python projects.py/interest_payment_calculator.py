def main():
    print("This is my monthly payement calculator")
    print("")

    principal = float (input("input the loan amount:"))
    apr = float (input("input the annual interest rate:"))
    years = int (input("input amount of years:"))


    monthly_interest_rate = apr/1200
    amount_of_months = years*12
    monthly_payment = principal*monthly_interest_rate/(1-(1+monthly_interest_rate)*())

    print("The monthly payement for this loan is: %.2f"% monthly_payement)

    main()