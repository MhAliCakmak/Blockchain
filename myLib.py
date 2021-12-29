import hashlib
import datetime
class dilKontrol:
    def __init__(self, kelime):
        self.kelime = kelime

    def kelimeyiAyirma(self):
        cumleyeAyirma = self.kelime.split()
        myList=[]
        for kelime in cumleyeAyirma:

            for i in range(len(kelime)):
                myList.append(kelime[i])
        print(myList)
    def buyukUnluUyumu(self):
        cumleAyirma = self.kelime.split()

        kalinUnlu = ["a", "ı", "o", "u","A","I","O","U"]
        inceUnlu = ["e", "i", "ö", "ü","E","İ","Ö","Ü"]
        for kelime in cumleAyirma:
            if (sum(kelime.count(kalin) for kalin in kalinUnlu)) != 0 and ( sum(kelime.count(ince) for ince in inceUnlu)) != 0:
                return f"{kelime} büyük unlu uyumuna uymaz"
            else:
                return f"{kelime} büyük unlu uyumuna uyar"

    def kucukUnluUyumu(self):
        unluler = list("aıoueiöüAIOUEİÖÜ")
        cumleAyrimi = self.kelime.split()
        myList = []
        for kelime in cumleAyrimi:
            for harf in kelime:
                if harf in unluler:
                    myList.append(harf)

        duz_unluler = list("aeıiAEIİ")
        duzden_sonra = list("aeıiAEIİ")
        yuvarlak_unluler = list("ouöüOUÖÜ")
        yuvarlaktan_sonra = list("aeuüAEUÜ")
        kurala_uyuyor = None

        for indeks in range(len(myList)):
            try:
                if myList[indeks] in duz_unluler and myList[indeks + 1] in duzden_sonra:
                    kurala_uyuyor = True
                elif myList[indeks] in yuvarlak_unluler and myList[indeks + 1] in yuvarlaktan_sonra:
                    kurala_uyuyor = True
                else:
                    kurala_uyuyor = False
                    break
            except IndexError:
                continue

        if kurala_uyuyor:
            print(" Küçük Ünlü Uyumuna Uyar.")
        else:
            print(" Küçük Ünlü Uyumuna Uymaz.")

    def sesliHarfSayisi(self):
        sesli_harf = 'AEIİOÖUÜaeıioöuü'
        cumleAyirma = self.kelime.split()
        count = 0
        for kelime in cumleAyirma:
            for harf in kelime:

                if harf in sesli_harf:
                    count += 1
        print(count)

    def cumleyiAyirma(self):
        cumleyeAyirma = self.kelime.split()
        myList=[]
        for kelime in range(len(cumleyeAyirma)):
            myList.append(cumleyeAyirma[kelime])
        print(myList)


class sifrelemeYontemleri:

    def __init__(self, data, previousHash="", timeStamp=datetime.datetime.now().day):

        self.data = data
        self.previousHash = previousHash
        self.timeStamp = timeStamp
        self.kuvvet = 0

    def md5(self):

        while True:
            self.kuvvet += 1
            transaction = hashlib.md5(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if transaction[0:2] == "00":
                break
        return transaction

    def sha256(self):
        while True:
            self.kuvvet += 1
            transaction = hashlib.sha256(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if transaction[0:2] == "00":
                break
        return transaction

    def sha1(self):
        while True:
            self.kuvvet += 1
            transaction = hashlib.sha1(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if transaction[0:2] == "00":
                break
        return transaction

    def sha224(self):
        while True:
            self.kuvvet += 1
            result = hashlib.sha224(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if result[0:2] == "00":
                break
        return result

    def sha512(self):
        while True:
            self.kuvvet += 1
            result = hashlib.sha512(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if result[0:2] == "00":
                break
        return result

    def sezarSifreleme(self):
        alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        myNewMessage= ""
        cumleAyirma=self.data.split()
        for kelime in cumleAyirma:
            for j in range(len(kelime)):
                if kelime[j] not in alphabet:
                    myNewMessage+=kelime[j]
                else:
                    myNewMessage+=alphabet[ (alphabet.index(kelime[j]) **2+111) % len(alphabet)]
        return myNewMessage

class help:

    def __init__(self):
        pass
    def DilKontrol(self):
        while True:
            try:
                print("Modüllerin içeriği:\n 1: Kelimeleri ayırma.")
                print(" 2: Cümlelere ayırma.")
                print(" 3: String ifade içerisinde kaç adet sesli harf olduğunu bulma.")
                print(" 4: Küçük ünlü uyumuna uyan kelimeleri bulma.")
                print(" 5. Büyük ünlü uyumuna uyan kelimeleri bulma.")
                print(" 0. Geri git")
                ayrinti=int(input("Ayrıntısını öğrenmek istediğiniz modülü giriniz: "))
                if ayrinti == 1:
                    print("Girilen cümleyi kelimelere ayırır. \n Örneğin: \"Hava bugün çok güzel.\" Kelimesini \"Hava\"-\"bugün\"-\"çok\"-\"güzel\"'e çevirir")
                    input("Devam etmek için entere tıklayın")
                elif ayrinti == 2:
                    print("Girilen metini cümlelere ayırır. ")
                    input("Devam etmek için entere tıklayın")
                elif ayrinti == 3:
                    print("Girilen metinin içerisinde kaç tane sesli harf olduğunu sayıp ekrana yazdırır.")
                    input("Devam etmek için entere tıklayın")
                elif ayrinti == 4:
                    print("Girilen metinin küçük ünlü uyumuna uyan kelimeleri sayar ve ekrana yazdırır.")
                    input("Devam etmek için entere tıklayın")
                elif ayrinti == 5:
                    print("Girilen metinin büyük ünlü uyumuna uyan kelimeleri sayar ve ekrana yazdırır.")
                    input("Devam etmek için entere tıklayın")
                elif ayrinti == 0:
                    break
                else:
                    raise BaskaDeger
                    break
            except Exception:
                print("Muhtemelen Yanlış bir değer girdiniz. Tekrar yazınız.")

    def Sifreleme(self):
        print("Şifreleme Yöntemleri")
        print("Modüllerin içeriği:\n 1. Hash şifreleme yöntemleri \n 2. Simetrik veya asimetrik şifreleme yöntemleri")
        ayrinti=int(input("Ayrıntısını öğrenmek istediğiniz modülü giriniz: "))
        if ayrinti == 1:
            print("SHA256 şifreleme:32 bitlik dahili blok boyutu")
            print("MD5 şifreleme:128 bitlik bir karma değer üreten bir karma işlevidir.")
            print("SHA1 şifreleme:MD5 karma değerine benzeyen 160 bitlik bir karma işlevdir.")
            print("SHA512 şifreleme:64 bit dahili blok boyutu")
            print("SHA224 şifreleme:32 bitlik dahili blok boyutu (kesilmiş versiyon)")
        elif ayrinti == 2:
            print("Simerik veya asimetri şifreleme")
