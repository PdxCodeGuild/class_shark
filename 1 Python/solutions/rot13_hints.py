# hints for lab 13

# approach 1: translate

# 1.1 using lists
eng = ['one', 'two', 'three']
span = ['uno', 'dos', 'tres']

for i in range(len(eng)):
    print(f'{eng[i]} in spanish is {span[i]}')

# 1.2 using dict
translate = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
for num in translate:
    print(f'{num} in spanish is {translate[num]}')


# approach 2: work with indexes
nums = list(range(1,11)) # list of nums 1 - 10

for i in range(20):
    # print(nums[i]) # IndexError when we get out of bounds
    index = i % len(nums) # wrap back to beginning when we reach the end of nums
    print(nums[index])


# approach 3: working with ascii values
# get ascii values using ord()
ascii_a = ord('a')
ascii_cap_a = ord('A')

# turn ascii values back into characters using chr()
a = chr(ascii_a)
cap_a = chr(ascii_cap_a)

print(f'{a} in ascii is {ascii_a}')
print(f'{cap_a} in ascii is {ascii_cap_a}')

