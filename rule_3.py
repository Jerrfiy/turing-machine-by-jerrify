def operation_3(list_operation, list_result):
    if list_operation[-1] == 0:
        list_result.append(0)
        list_operation.append(3)
    elif list_operation[-1] == 1:
        list_result.append(0)
        list_operation.append(3)
    elif list_operation[-1] == 2 and list_result[-1] == 1:
        list_result.append(0)
        list_operation.append(3)
    elif list_operation[-1] == 2 and list_result[-1] == 0:
        list_result.append(0)
        list_operation.append(3)
    elif list_operation[-1] == 3:
        list_result.append(1)
        list_operation.append(3)

def carry_over(list_operation, list_result):
    if list_operation[-2] == 3:
        list_result.append(1)
        list_operation.append(3)
    elif list_operation[-2] == 2 and list_result[-1] == 0:
        list_result.append(1)
        list_operation.append(3)
    elif list_operation[-2] == 2 and list_result[-1] == 1:
        list_result.append(1)
        list_operation.append(3)


'''
  When we translate this to Quintuple:

    # FOR CALCULATE NORMALLY:

    1. op_1: q0 1 
               |-------> 0 R q3
       op_2: q0 1

    2. op_1: q1 1
               |-------> 1 R q3
       op_2: q1 1

    3. op_1: q2 1                    op_RESULT: 0------->TAPE_3: R 1 R q3
               |-------> L IF ------->|       
       op_2: q2 1                    op_RESULT: 1------->TAPE_3: R 0 R q3

    4. op_1: q3 1
               |-------> 1 R q3
       op_2: q3 1
'''
