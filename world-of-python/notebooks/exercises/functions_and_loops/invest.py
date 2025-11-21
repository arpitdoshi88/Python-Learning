def invest(principal_amount,rate_of_interest,number_of_years):
    
    roi = rate_of_interest/100
    for i in range(number_of_years):
        amount_earned = principal_amount * (1+roi)
        print(f"Year {i+1}: Earned amount is ${amount_earned:.2f}")
        principal_amount = amount_earned
        
        
if __name__ == "__main__":
    principal_amount = float(input("Enter the principal amount: $"))
    rate_of_interest = float(input("Enter the rate of interest (in %): "))
    number_of_years = int(input("Enter the number of years: "))
    invest(principal_amount,rate_of_interest,number_of_years)  