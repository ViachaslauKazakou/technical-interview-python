mylist = (i for i in range(20))
print(mylist)
iter_list = iter(mylist)
print(iter_list)
print(next(iter_list))
print(next(mylist))
print(next(iter_list))
print(mylist is iter_list)
print(dir(mylist))

list1 = [i for i in range(1,11)]
print(list1)
list2 = reversed(list1)
print(list2)
for i in list2:
    print(i)

print(list1[::-1])
