mood_drinks = {
    "senang": "Es Teh Manis",
    "sedih": "Cokelat Hangat",
    "lelah": "Kopi Latte",
    "semangat": "Jus Jeruk",
    "galau": "Boba Brown Sugar",
    "relax": "Teh Chamomile"
}

def input_mood():
    mood = input("Masukkan mood Anda: ").lower()

    if mood in mood_drinks:
        minuman = mood_drinks[mood]
        print(f"Rekomendasi minuman untuk mood '{mood}': {minuman}")

        # Simpan riwayat ke file
        with open("riwayat.txt", "a") as file:
            file.write(f"Mood: {mood} -> Minuman: {minuman}\n")

    else:
        print("Maaf, mood tidak ditemukan dalam daftar.")


def lihat_daftar_mood():
    print("\n=== Daftar Mood dan Rekomendasi Minuman ===")
    for mood, drink in mood_drinks.items():
        print(f"- {mood.capitalize()} : {drink}")

def tambah_mood(mood_drinks):
    print("=== Tambah Mood Baru ===")
    mood = input("Masukkan mood baru: ")
    minuman = input("Masukkan minuman untuk mood tersebut: ")
    mood_drinks[mood] = minuman
    print("Mood baru berhasil ditambahkan!")
    print("Data sekarang:", mood_drinks)

mood_drinks = {}
tambah_mood(mood_drinks)

def hapus_mood(mood_drinks):
    print("=== Hapus Mood ===")
    mood = input("Masukkan mood yang ingin dihapus: ")

    if mood in mood_drinks:
        mood_drinks.pop(mood)
        print("Mood berhasil dihapus!")
    else:
        print("Mood tidak ditemukan.")

    print("Data sekarang:", mood_drinks)
    
mood_drinks = {}
hapus_mood(mood_drinks)

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


