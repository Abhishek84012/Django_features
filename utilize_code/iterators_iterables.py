# nums = [1, 2, 3]
# for num in nums:
#     print(num)

# i_nums = iter(nums)
# print(next(i_nums))
# print(next(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


# class Myrange:

#     def __init__(self, start, end):
#         self.value = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current


# nums = Myrange(1,10)

# for num in nums:
#     print(num)


# def my_range(start):
#     current = start
#     while True:
#         yield current
#         current += 1


# nums = my_range(1)

# for num in nums:
#     print(num)


from compiler.ast import flatten

Input = [1,3,4,5] 


a=list(flatten(Input))
print(a)