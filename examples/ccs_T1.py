from wick.index import Idx
from wick.expression import *
from wick.hamiltonian import one_e, two_e, get_sym, commute
from wick.wick import apply_wick

H1 = one_e("f",["occ","vir"], norder=True)

i = Idx(0,"occ")
a = Idx(0,"vir")
operators = [Operator(i,True), Operator(a,False)]
bra = Expression([Term(1.0, [], [Tensor([i,a],"")], operators, [])])
T1 = Expression([Term(1.0,
    [Sigma(i), Sigma(a)],
    [Tensor([a, i], "t")],
    [Operator(a, True), Operator(i, False)],
    [])])

HT = commute(H1,T1)
HTT = commute(HT,T1)
S = bra*(HT + 0.5*HTT)
out = apply_wick(S)
out.resolve()
print(out._print_str())