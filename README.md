# OperationalResearch
This is a basics for google ORtools + OR studies
The documentation can be found [here](https://developers.google.com/optimization/examples) and [example](https://developers.google.com/optimization/lp/lp_example) or in [git](https://github.com/google/or-tools/blob/stable/ortools/linear_solver/samples/linear_programming_example.py)

Please install the module
`python -m pip install ortools`

# Instructions to solving Linear Problems w/ ORtools

To solve a LP problem, your program should include the following steps:

1. Import the linear solver wrapper,
2. declare the LP solver,
3. define the variables,
4. define the constraints,
5. define the objective,
6. call the LP solver; and
7. display the solution