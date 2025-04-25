from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver(pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
'''can also be created as
solver = pywraplp.Solver.CreateSolver('GLOP') or solver = pywraplp.Solver.CreateSolver('GLOP_LP')
but the first one is more general and can be used for other types of solvers as well.
'''

# Agora é necessário o instanciamento de parametros
# [START variables]
f = [3, 5]
lb = [4, solver.infinity()]
ub = [0, 0]
a = [[0, 2], [3, 2]]
b = [12, 18]

x = solver.NumVar(0, solver.infinity(), "x")
y = solver.NumVar(0, solver.infinity(), "y")


x = [solver.NumVar()]


#  4

ct = solver.cosntraint(-solver.inifity(), 12)
