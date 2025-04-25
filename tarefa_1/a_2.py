from ortools.linear_solver import pywraplp
import random

solver = pywraplp.Solver('LP_RANDOM', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
'''can also be created as
solver = pywraplp.Solver.CreateSolver('GLOP') or solver = pywraplp.Solver.CreateSolver('GLOP_LP')
but the first one is more general and can be used for other types of solvers as well.
'''

# Agora é necessário o instanciamento de parametros
# [START variables]
C = random.randint(1, 5)
print('C', C)
Li = [random.randint(1, 10) for i in range(C)]
print('Li', Li)
Ei = [random.randint(1, 10) for i in range(C)] #ub
print('Ei', Ei)
T = random.randint(1, 10)
print('T', T)
Ti = [random.randint(1, 10) for i in range(C)]
print('Ti', Ti)
lb = [0 for i in range(C)]
print('lb', lb)

x = solver.NumVar(0, solver.infinity(), "x")
y = solver.NumVar(0, solver.infinity(), "y")

#VD

#xi = [solver.NumVar(lb[i], ub, rot)]
xi = [solver.NumVar(lb[i], Ei[i], f"x{i+1}") for i in range(C)]
print('xi', xi)

#restrictions
ct = solver.Constraint(-solver.infinity(), T)
for i in range(C):
    ct.SetCoefficient(xi[i], Ti[i])
    
#f(obj)

objective = solver.Objective()
for i in range(C):
    objective.SetCoefficient(xi[i] * Li[i]git )
objective.SetMaximization()

#resolver

resultado = solver.Solve()

if not resultado:
    print("Solucao")
    print("Obj", objective.Value())
    for i in range(C):
        print(f'{xi[i]} = {xi[i].solution_value()}')
