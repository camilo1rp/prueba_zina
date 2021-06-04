def find_bouncy_percentage(value_target):
    """This function finds the exact number for the proportion
      of bouncy number is exactly 99% for the first time"""

    # declaring variables for calculation
    target_rate = value_target / 100
    counter = 0
    bouncing = 0
    bouncing_rate = 0
    while bouncing_rate != target_rate:
        counter += 1
        # convert number into list of digit of itself
        list_digit = [int(dig) for dig in str(counter)]

        # check if number is increasing
        numb_ascending = all([list_digit[dig] <= list_digit[dig + 1]
                              for dig in range(len(list_digit) - 1)])
        # check if number is decreasing
        numb_descending = all([list_digit[dig] >= list_digit[dig + 1]
                               for dig in range(len(list_digit) - 1)])

        # calculate new bouncing rate
        if not numb_ascending and not numb_descending:
            bouncing += 1
        bouncing_rate = bouncing / counter
    return counter


# running function
target = 99
num = find_bouncy_percentage(target)
print(f'least number for which the proportion of bouncy numbers is exactly'
      f' {target}% is {num}')
# least number for which the proportion of
# bouncy numbers is exactly 99% is 1587000
