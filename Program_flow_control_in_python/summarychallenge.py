option = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]

print("Please choose your option from the list bellow: \n1. {1} \n2. {2} \n3. {3} \n4. {4} \n5. {5} \n0. {0}"
      .format(option[0], option[1], option[2], option[3], option[4], option[5]))

while True:
    opt = int(input("Enter your option: "))
    if 0 < opt <= 5:
        print("You have selected the option to {} from the list".format(option[opt]))
    elif option == 0:
        break
    else:
        print(option)




