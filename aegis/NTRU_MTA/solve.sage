#P.<x> = PolynomialRing(Zmod(128))
F.<x> = PolynomialRing(Zmod(128))
R_poly = x ** 167 - 1
#P.<x> = F.quotient(R_poly)

N = 167
h_poly = 43*x**166 + 51*x**165 + 14*x**164 + 47*x**162 + 4*x**161 - 40*x**160 - 45*x**159 + 30*x**158 + 13*x**157 + 19*x**156 - 63*x**155 - 25*x**154 - 42*x**153 + 19*x**152 - 58*x**151 - 32*x**150 + 30*x**149 - 37*x**148 + 44*x**147 + 55*x**146 - 46*x**145 + 41*x**144 + 20*x**143 - 32*x**142 + 41*x**141 - 45*x**140 - 54*x**139 - 63*x**138 - 11*x**137 + 6*x**136 - 31*x**135 - x**134 + 29*x**133 + 12*x**132 - 51*x**131 - 49*x**130 - 53*x**129 - 52*x**128 - 54*x**127 - 54*x**126 + 49*x**125 - 18*x**124 - 21*x**123 + 27*x**122 - 9*x**121 + 19*x**120 - 5*x**119 - 55*x**118 - 28*x**117 + 57*x**116 + 62*x**115 - 24*x**114 - 22*x**113 - 51*x**112 - 43*x**111 - 40*x**110 + 14*x**109 + x**108 - 17*x**107 - 7*x**106 - 27*x**105 - 26*x**104 - 28*x**103 + 48*x**102 + 43*x**101 - 24*x**100 + 34*x**99 - 18*x**98 - 22*x**97 + 62*x**96 + 51*x**95 + 13*x**94 - 44*x**93 + 58*x**92 + 57*x**91 + 53*x**90 + 8*x**89 - x**88 + 33*x**87 - 16*x**86 - 16*x**85 + 11*x**84 + 39*x**83 + 37*x**82 + 46*x**81 - 15*x**80 + 13*x**79 + 4*x**78 - 34*x**77 - 19*x**76 - 56*x**75 + 58*x**74 - 6*x**73 - 15*x**72 + 33*x**71 - 40*x**70 - 28*x**69 + 61*x**68 - 32*x**67 + 48*x**66 + 14*x**65 + 49*x**64 + 2*x**63 + 7*x**62 + 18*x**61 - 8*x**60 + 39*x**59 - 22*x**58 - 14*x**57 - 24*x**56 + 18*x**55 + 5*x**54 + 2*x**53 - 14*x**52 + 52*x**51 + 28*x**50 - 42*x**49 + 26*x**48 - 14*x**47 + 29*x**46 + 39*x**45 + 20*x**44 + 4*x**43 - 17*x**42 - 30*x**41 - 12*x**40 + 27*x**39 + 37*x**38 + 41*x**37 - 32*x**36 + 29*x**35 - 29*x**34 - 39*x**33 - 50*x**32 + 32*x**31 - 39*x**30 - 49*x**29 + 2*x**28 - 34*x**27 + 37*x**26 - 56*x**25 - 21*x**24 - 15*x**23 + 11*x**22 - 62*x**21 - 49*x**20 - 22*x**19 - 40*x**18 + 22*x**17 + 9*x**16 - 16*x**15 - 8*x**14 - 24*x**13 - 22*x**12 + 43*x**11 - 14*x**10 - 40*x**9 + 64*x**8 - 63*x**7 + 26*x**6 - 2*x**5 - 50*x**4 + 56*x**3 + 60*x**2 + 38*x + 19

def to_poly(lst):
    return sum(co*x**i for i, co in enumerate(reversed(lst)))

lines = open('data').readlines()
cipher = []
for line in lines:
    coe = line.strip()[1:-1].split(',')
    coe = map(int, coe)
    cipher.append(to_poly(coe))
h = h_poly
new_c = []
for i in xrange(len(cipher)-1):
    new_c.append((cipher[i]-cipher[-1])%R_poly)

M = matrix.circulant(h.list())
M = matrix(Zmod(128), M).transpose()
f = open('out','w')
cnt = 0
for xx in new_c:
    A = vector(Zmod(128), xx.list())
    d = M.solve_right(A)
    f.write(str(d)+'\n')
    print cnt, d
    print '=============='
    cnt += 1
f.close()
