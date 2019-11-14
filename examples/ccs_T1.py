from fractions import Fraction
from wick.expression import *
from wick.ops import *
from wick.wick import apply_wick

H1 = one_e("f",["occ","vir"], norder=True)

bra = braE1("occ", "vir")
T1 = E1("t", ["occ"], ["vir"])

HT = commute(H1,T1)
HTT = commute(HT,T1)
S = bra*(H1 + HT + Fraction('1/2')*HTT)
out = apply_wick(S)
out.resolve()
final = AExpression(Ex=out)
print(final)
