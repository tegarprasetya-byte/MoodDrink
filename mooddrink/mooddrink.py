mood_drink = {
    "senang" : "Jus Mangga"
}
def rekomendasi_mood():
def lihat_daftar_mood():
def tambah_mood():
def hapus_mood():
def lihat_riwayat():

while True:
    print("===== Program Mood Drink =====")
    print("1. Rekomendasi Berdasarkan Mood")
    print("2. Lihat Daftar Mood")
    print("3. Tambah Mood baru")
    print("4. Hapus Mood")
    print("5. Lihat Riwayat")
    print("6. Keluar")
    
    try:
        pilihan = int(input("Masukan Pilihan (1-6) :"))
    except:
        print("Input Harus Berupa Angka!\n")
        
    if pilihan == 1:
        rekomendasi_mood():
    elif pilihan == 2:
        lihat_daftar_mood():
    elif pilihan == 3:
        tambah_mood():
    elif pilihan == 4:
        hapus_mood():
    elif pilihan == 5:
        lihat_riwayat():
    elif pilihan 
