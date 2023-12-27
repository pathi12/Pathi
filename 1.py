import tkinter as tk
from tkinter import messagebox

class AplikasiPemesananTiket:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pemesanan Tiket Pesawat")

        # Data penerbangan (hanya contoh)
        self.penerbangan_data = [
            {"maskapai": "Garuda Indonesia", "tujuan": "Jakarta - Bali", "jam_keberangkatan": "08:00", "harga": 500},
            {"maskapai": "Lion Air", "tujuan": "Jakarta - Jeddah", "jam_keberangkatan": "10:00", "harga": 15000},
            {"maskapai": "AirAsia", "tujuan": "Surabaya - Medan", "jam_keberangkatan": "12:30", "harga": 300},
            {"maskapai": "Citilink", "tujuan": "Yogyakarta - Bandung", "jam_keberangkatan": "14:00", "harga": 800},
            {"maskapai": "Batik Air", "tujuan": "Semarang - Makassar", "jam_keberangkatan": "16:30", "harga": 1200},
            # Tambahkan penerbangan lainnya
        ]

        # Variabel untuk menyimpan data pengguna
        self.nama_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.pilihan_pesawat = tk.StringVar()
        self.pilihan_tujuan = tk.StringVar()
        self.pilihan_jam = tk.StringVar()
        self.pilihan_seat = tk.StringVar()
        self.pilihan_kelas = tk.StringVar()

        # Label dan Entry untuk nama pengguna
        tk.Label(root, text="Nama:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.nama_var).grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label dan Entry untuk email pengguna
        tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.email_var).grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Label dan Combobox untuk memilih pesawat
        tk.Label(root, text="Pilih Pesawat:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.combobox_pesawat = tk.OptionMenu(root, self.pilihan_pesawat, *tuple([penerbangan['maskapai'] for penerbangan in self.penerbangan_data]), command=self.update_tombol)
        self.combobox_pesawat.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Label dan Combobox untuk memilih tujuan
        tk.Label(root, text="Pilih Tujuan:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.combobox_tujuan = tk.OptionMenu(root, self.pilihan_tujuan, *tuple([penerbangan['tujuan'] for penerbangan in self.penerbangan_data]), command=self.update_tombol)
        self.combobox_tujuan.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Label dan Combobox untuk memilih jam keberangkatan
        tk.Label(root, text="Pilih Jam Keberangkatan:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.combobox_jam = tk.OptionMenu(root, self.pilihan_jam, *tuple([penerbangan['jam_keberangkatan'] for penerbangan in self.penerbangan_data]), command=self.update_tombol)
        self.combobox_jam.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Label dan Combobox untuk memilih nomor kursi
        tk.Label(root, text="Pilih Nomor Kursi:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.combobox_seat = tk.OptionMenu(root, self.pilihan_seat, *tuple([str(i) for i in range(1, 31)]), command=self.update_tombol)
        self.combobox_seat.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        # Label dan Combobox untuk memilih kelas
        tk.Label(root, text="Pilih Kelas:").grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.combobox_kelas = tk.OptionMenu(root, self.pilihan_kelas, "Ekonomi", "Bisnis", "Eksekutif", command=self.update_tombol)
        self.combobox_kelas.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        # Tombol Pesan Tiket
        self.tombol_pesan = tk.Button(root, text="Pesan Tiket", command=self.pesan_tiket, state=tk.DISABLED)
        self.tombol_pesan.grid(row=7, column=0, columnspan=2, pady=10)

    def update_tombol(self, *args):
        self.tombol_pesan.config(state=tk.NORMAL)

    def pesan_tiket(self):
        nama = self.nama_var.get()
        email = self.email_var.get()
        pesawat_terpilih = self.pilihan_pesawat.get()
        tujuan_terpilih = self.pilihan_tujuan.get()
        jam_terpilih = self.pilihan_jam.get()
        seat_terpilih = self.pilihan_seat.get()
        kelas_terpilih = self.pilihan_kelas.get()

        # Menampilkan pesan konfirmasi menggunakan messagebox
        konfirmasi = f"Terima kasih, {nama}!\nAnda telah memesan tiket pesawat {pesawat_terpilih} ke {tujuan_terpilih} pada jam {jam_terpilih}.\nNomor Kursi: {seat_terpilih}\nKelas: {kelas_terpilih}"
        messagebox.showinfo("Konfirmasi Pemesanan", konfirmasi)

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiPemesananTiket(root)
    root.mainloop()


