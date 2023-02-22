#from utils import *

from sys import displayhook


def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    placeholder = '123456789'
    filled_boxes = dict(zip(boxes, grid))
    
    for box in filled_boxes:
        if filled_boxes[box] == '.':
            filled_boxes[box] = placeholder
            

            
    result = filled_boxes # code here
            
    return result

# Ucomment and run the code below to view your result.
# Make sure to **comment** the code below before submitting your code.

#grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
#output = grid_values(grid)
#displayhook(output)



def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    # code here
    columns = 'ABCDEFGHI'
    
    for box in values:
        if len(values[box]) == 1:
            
#defining what the peers of the box with the single digit is, but only inside the 3x3
            column = box[:1]
            row = box[1:]
            row = int(row)

            position = columns.index(column)
#defining what the peer columns are inside the 3x3
            if(position%3 == 0):
                peer_column1 = columns[position + 1: position + 2]
                peer_column2 = columns[position + 2: position + 3]
                
            if(position%3 == 1):
                peer_column1 = columns[position - 1: position]
                peer_column2 = columns[position + 1: position +2]
            
            if(position%3 == 2):
                peer_column1 = columns[position - 1: position]
                peer_column2 = columns[position - 2 : position -1]
#defining what the peer rows are inside the 3x3
            if(row%3 == 1):
                peer_row1 = row + 1
                peer_row2 = row + 2
            
            if(row%3 == 2):
                peer_row1 = row - 1
                peer_row2 = row + 2
            
            if(row%3 == 3):
                peer_row1 = row - 1
                peer_row2 = row - 2
            
            peers_in_3x3 = [
                f"{peer_column1}{peer_row1}",
                f"{peer_column1}{peer_row2}",
                f"{peer_column2}{peer_row1}",
                f"{peer_column2}{peer_row2}"
            ]

            for key in values:
                
                if (column in box) ^ (str(row) in box):
                    values[key].replace(values[box], '')
                    
                if(key in peers_in_3x3):
                    values[key].replace(values[box], '')
            
    return values

# Ucomment and run the code below to view your result.
# Make sure to **comment** the code below before submitting your code.
# from copy import deepcopy

#grid = {'A1': '123456789', 'A2': '123456789', 'A3': '3', 'A4': '123456789', 'A5': '2', 'A6': '123456789', 'A7': '6', 'A8': '123456789', 'A9': '123456789', 'B1': '9', 'B2': '123456789', 'B3': '123456789', 'B4': '3', 'B5': '123456789', 'B6': '5', 'B7': '123456789', 'B8': '123456789', 'B9': '1', 'C1': '123456789', 'C2': '123456789', 'C3': '1', 'C4': '8', 'C5': '123456789', 'C6': '6', 'C7': '4', 'C8': '123456789', 'C9': '123456789', 'D1': '123456789', 'D2': '123456789', 'D3': '8', 'D4': '1', 'D5': '123456789', 'D6': '2', 'D7': '9', 'D8': '123456789', 'D9': '123456789', 'E1': '7', 'E2': '123456789', 'E3': '123456789', 'E4': '123456789', 'E5': '123456789', 'E6': '123456789', 'E7': '123456789', 'E8': '123456789', 'E9': '8', 'F1': '123456789', 'F2': '123456789', 'F3': '6', 'F4': '7', 'F5': '123456789', 'F6': '8', 'F7': '2', 'F8': '123456789', 'F9': '123456789', 'G1': '123456789', 'G2': '123456789', 'G3': '2', 'G4': '6', 'G5': '123456789', 'G6': '9', 'G7': '5', 'G8': '123456789', 'G9': '123456789', 'H1': '8', 'H2': '123456789', 'H3': '123456789', 'H4': '2', 'H5': '123456789', 'H6': '3', 'H7': '123456789', 'H8': '123456789', 'H9': '9', 'I1': '123456789', 'I2': '123456789', 'I3': '5', 'I4': '123456789', 'I5': '1', 'I6': '123456789', 'I7': '3', 'I8': '123456789', 'I9': '123456789'}
#trial = eliminate(deepcopy(grid))
#for i in trial:
#    trial[i] = ''.join(sorted(trial[i]))


def search(values):
    '''
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    '''
    # First, reduce the puzzle using the previous function
    completed = False
    previous_results = []
    i = 0
    item_with_min = 'A1'
    
    while completed == False:
        
        values = eliminate(values)
        values = only_choice(values)
        
        resulting_puzzle = len([value for value in values if len(values[value]) == 1])
        previous_results.append(resulting_puzzle)
        i += 1
        
        if resulting_puzzle == len(values):
            completed = True
            return values
            
        
        if len(previous_results) > 1 and previous_results[i] == previous_results[i-1]:
            return False
        

        for item in values:
                
            if len(values[item]) <= len(values[item_with_min]):
                    item_with_min = item
                    
        for digit in values[item_with_min]: 
                
            values_copy = values.copy()
            values_copy[item_with_min] = digit
            result = search(values_copy)
            
            if result:
                return result
            
    return False



def main():

    grid = {'A1': '123456789', 'A2': '123456789', 'A3': '3', 'A4': '123456789', 'A5': '2', 'A6': '123456789', 'A7': '6', 'A8': '123456789', 'A9': '123456789', 'B1': '9', 'B2': '123456789', 'B3': '123456789', 'B4': '3', 'B5': '123456789', 'B6': '5', 'B7': '123456789', 'B8': '123456789', 'B9': '1', 'C1': '123456789', 'C2': '123456789', 'C3': '1', 'C4': '8', 'C5': '123456789', 'C6': '6', 'C7': '4', 'C8': '123456789', 'C9': '123456789', 'D1': '123456789', 'D2': '123456789', 'D3': '8', 'D4': '1', 'D5': '123456789', 'D6': '2', 'D7': '9', 'D8': '123456789', 'D9': '123456789', 'E1': '7', 'E2': '123456789', 'E3': '123456789', 'E4': '123456789', 'E5': '123456789', 'E6': '123456789', 'E7': '123456789', 'E8': '123456789', 'E9': '8', 'F1': '123456789', 'F2': '123456789', 'F3': '6', 'F4': '7', 'F5': '123456789', 'F6': '8', 'F7': '2', 'F8': '123456789', 'F9': '123456789', 'G1': '123456789', 'G2': '123456789', 'G3': '2', 'G4': '6', 'G5': '123456789', 'G6': '9', 'G7': '5', 'G8': '123456789', 'G9': '123456789', 'H1': '8', 'H2': '123456789', 'H3': '123456789', 'H4': '2', 'H5': '123456789', 'H6': '3', 'H7': '123456789', 'H8': '123456789', 'H9': '9', 'I1': '123456789', 'I2': '123456789', 'I3': '5', 'I4': '123456789', 'I5': '1', 'I6': '123456789', 'I7': '3', 'I8': '123456789', 'I9': '123456789'}
    eliminate(grid)
    print(grid['A2'])
    print("Hello")
    
    if __name__ == "__main__":
        main()