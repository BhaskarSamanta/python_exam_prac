import sys


# my_list = sys.argv
# o = my_list[0]
# n = my_list[1]
# m = my_list[2]
script_name, input_file, output_file = sys.argv

# count=0

with open(input_file,'r') as first, open(output_file,'w') as second:
    for count, line in enumerate(first, start=1):
        second.write(f"{count} {line.strip()} {len(line)}\n")

    print("the txt files are copied")

    print('name of the file current',script_name)

    print ('the total number in the first txt file is',count)
