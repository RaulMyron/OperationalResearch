from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")

M = int(input())  # fazendas
N = int(input())  # armazéns

# Matriz de custo de transporte (M x N)
C = []
for i in range(M):
    linha = []
    for j in range(N):
        linha.append(float(input()))
    C.append(linha)

# Vetor de produção (M fazendas)
P = []
for i in range(M):
    P.append(float(input()))

# Vetor de capacidade de armazenamento (N armazéns)
S = []
for j in range(N):
    S.append(float(input()))

# Definição das variáveis de decisão
# x[i][j] = quantidade transportada da fazenda i para o armazém j
x = {}
for i in range(M):
    for j in range(N):
        x[i, j] = solver.NumVar(0, solver.infinity(), f"x_{i}_{j}")

# Restrições

# Restrição 1: Todo o produto de cada fazenda deve ser escoado
for i in range(M):
    constraint = solver.Constraint(P[i], P[i])
    for j in range(N):
        constraint.SetCoefficient(x[i, j], 1)

# Restrição 2: Capacidade de cada armazém deve ser respeitada
# cada armazém receberá exatamente sua capacidade
for j in range(N):
    constraint = solver.Constraint(S[j], S[j])
    for i in range(M):
        constraint.SetCoefficient(x[i, j], 1)

# Função objetivo: minimizar o custo total de transporte
objective = solver.Objective()
for i in range(M):
    for j in range(N):
        objective.SetCoefficient(x[i, j], C[i][j])
objective.SetMinimization()

# Resolver o problema
status = solver.Solve()

print(f"Valor objetivo = {objective.Value()}")
for i in range(M):
    linha = "["
    for j in range(N):
        linha = linha + " " + "{:.2f}".format(x[i, j].solution_value())
    linha += " ]"
    print(linha)
