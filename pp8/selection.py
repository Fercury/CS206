#
# select returns the k-th smallest element of a
#
def select(a, k):
  b = sorted(a)
  return b[k]

# Implement the function quick_select.
# It also returns the k-th smallest element of a.
def quick_select(a, k):
    pivot = a[len(a) // 2]
    small = []
    equal = []
    large = []
    for x in a :
        if x < pivot :
            small.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            large.append(x)
    if len(small) >= k+1 :
        return quick_select(small, k)
    elif len(small) + len(equal)  >= k+1 :
        return equal[0]
    else :
        return quick_select(large, k - len(small) - len(equal))
