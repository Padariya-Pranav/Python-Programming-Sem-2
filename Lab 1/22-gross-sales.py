def gr_sales():

    gross_sales = float(input("Enter the Amount of gross sales done by you :\n"))

    discount=gross_sales*10/100

    net_sales = gross_sales - discount
    print("Total discount given is :", discount)
    print(f"The Net Sales done by you is : {net_sales:.3f}")

gr_sales()