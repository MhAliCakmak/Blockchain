from random import uniform,randint
import myLib
import time
class blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(myLib.sifrelemeYontemleri("sign of Eflatun").md5())

    def addBlock(self, data, secim):
        previous_hash =self.chain[-1]
        if secim == 1:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha256()
        elif secim == 2:
            node = myLib.sifrelemeYontemleri(data, previous_hash).md5()
        elif secim == 3:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha1()
        elif secim == 4:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha224()
        elif secim == 5:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha512()
        elif secim == 6:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sezarSifreleme()
        else:
            return "Eksik veya hatalı tuşladınız"
        self.chain.append(node)

        nonce = randint(1000, 45678)

        return f"\t   |\/\/\/\/\/|\t|/\/\/\/\/\|\nnonce:\t{nonce}\ndata:\t{data}\nhash:\t{node}\nprevious hash:\t{self.chain[-2]}\n\t   |\/\/\/\/\/|\t|/\/\/\/\/\|\n"
def turkçeYazımKurallari():
    girdi = input("Cumlenizi giriniz: \t")
    data1 = myLib.dilKontrol(girdi)
    result1 = int(input(
        30 * "-" + "\n1)Kelimelere Ayırma\n 2)Cumlelere Ayirma \n 3)Kucuk unlu uyumu \n 4)Buyuk unlu uyumu\n 5)Sesli Harf sayısı:\t"))
    if result1 == 1:
        data1.kelimeyiAyirma()
    elif result1 == 2:
        data1.cumleyiAyirma()
    elif result1 == 3:
        data1.kucukUnluUyumu()
    elif result1 == 4:
        print(data1.buyukUnluUyumu())
    elif result1 == 5:
        data1.sesliHarfSayisi()
    else:
        print("Eksik veya Hatalı tuşladınız.")


def sifreleme(girdiYontem):


    if girdiYontem<7:
        result2 = input("data giriniz :\t")


        saveBlock = int(input(30 * "-" + "\nBlock u kaydetmek istiyor musun ? \n1)YES\n2)no:\t"))
        if saveBlock == 1:
            try:
                print("Block Oluştruluyor ....")
                time.sleep(uniform(2, 5))

                with open("sifre.txt", "a+") as dosya:

                    değer = block1.addBlock(result2, girdiYontem)

                    print(değer)
                    dosya.write(değer)
                    print("Block başarıyla kaydedildi")
            except FileNotFoundError:
                print("Dosya bulunamadı")
        else:
            print(block1.addBlock(result2, girdiYontem))
            print("block kaydedilmedi")
    else:
        print("Eksik veya hatali tusladınız.\n")
block1 = blockchain()
while True:
        try:
            result = int(input(30 * "-" + "\n1)Turkce yazım kurallari kontrolu|\n2)Sifreleme|\n3)Help|\n0)Çıkış|\t"))
            if result == 1:
                turkçeYazımKurallari()
            elif result == 2:
                girdiYontem = int(input(30 * "-" + "\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224\n6)Simetrik sifreleme:\t"))
                sifreleme(girdiYontem)
            elif result==3:
                data2=myLib.help()
                helpSecim = int(input(" 1. Dil \n 2. Şifreleme yöntemleri \n 0. Çıkış"))
                if helpSecim == 1:
                    data2.DilKontrol()
                elif helpSecim == 2:
                    data2.Sifreleme()
                elif helpSecim == 0:
                    break
                else:
                    raise Exception
                    break
            elif result==0:
                break
        except ValueError:
            print("Karakteri yanlış")

