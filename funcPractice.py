

def RegularNames(l):
    return map(lambda s: s[0:1].upper()+s[1:].lower(), l)

def Prod(l):
    return reduce(lambda i,j: i*j, l)

print RegularNames(['adam', 'LISA', 'barT'])
a=Prod([2, 3, 6, 10])
print a
print map(lambda s: s*a, RegularNames(['adam', 'LISA', 'barT']))