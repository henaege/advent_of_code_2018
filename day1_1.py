
nums = open('input.txt')
# input_list = nums.split()

num_list = nums.readlines()

print(num_list)

input_sum = map(int, num_list)

total = sum(input_sum)

print total



