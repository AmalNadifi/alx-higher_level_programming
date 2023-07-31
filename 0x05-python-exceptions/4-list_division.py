#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    tmp = 0
    for itr in range(0, list_length):
        try:
            tmp = my_list_1[itr] / my_list_2[itr]
        except TypeError:
            tmp = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp = 0
            print("division by 0")
        except IndexError:
            tmp = 0
            print("out of range")
        finally:
            pass
        res.append(tmp)
    return(res)

