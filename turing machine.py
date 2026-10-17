import rule_1
import rule_2
import rule_3
import judging_rule

while True:
    binary_number_1 = input('please enter a binary number: ')
    binary_number_2 = input('please enter a binary number: ')
    binary_number_list_1 = []
    binary_number_list_2 = []
    binary_result = []
    operation_steps = [0]

    for i in binary_number_1:
        binary_number_list_1.append(int(i))
    for i in binary_number_2:
        binary_number_list_2.append(int(i))

    judging_rule.judging_note(binary_number_list_1 + binary_number_list_2)
    # To judge whether the input is binary or not.

    binary_number_list_1.reverse()
    binary_number_list_2.reverse()
    #

    for i in range(max(len(binary_number_list_1), len(binary_number_list_2))):
        if i == max(len(binary_number_list_1), len(binary_number_list_2)) - 1:

            if binary_number_list_1[i] == 0 and binary_number_list_2[i] == 0:
                rule_1.operation_1(operation_steps, binary_result)

            elif binary_number_list_1[i] == 0 and binary_number_list_2[i] == 1:
                rule_2.operation_2(operation_steps, binary_result)
                rule_2.carry_over(operation_steps, binary_result)

            elif binary_number_list_1[i] == 1 and binary_number_list_2[i] == 0:
                rule_2.operation_2(operation_steps, binary_result)
                rule_2.carry_over(operation_steps, binary_result)

            elif binary_number_list_1[i] == 1 and binary_number_list_2[i] == 1:
                rule_3.operation_3(operation_steps, binary_result)
                rule_3.carry_over(operation_steps, binary_result)

        elif binary_number_list_1[i] == 0 and binary_number_list_2[i] == 0:
            rule_1.operation_1(operation_steps, binary_result)

        elif binary_number_list_1[i] == 0 and binary_number_list_2[i] == 1:
            rule_2.operation_2(operation_steps, binary_result)

        elif binary_number_list_1[i] == 1 and binary_number_list_2[i] == 0:
            rule_2.operation_2(operation_steps, binary_result)

        elif binary_number_list_1[i] == 1 and binary_number_list_2[i] == 1:
            rule_3.operation_3(operation_steps, binary_result)


    binary_result.reverse()
    print(f'The result is ', *binary_result, sep='')
