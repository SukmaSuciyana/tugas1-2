# def sequenceGenerator (start, stop):
#     x = []
#     for i in range(start, stop+1):
#         x.append(i)
#     return x
# print(sequenceGenerator(1, 10))
# def fizzBuzz(a, b):
#     x = []
#     for num in range(a, b):
#         if num % 3 == 0 and num % 5 == 0:
#             x.append('FizzBuzz')
#         elif num % 3 == 0:
#             x.append('Fizz')
#         elif num % 5 == 0:
#             x.append('Buzz')
#         else:
#             x.append(num)
#     return x
# def twoNumber(l):
#     res = []
#     for i in 1:
#         if l.index(i) == len(1)-1:
#             break
#         z = i + l[i+1]
#         res.append(z)
#     return res

sequenceGenerator = lambda start, stop: list(range(start, stop + 1))
print(sequenceGenerator(1, 10))

fizzBuzz = lambda a, b: ['FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(a, b)]
print(fizzBuzz(1, 20))

twoNumber = lambda l: [l[i] + l[i + 1] for i in range(len(l) - 1)]
print(twoNumber([1, 2, 3, 4, 5]))
