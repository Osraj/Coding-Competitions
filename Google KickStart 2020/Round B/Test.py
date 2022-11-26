# string = "20 90 40 90"
# B = "100"
# li = list(string.split(" "))
#
# print (li)
#
# li.sort()
#
# print (li)
#
# houses = 0
# B = int(B)
# for cost in li:
#     if B < int(cost):
#         break
#     else:
#         houses += 1
#         B -= int(cost)
#
# print (houses)

l = input()
c = list(l.split())
print (c)
d = list(map(int, c))
print(d)