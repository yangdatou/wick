from wick.expression import *
from wick.ops import *
from wick.wick import apply_wick

H1 = one_e("f",["occ","vir"], norder=True)
H2 = two_e("I",["occ","vir"], norder=True)

H = H1 + H2
bra = braE2("occ", "vir", "occ", "vir")
C0 = E0("c")
C2 = E2("c", ["occ"], ["vir"])
ket = C0 + C2

HC = H*ket
S = bra*HC
out = apply_wick(S)
out.resolve()
final = AExpression(Ex=out)
print("Sigma2")
print(final)
S = HC
out = apply_wick(S)
out.resolve()
final = AExpression(Ex=out)
print("Sigma0")
print(final)
