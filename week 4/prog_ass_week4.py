# We have a list of annual rainfall recordings of cities. Each element in the list is of the form (c,r) where c is the city and r is the annual rainfall for a particular year. The list may have multiple entries for the same city, corresponding to rainfall recordings in different years.

# Write a Python function rainaverage(l) that takes as input a list of rainfall recordings and computes the avarage rainfall for each city. The output should be a list of pairs (c,ar) where c is the city and ar is the average rainfall for this city among the recordings in the input list. Note that ar should be of type float. The output should be sorted in dictionary order with respect to the city name.

# Here are some examples to show how rainaverage(l) should work.

# >>> rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
# [(1, 2.0), (2, 3.0), (3, 8.0)]

# >>> rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])
# [('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]
# A list in Python can contain nested lists. The degree of nesting need not be uniform. For instance [1,2,[3,4,[5,6]]] is a valid Python list. Write a Python function flatten(l) that takes a nonempty list of lists and returns a simple list of all the elements in the nested lists, flattened out. You can make use of the following function that returns True if its input is of type list.

# def listtype(l):
#   return(type(l) == type([]))
# Here are some examples to show how flatten(l) should work.

# >>> flatten([1,2,[3],[4,[5,6]]])
# [1, 2, 3, 4, 5, 6]

# >>> flatten([1,2,3,(4,5,6)])
# [1, 2, 3, (4, 5, 6)]

def rainaverage(l):
    sum = dict()
    count = dict()
    for (k, v) in l:
        sum[k] = sum.get(k, 0) + v
        count[k] = count.get(k, 0) + 1
    for k in sum:
        sum[k] /= count[k]
    return sorted(list(sum.items()))
def flatten(l):
    flat_list = []
    for item in l:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    #sum(l,flattened_list)
    return flat_list