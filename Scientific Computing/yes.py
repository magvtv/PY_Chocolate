# import math

# start = print("Enter co-efficients of x in the order: \nax^2 + bx + c:")
# lst = []
# j = 2
# for i in range(0, (j + 1)):
#     if i == 0:
#         a = input(("Enter co-efficient of a: "))
#         lst.append(int(a))
#     if i == 1:
#         b = input(("Enter co-efficient of b: "))
#         lst.append(int(b))
#     if i == 2:
#         c = input(("Enter co-efficient of c: "))
#         lst.append(int(c))

# x_value = int((input("Enter the value of x: ")))
# sum1 = 0
# for i in range(0, 2):
#     while(j > 0):
#         sum1 = sum1 + (lst[i]*math.pow(x_value, j))
#         break
#     j = j - 1

# sum1 = sum1 + lst[2]
# print(f"Value of polynomial: {int(sum1)}")

# a = []
# n = int(input("Enter number of elements you will enter: "))
# for i in range(1, n + 1):
#     b = int(input("Enter elements: "))
#     a.append(b)
# k = 0
# num = int(input("Enter number to be counted in list: "))
# for j in a:
#     if (j == num):
#         k= k + 1
# if k == 1:
#     print(f"{num} appears once")
# else:
#     print(f"{num} appears {k} times")

# string = input("Enter string: \n")
# count=0
# for i in string:
#     count = count + 1
# print("String length: " + str(count))


# bitches = ("sandra", "chelsea", "mitchelle")
# x = iter(bitches)



keys = []
values = []
n = int(input("Enter number of elements for dictionary: "))
print("For keys:")
for x in range(0, n):
    element = input("Enter element " + str(x+1) + ": ")
    keys.append(element)
print("For values:")
for x in range(0, n):
    element = input("Enter element " + str(x+1) + ": ")
    values.append(element)
d = dict(zip(keys, values))
print("The dictionary is:")
print(d)
