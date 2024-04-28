def count_anagram_substrings(T, S):
    """
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    """
    A = []
    k = len(S[0])
    print(k)
    print(build_freq_table(T,k))
    # char => order(int) "ord"

    # build frequence table
    # search from frequence table

    ##################
    # YOUR CODE HERE #
    ##################
    return tuple(A)

def build_freq_table(T:str,k:int) -> dict:
    freq_table = (0)*26
    H= dict()
    # traverse each letter
    # aaa => 3,
    for i in range(0,len(T)-k-1):
        # case 0 : k traverse
        if i == 0: #O(k)
            for j in range(i,k):
                freq_table[ char_to_int( T[j]) ] # car => [1,0,1,...,1,...,0]
                cur = freq_table
                H[cur] = 1 # {[1,0,...]:1}
        else: # i-1 : index => -1  , i+k:inex => +1 . O(1)
            to_be_deleted = T[i-1]
            to_be_added = T[i+k]
            del_idx = char_to_int(to_be_deleted)
            add_idx = char_to_int(to_be_added) 
            freq_table[del_idx] -= 1
            freq_table[add_idx] += 1
            cur = freq_table
            try:
                H[cur] += 1
            except KeyError:
                H[cur] = 1
        

    return H

def char_to_int(c:str)->int:
    return ord(c) - ord('a')