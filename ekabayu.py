import random

def main():
    tebakan_list = [
        {"tebakan": "Kenapa 6 takut sama 7?", "jawaban": "Karena 7 8 9 (seven ate nine)"},
        {"tebakan": "Apa yang kalau dipecahkan malah keluar isinya?", "jawaban": "Telur"},
        {"tebakan": "Ayam apa yang tidak bisa berkokok?", "jawaban": "Ayam mati"},
        {"tebakan": "Kenapa sumur ditutup?", "jawaban": "Karena kalau dibuka jadi sumur terbuka"},
        {"tebakan": "Kenapa pohon kelapa di depan rumah harus ditebang?", "jawaban": "Karena kalau dicabut berat"},
        {"tebakan": "Mobil apa yang bisa terbang?", "jawaban": "Mobilangan tinggi"},
        {"tebakan": "Apa yang makin dikejar makin jauh?", "jawaban": "Bayangan"},
        {"tebakan": "Kenapa komputer sering kedinginan?", "jawaban": "Karena banyak fansnya"},
        {"tebakan": "Kenapa ular selalu berbisik?", "jawaban": "Karena nggak punya kuping"},
        {"tebakan": "Kenapa pintu nggak bisa cerita?", "jawaban": "Karena cuma bisa ketok-ketok"}
    ]

    tebakan = random.choice(tebakan_list)
    print("Tebakan: " + tebakan["tebakan"])

    jawaban_pengguna = input("Jawaban kamu: ").strip().lower()

    if jawaban_pengguna == tebakan["jawaban"].lower():
        print("Benar! Kamu hebat!")
    else:
        print(f"Salah! Jawabannya adalah: {tebakan['jawaban']}")

if __name__ == "__main__":
    main()
