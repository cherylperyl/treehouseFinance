# Create a function to compute N layer of a Pascal Triangle

# let the number of levels be k
# let the position of a number at a level be n

# 1 - create function to compute the nth number at the kth level

# base case: number is always 1 at the sides of the triangle

# reduction step: compute num by retrieving the two numbers above it, and so on...


# 2 - create function to compute the N layer of the Pascal Triangle

# accumulate layer in list

# iterate through each position for the n layer

# use function (above) to obtain the specific num for each position