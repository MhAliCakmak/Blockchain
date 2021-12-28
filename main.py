import myLib

class blockchain:
    def __init__(self):
        self.chain = [self.genesisCreate]

    def genesisCreate(self):
        genesis = myLib.sifrelemeYontemleri("sign of Eflatun",periviousHash="00000000000000000000000000000000",timeStamp=684343,)
        return genesis.sha256()

    def addBlock(self, data):
        previous_hash = str(hash(self.chain[-1]))
        node = myLib.sifrelemeYontemleri(data, previous_hash)
        self.chain.append(node)

    def txtEkle(self):
        with open("sifre.txt", "a+") as dosya:

            for i in range(1,len(self.chain)):
                magic = self.chain[i]
                dosya.write(f"{str(hash(magic))}\n")

def turkçeYazımKurallari():
    girdi = input("Cumlenizi giriniz: \t")
    data1 = myLib.dilKontrol(girdi)
    result1 = int(input(30*"-"+"\n1)Kelimelere Ayırma\n 2)Cumlelere Ayirma \n 3)Kucuk unlu uyumu \n 4)Buyuk unlu uyumu\n 5)Sesli Harf sayısı\n"))
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
    hash1 = myLib.sifrelemeYontemleri(result2)
    ozelSifreleme = int(input(30*"-"+"\nÖzel bir sifrelme turu ister misiniz?\n1)YES\n2)no:\t"))

    block1 = blockchain()
    yontem = hash1.sha256()
    if ozelSifreleme == 1:
        girdiYontem = int(input(30*"-"+"\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224:\t"))
        if girdiYontem == 1:
            yontem = hash1.sha256()
            print(yontem)
        elif girdiYontem == 2:
            yontem = hash1.md5()
            print(yontem)
        elif girdiYontem == 3:
            yontem = hash1.sha1()
            print(yontem)
        elif girdiYontem == 4:
            yontem = hash1.sha512()
            print(yontem)
        elif girdiYontem == 5:
            yontem = hash1.sha224()
            print(yontem)
        elif girdiYontem == 6:
            pass
        elif girdiYontem == 7:
            pass

    else:
        print(hash1.sha256())
    saveBlock = int(input("block u kaydetmek istiyor musun ? \t1)YES\n2)no:\t"))
    if saveBlock == 1:
        block1.addBlock(result2)
        block1.txtEkle()
    else:
        print("block kaydedilmedi")


while True:
    result = int(input(30*"-"+"\n1)Turkce yazım kurallari kontrolu\n2)Sifreleme|\t"))

    if result == 1:

        turkçeYazımKurallari()

    elif result == 2:
        sifreleme()
    else:
        print("Eksik veya Hatalı tuşladınız.\n"+"-"*30)