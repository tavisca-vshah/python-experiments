lists = [1,2,4,4,5,6,7,8,9,2,3,5,2,5,4,4,5,0]

# most_common_items = max(set(lists),key=lists.count)

# print(most_common_items)

def max_items(items,func):
    counter  = 0
    max_value = None
    # for i in items:
    #     test = func(i)
    #     if counter < test:
    #         counter = test
    #         max_value = i

    
    print(max_value)

max_items(set(lists),lists.count)