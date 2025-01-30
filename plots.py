# plots.py
import matplotlib.pyplot as plt

def plot_ber(SNR_dB, BER_ZF, BER_MMSE):
    """Plots BER vs. SNR for ZF and MMSE equalizers."""
    plt.figure()
    plt.semilogy(SNR_dB, BER_ZF, 'k', label='ZF Equalizer')
    plt.semilogy(SNR_dB, BER_MMSE, 'b', label='MMSE Equalizer')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.title('BER Performance of ZF and MMSE Equalizers in MIMO')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
