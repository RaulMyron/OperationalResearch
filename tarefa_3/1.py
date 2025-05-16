from ortools.linear_solver import pywraplp

# Create solver
solver = pywraplp.Solver.CreateSolver('GLOP')

# Input data
N = int(input())
S = int(input())
T = int(input())

# Read adjacency matrix
Aij = [[float(input()) for j in range(0, N)] for i in range(0, N)]

# Create decision variables x[i][j] for each edge
x = {}
for i in range(N):
    for j in range(N):
        # Only create variables for valid edges (not 9999)
        if Aij[i][j] != 9999:
            x[(i, j)] = solver.NumVar(0, 1, f'x{i}{j}')
        else:
            x[(i, j)] = solver.NumVar(0, 0, f'x{i}{j}')  # Force to 0 for invalid edges

# Flow conservation constraints (divergence constraints)
for i in range(N):
    constraint = solver.Constraint(-solver.infinity(), solver.infinity())
    
    # Outgoing edges (positive)
    for j in range(N):
        if (i, j) in x:
            constraint.SetCoefficient(x[(i, j)], 1)
    
    # Incoming edges (negative)
    for j in range(N):
        if (j, i) in x:
            constraint.SetCoefficient(x[(j, i)], -1)
    
    # Set the right-hand side based on node type
    if i == S:  # Source node
        constraint.SetBounds(1, 1)
    elif i == T:  # Target node
        constraint.SetBounds(-1, -1)
    else:  # Intermediate nodes
        constraint.SetBounds(0, 0)

# Objective function: minimize sum of costs
objective = solver.Objective()
for i in range(N):
    for j in range(N):
        if Aij[i][j] != 9999:
            objective.SetCoefficient(x[(i, j)], Aij[i][j])
objective.SetMinimization()

# Solve the problem
status = solver.Solve()

# Output results
if status == pywraplp.Solver.OPTIMAL:
    print("Solucao:")
    print(f"Valor objetivo = {solver.Objective().Value():.1f}")
    
    # Print all variables in the required format
    for i in range(N):
        for j in range(N):
            value = x[(i, j)].solution_value()
            print(f"X{i}{j} = {abs(value):.1f}")
else:
    print("Problema não tem solução ótima.")