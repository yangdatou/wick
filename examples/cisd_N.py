from wick.expression import *
from wick.hamiltonian import *
from wick.wick import apply_wick

H1 = one_e("f",["occ","vir"], norder=True)
H2 = two_e("I",["occ","vir"], norder=True)

H = H1 + H2

C0 = E0("c")
C1 = E1("c", ["occ"], ["vir"])
C2 = E2("c", ["occ"], ["vir"])

ket = C0 + C1 + C2
HC = H*ket

bra = projE2("occ", "vir", "occ", "vir")
S = bra*HC
out = apply_wick(S)
out.resolve()
final = AExpression(Ex=out)
final.simplify()
final.sort()
print("Sigma2")
print(final._print_str())

bra = projE1("occ", "vir")
S = bra*HC
out = apply_wick(S)
out.resolve()
final = AExpression(Ex=out)
final.simplify()
final.sort()
print("Sigma1")
print(final._print_str())

bra = Expression([Term(1.0, [], [Tensor([], "")], [], [])])
S = bra*HC
out = apply_wick(S)
out.resolve()
final = AExpression(Ex=out)
final.simplify()
final.sort()
print("Sigma0")
print(final._print_str())

