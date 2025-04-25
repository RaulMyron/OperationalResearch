from ortools.linear_solver import pywraplp


def LinearProgrammingExample():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x1 = solver.NumVar(0, 4, "x1")
    x2 = solver.NumVar(0, solver.infinity(), "x2")

    print("Number of variables =", solver.NumVariables())

    # constraints
    solver.Add(x1 <= 4)
    solver.Add(x2 <= 12)
    solver.Add((3 * x1) + (2 * x2) <= 18)
    solver.Add(x1 >= 0)
    solver.Add(x2 >= 0)
    
    print("Number of constraints =", solver.NumConstraints())

    # Objective function: 3x + 4y.
    solver.Maximize(3 * x1 + 5 * x2)

    # Solve the system.
    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print(f"Objective value = {solver.Objective().Value():0.1f}")
        print(f"x = {x1.solution_value():0.1f}")
        print(f"y = {x2.solution_value():0.1f}")
    else:
        print("The problem does not have an optimal solution.")

    print("\nAdvanced usage:")
    print(f"Problem solved in {solver.wall_time():d} milliseconds")
    print(f"Problem solved in {solver.iterations():d} iterations")


LinearProgrammingExample()