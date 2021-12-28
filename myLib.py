import hashlib
import time


class dilKontrol:
    def __init__(self, kelime):
        self.kelime = kelime

    def kelimelereAyirma(self):
        cumleyeAyirma = self.kelime.split()
        for kelime in cumleyeAyirma:
            for i in range(len(kelime)):
                print(kelime[i])

    def buyukUnluUyumu(self):
        cumleAyirma = self.kelime.split()

        kalinUnlu = ["a", "ı", "o", "u"]
        inceUnlu = ["e", "i", "ö", "ü"]
        for kelime in cumleAyirma:
            if (sum(kelime.count(kalin) for kalin in kalinUnlu)) != 0 and (
            sum(kelime.count(ince) for ince in inceUnlu)) != 0:
                return f"{kelime} büyük unlu uyumuna uymaz"
            else:
                return f"{kelime} büyük unlu uyumuna uyar"

    def kucukUnluUyumu(self):
        unluler = ["a", "ı", "o", "u", "i", "ö", "ü", "e"]
        cumleAyirma = self.kelime.split()
        myList = []
        for harf in cumleAyirma:
            if harf in unluler:
                myList.append(harf)

        duz_unluler = ['a', 'e', 'ı', 'i']
        duzden_sonra = list("aeıi")
        yuvarlak_unluler = list("ouöü")
        yuvarlaktan_sonra = list("aeuü")
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
            print(f"'{self.kelime.capitalize()}' Küçük Ünlü Uyumuna Uyar.")
        else:
            print(f"'{self.kelime.capitalize()}' Küçük Ünlü Uyumuna Uymaz.")

    def sesliHarfSayisi(self):
        sesli_harf = 'AEIİOÖUÜaeıioöuü'
        cumleAyirma = self.kelime.split()
        count = 0
        for kelime in cumleAyirma:
            if kelime in sesli_harf:
                count += 1
        print(count)

    def cumlelereAyirma(self):
        cumleyeAyirma = self.kelime.split()
        for kelime in range(len(cumleyeAyirma)):
            print(cumleyeAyirma[kelime])


class sifrelemeYontemleri:

    def __init__(self, data, previousHash=""):

        self.data = data
        self.previousHash = previousHash
        self.timeStamp = time.ctime()
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


class help:
    pass
