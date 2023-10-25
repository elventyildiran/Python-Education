#
#! ----- Koşullu Durumlar ------

# Artık Python programlama dilinde belli bir noktaya geldik sayılır. Ama eğer farkettiyseniz, yine de elimizi kolumuzu bağlayan, istediğimiz şeyleri yapmamıza engel olan bir şeyler var. İşte bu bölümde, Python programlama dilinde hareket alanımızı bir hayli genişletecek araçları tanıyacağız.

# Aslında sadece bu bölümde değil, bu bölümü takip eden her bölümde, hareket alanımızı kısıtlayan duvarları tek tek yıktığımıza şahit olacaksınız. Özellikle bu bölümde inceleyeceğimiz ‘koşullu durumlar’ konusu, tabir yerindeyse, Python’da boyut atlamamızı sağlayacak.

#! ----- Koşul Deyimi -----

#- if -

# Python programlama dilinde koşullu durumları belirtmek için üç adet deyimden yararlanıyoruz:

#- * if
#- * elif
#- * else

# Önce if deyimi ile başlayalım.

# İngilizce bir kelime olan ‘if’, Türkçede ‘eğer’ anlamına gelir. Anlamından da çıkarabileceğimiz gibi, bu kelime bir koşul bildiriyor. Yani ‘eğer bir şey falanca ise…’ ya da ‘eğer bir şey filanca ise…’ gibi… İşte biz Python’da bir koşula bağlamak istediğimiz durumları if deyimi aracılığıyla göstereceğiz.

# Öncelikle elimizde şöyle bir değişken olsun:
#* ÖRNEK

#< n = 255

# Yukarıda verdiğimiz değişkenin değerinin bir karakter dizisi değil, aksine bir sayı olduğunu görüyoruz. Şimdi bu değişkenin değerini sorgulayalım:
#< if n > 10:

# Burada sayının 10’dan büyük olup olmadığına bakıyoruz.

# Burada gördüğümüz > işaretinin ne demek olduğunu açıklamaya gerek yok sanırım. Hepimizin bildiği ‘büyüktür’ işareti Python’da da aynen bildiğimiz şekilde kullanılıyor. Mesela ‘küçüktür’ demek isteseydik, < işaretini kullanacaktık. İsterseniz hemen şurada araya girip bu işaretleri yeniden hatırlayalım:

#- İşleç Anlamı
#? > büyüktür

#? < küçüktür

#? >= büyük eşittir

#? <= küçük eşittir

#? == eşittir

#? != eşit değildir

# Gördüğünüz gibi hiçbiri bize yabancı gelecek gibi değil. Yalnızca en sondaki ‘eşittir’ (==) ve ‘eşit değildir’ (!=) işaretleri biraz değişik gelmiş olabilir. Burada ‘eşittir’ işaretinin = olmadığına dikkat edin. Python’da = işaretini değer atama işlemleri için kullanıyoruz. == işaretini ise iki adet değerin birbirine eşit olup olmadığını denetlemek için… Mesela:

#< a = 26

# Burada değeri 26 olan a adlı bir değişken belirledik. Yani a değişkenine değer olarak 26 sayısını atadık. Ayrıca burada, değer atama işleminin ardından Enter tuşuna bastıktan sonra Python hiçbir şey yapmadan bir alt satıra geçti. Bir de şuna bakalım:

# < a == 26
#True

# Burada ise yaptığımız şey a değişkeninin değerinin 26 olup olmadığını sorgulamak a == 26 komutunu verdikten sonra Python bize True diye bir çıktı verdi. Bu çıktının anlamını biraz sonra öğreneceğiz. Ama şimdi isterseniz konuyu daha fazla dağıtmayalım. Biz şimdilik sadece = ve == işaretlerinin birbirinden tamamen farklı anlamlara geldiğini bilelim yeter.

# Ne diyorduk?
#< if n > 10:

# Bu ifadeyle Python’a şöyle bir şey demiş oluyoruz:
#?  Eğer n sayısının değeri 10’dan büyükse…

# Burada kullandığımız işaretlere dikkat edin. En sonda bir adet : işaretinin olduğunu gözden kaçırmıyoruz. Bu tür işaretler Python için çok önemlidir. Bunları yazmayı unutursak Python gözümüzün yaşına bakmayacaktır.

# Dedik ki, if n > 10: ifadesi, ‘eğer n değişkeninin değeri 10’dan büyükse…’ anlamına gelir. Bu ifadenin eksik olduğu apaçık ortada. Yani belli ki bu cümlenin bir de devamı olması gerekiyor. O halde biz de devamını getirelim:

n = 50
if n > 10:
    print("Sayı 10'dan büyüktür!")
    

# * Örnek 1:
# Girilen sayının 10'dan büyük veya küçük olduğunu söyleyen programı yazalım :

sayi = int(input("Bir sayı giriniz : "))
if sayi > 10:
    print("Sayi 10'dan büyüktür.")
if sayi < 10:
    print("Girdiğiniz sayı 10'dan küçüktür.")
