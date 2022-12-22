#Write a function implementing a Linear Search Algorithm. A linear seach is a method for finding an element within a list. 
#It sequentially checks each element of the list until a match is found or the whole list has been searched. If you do not find a match, return -1

# Search. 



def linear_search(a_list, target):

    for i in range(len(a_list)):
        if a_list[i] == target:
            return (f"{target} is in list")
    return -1


nums_list = [10,23,45,70,11,15]
linear_search(nums_list, 70)
x = linear_search(nums_list, 70)
print(x)

    #index begins at 0, and adds 1 after each evaluation
    # focus = [0]
    
    # i = 0
        # != target:

    # for num in a_list:
    #     if focus != target:
    #         focus += [1]
    # print(focus)

    # for x in a_list:
    #     if focus == target:
    #         print("match")
    #         return "match"
    #     if focus != target:
    #         focus += 1