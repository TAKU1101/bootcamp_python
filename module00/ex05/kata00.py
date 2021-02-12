if __name__ == '__main__':
    t = (19, 42, 21)

    t_list = [str(e) for e in t]
    print("The {} number are: {}".format(len(t), ", ".join(t_list)))
#    for i, val in enumerate(t):
#        if i < 3:
#            print(val, end="")
#        if i < 2:
#            print(", ", end="")