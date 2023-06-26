#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count == x:
                break
            print(item, end=" ")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
