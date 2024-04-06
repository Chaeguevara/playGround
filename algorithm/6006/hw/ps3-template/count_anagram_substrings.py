def count_anagram_substrings(T, S):
    """
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    """
    A = []
    k = len(S[0])
    fre_table = build_hash_table(T,k)
    base26_str_table = list(map(turn_string_into_base_ts,S))
    A = list(map(lambda x: fre_table[x],base26_str_table))
    ##################
    # YOUR CODE HERE #
    ##################
    return tuple(A)


def build_hash_table(T: str, k: int) -> dict:
    result:dict = {}
    base_26_digits = 0
    for i in range(0,len(T)-k+1):
        cur_slice = T[i:i+k]
        if i==0:
            base_26_digits = turn_string_into_base_ts(cur_slice)
            result[base_26_digits] = 1
        else:
            # decrement for previous
            base_26_digits -= 10**(ord(T[i-1])%97)
            # increment for new digit
            base_26_digits += 10**(ord(T[i+k-1])%97)
            try:
                result[base_26_digits] +=1
            except KeyError:
                result[base_26_digits] = 1
    return result


def turn_string_into_base_ts(s: str) -> int:
    a = 0
    for char in s:
        a += 10 ** (ord(char) % 97)
    return a


test = turn_string_into_base_ts("abc")

print(test)
