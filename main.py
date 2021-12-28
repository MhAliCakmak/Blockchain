import myLib

class Ekle:
    def __init__(self):
        self.chain = [self.genesisCreate]
    def genesisCreate(self):

        return  myLib.sifrelemeYontemleri("sign of Eflatun",)
    def addBlock(self,data):
        node=myLib.sifrelemeYontemleri(data,self.chain[-1].hash)
        #with open("dosyaadı", "r") as dosya: print(dosya.read())
        self.chain.append(node)
    def txtEkle(self):
        pass


while True:
    result=int(input("1)Turkce yazım kurallari kontrolu\n 2)Block Ekle|"))

    if result==1:

        girdi=input("Cumlenizi giriniz: \t")
        data1 = myLib.dilKontrol(girdi)
        result1=int(input("1)Kelimelere Ayırma\n 2)Cumlelere Ayirma \n 3)Kucuk unlu uyumu \n 4)Buyuk unlu uyumu\n 5)Sesli Harf sayısı\t"))
        if result1==1:
            data1.kelimelereAyirma()
        elif result1==2:
            data1.cumlelereAyirma()
        elif  result1==3:
            print(data1.kucukUnluUyumu())
        elif result1==4:
            data1.buyukUnluUyumu()
        elif result1==5:
            data1.sesliHarfSayisi()
        else:
            print("Eksik veya Hatalı tuşladınız.")
    if result==2:
        result1=input("data giriniz : \t")
        hash1=myLib.sifrelemeYontemleri(result1)
        ozelSifreleme=int(input("Özel bir sifrelme turu ister misiniz?\n1)YES\n2)no"))

        if ozelSifreleme==1:
            girdiYontem = int(input("1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224"))
            if girdiYontem==1:
                print(hash1.sha256())
            elif girdiYontem==2:
                print(hash1.md5())
            elif girdiYontem==3:
                print(hash1.sha1())
            elif girdiYontem==4:
                print(hash1.sha512())
            elif girdiYontem==5:
                print(hash1.sha224())
            elif girdiYontem==6:
                pass
            elif girdiYontem==7:
                pass

        else:
            print(hash1.sha256())

