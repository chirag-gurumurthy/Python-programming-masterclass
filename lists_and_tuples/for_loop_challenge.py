numbers = input("Please enter three integers: ")
my_list = numbers.split(",")
# my_list = int(numbers)
for index in range(len(my_list)):
    my_list[index] = int(my_list[index])

magical_adder = my_list[0] + my_list[1] - my_list[2]

print(magical_adder)



