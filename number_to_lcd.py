lcd_numbers = {
    '0': [' {under} ', '{pipe}{space}{pipe}', '{pipe}{under}{pipe}'],
    '1': [' {space} ', ' {space}{pipe}', ' {space}{pipe}'],
    '2': [' {under} ', ' {under}{pipe}', '{pipe}{under} '],
    '3': [' {under} ', ' {under}{pipe}', ' {under}{pipe}'],
    '4': [' {space} ', '{pipe}{under}{pipe}', ' {space}{pipe}'],
    '5': [' {under} ', '{pipe}{under} ', ' {under}{pipe}'],
    '6': [' {under} ', '{pipe}{under} ', '{pipe}{under}{pipe}'],
    '7': [' {under} ', ' {space}{pipe}', ' {space}{pipe}'],
    '8': [' {under} ', '{pipe}{under}{pipe}', '{pipe}{under}{pipe}'],
    '9': [' {under} ', '{pipe}{under}{pipe}', ' {under}{pipe}']
}

auxillary_height = {
    '0': ['{pipe}{space}{pipe}', '{pipe}{space}{pipe}'],
    '1': [' {space}{pipe}', ' {space}{pipe}'],
    '2': [' {space}{pipe}', '{pipe}{space} '],
    '3': [' {space}{pipe}', ' {space}{pipe}'],
    '4': ['{pipe}{space}{pipe}', ' {space}{pipe}'],
    '5': ['{pipe}{space} ', ' {space}{pipe}'],
    '6': ['{pipe}{space} ', '{pipe}{space}{pipe}'],
    '7': [' {space}{pipe}', ' {space}{pipe}'],
    '8': ['{pipe}{space}{pipe}', '{pipe}{space}{pipe}'],
    '9': ['{pipe}{space}{pipe}', ' {space}{pipe}']
}

def get_lcd_string(numbers, width, height):
    under = '_' * width
    space = ' ' * width
    pipe = '|'

    print_string = []

    # Height adjustments
    top_string = ' '.join([lcd_numbers[number][0].format(under=under, space=space, pipe=pipe) for number in numbers])
    for i in range(height):
        upper_height_string = ' '.join([auxillary_height[number][0].format(space=space, pipe=pipe) for number in numbers])
    middle_string = ' '.join([lcd_numbers[number][1].format(under=under, space=space, pipe=pipe) for number in numbers])
    for i in range(height):
        lower_height_string = ' '.join([auxillary_height[number][1].format(space=space, pipe=pipe) for number in numbers])
    bottom_string = ' '.join([lcd_numbers[number][2].format(under=under, space=space, pipe=pipe) for number in numbers])

    print_string.append(top_string)
    print_string.append(upper_height_string)
    print_string.append(middle_string)
    print_string.append(lower_height_string)
    print_string.append(bottom_string)
    return print_string

def print_lcd_number(numbers, width=1, height=1):
    if width < 0 or height < 0:
        print('')

    # Put everything in
    print_string = get_lcd_string(numbers, width, height)
    print('\n'.join(print_string))

for i in range(2):
    print_lcd_number('0123456789', 4, 2)
