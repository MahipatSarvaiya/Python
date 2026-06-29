thermo_stat = input("enter status : ").lower() 



if(thermo_stat == "active"):

    thermo_temp = int(input("enter temparature : "))

    if(thermo_temp> 35):
        print ("high temp!")
    else :
        print("normal temp")

elif(thermo_stat == "off"):
    print("thermo is off")

else:
    print("enter valid")