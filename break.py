# T = int(input())
# s = []
# ch = []
# for i in range(0,T):
#     s.append(input())
#
# for j in range(0,len(s)):
#     print(j)
#     for k in s:
#         print(k)
#         if j%2 ==0:
#             ch.append(s)
#
# print (ch)

T = int(input())
s = []

for i in range(0,T):
    s=(input())
    print (s[0::2] + " " + s[1::2])






