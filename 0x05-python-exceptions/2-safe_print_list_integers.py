#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            try:
                print("{:d}".format(item), end="")
                count += 1
            except (ValueError, TypeError):
                pass
            if count == x:
                break
    except IndexError:
        pass
    finally:
        print()
        return (count)
