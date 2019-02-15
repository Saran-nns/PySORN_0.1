from utils import  generate_strong_inp


# """# PERTURBATION / CRITICALITY ANALYSIS"""
#
# with open('stdp2013_3020k.pkl', 'rb') as f:
#     plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = pickle.load(f)
#
# actual_states = plastic_matrices['X'][:, 1]
# perturbed_states = plastic_matrices['X'][:, 1].copy()
# print(plastic_matrices['X'][:, 1])
#
# """#### Perturbate the network by changing the activity of 4th neuron"""
#
# perturbed_states[3] = 1.0
#
# plastic_matrices['X'][:, 1] = perturbed_states.copy()
#
# print(plastic_matrices['X'][:, 1])
#
# """## Run SORN using perturbated network state
# ### CHECK: Random input defined inside the train class
# """
#
# with open('stdp2013_5_perturbed1.pkl', 'rb') as f:
#     plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = pickle.load(f)
#
# plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = RunSorn(phase='Plasticity', matrices=plastic_matrices,
#                                                                       time_steps=30000).run_sorn(None)
#
# with open('stdp2013_5_perturbed2.pkl', 'wb') as f:
#     pickle.dump([plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn], f)
#
# with open('stdp2013_5_perturbed2.pkl', 'rb') as f:
#     plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = pickle.load(f)
#
# plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = RunSorn(phase='Plasticity', matrices=plastic_matrices,
#                                                                       time_steps=30000).run_sorn(None)
#
# with open('stdp2013_5_perturbed3.pkl', 'rb') as f:
#     plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = pickle.load(f)
#
# plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = RunSorn(phase='Plasticity', matrices=plastic_matrices,
#                                                                       time_steps=30000).run_sorn(None)
#
# with open('stdp2013_5_perturbed4.pkl', 'wb') as f:
#     pickle.dump([plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn], f)
#
# """## Run SORN with actual states"""
#
# with open('stdp2013_5_act1.pkl', 'rb') as f:
#     plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = pickle.load(f)
#
# plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = RunSorn(phase='Plasticity', matrices=plastic_matrices,
#                                                                       time_steps=30000).run_sorn(None)
#
# with open('stdp2013_5_act2.pkl', 'wb') as f:
#     pickle.dump([plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn], f)
#
# with open('stdp2013_5_act2.pkl', 'rb') as f:
#     plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = pickle.load(f)
#
# plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn = RunSorn(phase='Plasticity', matrices=plastic_matrices,
#                                                                       time_steps=30000).run_sorn(None)
#
# with open('stdp2013_5_act3.pkl', 'wb') as f:
#     pickle.dump([plastic_matrices, X_all, Y_all, R_all, frac_pos_active_conn], f)
#
