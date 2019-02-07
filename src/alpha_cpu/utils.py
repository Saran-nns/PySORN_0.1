# -*- coding: utf-8 -*-

"""### IMPORT REQUIRED LIBRARIES"""

from __future__ import division

import numpy as np
from scipy.stats import norm
import random
import tqdm
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt
import heapq
import pickle


# Random seeds

random.seed(110)
np.random.seed(1101)


"""### UTILS"""

# INPUT GENERATORS

# Generate strong one-hot vector of input


def generate_strong_inp(length,reservoir_size):

    # Randomly neurons in the reservoir acts as inputs

    """
    Args:
        length - Number of input neurons
    Returns:
        out - Input vector of length equals the number of neurons in the reservoir
              with randomly chosen neuron set active
        idx - List of chosen input neurons """

    out = [0] * reservoir_size
    x = [0] * length
    idx = np.random.choice(length, np.random.randint(reservoir_size))

    for i in idx:
        x[i] = 1.0e4

    out[:len(x)] = x

    return out, idx

# Generate multi-node one-hot strong inputs


def multi_one_hot_inp(ne, inputs, n_nodes_per_inp):
    """Args:

      ne - Number of excitatory units in sorn
      inputs - input labels
      n_nodes_per_inp - Number of target units in pool that receives single input

    Returns:

      one_hot_vector for each label with length equals ne"""

    one_hot = np.zeros((ne, len(inputs)))

    idxs = []

    for _ in range(n_nodes_per_inp):
        idxs.append(random.sample(range(0, ne), len(inputs)))

    idxs = list(zip(*idxs))

    j = 0  # Max(j) = len(inputs)
    for idx_list in idxs:
        for i in idx_list:
            one_hot[i][j] = 1
        j += 1

    return one_hot, idxs

# one_hot_inp_identity, input_neurons = multi_one_hot_inp(200, inputs, 1)
# """Edit: ROWS Equals number of neurons, hence each input has to be transposed"""
#
#
# # print('Shape of one hot inputs',list(one_hot_inp_identity[:,1]),input_neurons)
#
# # # np.shape(list(one_hot_inp_identity[:,1]))
# # c = np.expand_dims(np.asarray(one_hot_inp_identity[:,1]),1)
# # c.shape


# NOTE: Gaussian input is passed directly inside the class RunSORN:
# TODO: generate_gaussian_inputs will be removed from RunSORN in future versions

def generate_gaussian_inputs(length, reservoir_size):

    # Randomly neurons in the reservoir acts as inputs

    """
    Args:
        length - Number of input neurons
    Returns:
        out - Input vector of length equals the number of neurons in the reservoir
              with randomly chosen neuron set active
        idx - List of chosen input neurons """

    out = [0] * reservoir_size
    x = [0] * length
    idx = np.random.choice(length, np.random.randint(reservoir_size))
    inp = np.random.normal(length)

    for i in idx:
        x[i] = inp[i]

    out[:len(x)] = x

    return out, idx


def normalize_weight_matrix(weight_matrix):

    # Applied only while initializing the weight. During simulation, Synaptic scaling applied on weight matrices

    """ Normalize the weights in the matrix such that incoming connections to a neuron sum up to 1

    Args:
        weight_matrix(array) -- Incoming Weights from W_ee or W_ei or W_ie

    Returns:
        weight_matrix(array) -- Normalized weight matrix"""

    normalized_weight_matrix = weight_matrix / np.sum(weight_matrix, axis=0)

    return normalized_weight_matrix


"""Connection Generator:
 lambda incoming connections for Excitatory neurons and outgoing connections per Inhibitory neuron"""


