import sys

sys.argv

input_file = open(sys.argv[1])

print(input_file.readline(), "This is Dear")