def rec():
    l=float(input("Enter the length of the square you want to find the area and perimeter of:\n"))
    b=float(input("Enter the breadth of the square you want to find the area and perimeter of:\n"))

    Area= (l*b)
    perimeter=2*(l+b)
    print()

    print("The Area Of Square of Length",l, "& breadth", b, "is :" ,Area, "sq.meter")
    print("The perimeter of the square of length " ,l, "& breadth" ,b, "is :" ,perimeter, "meter")


rec()