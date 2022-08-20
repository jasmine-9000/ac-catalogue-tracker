def lottery():
    all_items = []

    # extract all furniture pieces, since lottery prizes are only furniture
    try:
        fp1 = open("furniture_sets/sets1.txt", "r")
        fp2 = open("furniture_sets/sets2.txt", "r")
        fp3 = open("furniture_sets/sets3.txt", "r")
        fp4 = open("furniture_sets/sets4.txt", "r")
        fp5 = open("furniture_sets/sets5.txt", "r")
        fpArray = (fp1, fp2, fp3, fp4, fp5)

        for fp in fpArray:
            items = fp.readlines()
            all_items.extend(items)
            fp.close()

    except IOError as e:
        print("Error: ", file=stderr)
        print(e.msg, file=stderr) 

    lottery_items = []
    for item in all_items:
        if item.find("-(L)") != -1: # search for the "-(L)" string. all the lottery items have that. 
            lottery_items.append(item)
    return lottery_items
if __name__ == "__main__":
    print(''.join(map(str,lottery())))