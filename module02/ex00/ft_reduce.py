def ft_reduce(function_to_apply, list_of_inputs):
    sum_val = 0
    for elem in list_of_inputs:
        sum_val = function_to_apply(sum_val, elem)
    return sum_val