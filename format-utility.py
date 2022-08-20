"""
    This module formats the things the developer finds on gamefaqs.com.
    No arguments whatsoever formats things from utility_holdables.txt and spits it out to holdables.txt
"""

from utils import div, format_line
import sys, getopt

infile = "utility_holdables.txt"
outfile = "holdables.txt"
commandlineoutput = False
debug = False

# parse arguments. 
# -c and --commandline spits out the results to the commandline
# -i and --infile specifies the input file. no 
try:
    opts, args = getopt.getopt(sys.argv[1:], "ci:o:", ["commandline", "infile=", "outfile="])
except getopt.GetoptError as e:
    print("format-utility.py -i <inputfile> -o <outputfile>")
    sys.stderr.write("%s\n" % e.msg)
    sys.exit(2)
for opt, arg in opts:
    if opt in ( '-i', "--infile"):
        infile = arg 
    elif opt in ('-o', "--outfile"):
        outfile = arg
    elif opt in ('-c', "--commandline"):
        commandlineoutput = True


if debug:
    sample_line = "[] Gelato Umbrella          [] Paper Parasol                [] Green Pinwheel   [] Fucking pinwheel"
    print(format_line(sample_line))
    #sys.exit(0)


#read in file, and convert the list.
result = []
with open(infile, "r") as fp:
    lines = fp.readlines()
    #div()
    for line in lines:
        result.append(format_line(line))


# column first approach
with open(outfile, "w+") as fp:
    for i in range(len(result[0])):
        for lst in result:
            if not i > len(lst):
                #print(lst)
                #print(i, len(lst))
                fp.write(lst[i-1] + "\n")


# row first approach
#open new file, spit out results.
x  =""""
with open(outfile, "w+") as fp:
    for lst in result:
        for item in lst:
            fp.write(item + "\n")
"""
# if user specified commandline output, put it on commandline.
if commandlineoutput:
    with open(outfile, "r+") as fp:
        print(''.join(map(str, fp.readlines()))) 