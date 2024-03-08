num_of_apps = 5
memory_to_get = 60

def get_minimum_memeroy_cost(num_app_and_memory:tuple,
                            occ_memory:list[int],
                            deactive_cost:list[int]
                             )->int:
    """ Knapsack?
    """
    # base case
    if num_app_and_memory[0] ==0:
        raise ValueError
    result = 0
    required_memory = num_app_and_memory[1]
    for deac_cost,occ_mem in sorted(zip(deactive_cost,occ_memory)):
        # condition met
        if required_memory <= 0:
            break
        required_memory -= occ_mem
        result += deac_cost
    # even after all loop, if required memory is not secured then throw error
    if required_memory > 0:
        raise ValueError
    return result

print(get_minimum_memeroy_cost((5,60),[30,10,20,35,40],[3,0,3,5,4]))
