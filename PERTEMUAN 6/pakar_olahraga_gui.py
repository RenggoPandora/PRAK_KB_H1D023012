import tkinter as tk
from pyswip import Prolog
from tkinter import messagebox
from tkinter import ttk

# Inisialisasi prolog
prolog = Prolog()
prolog.consult("pakar_olahraga_gui.pl")

olahraga = list()
kriteria = dict()
index_olahraga = 0
index_kriteria = 0
current_olahraga = ""
current_kriteria = ""

def mulai_diagnosa():
    global olahraga, kriteria, index_olahraga, index_kriteria
    prolog.retractall("kriteria_pos(_)")  
    prolog.retractall("kriteria_neg(_)")  
    
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)
    
    olahraga = [o["X"] for o in list(prolog.query("olahraga(X)"))]
    for o in olahraga:
        kriteria[o] = [k["X"] for k in list(prolog.query(f'kriteria(X, {o})'))]  # ← ini sudah betul!

    index_olahraga = 0
    index_kriteria = -1
    pertanyaan_selanjutnya()


def pertanyaan_selanjutnya(ganti_olahraga=False):
    global current_olahraga, current_kriteria, index_olahraga, index_kriteria
    
    if ganti_olahraga:
        index_olahraga += 1
        index_kriteria = -1
    
    if index_olahraga >= len(olahraga):
        hasil_diagnosa()
        return
    
    current_olahraga = olahraga[index_olahraga]
    
    index_kriteria += 1
    
    if index_kriteria >= len(kriteria[current_olahraga]):
        hasil_diagnosa(current_olahraga)
        return
    
    current_kriteria = kriteria[current_olahraga][index_kriteria]
    
    if list(prolog.query(f"kriteria_pos({current_kriteria})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"kriteria_neg({current_kriteria})")):
        pertanyaan_selanjutnya(ganti_olahraga=True)
        return
    
    pertanyaan = list(prolog.query(f"pertanyaan({current_kriteria}, Y)"))[0]["Y"]
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"kriteria_pos({current_kriteria})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"kriteria_neg({current_kriteria})")
        pertanyaan_selanjutnya(ganti_olahraga=True)

def hasil_diagnosa(olahraga_rekomendasi=""):
    if olahraga_rekomendasi:
        messagebox.showinfo("Rekomendasi Olahraga", f"Olahraga yang cocok untuk Anda: {olahraga_rekomendasi}.")
    else:
        messagebox.showinfo("Rekomendasi Olahraga", "Maaf, tidak ada olahraga yang cocok ditemukan.")
    
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# Inisialisasi window utama
root = tk.Tk()
root.title("Sistem Pakar Rekomendasi Olahraga")

# Inisialisasi frame utama
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Membuat widget yang diperlukan
ttk.Label(
    mainframe,
    text="Sistem Pakar Rekomendasi Olahraga",
    font=("Arial", 16)
).grid(column=0, row=0, columnspan=3)

ttk.Label(mainframe, text="Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(
    mainframe,
    height=4,
    width=40,
    state=tk.DISABLED
)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(
    mainframe,
    text="Tidak",
    state=tk.DISABLED,
    command=lambda: jawaban(False)
)
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(
    mainframe,
    text="Ya",
    state=tk.DISABLED,
    command=lambda: jawaban(True)
)
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(
    mainframe,
    text="Mulai Diagnosa",
    command=mulai_diagnosa
)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Tambah padding ke setiap widget
for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Menjalankan GUI
root.mainloop()
