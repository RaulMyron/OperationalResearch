from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

N = int(input())
S = int(input())
T = int(input())

C = []
for i in range(N):
    linha = []
    for j in range(N):
        linha.append(float(input()))
    C.append(linha)

x = {}
for i in range(N):
    for j in range(N):
        x[i, j] = solver.NumVar(0, C[i][j], f"X[{i},{j}]")

x[T, S] = solver.NumVar(0, solver.infinity(), f"X[{T},{S}]")

for i in range(N):
    constraint = solver.Constraint(0, 0)
    for j in range(N):
        if (i, j) in x and (i, j) != (T, S):
            constraint.SetCoefficient(x[i, j], -1)
    for j in range(N):
        if (j, i) in x and (j, i) != (T, S):
            constraint.SetCoefficient(x[j, i], 1)
    if i == S:
        constraint.SetCoefficient(x[T, S], 1)
    elif i == T:
        constraint.SetCoefficient(x[T, S], -1)

objective = solver.Objective()
objective.SetCoefficient(x[T, S], 1)
objective.SetMaximization()

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(f"Valor objetivo = {objective.Value()}")
    if objective.Value() > 1e-6:
        for i in range(N):
            for j in range(N):
                if (i, j) in x and (i, j) != (T, S):
                    valor = x[i, j].solution_value()
                    if valor > 1e-6:
                        capacidade = C[i][j]
                        print(f"{x[i, j].name()}={valor:.2f} de MAX_CAP: {capacidade:.2f}")
        valor_ficticio = x[T, S].solution_value()
        print(f"X[T,S]={valor_ficticio:.2f} de MAX_CAP: -1.00")
else:
    print("O problema não possui solução ótima.")
