import numpy as np


class NetworkState(Plasticity):
    """The evolution of network states"""

    def __init__(self, v_t):
        super().__init__()
        self.v_t = v_t

    def incoming_drive(self, weights, activity_vector):

        # Broadcasting weight*acivity vectors

        incoming = weights * activity_vector
        incoming = np.array(incoming.sum(axis=0))
        return incoming

    def excitatory_network_state(self, wee, wei, te, x, y, white_noise_e):

        """ Activity of Excitatory neurons in the network"""

        xt = x[:, 1]
        xt = xt.reshape(self.ne, 1)
        yt = y[:, 1]
        yt = yt.reshape(self.ni, 1)

        incoming_drive_e = np.expand_dims(self.incoming_drive(weights=wee, activity_vector=xt), 1)
        incoming_drive_i = np.expand_dims(self.incoming_drive(weights=wei, activity_vector=yt), 1)

        tot_incoming_drive = incoming_drive_e - incoming_drive_i + white_noise_e + np.asarray(self.v_t) - te

        """Heaviside step function"""

        heaviside_step = [0] * len(tot_incoming_drive)
        for t in range(len(tot_incoming_drive)):
            heaviside_step[t] = 0.0 if tot_incoming_drive[t] < te[t] else 1.0

        xt_next = np.asarray(heaviside_step.copy())

        return xt_next

    def inhibitory_network_state(self, wie, ti, x, white_noise_i):

        # Activity of inhibitory neurons

        wie = np.asarray(wie)
        xt = x[:, 1]
        xt = xt.reshape(Sorn.ne, 1)

        incoming_drive_e = np.expand_dims(self.incoming_drive(weights=wie, activity_vector=xt), 1)

        tot_incoming_drive = incoming_drive_e + white_noise_i - ti

        """Implement Heaviside step function"""

        heaviside_step = [0] * len(tot_incoming_drive)

        for t in range(len(tot_incoming_drive)):
            heaviside_step[t] = 0.0 if tot_incoming_drive[t] < ti[t] else 1.0

        yt_next = np.asarray(heaviside_step.copy())

        return yt_next

    def recurrent_drive(self, wee, wei, te, x, y, white_noise_e):

        """Network state due to recurrent drive received by the each unit at time t+1"""

        xt = x[:, 1]
        xt = xt.reshape(self.ne, 1)
        yt = y[:, 1]
        yt = yt.reshape(self.ni, 1)

        incoming_drive_e = np.expand_dims(self.incoming_drive(weights=wee, activity_vector=xt), 1)
        incoming_drive_i = np.expand_dims(self.incoming_drive(weights=wei, activity_vector=yt), 1)

        tot_incoming_drive = incoming_drive_e - incoming_drive_i + white_noise_e - te

        """Heaviside step function"""

        heaviside_step = [0] * len(tot_incoming_drive)
        for t in range(len(tot_incoming_drive)):
            heaviside_step[t] = 0.0 if tot_incoming_drive[t] < te[t] else 1.0

        xt_next = np.asarray(heaviside_step.copy())

        return xt_next


"""### Run SORN to study the internal dynamics of the network

## Generate random strings of length 20 as input
"""


### Generate gaussian input

def generate_normal_inp(length):
    '''First 10 neurons in the reservoir acts as inputs'''

    out = [0] * 200
    x = [0] * length
    idx = np.random.choice(length, np.random.randint(10))

    for i in idx:
        x[i] = 1.0e4

    out[:len(x)] = x

    return out

