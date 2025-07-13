import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulasi EOQ - Economic Order Quantity")
st.write("Model matematika untuk menghitung jumlah pemesanan optimal agar biaya persediaan minimum.")

# Input pengguna
D = st.number_input("Permintaan Tahunan (D)", value=2000)
S = st.number_input("Biaya Pemesanan per Order (S)", value=150000)
H = st.number_input("Biaya Penyimpanan per Unit per Tahun (H)", value=3000)

if D > 0 and S > 0 and H > 0:
    EOQ = math.sqrt((2 * D * S) / H)
    freq = D / EOQ
    total_cost = (D / EOQ) * S + (EOQ / 2) * H

    st.subheader("📊 Hasil Perhitungan:")
    st.write(f"EOQ (Jumlah Pemesanan Optimal): **{EOQ:.2f}** unit")
    st.write(f"Frekuensi Pemesanan per Tahun: **{freq:.2f}** kali")
    st.write(f"Total Biaya Persediaan: **Rp {total_cost:,.2f}**")

    # Grafik hubungan antara Q dan biaya total
    st.subheader("📈 Grafik Biaya Persediaan vs Jumlah Pemesanan")
    Q_vals = np.linspace(100, 1000, 100)
    TC_vals = (D / Q_vals) * S + (Q_vals / 2) * H

    fig, ax = plt.subplots()
    ax.plot(Q_vals, TC_vals, label="Total Biaya", color='blue')
    ax.axvline(x=EOQ, color='red', linestyle='--', label=f'EOQ = {EOQ:.2f}')
    ax.set_xlabel("Jumlah Pemesanan (Q)")
    ax.set_ylabel("Total Biaya Persediaan")
    ax.set_title("Grafik Total Biaya vs Jumlah Pemesanan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("Masukkan semua nilai dengan benar.")
