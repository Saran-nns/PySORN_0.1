import numpy as np


class MatrixCollection(Sorn):
    def __init__(self, phase, matrices=None):
        super().__init__()

        self.phase = phase
        self.matrices = matrices
        if self.phase == 'Plasticity' and self.matrices == None:

            self.time_steps = Sorn.time_steps + 1  # Total training steps
            self.Wee, self.Wei, self.Wie, self.Te, self.Ti, self.X, self.Y = [0] * self.time_steps, [
                0] * self.time_steps, \
                                                                             [0] * self.time_steps, [
                                                                                 0] * self.time_steps, \
                                                                             [0] * self.time_steps, [
                                                                                 0] * self.time_steps, \
                                                                             [0] * self.time_steps
            wee, wei, wie, te, ti, x, y = Plasticity.initialize_plasticity()

            # Assign initial matrix to the master matrices
            self.Wee[0] = wee
            self.Wei[0] = wei
            self.Wie[0] = wie
            self.Te[0] = te
            self.Ti[0] = ti
            self.X[0] = x
            self.Y[0] = y

        elif self.phase == 'Plasticity' and self.matrices != None:

            self.time_steps = Sorn.time_steps + 1  # Total training steps
            self.Wee, self.Wei, self.Wie, self.Te, self.Ti, self.X, self.Y = [0] * self.time_steps, [
                0] * self.time_steps, \
                                                                             [0] * self.time_steps, [
                                                                                 0] * self.time_steps, \
                                                                             [0] * self.time_steps, [
                                                                                 0] * self.time_steps, \
                                                                             [0] * self.time_steps
            # Assign matrices from plasticity phase to the new master matrices for training phase
            self.Wee[0] = matrices['Wee']
            self.Wei[0] = matrices['Wei']
            self.Wie[0] = matrices['Wie']
            self.Te[0] = matrices['Te']
            self.Ti[0] = matrices['Ti']
            self.X[0] = matrices['X']
            self.Y[0] = matrices['Y']

        elif self.phase == 'Training':

            """NOTE:
            time_steps here is diferent for plasticity or trianing phase"""
            self.time_steps = Sorn.time_steps + 1  # Total training steps
            self.Wee, self.Wei, self.Wie, self.Te, self.Ti, self.X, self.Y = [0] * self.time_steps, [
                0] * self.time_steps, \
                                                                             [0] * self.time_steps, [
                                                                                 0] * self.time_steps, \
                                                                             [0] * self.time_steps, [
                                                                                 0] * self.time_steps, \
                                                                             [0] * self.time_steps
            # Assign matrices from plasticity phase to new respective matrices for training phase
            self.Wee[0] = matrices['Wee']
            self.Wei[0] = matrices['Wei']
            self.Wie[0] = matrices['Wie']
            self.Te[0] = matrices['Te']
            self.Ti[0] = matrices['Ti']
            self.X[0] = matrices['X']
            self.Y[0] = matrices['Y']

    # @staticmethod
    def weight_matrix(self, wee, wei, wie, i):
        # Get delta_weight from Plasticity.stdp

        # i - training step
        self.Wee[i + 1] = wee
        self.Wei[i + 1] = wei
        self.Wie[i + 1] = wie

        return self.Wee, self.Wei, self.Wie

    # @staticmethod
    def threshold_matrix(self, te, ti, i):
        self.Te[i + 1] = te
        self.Ti[i + 1] = ti
        return self.Te, self.Ti

    # @staticmethod
    def network_activity_t(self, excitatory_net, inhibitory_net, i):
        self.X[i + 1] = excitatory_net
        self.Y[i + 1] = inhibitory_net

        return self.X, self.Y

    # @staticmethod
    def network_activity_t_1(self, x, y, i):
        x_1, y_1 = [0] * self.time_steps, [0] * self.time_steps
        x_1[i] = x
        y_1[i] = y

        return x_1, y_1

