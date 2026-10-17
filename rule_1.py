
def operation_1(list_operation, list_result):
    if list_operation[-1] == 0:
        list_result.append(0)
        list_operation.append(1)
    elif list_operation[-1] == 1:
        list_result.append(0)
        list_operation.append(1)
    elif list_operation[-1] == 2 and list_result[-1] == 0:
        list_result.append(1)
        list_operation.append(1)
    elif list_operation[-1] == 2 and list_result[-1] == 1:
        list_result.append(0)
        list_operation.append(0)
    elif list_operation[-1] == 3:
        list_result.append(1)
        list_operation.append(1)


'''
  When we translate this to Quintuple:
    1. op_1: q0 0
               |-------> 0 R q1
       op_2: q0 0
    
    2. op_1: q1 0
               |-------> 0 R q1
       op_2: q1 0
    
    3. op_1: q2 0                     0------->TAPE_3: R 1 R q1
               |-------> L IF ------->|       
       op_2: q2 0                     1------->TAPE_3: R 0 R q1
    
    4. op_1: q3 0
               |-------> 1 R q1
       op_2: q3 0
'''