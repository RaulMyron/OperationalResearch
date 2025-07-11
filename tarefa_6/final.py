from ortools.linear_solver import pywraplp

N = int(input())
T = int(input())
L = int(input())
C = int(input())

Xtn = [[int(input()) for _ in range(N)] for _ in range(T)]
Lnm = [[int(input()) for _ in range(N)] for _ in range(N)]
Kn = [int(input()) for _ in range(N)]

solver = pywraplp.Solver.CreateSolver('CBC')

y = {}
for t in range(T):
    for n in range(N):
        y[t, n] = solver.BoolVar(f'y_{t}_{n}')

z = {}
for t in range(T):
    for n in range(N):
        for m in range(N):
            z[t, n, m] = solver.BoolVar(f'z_{t}_{n}_{m}')

for t in range(T):
    for n in range(N):
        solver.Add(solver.Sum(z[t, n, m] for m in range(N)) == Xtn[t][n])

for t in range(T):
    for n in range(N):
        for m in range(N):
            solver.Add(z[t, n, m] <= y[t, m])

for t in range(T):
    for m in range(N):
        solver.Add(solver.Sum(z[t, n, m] * Kn[n] for n in range(N)) <= C)

for t in range(T):
    for n in range(N):
        for m in range(N):
            if Lnm[n][m] > L:
                solver.Add(z[t, n, m] == 0)

for t in range(T):
    for n in range(N):
        solver.Add(z[t, n, n] == y[t, n])

for t in range(T - 1):
    for n in range(N):
        solver.Add(y[t, n] <= y[t + 1, n])

objective_y = solver.Sum(y[t, n] for t in range(T) for n in range(N))
tie_breaker_z = solver.Sum(z[t, n, m] * m for t in range(T) for n in range(N) for m in range(N))
solver.Minimize(objective_y + tie_breaker_z * 0.0001)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print("Solucao:")
    print("Localizacao dos controladores:")
    for t in range(T):
        print(' '.join([str(y[t, n].solution_value()) for n in range(N)]))

    print("Associacao switch-controlador:")
    for t in range(T):
        if t == 0:
            print(f"Periodo {t+1}")
        else:    
            print(f"\nPeriodo {t+1}")
        active_controllers = sorted([m for m in range(N) if y[t, m].solution_value() > 0.5])
        for m in active_controllers:
            print(f"Controlador: [ {m} ]")
            for n in range(N):
                if z[t, n, m].solution_value() > 0.5:
                    print(f"Z[ {n} ] Latencia = {Lnm[n][m]}")
    
    print("\nCarga do controlador:")
    for t in range(T):
        active_controllers = sorted([m for m in range(N) if y[t, m].solution_value() > 0.5])
        for m in active_controllers:
            carga = sum(z[t, n, m].solution_value() * Kn[n] for n in range(N))
            if carga > 0:
                print(f"periodo {t+1} controlador {m} = {int(round(carga))}")

else:
    print("Nenhuma solução ótima foi encontrada.")
