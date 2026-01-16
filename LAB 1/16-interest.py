def int():

    premium=float(input("Enter the Premium Amount\n"))

    rate=float(input("Enter the rate of interest\n"))

    n=float(input("Enter the time period for the policy term\n"))

    I=(premium*rate*n)/100

    print(f"The Calculated interest for {premium:.2f} premium , {rate:.2f} rate of interest and {n:.3f}Years of time is: {I}")

int()