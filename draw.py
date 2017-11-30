import shutil
from math import ceil
import random
from enum import Enum

term_width = shutil.get_terminal_size().columns

LEFT_END = '<'
RIGHT_END = '>'
BASE_CHAR = '#'
FILLER_CHARS = []
SIZE_RANGE = (8, 50)

'''  v
    >X<
     A
    <#>
  <#####>
 <#######>
  <#####>  
 <#######>
<#########>
    ###
    ###
    ###     '''

def initialize_fillers():
    for _ in range(0, 10):
        FILLER_CHARS.append('#')
    FILLER_CHARS.extend(['@', '$', '*', '&'])

def print_centered(text):
    startIndex = int(ceil(term_width / 2 - ceil(len(text) / 2)))
    for _ in range(0, startIndex):
        print(" ", end='')
    print(text)

def print_star():
    print_centered('v')
    print_centered(LEFT_END + 'X' + RIGHT_END)
    print_centered('A')    

def print_base(height, width):
    base_string = ""
    for _ in range(0, width):
        base_string += '#'
    for _ in range(0, height):
        print_centered(base_string)

def print_tree(tree_height, base_height):
    max_area_width = tree_height
    max_height = tree_height - 3 - base_height
    current_total_height = 0
    isFirstArea = True
    area_length = tree_height / 3
    previous_row_width = 0

    while current_total_height < max_height:
        current_area_length = 0
        current_width = int(ceil(previous_row_width / 2))
        
        if current_width % 2 == 0:
            current_width += 1

        if isFirstArea:
            current_width = 3
        while current_width < max_area_width and current_area_length < area_length:
            stringToPrint = LEFT_END 
            fillers_printed = 0
            while fillers_printed < current_width - 2:
                stringToPrint += random.choice(FILLER_CHARS)
                fillers_printed += 1
            stringToPrint += RIGHT_END
            print_centered(stringToPrint)
            current_area_length += 1
            current_total_height += 1
            current_width += 2
            if isFirstArea:
                isFirstArea = False
        previous_row_width = current_width

while True:
    tree_height = 0
    while tree_height < SIZE_RANGE[0] or tree_height > SIZE_RANGE[1]:
        user_input = input("Tree height (" + str(SIZE_RANGE[0]) + "-" + str(SIZE_RANGE[1]) + ") ('q' to quit): ")
        if user_input == 'q':
            exit()
        try:
            tree_height = int(user_input)
        except ValueError:
            print("Please enter a number between 8 and 50!")
    base_height = int(ceil(tree_height / 8))
    base_width = int(ceil(tree_height / 12))
    if base_width % 2 == 0:
        base_width -= 1

    initialize_fillers()
    print_star()
    print_tree(tree_height, base_height)
    print_base(base_height, base_width)