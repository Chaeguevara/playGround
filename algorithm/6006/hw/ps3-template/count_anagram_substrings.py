def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    return tuple(A)

def turn_string_into_base_ts(s:str) -> int: 
    a = 0
    for char in s:
        print(ord(char)%97)
        print(f"{a=}")
        a += 10**(ord(char)%97)
    return a

test = turn_string_into_base_ts("abc")

print(test)