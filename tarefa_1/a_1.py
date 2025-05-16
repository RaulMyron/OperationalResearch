from ortools.linear_solver import pywraplp

# Create solver
solver = pywraplp.Solver.CreateSolver(pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Instanciamento de Parâmetros
# Os parâmetros do problema dado são relacionados com os valores que
# acompanham x1 e x2 na função objetivo e nas restrições

# F. Obj: f1*x1 + f2*x2
f1 = 3; f2 = 5

# Rest de limites: lbi<=xi<=ubi
lb1 = 0; lb2 = 0; ub1 = 4; ub2 = solver.infinity()

# Rest de relacionamento: a1*x1+a2*x2 <= b1
a1 = 1; a2 = 1; b1 = 2

# Definição dos parâmetros
lb = [0, 0]
ub = [4, 2]  # Note: x2 has upper bound of 2 based on constraint 2*x2 <= 12
f = [3, 5]
a = [[1, 1]]
b = [2]

# Definição das variáveis de decisão
# Define-se as variáveis de decisão, bem como seus limites
x1 = solver.NumVar(lb[0], ub[0], 'x1')
x2 = solver.NumVar(lb[1], ub[1], 'x2')

# Utilizando nossa notação para os parâmetros anteriores, fica
# x1 = solver.NumVar(lb[0], ub[0], 'x1')
# x2 = solver.NumVar(lb[1], ub[1], 'x2')

# Criação das restrições do problema
# Primeiro cria-se a restrição de acordo com os limites
# a1*x1+a2*x2 <= b -> x1+x2 <= 2

# Vamos criar as restrições do problema para as variáveis criadas
# Restrição linear x1+x2<=2; para isso, precisamos definir o mínimo e o máximo valor
# e rescrever a restrição como: x1+x2 <= 2
ct = solver.Constraint(-solver.infinity(), 2, 'ct')

# Agora, precisamos instanciar os valores de a1 e a2
# Agora, precisaremos colocar os coeficientes multiplicativos de x1 e x2
ct.SetCoefficient(x1, 1)
ct.SetCoefficient(x2, 1)

# Additional constraints from the problem
# Constraint 2: 2*x2 <= 12 -> x2 <= 6 (already handled by ub[1] = 6)
# But we need to add it explicitly
ct2 = solver.Constraint(-solver.infinity(), 12, 'ct2')
ct2.SetCoefficient(x2, 2)

# Constraint 3: 3*x1 + 2*x2 <= 18
ct3 = solver.Constraint(-solver.infinity(), 18, 'ct3')
ct3.SetCoefficient(x1, 3)
ct3.SetCoefficient(x2, 2)

# Define objective function
# Maximize f1*x1 + f2*x2 = 3*x1 + 5*x2
objective = solver.Objective()
objective.SetCoefficient(x1, f[0])
objective.SetCoefficient(x2, f[1])
objective.SetMaximization()

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Solução:")
    print(f"Valor objetivo = {solver.Objective().Value():0.1f}")
    print(f"x1 = {x1.solution_value():0.1f}")
    print(f"x2 = {x2.solution_value():0.1f}")
else:
    print("O problema não tem solução ótima.")
    
print(f"\nAdvanced usage:")
print(f"Problem solved in {solver.wall_time():d} milliseconds")
print(f"Problem solved in {solver.iterations():d} iterations")
