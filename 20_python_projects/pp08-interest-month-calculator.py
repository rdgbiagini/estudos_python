# ==================================================================================================================================================================== #
# COLECT THE NECESSARY INPUT - PRINCIPAL, APR, YEARS
# CALCULATE THE MONTHLY PAYMENTS 
# SHOW TO THE USER
# ==================================================================================================================================================================== #

def main():
    print("This is you monthly payment loan calculator. ")
    print("")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the anual interest rating: "))
    years = int(input("Input amout of years: "))
    
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payments = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    
    print("The monthly payment for this loan is: %.2f " % monthly_payments)
    
main()