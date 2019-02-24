import liblll

# Private Key
S, m, n, k = [2, 3, 7, 14, 30, 57, 120, 251], 41, 491, 12

# Public Key
T = [82, 123, 287, 83, 248, 373, 10, 471]

# Ciphertext
C = 548

# LLLL Algorithm
M = liblll.create_matrix_from_knapsack(T, C)
M_reduced = liblll.lll_reduction(M)
U = liblll.best_vect_knapsack(M_reduced)
print 'U =', U

assert liblll.scalar_product(T, U) == C