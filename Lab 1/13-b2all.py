def b2all() :

    byte=float(input("Enter the number of bytes you want to convert\n"))

    kb= byte/1024
    mb=kb/1024
    gb=mb/1024

    print(byte,f"Byte converted to Kb are {kb:.2f} , Mb are {mb:.5f} , Gb are {gb:.10f}.")
    


b2all()