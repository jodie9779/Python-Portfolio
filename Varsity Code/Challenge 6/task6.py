# Things to think about - axis not in list, same presents go to same place,

def store_items(axis, storageInstructions, getItem):
    import re
    axis_list = list()
    for character in axis:
        if character in axis_list:
            continue
        else:
            axis_list.append(character)
    present_locations = dict()  # key = letter, value = location
    present_amount = dict()  # key = letter, value = amount
    for item in storageInstructions:
        first, second = item.split(':')
        if first[0].isnumeric():  # Finding presents
            present_list = re.findall('([0-9]+[A-Za-z]+)', first)
            instructions = re.findall('([A-Za-z]+[-0-9]*)', second)
            location = dict()  # Key = axis letter, value = location
            for instruction in instructions:
                axis_letter = re.findall('([a-zA-Z]+)', instruction)[0]
                movement = re.findall('[-0-9]+', instruction)
                if len(movement) == 0:
                    movement_amount = 1
                else:
                    movement_amount = int(movement[0])
                if axis_letter in location:
                    number = location[axis_letter]
                    number += movement_amount
                    location[axis_letter] = number
                else:
                    location[axis_letter] = movement_amount
            this_warehouse = True
            for item in location.keys():
                if item not in axis_list:
                    this_warehouse = False
            if this_warehouse is False:
                continue
            for present in present_list:
                amount = re.findall('([0-9]+)', present)[0]
                present_letter = re.findall('([A-Za-z]+)', present)[0]
                if int(amount) < 1:
                    continue
                elif present_letter in present_locations:
                    current_value = present_amount[present_letter]
                    new_value = int(current_value) + int(amount)
                    present_amount[present_letter] = new_value
                else:
                    present_amount[present_letter] = int(amount)
                    this_location = ''
                    for key, value in location.items():
                        this_location += key + str(value)
                    present_locations[present_letter] = this_location
        else:
            items_to_move_location = first
            movement_location = dict()
            # Getting Starting location
            initial_location = re.findall('([a-zA-Z]+[0-9]+)',items_to_move_location)
            for item in initial_location:
                initial_axis = re.findall('([a-zA-Z]+)', item)[0]
                initial_amount = re.findall('([-0-9]+)', item)[0]
                if initial_axis in movement_location:
                    number = int(movement_location[initial_axis])
                    number += int(initial_amount)
                    movement_location[initial_axis] = number
                else:
                    movement_location[initial_axis] = int(initial_amount)
            # Getting final location
            movement_instructions = re.findall('([A-Za-z]+[-0-9]+)', second)
            for item in movement_instructions:
                axis_to_move = re.findall('([a-zA-Z]+)', item)[0]
                amount_to_move = re.findall('([-0-9]+)', item)[0]
                if axis_to_move in movement_location:
                    number = int(movement_location[axis_to_move])
                    number += int(amount_to_move)
                    movement_location[axis_to_move] = number
                else:
                    movement_location[axis_to_move] = int(amount_to_move)
            # Getting string for final location
            final_location = ''
            for key, value in movement_location.items():
                final_location = final_location + str(key) + str(value)
            for item in present_locations:
                this_item_to_move = True
                location_axis = re.findall('([A-Za-z]*[-0-9]*)', present_locations[item])
                for location_value in initial_location:
                    if location_value not in location_axis:
                        this_item_to_move = False
                if this_item_to_move is True:
                    present_locations[item] = final_location
    # Getting the return items
    get_item_instructions = re.findall('([A-Za-z]+[-0-9]+)', getItem)
    which_item_letters = list()
    for item in present_locations:
        this_item = True
        for location in get_item_instructions:
            if location in present_locations[item]:
                continue
            else:
                this_item = False
        if this_item is True:
            amount_of_item = str(present_amount[item])
            letter_and_amount = amount_of_item + item
            which_item_letters.append(letter_and_amount)
    sorted_list = sorted(which_item_letters)
    return_string = ''.join(sorted_list)
    print(return_string)




store_items("X", [ "3A2B:X10Y2", "3D:X10", "3C:X-5X15" ], "X10")


