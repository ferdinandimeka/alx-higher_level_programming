#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)
    new_list = my_list.copy()
    indexof = new_list[idx]
    new_list.remove(indexof)
    new_list.insert(idx, element)
    return (new_list)
