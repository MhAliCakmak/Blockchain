import hashlib
import time


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
        myList = []  # Boş bir liste oluşturulur.
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

    def __init__(self, data, previousHash="", timeStamp=time.ctime()):

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

    def simetrikSifreleme(self):
        pass

    def asimetrikSifreleme(self):
        pass


class help:
    pass
