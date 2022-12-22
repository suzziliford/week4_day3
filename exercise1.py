#Reverse the list below in-place using an in-place algorithm. For extra credit: Reverse the strings at the same time.

words = ['this', 'is', 'a', 'sentence', '.']

# list1 = [1,2,3,4,5]

# def swap (a_list, index_a, index_b):
#     a_list [index_a] = a_list [index_b]
#     a_list[index_b] = a_list[index_a]

# print(list1)
# swap(list1, 0, 4)
# print(list1)

def reverse_list(a_list, idx_1, idx_2, idx_4, idx_5):
    temp = a_list[idx_1]
    a_list[idx_1] = a_list[idx_5]
    a_list[idx_5] = temp
    temp2 = a_list[idx_2]
    a_list[idx_2] = a_list[idx_4]
    a_list[idx_4] = temp2

    # for word in a_list:
    #     word = word[::1]

reverse_list(words, 0, 1, 3, 4,)

print (words)

