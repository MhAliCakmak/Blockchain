class help:
    def __init__(self,stro):
        self.stro=stro
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
            print("SHA256 şifreleme")
            print("MD5 şifreleme")
            print("SHA1 şifreleme")
            print("SHA512 şifreleme")
            print("SHA224 şifreleme")
        elif ayrinti == 2:
            print("Simerik veya asimetri şifreleme")
while True:
    try:
        print(" 1. Dil \n 2. Şifreleme yöntemleri \n 0. Çıkış")
        klavye=int(input())
        araba=help(klavye)
        if klavye==1:
            araba.DilKontrol()
        elif klavye==2:
            araba.Sifreleme()
        elif klavye==0:
            break
        else:
            raise Exception
            break
    except Exception:
        print("Muhtemelen Yanlış bir değer girdiniz. Tekrar yazınız.")

