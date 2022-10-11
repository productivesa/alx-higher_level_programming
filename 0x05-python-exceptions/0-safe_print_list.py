#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    lister = 0
    for x in range(y):
        try:
            print("{}".format(my_list[x]), end='')
        except Exception:
            break
        else:
            lister = lister + 1
    print()
    return (lister)
