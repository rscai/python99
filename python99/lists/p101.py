## find the last element of a list
def find_last_one(list):
    if len(list) == 0:
        return None
    return list[len(list)-1]