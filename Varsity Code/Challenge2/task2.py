import re

def number_prediction(input):
    initial_sequence = input
    final_sequence = list()
    count = 0
    for digit in initial_sequence:
        if digit == "_":
            if count == 0:
                final_sequence.append('0')
            else:
                end_position = count
                start_position = count
                number = final_sequence[count-1]
                while True:
                    start_position = start_position - 1
                    if start_position < 0:
                        break
                    if count - start_position > 10:
                        break
                    mini_sequence = ''.join(final_sequence)[start_position:end_position]
                    search_sequence = re.findall('%s' % (mini_sequence), ''.join(final_sequence))
                    if len(search_sequence) > 1:
                        last_sequence = ''.join(final_sequence[:count-1]).rfind(mini_sequence)
                        number = ''.join(final_sequence)[last_sequence+len(search_sequence[1])]
                if re.search('^[1-9][0]+$',''.join(final_sequence)):
                    number = initial_sequence[0]

                final_sequence.append(number)
        else:
            final_sequence.append(digit)
        count=count+1
    final_string = ''.join(final_sequence)
    return final_string


test = number_prediction('219_168_926629293_776892_9_1_8_8049287_298_9343647_9_2334_4_6_7__57__30785__7__62_1____4_____382__1226816__04__67___0119_47__0_0_7___0___0_3__3_____06_37_')
print(test)
correct = '81804928762981934364769323343436476957693078576760629193434364763829112268168904926760601193476307077689049204364364364060374
'
correct = '81804928762981934364769323343436476957693078576760629193434364763829112268168904926760601193476307077689049204312334343060374'
if correct == test:
    print('true')
else:
    print('false')


# ___ 000
