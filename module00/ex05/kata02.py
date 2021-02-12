if __name__ == '__main__':
    time = (3, 30, 2019, 9, 25)


    # print("{:02}/{:02}/{:04} {:02}:{:02}".format(
    #     time[3], time[4], time[2], time[0], time[1]
    # ))

    
    print("{3:02}/{4:02}/{2:04} {0:02}:{1:02}".format(*time))