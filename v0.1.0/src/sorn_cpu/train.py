from sorn import RunSorn

inputs = [0.]
plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = RunSorn(phase='Plasticity', matrices=None,
                                                                          time_steps=100).run_sorn(inputs)

