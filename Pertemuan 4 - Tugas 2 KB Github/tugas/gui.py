import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("logic.pl")

gejalas = [
    "berbulu", "berkaki_empat", "mengeong", "bisa_terbang", "bertelur",
    "berenang", "berinsang", "merayap", "menggonggong", "berlari_cepat", "bercangkang"
]

index = 0
jawaban = {}

def mulai_diagnosa():
    start_btn.configure(state=tk.DISABLED)
    tampilkan_pertanyaan()

def tampilkan_pertanyaan():
    global index
    if index < len(gejalas):
        gejala = gejalas[index]
        result = list(prolog.query(f"pertanyaan({gejala}, Y)"))
        pertanyaan = result[0]["Y"]
        kotak_pertanyaan.configure(state=tk.NORMAL)
        kotak_pertanyaan.delete(1.0, tk.END)
        kotak_pertanyaan.insert(tk.END, pertanyaan)
        kotak_pertanyaan.configure(state=tk.DISABLED)
    else:
        cek_hewan()

def jawab(ya):
    global index
    gejala = gejalas[index]
    if ya:
        prolog.assertz(f"gejala_pos({gejala})")
    else:
        prolog.assertz(f"gejala_neg({gejala})")
    index += 1
    tampilkan_pertanyaan()

def cek_hewan():
    hasil = list(prolog.query("diagnosa(X)"))
    if hasil:
        nama = hasil[0]["X"]
        messagebox.showinfo("Tebakan", f"Hewan yang Anda pikirkan adalah: {nama}")
    else:
        messagebox.showinfo("Tebakan", "Maaf, hewan tidak dikenali.")
    prolog.query("reset")
    window.destroy()

# GUI
window = tk.Tk()
window.title("Tebak Hewan!")
window.geometry("600x400")
window.configure(bg="#fff8e1")

title = tk.Label(window, text="TEBAK HEWAN!", font=("Comic Sans MS", 24, "bold"), bg="#fff8e1", fg="#ff6f00")
title.pack(pady=20)

kotak_pertanyaan = tk.Text(window, height=4, width=50, state=tk.DISABLED, bg="white", font=("Arial", 14))
kotak_pertanyaan.pack(pady=20)

frame = tk.Frame(window, bg="#fff8e1")
frame.pack()

btn_ya = tk.Button(frame, text="✅ YA", font=("Arial", 14), bg="#4caf50", fg="white", width=10, command=lambda: jawab(True))
btn_ya.grid(row=0, column=0, padx=20)

btn_tidak = tk.Button(frame, text="❌ TIDAK", font=("Arial", 14), bg="#f44336", fg="white", width=10, command=lambda: jawab(False))
btn_tidak.grid(row=0, column=1, padx=20)

start_btn = tk.Button(window, text="Mulai Tebak!", font=("Arial", 14, "bold"), bg="#29b6f6", fg="white", command=mulai_diagnosa)
start_btn.pack(pady=30)

window.mainloop()
