from ortools.linear_solver import pywraplp

# Create solver using the alternative method you showed
solver = pywraplp.Solver('LP_PROBLEM', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Entrada de dados
# Receber número de elementos N
N = int(input())

# Receber os limites superiores Ei
Ei = []
for i in range(0, N):
    Ei.append(float(input()))

# Receber os coeficientes da função objetivo Li
Li = []
for i in range(0, N):
    Li.append(float(input()))

# Receber os valores proporcionais Ti
Ti = []
for i in range(0, N):
    Ti.append(float(input()))

# Receber o valor total T
T = float(input())

# Definição dos parâmetros usando sua nomenclatura
C = N  # Número de elementos do conjunto C
lb = [0 for i in range(C)]  # Lower bounds (todos zero)

# Instanciamento de Parâmetros
#print('C =', C)
#print('Li =', Li)
#print('Ei =', Ei)
#print('T =', T)
#print('Ti =', Ti)
#print('lb =', lb)

# Definição das variáveis de decisão (VD)
# Criar variáveis xi para i ∈ C
xi = [solver.NumVar(lb[i], Ei[i], f"x{i+1}") for i in range(C)]
#print('xi =', xi)

# Criação das restrições (restrictions)
# Restrição: ΣCi Ti*xi ≤ T
ct = solver.Constraint(-solver.infinity(), T)
for i in range(C):
    ct.SetCoefficient(xi[i], Ti[i])

# Definição da função objetivo (f(obj))
# Maximizar: ΣCi Li*xi
objective = solver.Objective()
for i in range(C):
    objective.SetCoefficient(xi[i], Li[i])
objective.SetMaximization()

# Resolver (resolver)
resultado = solver.Solve()

# Saída de dados (corrigida)
if resultado == pywraplp.Solver.OPTIMAL:
    print("Solucao:")
    print(f"Valor objetivo = {objective.Value():.1f}")
    for i in range(C):
        print(f"x{i+1} = {xi[i].solution_value():.1f}")
else:
    print("O problema não tem solução ótima.")
