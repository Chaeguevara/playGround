def satisfying_booking(R):
    """
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    """
    B = list(map(lambda x: (1, x[0], x[1]), R))
    B = merge_sort(B)
    return tuple(B)


def merge_sort(B):
    if len(B) == 1:
        return B
    m_idx = int(len(B) / 2)
    L = merge_sort(B[:m_idx])
    R = merge_sort(B[m_idx:])
    M = merge(L, R)
    return M


def merge(L, R):
    i, j, n1, n2 = 0, 0, len(L), len(R)
    x = 0
    M = []
    while i + j < n1 + n2:
        if i < n1:
            k1, s1, t1 = L[i]
        if j < n2:
            k2, s2, t2 = R[j]

        if j == n2:
            k, s, x = k1, max(x, s1), t1
            i += 1
        elif i == n1:
            k,s,x = k2,max(x,s2),t2
            j += 1
        else:
            if x < min(s1,s2):
                x = min(s1,s2)
            if t1<=s2:
                k,s,x = k1,x,t1
                i += 1
            elif t2 <= s1:
                k,s,x = k2,x,t2
                j +=1
            elif x < s2:
                k,s,x, = k1,x,s2
            elif x<s1:
                k,s,x = k2,x,s1
            else:
                k,s,x = k1+k2,x,min(t1,t2)
                if t1 == x:
                    i +=1
                if t2 == x:
                    j +=1
        M.append((k,s,x))
    M_ = [M[0]]
    for k,s,t in M[1:]:
        k_,s_,t_ = M_[-1]
        if (k==k_) and (t_==s):
            M_.pop()
            s=s_
        M_.append((k,s,t))
    return M_
