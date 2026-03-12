#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divs = []
    for i in range(list_length):
        try:
            divs.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            divs.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            divs.append(0)
            continue
        except IndexError:
            print("out of range")
            divs.append(0)
            continue
        finally:
            pass
    return divs
