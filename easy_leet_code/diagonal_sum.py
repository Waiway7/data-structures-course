def diagonalSum(self, mat: List[List[int]]) -> int:
    p = 0
    t = len(mat[0]) - 1
    res = 0
    for x in mat:
        first_sum = x[p]
        second_sum = x[t]
        if p == t:
            res += first_sum
        else:
            res = res + first_sum + second_sum
        p += 1
        t -= 1
    return res