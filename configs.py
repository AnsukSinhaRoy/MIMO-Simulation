# configs.py
import numpy as np

# MIMO System Configuration
M = 4  # Number of transmit antennas
N = 4  # Number of receive antennas
mod_order = 4  # QPSK modulation (4-QAM)
num_symbols = int(3e6)  # Number of symbols per transmission

# SNR values (in dB)
SNR_dB = np.arange(0, 10, 0.5)  # From 0 to 30 dB with step of 2

# Derived parameters
SNR_linear = 10 ** (SNR_dB / 10)  # Convert SNR from dB to linear scale
