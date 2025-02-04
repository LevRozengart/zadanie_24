with open("24.txt") as f:
    s = f.readline()
s = s.replace("A", " A")
s = s.split()
resulted_lst = list()
for elem in s:
    cs = ""
    cnt = 0
    for char in elem[1:]:
        cs += char
        if char in "ABCD-*":
            resulted_lst.append(cs[:-1])
            break
        if cnt == 0:
            if (not char.isdigit()) and (char != '+'):
                resulted_lst.append(cs[:-1])
                break
            if char == "+":
                cnt = 1
                continue
        if cnt == 1:
            if not char.isdigit():
                resulted_lst.append(cs[:-1])
                break
            else:
                cnt = 0
    else:
        resulted_lst.append(cs)

resulted_lst = list(filter(lambda x: len(x) > 0 and x[0] != "+", resulted_lst))
resulted_lst = list(map(lambda x: x[:-1] if x[-1] == "+" else x, resulted_lst))

mx = 0
for elem in resulted_lst:
    if elem.isdigit():
        mx = max(mx, int(elem))
    else:
        mx = max(mx, eval(elem))
print(mx)