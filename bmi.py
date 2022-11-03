def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight/(height*height)
#Add code here to display calculate BMI
    print("Bmi = "+ str(bmi))
    if (bmi < 18.5):
        print("Under weight")
    if (bmi >=18.5 and bmi <= 25 ):
        print("Normal weight")
    if (bmi > 25):
        print("Over weight")

calculate_bmi(weight=57, height=1.73)