def generate_lambd_connections(synaptic_connection, ne, ni, lambd_w, lambd_std):

    """
    Args:
    synaptic_connection -  Type of sysnpatic connection (EE,EI or IE)
    ne - Number of excitatory units
    ni - Number of inhibitory units
    lambd_w - Average number of incoming connections
    lambd_std - Standard deviation of average number of connections per neuron

    Returns:

    connection_weights - Weight matrix

    """

    if synaptic_connection == 'EE':

        """Choose random lamda connections per neuron"""

        # Draw normally distribued ne integers with mean lambd_w

        lambdas_incoming = norm.ppf(np.random.random(ne), loc=lambd_w, scale=lambd_std).astype(int)

        # lambdas_outgoing = norm.ppf(np.random.random(ne), loc=lambd_w, scale=lambd_std).astype(int)

        # List of neurons

        list_neurons = list(range(ne))

        # Connection weights

        connection_weights = np.zeros((ne, ne))

        # For each lambd value in the above list,
        # generate weights for incoming and outgoing connections

        # -------------Gaussian Distribution of weights --------------

        # weight_matrix = np.random.randn(Sorn.ne, Sorn.ni) + 2 # Small random values from gaussian distribution
        # Centered around 2 to make all values positive

        # ------------Uniform Distribution --------------------------
        global_incoming_weights = np.random.uniform(0.0, 0.1, sum(lambdas_incoming))

        # Index Counter
        global_incoming_weights_idx = 0

        # Choose the neurons in order [0 to 199]

        for neuron in list_neurons:

            # Choose ramdom unique (lambdas[neuron]) neurons from  list_neurons
            possible_connections = list_neurons.copy()

            possible_connections.remove(neuron)  # Remove the selected neuron from possible connections i!=j

            # Choose random presynaptic neurons
            possible_incoming_connections = random.sample(possible_connections, lambdas_incoming[neuron])

            incoming_weights_neuron = global_incoming_weights[
                                      global_incoming_weights_idx:global_incoming_weights_idx + lambdas_incoming[
                                          neuron]]

            # ---------- Update the connection weight matrix ------------

            # Update incoming connection weights for selected 'neuron'

            for incoming_idx, incoming_weight in enumerate(incoming_weights_neuron):
                connection_weights[possible_incoming_connections[incoming_idx]][neuron] = incoming_weight

            global_incoming_weights_idx += lambdas_incoming[neuron]

        return connection_weights

    if synaptic_connection == 'EI':

        """Choose random lamda connections per neuron"""

        # Draw normally distribued ni integers with mean lambd_w
        lambdas = norm.ppf(np.random.random(ni), loc=lambd_w, scale=lambd_std).astype(int)

        # List of neurons

        list_neurons = list(range(ni))  # Each i can connect with random ne neurons

        # Initializing connection weights variable

        connection_weights = np.zeros((ni, ne))

        # ------------Uniform Distribution -----------------------------
        global_outgoing_weights = np.random.uniform(0.0, 0.1, sum(lambdas))

        # Index Counter
        global_outgoing_weights_idx = 0

        # Choose the neurons in order [0 to 40]

        for neuron in list_neurons:

            ### Choose ramdom unique (lambdas[neuron]) neurons from  list_neurons
            possible_connections = list(range(ne))

            possible_outgoing_connections = random.sample(possible_connections, lambdas[
                neuron])  # possible_outgoing connections to the neuron

            # Update weights
            outgoing_weights = global_outgoing_weights[
                               global_outgoing_weights_idx:global_outgoing_weights_idx + lambdas[neuron]]

            # ---------- Update the connection weight matrix ------------

            # Update outgoing connections for the neuron

            for outgoing_idx, outgoing_weight in enumerate(
                    outgoing_weights):  # Update the columns in the connection matrix
                connection_weights[neuron][possible_outgoing_connections[outgoing_idx]] = outgoing_weight

            # Update the global weight values index
            global_outgoing_weights_idx += lambdas[neuron]

        return connection_weights


""" More Util functions"""


def get_incoming_connection_dict(weights):

    """ Get the non-zero entries in columns is the incoming connections for the neurons"""

    # Indices of nonzero entries in the columns
    connection_dict = dict.fromkeys(range(1, len(weights) + 1), 0)

    for i in range(len(weights[0])):  # For each neuron
        connection_dict[i] = list(np.nonzero(weights[:, i])[0])

    return connection_dict


def get_outgoing_connection_dict(weights):

    """Get the non-zero entries in rows is the outgoing connections for the neurons"""

    # Indices of nonzero entries in the rows
    connection_dict = dict.fromkeys(range(1, len(weights) + 1), 1)

    for i in range(len(weights[0])):  # For each neuron
        connection_dict[i] = list(np.nonzero(weights[i, :])[0])

    return connection_dict


def prune_small_weights(weights, cutoff_weight):

    """ Prune the connections with negative connection strength"""

    weights[weights <= cutoff_weight] = cutoff_weight

    return weights


def set_max_cutoff_weight(weights, cutoff_weight):
    """ Set cutoff limit for the values in given array"""

    weights[weights > cutoff_weight] = cutoff_weight

    return weights


def get_unconnected_indexes(wee):
    """
    Helper function for Structural plasticity to randomly select the unconnected units

    Args:
    wee -  Weight matrix

    Returns:
    list (indices) // indices = (row_idx,col_idx)"""

    i, j = np.where(wee <= 0.)
    indices = list(zip(i, j))

    self_conn_removed = []
    for i, idxs in enumerate(indices):

        if idxs[0] != idxs[1]:
            self_conn_removed.append(indices[i])

    return self_conn_removed


def white_gaussian_noise(mu, sigma, t):
    """Generates white gaussian noise with mean mu, standard deviation sigma and
    the noise length equals t """

    noise = np.random.normal(mu, sigma, t)

    return np.expand_dims(noise, 1)


### SANITY CHECK EACH WEIGHTS
#### Note this function has no influence in weight matrix, will be deprecated in next version

def zero_sum_incoming_check(weights):
    zero_sum_incomings = np.where(np.sum(weights, axis=0) == 0.)

    if len(zero_sum_incomings[-1]) == 0:
        return weights
    else:
        for zero_sum_incoming in zero_sum_incomings[-1]:

            rand_indices = np.random.randint(40,
                                             size=2)  # 5 because each excitatory neuron connects with 5 inhibitory neurons
            # given the probability of connections 0.2
            rand_values = np.random.uniform(0.0, 0.1, 2)

            for i, idx in enumerate(rand_indices):
                weights[:, zero_sum_incoming][idx] = rand_values[i]

    return weights

