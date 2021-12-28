

import myLib


class blockchain:
    def __init__(self):
        self.chain = [self.genesisCreate]

    def genesisCreate(self):
        genesis = myLib.sifrelemeYontemleri("sign of Eflatun", periviousHash="00000000000000000000000000000000",timeStamp=684343 )
        return genesis.sha256()

    def addBlock(self, data,secim):
        previous_hash = self.chain[-1]
        if secim==1:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha256()
        elif secim==2:
            node = myLib.sifrelemeYontemleri(data, previous_hash).mdo()
        elif secim==3:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha1()
        elif secim==4:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha224()
        elif secim==5:
            node = myLib.sifrelemeYontemleri(data, previous_hash).sha512()
        self.chain.append(node)
        return node

    def txtEkle(self):
        with open("sifre.txt", "a+") as dosya:
            dosya.writelines(f"{self.chain}\n")


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


def sifreleme():
    result2 = input("data giriniz :\t")
    ozelSifreleme = int(input(30 * "-" + "\nÖzel bir sifrelme turu ister misiniz?\n1)YES\n2)no:\t"))

    block1 = blockchain()

    if ozelSifreleme == 1:
        girdiYontem = int(input(30 * "-" + "\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224:\t"))
        saveBlock = int(input(30 * "-" + "\nBlock u kaydetmek istiyor musun ? \n1)YES\n2)no:\t"))

    else:
        print("Eksik veya Hatalı tuşladınız")
    if saveBlock == 1:
        block1.addBlock(result2,girdiYontem)
        print(block1.addBlock(result2, girdiYontem))
        block1.txtEkle()
        print("Block başarıyla kaydedildi")
    else:
        print(block1.addBlock(result2, girdiYontem))
        print("block kaydedilmedi")


while True:
    result = int(input(30 * "-" + "\n1)Turkce yazım kurallari kontrolu\n2)Sifreleme|\t"))

    if result == 1:
        turkçeYazımKurallari()
    elif result == 2:
        sifreleme()
    else:
        print("Eksik veya Hatalı tuşladınız.\n" + "-" * 30)
