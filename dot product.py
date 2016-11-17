#   dot(L, K) should output the dot product of the lists L and K.
#   Recall that the dot product of two vectors or lists is the sum of the products of the elements in the same position in the two vectors.
#   You may assume that the two lists are of equal length.
#   If they are of different lengths, it's up to you what result is returned.
#   If these two lists are both empty, dot should output 0.0.
#   Assume that the input lists contain only numeric values.

def dot(L, K):

    sum = 0

    if len(L) > len(K):
        print "vector L has a larger length, will compute dot product up to K length if not 0"
        r = len(K)
    elif len(K) > len(L):
        print "vector K has a larger length, will compute dot product up to L length if not 0"
        r = len(L)
    else:
        r = len(L)

    if len(L) == 0 or len(K) == 0:
        return 0.0
    else:
        for i in range(r):
            sum += L[i]*K[i]

    return sum


print dot([5,3,5,3], [6,4,3,5,6])
