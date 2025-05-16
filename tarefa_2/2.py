from ortools.linear_solver import pywraplp

# Leitura dos dados de entrada
N = int(input())

# Matriz de benefícios a_ij
A = []
for i in range(N):
    linha = []
    for j in range(N):
        linha.append(float(input()))
    A.append(linha)

# Inicialização do solver
solver = pywraplp.Solver.CreateSolver('GLOP')

# Criação das variáveis de decisão x_ij (0 ou 1)
# x_ij = 1 significa que a pessoa i é atribuída ao objeto j
x = {}
for i in range(N):
    for j in range(N):
        x[i, j] = solver.NumVar(0, 1, f'x_{i}_{j}')

# Restrição 1: Cada pessoa é atribuída a exatamente um objeto
for i in range(N):
    constraint = solver.Constraint(1, 1)  # = 1
    for j in range(N):
        constraint.SetCoefficient(x[i, j], 1)

# Restrição 2: Cada objeto é atribuído a exatamente uma pessoa
for j in range(N):
    constraint = solver.Constraint(1, 1)  # = 1
    for i in range(N):
        constraint.SetCoefficient(x[i, j], 1)

# Definição da função objetivo: maximizar o benefício total
objetivo = solver.Objective()
for i in range(N):
    for j in range(N):
        objetivo.SetCoefficient(x[i, j], A[i][j])
objetivo.SetMaximization()

# Resolução do modelo
status = solver.Solve()

# Apresentação dos resultados
if status == pywraplp.Solver.OPTIMAL:
    print("Solucao:")
    print(f"Valor objetivo = {objetivo.Value():.1f}")
    
    # Imprimir valores das variáveis x_ij
    for i in range(N):
        for j in range(N):
            print(f"X{i}{j} = {x[i, j].solution_value():.1f}")
else:
    print("O problema não possui solução ótima.")
