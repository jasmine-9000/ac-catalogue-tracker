all_items = []

# extract all furniture pieces, since Redd only sells furniture
try:
    fp1 = open("carpet_1.txt", "r")
    fpArray = [fp1]

    for fp in fpArray:
        items = fp.readlines()
        all_items.extend(items)
        fp.close()

except IOError as e:
    print("Error: ", file=stderr)
    print(e.msg, file=stderr) 

redd_items = []
for item in all_items:
    if item.find("-(S)") != -1: # search for the "-(S)" string. all sahara's items have that. 
        redd_items.append(item)
print(''.join(map(str,redd_items)))