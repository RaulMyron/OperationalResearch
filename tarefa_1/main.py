from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver(pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
'''can also be created as
solver = pywraplp.Solver.CreateSolver('GLOP') or solver = pywraplp.Solver.CreateSolver('GLOP_LP')
but the first one is more general and can be used for other types of solvers as well.
'''

# Agora é necessário o instanciamento de parametros