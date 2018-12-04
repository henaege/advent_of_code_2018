# "Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.
# #
# # Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).
# #
# # To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.
# #
# # For example, if you see the following box IDs:
# #
# # abcdef contains no letters that appear exactly two or three times.
# # bababc contains two a and three b, so it counts for both.
# # abbcde contains two b, but no letter appears exactly three times.
# # abcccd contains three c, but no letter appears exactly two times.
# # aabcdd contains two a and two d, but it only counts once.
# # abcdee contains two e.
# # ababab contains three a and three b, but it only counts once.
# # Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.
# #
# # What is the checksum for your list of box IDs?


box_id_set = set(line.strip() for line in open('input2.txt'))
input_file = open('input2.txt')

box_id_list = input_file.readlines()

input_file.close()

print(box_id_set)
print(box_id_list)

print len(box_id_list)

ids_with_2 = 0
ids_with_3 = 0
ids_with_both = 0

for entry in box_id_list:
    result2 = {x for x in entry if entry.count(x) == 2}
    if len(result2) > 0:
        ids_with_2 += 1

print(ids_with_2)


for entry in box_id_list:
    result3 = {x for x in entry if entry.count(x) == 3}
    if len(result3) > 0:
        ids_with_3 += 1


print(ids_with_3)

for entry in box_id_list:
    results_with2 = {x for x in entry if entry.count(x) == 2}
    results_with3 = {x for x in entry if entry.count(x) == 3}
    if len(results_with2) > 0 and len(results_with3) > 0:
        ids_with_both += 1

# ids_with_2 += ids_with_both
# ids_with_3 += ids_with_both

print("IDs with 2: {}".format(ids_with_2))
print("IDs with 3: {}".format(ids_with_3))
print("IDs with both: {}".format(ids_with_both))

checksum = ids_with_2 * ids_with_3

print("Checksum: {}".format(checksum))
