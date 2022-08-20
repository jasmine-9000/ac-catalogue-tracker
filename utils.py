import sys

def div():
    print("----------------------------------------------------")
def format_line(sample_line: str):    
    item = ""
    sample_list = []
    f1 = False
    reading = False
    # read in the string 1 byte at a time. if the string "[]" comes up, read in the item until the next "[]" comes up. 
    for c in sample_line:
        if c == '[':
            reading = False
            f1 = True
        elif f1 and c == ']':
            sample_list.append(item)
            item = ""
            reading = False
            f1 = False
        else:
            reading = True
            f1 = False

        if reading:
            item += c
    # add last item
    if item != "":
        sample_list.append(item)
    # remove dummy item
    sample_list.pop(0)
    #print(sample_list)
    c = []
    for s in sample_list:
        #print(s.strip(" "))
        c.append(s.strip(" \t\n"))
    return c
def versioncheck():
    #python version check.
    cont = True
    if sys.version_info < (3,0,0):
        sys.stderr.write("You must have Python 3 to run this scrypt")
        return False
    elif sys.version_info < (3,2,0):
        c = input("Python 3.2 is recommended for this script. Continue?(y/n)")
        if c == 'y': 
            cont = True
        elif c == 'n':
            cont = False
    return cont

