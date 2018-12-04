from sets import Set
nums = open('input.txt')

num_list = nums.readlines()

nums.close()

print(num_list)

input_sum1 = map(int, num_list)
input_sum2 = map(int, num_list)



# total = sum(input_sum)
total1 = 0
total1_list = []
duplicate = False

for i in input_sum1:
    total1 += i
    total1_list.append(total1)

total_set1 = set(total1_list)

while not duplicate:
    for j in input_sum1:
        total1 += j
        if total1 in total_set1 :
                print("Found {} twice!".format(total1))
                duplicate = True
    # total2_list.append(total1)

# for i in total1_list:
#     for j in total2_list:
#         if j == i:
#             print("Found {} twice!".format(i))
