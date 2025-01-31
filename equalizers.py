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

def vblast_detection(H, rx_signal):
    """ V-BLAST Successive Interference Cancellation (SIC) Detector """
    N, M = H.shape
    y = rx_signal.copy()
    detected_symbols = np.zeros((M, rx_signal.shape[1]), dtype=complex)  # Store symbols for all transmitted bits
    order = np.arange(M)  # Default ordering

    for _ in range(M):
        # Find strongest column
        norm_values = np.linalg.norm(H, axis=0)
        max_index = np.argmax(norm_values)
        selected_col = H[:, max_index].reshape(-1, 1)  # Ensure column vector

        # Detect symbols for all transmitted bits
        h_pseudo_inv = np.linalg.pinv(selected_col)  # Pseudo-inverse
        detected_symbol = h_pseudo_inv @ y  # Returns a vector for all symbols

        detected_symbols[order[max_index], :] = detected_symbol.flatten()  # Assign detected symbols

        # Subtract detected symbols from received signal
        y -= selected_col @ detected_symbol  # Ensure proper broadcasting

        # Remove detected column from H
        H[:, max_index] = 0

    return detected_symbols
