# modulation.py
import numpy as np
import scipy.signal as signal

def qpsk_modulate(bits):
    """Modulate bits into QPSK symbols."""
    symbols = 2 * (bits // 2) - 1 + 1j * (2 * (bits % 2) - 1)
    return symbols / np.sqrt(2)  # Normalization

def qpsk_demodulate(symbols):
    """Demodulate QPSK symbols into bits."""
    bits_real = (np.real(symbols) > 0).astype(int)
    bits_imag = (np.imag(symbols) > 0).astype(int)
    return 2 * bits_real + bits_imag
