def display_main_menu():
    print("Enter some numbers separated by commas ")

def get_user_input():

    x=input(":")
    txt=x.split(",")
    return txt

def calc_average_temperature(array):
    total=0
    for i in range (int(len(array))):
        total=total+int(array[i])
        average = total/int(len(array))
    return average

def calc_min_max_temperature(array):
    max=0
    min=10000000000000000
    for i in range(int(len(array))):
        if int(array[i])>max:
            max=int(array[i])
        if int(array[i])<min:
            min=int(array[i])
    return max,min




display_main_menu()
txt=get_user_input()
average=calc_average_temperature(txt)
print("Average: "+str(average))
max,min=calc_min_max_temperature(txt)
print("Max: "+str(max))
print("Min: "+str(min))







