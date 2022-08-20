def wallpaper():
    all_items = []

    # extract all wallpaper items, since Wendell only gives out wallpaper
    try:
        fp1 = open("wallpaper-formatted.txt", "r")
        fpArray = [fp1]

        for fp in fpArray:
            items = fp.readlines()

            items = [x.strip('\n') for x in items]
            all_items.extend(items)
            fp.close()

    except IOError as e:
        print("Error: ", file=stderr)
        print(e.msg, file=stderr)
    return all_items

def wendell():
    all_items = []

    # extract all wallpaper items, since Wendell only gives out wallpaper
    try:
        fp1 = open("wendell-items.txt", "r")
        fpArray = [fp1]

        for fp in fpArray:
            items = fp.readlines()
            
            items = [x.strip('\n') for x in items]
            all_items.extend(items)
            fp.close()

    except IOError as e:
        print("Error: ", file=stderr)
        print(e.msg, file=stderr) 

    return all_items

    wendell_items = []
    for item in all_items:
        if item.find("-(W)") != -1: # search for the "-(W)" string. all wendell's items have that. 
            wendell_items.append(item)
    return wendell_items()
if __name__ == "__main__":
    print(''.join(map(str,wendell())))