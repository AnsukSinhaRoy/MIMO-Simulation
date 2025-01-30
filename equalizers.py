# equalizers.py
import numpy as np

def zero_forcing_equalizer(H, received_signal):
    """ZF equalization: x_hat = (H^H H)^(-1) H^H y"""
    H_inv = np.linalg.pinv(H)  # Moore-Penrose Pseudo-inverse
    return np.dot(H_inv, received_signal)

def mmse_equalizer(H, received_signal, noise_variance):
    """MMSE equalization: x_hat = (H^H H + σ² I)^(-1) H^H y"""
    M = H.shape[1]  # Number of transmit antennas
    H_H = np.conjugate(H.T)  # Hermitian transpose
    W_mmse = np.linalg.inv(H_H @ H + noise_variance * np.eye(M)) @ H_H
    return W_mmse @ received_signal
