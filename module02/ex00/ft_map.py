def ft_map(function_to_apply, list_of_inputs):
    rtv = []
    for elem in list_of_inputs:
        rtv.append(function_to_apply(elem))
    return rtv
