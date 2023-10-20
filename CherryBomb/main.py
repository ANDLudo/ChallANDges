import re
import random

def method_1(file, target):
    return re.findall(target,open(file, 'r').read())

def bogo_search(file, target):
    data = open(file, 'r').read()
    target_len = len(target)
    bogo_max = len(data) - target_len
    attempts = 0
    while True:
        attempts +=1
        bogo = random.randint(0, bogo_max)
        if data[bogo: bogo + target_len] == target:
            return bogo, data[bogo: bogo + target_len], attempts

def edge_detection(file):
    data = open(file, 'r').read()

    data = data.split('\n')
    
    def zero_func(num):
        return 0
    
    def letter_maximum_curve_func_func(letter):
        target = ord(letter)
        def func(num):
            num = ord(num)
            distance = min(abs(target - num), abs(128-(128-127)) % 128)# wrap around distance

            return (128.0-distance)/128
        return func
    mask = [[zero_func,zero_func,zero_func,zero_func,zero_func,zero_func],
            [letter_maximum_curve_func_func("C"),letter_maximum_curve_func_func("H"),letter_maximum_curve_func_func("E"),letter_maximum_curve_func_func("R"),letter_maximum_curve_func_func("R"),letter_maximum_curve_func_func("Y"),],
            [zero_func,zero_func,zero_func,zero_func,zero_func,zero_func]]
    mask_x = len(mask[0])
    mask_y = len(mask)
    data_output = []
    score_output = ""
    def apply_mask(block, mask):
        '''
        block x == mask x
        block y == mask y
        '''
        output = 0
        for b_row,m_row in zip(block, mask):
            for b, m_func in zip(b_row,m_row):
                output += m_func(b)
        return output
    for row in range(len(data)):
        for cell in range(len(data[0])):
            cell_upper = min(cell + int(mask_x/2), len(data[0]))
            cell_lower = max(cell - int(mask_x/2), 0)
            right_padding = min(cell + int(mask_x/2) - len(data[0]), 0) 
            left_padding = abs(min(cell - int(mask_x/2), 0))
            if row == 0:
                row_1 = "\0"*mask_x
            else:
                row_1 = ("\0"* left_padding) + data[row-1][cell_lower : cell_upper] + ("\0" * right_padding)
            row_2 = ("\0" * left_padding) + data[row][cell_lower : cell_upper] + ("\0" * right_padding)
            if row == len(data)-1:
                row_3 = "\0"*mask_x
            else:
                row_3 = ("\0" * left_padding) + data[row+1][cell_lower : cell_upper] + ("\0" * right_padding)
            
            score = apply_mask([
                row_1,row_2,row_3
            ], mask)
            if score >=6 :
                data_output.append(f"Row: {row}, Col: {cell}" )
            def score_to_color(s):
                if s >=6:
                    return "🍒"
                elif s >= 5.5: 
                    return "🟥"
                elif s >= 5:
                    return "🟧"
                elif s >=4:
                    return "🟨"
                else:    
                    return "⬛️"
                

            score_output += score_to_color(score)
        score_output += "\n"   
    return (score_output,data_output)
     

def get_cherry_chars():
    return set(open('cherry.txt','r').read())

def get_cherry_file_size():
    return len(open('cherry.txt','r').read())


class NeuralNetwork:
    matrix= []
    def __init__(self,input_size, output_size,internal_layer_sizes):
        self.matrix.append([0]*input_size)
        for l in internal_layer_sizes:
            self.matrix.append([0]*l)
        self.matrix.append(output_size  * [0])

def run_ai():
    alphabet = list(get_cherry_chars())
    gen_size = get_cherry_file_size()
    # testing
    tests = 1000
    for i in range(tests):
        cherry_file = cherry_file_generator(alphabet,gen_size)

def cherry_file_generator(alphabet,gen_size)->str:
    new_file = ''.join([alphabet[random.randint(0,len(alphabet)-1)] for _ in range(gen_size)])
    splice_loc = random.randint(0,gen_size-7)
    return new_file[0:splice_loc] + 'CHERRY' + new_file[splice_loc:-6]
from time import time
print("Method 1: REGEX")
t = time()
print(method_1('cherry.txt','CHERRY'))
print(f"Took {1000*(time() - t)}ms")

input("Next")
print("Method 2: Bogo Search (my own invention)")
t = time()

location, string, attempts = bogo_search('cherry.txt','CHERRY')
print(f"Found {string} at charindex {location}. Took {attempts} attempts")
print(f"Took {1000*(time() - t)}ms")


input("Next")
print("Method3: Edge detection")
t = time()
picture, locations = edge_detection('cherry.txt')
print(picture)
print(locations)
print(f"Took {1000*(time() - t)}ms")

input("Next")

print("Method 4: Word")
print("See file att")

input("Next")
print("Method 5: ")