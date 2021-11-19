def fix_fuel_config(config):
    points = config.split(';')
    if len(config) == 0:
        return "KEEP_PREVIOUS"
    if len(points) != 4:
        return "KEEP_PREVIOUS"
    fractions = list()
    fraction_check = dict()
    for point in points:
        number_1 = point.split(':')[0]
        number_2 = point.split(':')[1]
        division = float(number_1) / float(number_2)
        fractions.append(division)
        fraction_check[division] = fraction_check.get(division, 0) + 1
    if len(fraction_check) == 1:
        if len(points) > len(set(points)):
            return "KEEP_PREVIOUS"
        else:
            return config
    elif len(fraction_check) == 2:
        lowest_key = 0
        lowest_value = 10000
        highest_key = 0
        highest_value = 0
        for key, value in fraction_check.items():
            if value < lowest_value:
                lowest_value = value
                lowest_key = key
            if value > highest_value:
                highest_value = value
                highest_key = key
        position = fractions.index(lowest_key)
        problem_point = points[position]
        numbers = problem_point.split(':')
        numbers[1] = str(float(numbers[0]) / highest_key)
        if float(numbers[1]) % 1 == 0:
            number = int(float(numbers[1]))
            numbers[1] = str(number)
        new_point = ':'.join(numbers)
        points[position] = new_point
        if len(points) > len(set(points)):
            return "KEEP_PREVIOUS"
        else:
            return ';'.join(points)
    else:
        return "KEEP_PREVIOUS"


print(fix_fuel_config('1:2;1:2;3.5:7;4:8'))