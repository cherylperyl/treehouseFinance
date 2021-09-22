# Task: Create a function to compute N layer of a Pascal Triangle

# let the number of levels be n
# let the position of a number at a level be k

# 1 - create function to compute the nth number at the kth level
def computePascalNum(n,k):

    # base case: number is always 1 at the sides of the triangle
    if k == 1 or k == n:
        return 1
    
    # reduction step: compute num by retrieving the two numbers above it, and so on...
    return computePascalNum(n-1,k) + computePascalNum(n-1,k-1)


# 2 - create function to compute the N layer of the Pascal Triangle
def  computePascalLayer(n):

    # accumulate layer in list
    layer = []

    # iterate through each position for the n layer
    for i in range(1,n+1):

        # use function (above) to obtain the specific num for each position
        layer.append(computePascalNum(n,i))
    
    return layer

# # test
# print(computePascalLayer(1))
# print(computePascalLayer(2))
# print(computePascalLayer(3))
# print(computePascalLayer(4))