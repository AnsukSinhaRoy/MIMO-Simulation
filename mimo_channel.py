# mimo_channel.py
import numpy as np

def rayleigh_channel(M, N):
    """Generates a MIMO Rayleigh fading channel matrix H (N x M)."""
    return (np.random.randn(N, M) + 1j * np.random.randn(N, M)) / np.sqrt(2)

def add_awgn_noise(signal, noise_variance):
    """Adds AWGN noise to the signal."""
    noise = np.sqrt(noise_variance / 2) * (np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape))
    return signal + noise
