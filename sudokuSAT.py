from pycryptosat import Solver
import numpy as np

import time

def B(row, col):
    sol = []
    for i in range(1, 4):
        for j in range(1, 4):
            sol.append((row * 3 + i, col * 3 + j))
    return sol

s = Solver()

for row in range(1, 10):
    for col in range(1, 10):
        rc = (100 * row) + (10 * col)
        s.add_clause([rc + 1, rc + 2, rc+3, rc+4, rc+5, rc+6, rc+7, rc+8, rc+9])
        for val in range(1, 10):
            for val2 in range(1, 10):
                if (val < val2):
                    s.add_clause([-(rc + val), -(rc + val2)])

for row in range(1, 10):
    for val in range(1, 10):
        rv = (100 * row) + val
        s.add_clause([rv + 10, rv + 20, rv+30, rv+40, rv+50, rv+60, rv+70, rv+80, rv+90])
for col in range(1, 10):
    for val in range(1, 10):
        cv = (col * 10) + val
        s.add_clause([cv + 100, cv+200, cv+300, cv+400, cv+500, cv+600, cv+700, cv+800, cv+900])

temp = []

for row2 in range(3):
    for col2 in range(3):
        b = B(row2, col2)
        for val in range(1, 10):
            for row in range(1, 10):
                for col in range(1, 10):
                    if (row, col) in b:
                        temp.append((100 * row) + (10 * col) + val)
            s.add_clause(temp)
            temp = []

s.add_clause([118])
s.add_clause([233])
s.add_clause([246])
s.add_clause([327])
s.add_clause([359])
s.add_clause([372])
s.add_clause([425])
s.add_clause([467])
s.add_clause([554])
s.add_clause([565])
s.add_clause([577])
s.add_clause([641])
s.add_clause([683])
s.add_clause([731])
s.add_clause([786])
s.add_clause([798])
s.add_clause([838])
s.add_clause([845])
s.add_clause([881])
s.add_clause([929])
s.add_clause([974])


sat, solution = s.solve()
print(sat)

table = np.zeros(shape=(9, 9))

for i in range(len(solution)):
    if (solution[i]):
        table[(i // 100) - 1][((i % 100) // 10) - 1] = i % 10

print(table)