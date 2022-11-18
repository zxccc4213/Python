####exception

try:
    examNote = float(input("Not girin: "))
    print(examNote)
except ValueError:
    print("Deneme 123")
except ZeroDivisionError:
    print("hiçbir sayı 0' a bölünemez")
except:
    print("Yanlış girdi...")
finally:
    print("Try except bloğu sona erdi..")
    