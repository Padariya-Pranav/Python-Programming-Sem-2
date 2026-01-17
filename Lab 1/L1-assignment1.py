def avg() :

    maths=float(input("Enter the marks obtained in Maths examination:\n"))

    computer=float(input("Enter the marks obtained in Computer examination:\n"))

    geology=float(input("Enter the marks obtained in Geology examination:\n"))

    total= maths + computer + geology

    average= total/3

    print("The total marks obtained in the examination are :", total)

    print("The average of 3 subjects in the examination is :", average)

avg()
