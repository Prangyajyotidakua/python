# without map function
nums = [1,2,3,4,5,6,7,8,9]
# normal method of computing num^2 for each element in the list

squared=[]
for num in nums:
    squared.append(num**2)
print(squared)  #[1, 4, 9, 16, 25, 36, 49, 64, 81]


# with map function
def sqr(num):
    return num**2
squared2 = list(map(sqr,nums))
print(squared2) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

"""Performance: map() is implemented in C and is generally faster than a Python for loop because it's optimized for efficiency. It can take advantage of multi-threading and other low-level optimizations.

Conciseness: map() often results in more concise and readable code, especially when combined with lambda functions or predefined functions.

Potential for Parallelism: Some Python implementations (like CPython) might not fully utilize multi-core processors with map(), but you have the potential to leverage parallelism or map-reduce frameworks for even larger datasets, which can provide substantial speed benefits.

Functional Programming Style: map() aligns with functional programming principles, which can make your code more modular and easier to reason about, especially when dealing with complex data transformations."""
