## find the last element of a list
def find_last_one(list):
    if len(list) == 0:
        return None
    return list[len(list)-1]

def find_last_one_recursive(list):
    first = list[0]
    remain = list[1:]
    if remain == []:
        return first
    return find_last_one_recursive(remain)