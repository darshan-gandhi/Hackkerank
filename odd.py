# Python3 program to find the
# nth catalan number

# Returns value of Binomial
# Coefficient C(n, k)
def binomialCoeff(n, k):

    res = 1;

# Since C(n, k) = C(n, n-k)
    if (k > (n-k)):
        k = (n-k)

# Calculate value of
# [n*(n-1)*—*(n-k+1)] /
# [k*(k-1)*—*1]
    for i in range(k):

        res *= (n-i);
        res /= (i + 1);

    return res;

# A Binomial coefficient based
# function to find nth catalan
# number in O(n) time
def catalan(n):

# Calculate value of 2nCn
    c = binomialCoeff(2 * n, n);

# return 2nCn/(n+1)
    return int(c / (n + 1));

# Driver code
n = 12;
print(catalan(n));

# This code is contributed
# by mits