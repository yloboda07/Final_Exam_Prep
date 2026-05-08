import json

def process_file(filename):
    diff_sum = 0
    with open (filename) as fn:
        for line in fn:
            first = find_first(line) 
            last = find_last(line) 
            diff = first- last 
            diff_sum += diff 
    return diff_sum

def find_first(line): 
    """Finds the first number to occur on a line.""" 
    number = "" 
    i = 0 
    while not line[i].isdigit(): #find where num starts 
        i += 1 
    while line[i].isdigit(): #read num 
        number += line[i] 
        i += 1 
    return int(number)

def find_last(line):
    number = "" 
    i = len(line)- 1 
    while not line[i].isdigit():
        i-= 1 
    while line[i].isdigit():
        number = line[i] + number 
        i-= 1 
    return int(number)
    
process_file("data.txt")
