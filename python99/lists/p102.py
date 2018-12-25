## find the last but one element of a list

def find_last_but_one(list):
    if len(list) < 2:
        return None
    return list[len(list)-2]


def find_last_but_one_recursive(l):
    first = l[0]
    second = l[1]
    remain = l[2:]
    if remain == []:
        return first
    return find_last_but_one_recursive([second]+remain)