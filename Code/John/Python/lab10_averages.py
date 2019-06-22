# lab10_averages.py

# nums = [1.0, 2.0, 3.0, 4.0]
total = 0.0
averaging = True
nums = []
while averaging:
    user_input = (input("\n" + "Enter a number, or 'done' to receive your average: "))
    if user_input == 'done':
        averaging = False
    else:
        try:
            user_input = float(user_input)
            nums.append(user_input)
        except ValueError:
            print("\n" + "Invalid input")
for i in range(len(nums)):
    total += nums[i]

if total == 0:
    print("\n" + "Thanks for coming, goodbye!!")
else:
    average = total / len(nums)
    print(f"\n{average}")
