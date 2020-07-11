from string import ascii_lowercase as alpstr
def rangoli_pattern(size):
    lst = []
    for i in range(size,0,-1):
        s = alpstr[size-i:size]
        cs = '-'.join(list(s[i:0:-1]+s)).center(4*size-3,'-')
        lst.append(cs)
    print('\n'.join(lst[::-1]+lst[1:]))
