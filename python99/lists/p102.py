## find the last but one element of a list

def find_last_but_one(list):
    if len(list) < 2:
        return None
    return list[len(list)-2]