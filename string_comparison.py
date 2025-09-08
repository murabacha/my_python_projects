x = "qwertyuiopasdfghjklzxcvbnm"
y = "qwertyuiopasxfghjklzxcvbnmz"
w = min(len(x), len(y))
z = []
print(y[0])
print(len(y))
if len(x) > len(y):
    print('x is longer')
else:
    print('y is longer')
for i in range(w):
    z.append((x[i] , y[i]))
print(f'stopping at index {i} because thats where the shortest string ends')
for tuple in enumerate(z):
    if tuple[1][0] != tuple[1][1]:
        print(f'the index where the difference between the strings is at {tuple[0]} and the caracters are {{{tuple[1][0]}}} and {{{tuple[1][1]}}}')

#second method using zip and enumerate method
list = []
list1 = []
for i,(d,c) in enumerate(zip(x,y)):
    list.append(d)
    list1.append(c)
    if d != c:
        print(list.index(d))
print(list)
print(list1)
def visual_diff(str1, str2):
    print("String 1:", str1)
    print("String 2:", str2)

    markers = []
    for ch1, ch2 in zip(str1, str2):
        if ch1 == ch2:
            markers.append(" ")
        else:
            markers.append("^") 
    if len(str1) > len(str2):
        markers.extend("^" * (len(str1) - len(str2)))
    elif len(str2) > len(str1):
        markers.extend("^" * (len(str2) - len(str1)))
    print("Diff    :", "".join(markers))
    for i, (ch1, ch2) in enumerate(zip(str1, str2)):
        if ch1 != ch2:
            print(f"Mismatch at index {i}: '{ch1}' vs '{ch2}'")

    if len(str1) != len(str2):
        print("Strings have different lengths.")
        if len(str1) > len(str2):
            print(f"Extra in String 1: '{str1[len(str2):]}'")
        else:
            print(f"Extra in String 2: '{str2[len(str1):]}'")

s1 = "qwertyuiopasdfghjklzxcvbnm"
s2 = "qwertyuiopasxfghjklzxcvbnmz"

visual_diff(s1, s2)
# import re
# format = re.compile("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-].[a-z]{2,}")
# emails = ["user@example.com",
#     "john.doe123@gmail.co.uk",
#     "bad-email@",
#     "hello@site"]
# if re.findall(format, (email for email in emails)):
#     print("yes")
# else: 
#     print("no") 
