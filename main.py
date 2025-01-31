# main.py
from simulation import run_simulation
from plots import plot_ber

if __name__ == "__main__":
    SNR_dB, BER_ZF, BER_MMSE, BER_VBLAST = run_simulation()
    plot_ber(SNR_dB, BER_ZF, BER_MMSE, BER_VBLAST)
