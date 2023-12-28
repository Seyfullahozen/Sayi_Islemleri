#20010011055 Mehmet Seyfullah Özen
def menu():
    secim =-1
    while secim!=3:
        print("1. Onluk tabandan ikilik tabana çevirme")
        print("2. İkilik tabandan onluk tabana çevirme")
        print("3. Çıkış")
        secim=int(input("Hangi taban çevirmeyi yapmak istiyosunuz: "))
        if secim==1:
            ikiliksayi = " "
            sayi = int(input("Lütfen 2lik tabana cevrilmesini istediginiz sayiyi giriniz: "))
            while sayi != 0:
                ikiliksayi = str(sayi % 2) + ikiliksayi
                sayi = sayi // 2
            print("Onluktan ikiliğe çevriliyor...")
            print(ikiliksayi)

        elif secim==2:
            onluksayi = 0
            sayi1 = input("Lütfen 10luk tabana cevrilmesini istediginiz 2lik sayiyi giriniz: ")
            for i in range(len(sayi1)):
                basamak = sayi1[i]
                basamak_degeri = len(sayi1) - 1 - i
                if basamak == "1":
                    onluksayi += 2 ** basamak_degeri
            print("İkilikten onluğa çeviriliyor...")
            print(onluksayi)

        elif secim==3:
            print("Çıkış yapılıyor...")

        else:
            print("Tekrar seçim yapınız...")

menu()