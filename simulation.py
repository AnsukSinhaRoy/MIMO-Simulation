# simulation.py
import numpy as np
from configs import M, N, mod_order, num_symbols, SNR_dB, SNR_linear
from mimo_channel import rayleigh_channel, add_awgn_noise
from QAM_Modulation import qpsk_modulate, qpsk_demodulate
from equalizers import zero_forcing_equalizer, mmse_equalizer, vblast_detection

def run_simulation():
    """Runs MIMO BER simulation for ZF and MMSE equalizers."""
    BER_ZF = np.zeros(len(SNR_dB))
    BER_MMSE = np.zeros(len(SNR_dB))
    BER_VBLAST = np.zeros(len(SNR_dB))

    # Generate random symbols
    bits = np.random.randint(0, mod_order, (M, num_symbols))
    tx_symbols = qpsk_modulate(bits)  # QPSK modulation

    for idx, snr in enumerate(SNR_linear):
        noise_variance = 1 / snr

        # Generate MIMO Channel
        H = rayleigh_channel(M, N)

        # Transmit over the channel
        rx_signal = H @ tx_symbols + add_awgn_noise(np.zeros_like(tx_symbols), noise_variance)

        # Apply Equalizers
        est_symbols_ZF = zero_forcing_equalizer(H, rx_signal)
        est_symbols_MMSE = mmse_equalizer(H, rx_signal, noise_variance)
        est_symbols_VBLAST = vblast_detection(H, rx_signal)

        # Demodulation
        demod_bits_ZF = qpsk_demodulate(est_symbols_ZF)
        demod_bits_MMSE = qpsk_demodulate(est_symbols_MMSE)
        demod_symbols_VBLAST = qpsk_demodulate(est_symbols_VBLAST)

        # BER Calculation
        BER_ZF[idx] = np.mean(demod_bits_ZF != bits)
        BER_MMSE[idx] = np.mean(demod_bits_MMSE != bits)
        BER_VBLAST[idx] = np.mean(demod_symbols_VBLAST != bits)

        print(f"SNR: {SNR_dB[idx]} dB -> BER_ZF: {BER_ZF[idx]:.6f}, BER_MMSE: {BER_MMSE[idx]:.6f}, BER_VBLAST: {BER_VBLAST[idx]:.6f}")

    return SNR_dB, BER_ZF, BER_MMSE, BER_VBLAST
