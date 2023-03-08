try:
    sys = input("Which measurement system will you like to use (I for Imperial/English, and M for metric):  ")


    def imperial():
        global result
        ht = input("Enter your height in ft in (format: X XX):  ")
        wt = input("Enter your weight in pounds:  ")
        ft_in_ht = float(ht[0])
        in_ht = 0
        if len(ht) == 4:
            in_ht = float(ht[2:4])
        elif len(ht) == 3:
            in_ht = float(ht[2:3])
        else:
            print("Invalid height format")
            print(len(ht))
        tot_height = (ft_in_ht * 12) + in_ht
        result = (float(wt) / (tot_height * tot_height)) * 703
        result = round(result, ndigits=2)
        print("Your BMI is: " + str(result))


    def metric():
        global result
        ht = float(input("Enter your height in cm(s):  "))
        wt = float(input("Enter your weight in kgs:  "))
        ht /= 100
        result = wt / (ht * ht)
        result = round(result, ndigits=2)
        print("Your BMI is: " + str(result))


    if sys == "I":
        imperial()
    elif sys == "M":
        metric()
    else:
        print("Invalid measurement system!")

    if result < 18.5:
        print("You are underweight!")
    elif 18.5 <= result < 25:
        print("You are normal weight!")
    elif 25 <= result < 30:
        print("You are overweight!")
    elif 30 <= result < 35:
        print("You are OBESE !")
    elif result >= 35:
        print("You are VERY OBESE!")
    else:
        print("You are very underweight!")
except:
    print("The program encountred an error")

input()

