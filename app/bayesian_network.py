from pgmpy.models import BayesianModel
from pgmpy.factors.discrete.CPD import TabularCPD
from pgmpy.inference import VariableElimination


def gradeBayesianInference(evidences):
    aff_infer = VariableElimination(grades)
    aff = aff_infer.query(variables=['Crowding'], evidence=evidences)
    return aff


grades = BayesianModel([('Hour', 'Crowding'),
                        ('Location', 'Crowding'),
                        ('Day', 'Crowding'),
                        ])

hour_cpd = TabularCPD('Hour', 2, [[0.65],
                                  [0.35]])

day_cpd = TabularCPD('Day', 2, [[0.25],
                                [0.75]])

location_cpd = TabularCPD('Location', 3, [[0.6],
                                          [0.2],
                                          [0.2]])

crowding_cpd = TabularCPD('Crowding', 3, [[0.15, 0.45, 0.7, 0.1, 0.05, 0.05, 0.4, 0.85, 0.90, 0.25, 0.3, 0.9],
                                          [0.25, 0.25, 0.25, 0.1, 0.15, 0.2, 0.5, 0.1, 0.05, 0.35, 0.35, 0.05],
                                          [0.6, 0.3, 0.05, 0.8, 0.8, 0.75, 0.1, 0.05, 0.05, 0.4, 0.35, 0.05],
                                          ], evidence=['Hour', 'Day', 'Location'], evidence_card=[2, 2, 3])

grades.add_cpds(hour_cpd, day_cpd, location_cpd, crowding_cpd)

if not grades.check_model():
    print("Errore nella generazione della Rete Bayesiana!")
    exit

#print(gradeBayesianInference({'Day':0}))
