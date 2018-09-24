#
# A few examples using recursion
#

def number_of_threes(n):
    if n == 0 :
        return 0

    if n % 10 == 3 :
        ret = 1
    else :
        ret = 0

    return ret + number_of_threes(n // 10)

def palindrome(s):
    l = len(s)
    if l <= 1 : 
        return True

    if s[0] != s[l-1] :
        return False

    return palindrome(s[1:l-1])


def bin_log(n):
    ret = 1

    if n < 2 :
        return 0

    return ret + bin_log(n // 2)

if __name__ == "__main__":
  for n in [ 0, 7, 3, 13, 33333, 123454321, 12333983393893 ]:
    print("%d contains %d threes" % (n, number_of_threes(n)))
  print()
  for s in ["abba", "omma", "a", "", "ere", "era", 
            "amanaplanacanalpanama" ]:
    print("'%s' is a palindrome? %s" % (s, palindrome(s)))
  print()
  for n in [7, 8, 17, 1000, 1024, 2500, 1000000, 1000000000]:
    print("binLog(%d) = %d" % (n, bin_log(n)))