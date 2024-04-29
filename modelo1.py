#Quiz 5
# Autor: Tomas Angel y Felipe Nunez
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, maximize, summation
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Crear un modelo concreto en Pyomo
model = ConcreteModel()

# Conjuntos
model.j = Set(initialize=['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17'])
model.i = Set(initialize=['POR', 'DFI', 'DFC', 'DFD', 'MCD', 'MCO','DC',])

# Parámetros
prices = {'J1': 5000, 'J2': 5000, 'J3': 5000, 'J4': 5000, 'J5': 5000, 'J6': 5000, 'J7': 5000, 'J8': 5000,
          'J9': 1200, 'J10': 0, 'J11': 0, 'J12': 5000, 'J13': 5000, 'J14': 5000, 'J15': 5000, 'J16': 0, 'J17': 0}
ratings = {'J1': 70, 'J2': 80, 'J3': 85, 'J4': 90, 'J5': 60, 'J6': 95, 'J7': 88, 'J8': 75,
           'J9': 65, 'J10': 50, 'J11': 78, 'J12': 55, 'J13': 60, 'J14': 65, 'J15': 70, 'J16': 40, 'J17': 80}

position_matrix = {
    ('POR', 'J1'): 1, ('POR', 'J2'): 1, ('POR', 'J3'): 0, ('POR', 'J4'): 0, ('POR', 'J5'): 0, ('POR', 'J6'): 0, ('POR', 'J7'): 0, ('POR', 'J8'): 0, ('POR', 'J9'): 0, ('POR', 'J10'): 0, ('POR', 'J11'): 0, ('POR', 'J12'): 0, ('POR', 'J13'): 0, ('POR', 'J14'): 0, ('POR', 'J15'): 0, ('POR', 'J16'): 0, ('POR', 'J17'): 0,
    ('DFI', 'J1') : 0, ('DFI', 'J2'): 0, ('DFI', 'J3'): 0, ('DFI', 'J4'): 0, ('DFI', 'J5'): 0, ('DFI', 'J6'): 0, ('DFI', 'J7'): 1, ('DFI', 'J8'): 1, ('DFI', 'J9'): 0, ('DFI', 'J10'): 0, ('DFI', 'J11'): 0, ('DFI', 'J12'): 0, ('DFI', 'J13'): 0, ('DFI', 'J14'): 0, ('DFI', 'J15'): 0, ('DFI', 'J16'): 0, ('DFI', 'J17'): 0,
    ('DFC', 'J1'): 0, ('DFC', 'J2'): 0, ('DFC', 'J3'): 0, ('DFC', 'J4'): 1, ('DFC', 'J5'): 1, ('DFC', 'J6'): 1, ('DFC', 'J7'): 0, ('DFC', 'J8'): 0, ('DFC', 'J9'): 0, ('DFC', 'J10'): 0, ('DFC', 'J11'): 0, ('DFC', 'J12'): 0, ('DFC', 'J13'): 0, ('DFC', 'J14'): 0, ('DFC', 'J15'): 0, ('DFC', 'J16'): 0, ('DFC', 'J17'): 0,
    ('DFD', 'J1'): 0, ('DFD', 'J2'): 0, ('DFD', 'J3'): 1, ('DFD', 'J4'): 0, ('DFD', 'J5'): 0, ('DFD', 'J6'): 0, ('DFD', 'J7'): 0, ('DFD', 'J8'): 0, ('DFD', 'J9'): 0, ('DFD', 'J10'): 0, ('DFD', 'J11'): 0, ('DFD', 'J12'): 0, ('DFD', 'J13'): 0, ('DFD', 'J14'): 0, ('DFD', 'J15'): 0, ('DFD', 'J16'): 0, ('DFD', 'J17'): 0,
    ('MCD', 'J1'): 0, ('MCD', 'J2'): 0, ('MCD', 'J3'): 0, ('MCD', 'J4'): 0, ('MCD', 'J5'): 0, ('MCD', 'J6'): 0, ('MCD', 'J7'): 0, ('MCD', 'J8'): 0, ('MCD', 'J9'): 1, ('MCD', 'J10'): 1, ('MCD', 'J11'): 1, ('MCD', 'J12'): 0, ('MCD', 'J13'): 0, ('MCD', 'J14'): 0, ('MCD', 'J15'): 0, ('MCD', 'J16'): 0, ('MCD', 'J17'): 0,
    ('MCO', 'J1'): 0, ('MCO', 'J2'): 0, ('MCO', 'J3'): 0, ('MCO', 'J4'): 0, ('MCO', 'J5'): 0, ('MCO', 'J6'): 1, ('MCO', 'J7'): 0, ('MCO', 'J8'): 0, ('MCO', 'J9'): 0, ('MCO', 'J10'): 0, ('MCO', 'J11'): 0, ('MCO', 'J12'): 1, ('MCO', 'J13'): 1, ('MCO', 'J14'): 1, ('MCO', 'J15'): 0, ('MCO', 'J16'): 0, ('MCO', 'J17'): 0,
    ('DC', 'J1'): 0, ('DC', 'J2'): 0, ('DC', 'J3'): 0, ('DC', 'J4'): 0, ('DC', 'J5'): 0, ('DC', 'J6'): 0, ('DC', 'J7'): 0, ('DC', 'J8'): 0, ('DC', 'J9'): 0, ('DC', 'J10'): 0, ('DC', 'J11'): 0, ('DC', 'J12'): 0, ('DC', 'J13'): 0, ('DC', 'J14'): 0, ('DC', 'J15'): 1, ('DC', 'J16'): 1, ('DC', 'J17'): 1,   
}

formation = {'POR': 1, 'DFI': 1, 'DFC': 2, 'DFD' : 1
             , 'MCD': 2, 'MCO' : 2, 'DC': 2}

# Definir los parámetros en Pyomo
model.P = Param(model.j, initialize=prices)
model.R = Param(model.j, initialize=ratings)
model.posij = Param(model.i, model.j, initialize=position_matrix)
model.f = Param(model.i, initialize=formation)
model.p = Param(initialize=100000) 


# Variable binaria que indica si el jugador j es seleccionado para la posición i
model.x = Var(model.i, model.j, domain=Binary)

model.total_players = Constraint(expr=sum(model.x[i, j] for i in model.i for j in model.j) == 11)

# Maximizar la valoración total del equipo considerando la posibilidad de posición
def objective_rule(model):
    return sum(model.R[j] * model.x[i, j] for i in model.i for j in model.j if model.posij[i, j] == 1)

model.objective = Objective(rule=objective_rule, sense=maximize)


# Restricción de presupuesto
def budget_constraint_rule(model):
    return sum(model.P[j] * model.x[i, j] for i in model.i for j in model.j) <= model.p

model.budget_constraint = Constraint(rule=budget_constraint_rule)

# Restricción para asegurar que cada posición está cubierta por un jugador que puede jugar en esa posición
def position_constraint_rule(model, i):
    return sum(model.x[i, j] * model.posij[i, j] for j in model.j) == model.f[i]

model.position_constraint = Constraint(model.i, rule=position_constraint_rule)


# Específico del solver que utilizarás, por ejemplo, podría ser 'glpk' o 'cbc'
solver = SolverFactory('glpk')
result = solver.solve(model)

# Imprimir resultados
if (result.solver.status == SolverStatus.ok) and (result.solver.termination_condition == TerminationCondition.optimal):
    for i in model.i:
        for j in model.j:
            if model.x[i, j].value > 0.5:
                print(f"Jugador {j} seleccionado para posición {i}")
else:
    print("No se encontró solución óptima.")