if sayi == 10:
    print("Girdiğiniz sayi 10'dur.")


#- if deyiminin basitçe kullanımı bu şekildedir. Şimdi "elif" ve `else` deyimine bakalım.

# elif deyiminin anlamı aslında "else if"(aksi takdirde eğer)'den gelir.
# else deyimi ise "aksi takdirde" anlamını taşımaktadır.
# Yukarıdaki örneği "elif" deyimini kullanarak yapalım ;

sayi1 = int(input("Lütfen bir sayı girin : "))
if sayi1 > 10:
    print("Girilen sayı 10'dan büyüktür.")
elif sayi1 < 10:
    print("Girilen sayi 10'dan küçüktür.")
else:
    print("Sayi 10'dur.")


#! ----- Örnek Alıştırmalar -----
#* Ödev 1 :  
#- Toplama ve Çıkarma Makinesi (Öncelikle bakmadan yapmaya çalışınız)
# Kullanıcıdan iki sayı alın. Ardından kullanıcıdan bir işlem seçmesini isteyin (toplama veya çıkarma) ve sonucu hesaplayarak ekrana yazdırın.

print("Sırayla iki adet sayı girin...")
sayi1 = int(input("Lütfen 1. sayıyı girin : "))
sayi2 = int(input("Lütfen 2. sayıyı girin : "))
karakter = input("""Yapmak istediğiniz işlem hangisi?\n
                 Toplama işlemi için : +\n
                 Çıkarma işlemi için : -\n
                 Çarpma işlemi için  : *\n
                 Bölme işlemi için   : /\n
İşlem yapmak istediğiniz operatörü girin ardından "Enter" tuşuna basın :  """)

if karakter == '+':
    print("Girilen sayıların toplamı : ", sayi1 + sayi2)
elif karakter == '-':
    print("{} - {} = {}".format(sayi1, sayi2, sayi1 - sayi2))
elif karakter == '*':
    print("Girilen sayıların çarpım sonucu : {}".format(sayi1 * sayi2))
elif karakter == '/':
    print("Bölme sonucu : {} / {} = {}".format(sayi1, sayi2, sayi1 / sayi2))
else:
    print("Herhangi bir operatör seçmediniz!")

# Kodumuz oldukça temiz ve çalışır durumda, temel hesaplamaları da doğru bir şekilde yapıyor. 
# Elbette henüz hata denetimlerini bilmediğimiz için gerekli denetlemeleri yapamıyoruz, örneğin kullanıcı eğer bir sayı girmezse programımız hata verecektir. Ancak merak etmeyin bunları ilerleyen konularda detaylıca öğreneceğiz şimdilik bizim görevimiz bu.



#* Örnek uygulama ;

# Diyelim ki sisteme kayıt için kullanıcı adı ve parola belirlenmesini isteyen bir program yazıyorsunuz. Yazacağınız bu programda, belirlenebilecek kullanıcı adı ve parolanın toplam uzunluğu 40 karakteri geçmesin.

kullanici_adi = input("Kullanıcı adınız : ")
parola = input("Parolanız               : ")
toplam_uzunluk = len(kullanici_adi) + len(parola)
mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"

if toplam_uzunluk > 40:
    print(mesaj.format(toplam_uzunluk))
else:
    print("Tebrikler işlem başarıyla tamamlandı. Sisteme hoş geldiniz!")
    
#* Yukarıdaki kodları açıklayalım; 
# 1 - İlk olarak, kullanıcıdan kullanıcı adını girmesi istenir ve bu değer kullanici_adi değişkenine atanır.
# 2 - Ardından, kullanıcıdan parolasını girmesi istenir ve bu değer parola değişkenine atanır.
# 3 - Kullanıcı adının uzunluğu ve parolanın uzunluğu hesaplanır ve bu uzunluklar kullanici_adi ve parola değişkenlerinin uzunlukları toplanarak toplam_uzunluk değişkenine atanır.
# 4 - Şimdi, bir if ifadesi ile toplam_uzunluk değişkeni 40'tan büyük mü diye kontrol edilir. Eğer bu koşul sağlanıyorsa, mesaj değişkeni kullanılarak kullanıcıya "Kullanıcı adı ve parolanız toplam X karakterden oluşuyor!" şeklinde bir mesaj gösterilir, burada X, toplam karakter sayısıdır.
# 5 - Eğer toplam_uzunluk 40'tan büyük değilse, else bloğu çalışır ve kullanıcıya "Tebrikler işlem başarıyla tamamlandı. Sisteme hoş geldiniz!" şeklinde bir hoş geldiniz mesajı gösterilir.

# Bu kod, kullanıcıdan kullanıcı adı ve parola bilgisi alır, bu bilgilerin toplam karakter uzunluğunu hesaplar ve bu uzunluğa göre bir karar verir. Eğer toplam uzunluk 40 karakterden fazlaysa, kullanıcıya bilgilendirici bir mesaj gösterir; aksi takdirde, kullanıcıyı başarıyla giriş yapmış olarak karşılar.

