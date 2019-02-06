"""### SORN"""


class Sorn(object):
    """SORN 1 network model Initialization"""

    def __init__(self):
        pass

    """Initialize network variables as class variables of SORN"""

    nu = 10  # Number of input units
    ne = 200  # Number of excitatory units
    ni = int(0.2 * ne)  # Number of inhibitory units in the network
    eta_stdp = 0.004
    eta_inhib = 0.001
    eta_ip = 0.01
    te_max = 1.0
    ti_max = 0.5
    ti_min = 0.0
    te_min = 0.0
    mu_ip = 0.1
    sigma_ip = 0.0  # Standard deviation, variance == 0

    # Initialize weight matrices

    def initialize_weight_matrix(self, network_type, synaptic_connection, self_connection, lambd_w):

        """
        Args:

        network_type(str) - Spare or Dense
        synaptic_connection(str) - EE,EI,IE: Note that Spare connection is defined only for EE connections
        self_connection(str) - True or False: i-->i ; Network is tested only using j-->i
        lambd_w(int) - Average number of incoming and outgoing connections per neuron

        Returns:
        weight_matrix(array) -  Array of connection strengths
        """

        if (network_type == "Sparse") and (self_connection == "False"):

            """Generate weight matrix for E-E/ E-I connections with mean lamda incoming and outgiong connections per neuron"""

            weight_matrix = generate_lambd_connections(synaptic_connection, Sorn.ne, Sorn.ni, lambd_w, lambd_std=1)

        # Dense matrix for W_ie

        elif (network_type == 'Dense') and (self_connection == 'False'):

            # Gaussian distribution of weights
            # weight_matrix = np.random.randn(Sorn.ne, Sorn.ni) + 2 # Small random values from gaussian distribution
            # Centered around 1
            # weight_matrix.reshape(Sorn.ne, Sorn.ni)
            # weight_matrix *= 0.01 # Setting spectral radius

            # Uniform distribution of weights
            weight_matrix = np.random.uniform(0.0, 0.1, (Sorn.ne, Sorn.ni))
            weight_matrix.reshape((Sorn.ne, Sorn.ni))

        return weight_matrix

    def initialize_threshold_matrix(self, te_min, te_max, ti_min, ti_max):

        # Initialize the threshold for excitatory and inhibitory neurons

        """Args:
            te_min(float) -- Min threshold value for excitatory units
            ti_min(float) -- Min threshold value for inhibitory units
            te_max(float) -- Max threshold value for excitatory units
            ti_max(float) -- Max threshold value for inhibitory units
        Returns:
            te(vector) -- Threshold values for excitatory units
            ti(vector) -- Threshold values for inhibitory units"""

        te = np.random.uniform(0., te_max, (Sorn.ne, 1))
        ti = np.random.uniform(0., ti_max, (Sorn.ni, 1))

        return te, ti

    def initialize_activity_vector(self, ne, ni):

        # Initialize the activity vectors X and Y for excitatory and inhibitory neurons

        """Args:
            ne(int) -- Number of excitatory neurons
            ni(int) -- Number of inhibitory neurons
        Returns:
             x(array) -- Array of activity vectors of excitatory population
             y(array) -- Array of activity vectors of inhibitory population"""

        x = np.zeros((ne, 2))
        y = np.zeros((ni, 2))

        return x, y


"""## NOTE: DO NOT TRANSPOSE THE WEIGHT MATRIX WEI FOR SORN 2 MODEL"""

# Create and initialize sorn object and varaibles

sorn_init = Sorn()
WEE_init = sorn_init.initialize_weight_matrix(network_type='Sparse', synaptic_connection='EE', self_connection='False',
                                              lambd_w=20)
WEI_init = sorn_init.initialize_weight_matrix(network_type='Sparse', synaptic_connection='EI', self_connection='False',
                                              lambd_w=40)
WIE_init = sorn_init.initialize_weight_matrix(network_type='Dense', synaptic_connection='IE', self_connection='False',
                                              lambd_w=None)

Wee_init = zero_sum_incoming_check(WEE_init)
# Wei_init = zero_sum_incoming_check(WEI_init.T)
Wei_init = zero_sum_incoming_check(WEI_init)
Wie_init = zero_sum_incoming_check(WIE_init)

c = np.count_nonzero(Wee_init)
v = np.count_nonzero(Wei_init)
b = np.count_nonzero(Wie_init)

print(c, v, b)
print('Shapes Wee %s Wei %s Wie %s' % (Wee_init.shape, Wei_init.shape, Wie_init.shape))

# Normaalize the incoming weights i.e sum(incoming weights to a neuron) = 1

normalized_wee = normalize_weight_matrix(Wee_init)
normalized_wei = normalize_weight_matrix(Wei_init)
normalized_wie = normalize_weight_matrix(Wie_init)

normalized_wee = normalize_weight_matrix(Wee_init)
normalized_wei = normalize_weight_matrix(Wei_init)
normalized_wie = normalize_weight_matrix(Wie_init)
te_init, ti_init = sorn_init.initialize_threshold_matrix(Sorn.te_min, Sorn.te_max, Sorn.ti_min, Sorn.ti_max)
x_init, y_init = sorn_init.initialize_activity_vector(Sorn.ne, Sorn.ni)

# Measure the mean number of incoming and outgoing connections in WEE and WEI

# Initializing variables from sorn_initialize.py

wee_init = normalized_wee.copy()
wei_init = normalized_wei.copy()
wie_init = normalized_wie.copy()
te_init = te_init.copy()
ti_init = ti_init.copy()
x_init = x_init.copy()
y_init = y_init.copy()