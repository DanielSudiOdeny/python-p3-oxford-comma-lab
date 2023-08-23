def oxford_comma(items):
    if (len(items) == 1):
        return ''.join(items)
    elif (len(items)) == 2:
        return ' and '.join(items)
    elif (len(items) == 3):
        comma_seperated = ', '.join(items[:-1])
        return f"{comma_seperated}, and {items[-1]}"
    elif (len(items) > 3):
        comma_seperated = ', '.join(items[:-1])
        return f"{comma_seperated}, and {items[-1]}"


print(oxford_comma(["Hello", "kiwi", "starfruid"]))
