kalan = 0
geçen = 0
dersSayisi = int(input("Ders sayısı girin:"))
geçenlerListe = []
kalanlarListe = []


vize = float(input("Vize gir:"))
final = float(input("final gir:"))

ortalama = vize*0.4 + final*0.6



if 0>= ortalama <= 49 :
    print(f"Not ortalamanız : {ortalama} Harf notunuz: FF")
elif 50>= ortalama <= 60 :
    print(f"Not ortalamanız : {ortalama} Harf notunuz: DD")  
elif 60> ortalama <= 70 :
    print(f"Not ortalamanız : {ortalama} Harf notunuz: CC") 
elif 70> ortalama <= 80 :
    print(f"Not ortalamanız : {ortalama} Harf notunuz: BB") 
elif 80> ortalama <= 100 :
    print(f"Not ortalamanız : {ortalama} Harf notunuz: AA")  
else :
    print("Geçersiz değer")
    
    ######Yarım kaldı- devam edilecek#####