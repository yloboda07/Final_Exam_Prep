

print("Enter integers:")
all_inputs = []
user_input = input("  ? ")
if user_input != "":
    all_inputs.append(int(user_input))
    while user_input != "":
        user_input = input("  ? ")
        if user_input != "":
            all_inputs.append(int(user_input))

odd_values = []
even_values = []
for number in all_inputs:
    if number % 2 == 1:
        odd_values.append(number)
    else:
        even_values.append(number) 

if len(odd_values) > 0:
    odd_avg = sum(odd_values)/len(odd_values)
    print(f"The average of the odd numbers is {round(odd_avg,2)}")
    # print(f"The average of the odd numbers is {odd_avg:.2f}")


if len(even_values) > 0:
    even_avg = sum(even_values)/len(even_values)
    print(f"The average of the even numbers is {round(even_avg,2)}")
    # print(f"The average of the even numbers is {even_avg:.2f}")

### Jed's solution

# odds = [] 
# evens = [] 
# finished = False 
# print("Enter integers:") 
# while not finished: 
#     num_str = input(" ? ") 
#     if num_str == "": 
#         finished = True 
#     else: 
#         num = int(num_str) 
#         if num % 2 == 0: 
#             evens.append(num) 
#         else: odds.append(num)
# odd_avg = sum(odds)/len(odds) 
# even_avg = sum(evens)/len(evens) 
# print(f"The average of the odd numbers is {odd_avg:.2f}") 
# print(f"The average of the even numbers is {even_avg:.2f}")