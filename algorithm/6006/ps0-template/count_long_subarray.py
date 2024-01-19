def count_long_subarray(A):
    """
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    """
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    n = len(A)
    cur_len = 1
    cur_max = 1
    for i in range(1, n):
        if A[i] > A[i - 1]:
            cur_len += 1
        else:
            cur_len = 1
        if cur_len == cur_max:
            count +=1
        elif cur_len > cur_max:
            cur_max = cur_len
            count = 1

    return count
