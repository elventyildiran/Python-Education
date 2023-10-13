# Şimdi şöyle bir durum düşünün: Diyelim ki sisteme kayıt için kullanıcı adı ve parola belirlenmesini isteyen bir program yazıyorsunuz. Yazacağınız bu programda, belirlenebilecek kullanıcı adı ve parolanın toplam uzunluğu 40 karakteri geçmeyecek.

# Bu programı yazarken ilk aşamada yapmanız gereken şey, kullanıcının belirlediği kullanıcı adı ve parolanın uzunluğunu tek tek denetlemek olmalı.
# Mesela kullanıcı şöyle bir kullanıcı adı belirlemiş olsun:

#* firat_ozgul_1980

#Kullanıcının belirlediği parola ise şu olsun:

#* rT%65#$hGfUY56123

# İşte bizim öncelikle kullanıcıdan gelen bu verilerin teker teker uzunluğunu biliyor olmamız lazım, ki bu verilerin toplam 40 karakter sınırını aşıp aşmadığını denetleyebilelim.

# Peki bu verilerin uzunluğunu nasıl ölçeceğiz? Elbette bunun için verilerdeki harfleri elle tek tek saymayacağız. Bunun yerine, Python programlama dilinin bize sunduğu bir aracı kullanacağız. Peki nedir bu araç?

# Hatırlarsanız birkaç sayfa önce type() adlı bir fonksiyondan söz etmiştik. Bu fonksiyonun görevi bir verinin hangi tipte olduğunu bize bildirmekti. İşte tıpkı type() gibi, Python’da len() adlı başka bir fonksiyon daha bulunur. Bu fonksiyonun görevi ise karakter dizilerinin (ve ileride göreceğimiz gibi, başka veri tiplerinin) uzunluğunu ölçmektir. Yani bu fonksiyonu kullanarak bir karakter dizisinin toplam kaç karakterden oluştuğunu öğrenebiliriz.

#. Key : len() fonksiyonu kullanımı. (Bir verinin karakter sayısını öğrenme)

# Biz henüz kullanıcıdan nasıl veri alacağımızı bilmiyoruz. Ama şimdilik şunu söyleyebiliriz: Python’da kullanıcıdan herhangi bir veri aldığımızda, bu veri bize bir karakter dizisi olarak gelecektir. Yani kullanıcıdan yukarıdaki kullanıcı adı ve parolayı aldığımızı varsayarsak, bu veriler bize şu şekilde gelir:

#* "firat_ozgul_1980"
#ve
#* "rT%65#$hGfUY56123"

#Gördüğünüz gibi, elde ettiğimiz veriler tırnak içinde yer alıyor. Yani bunlar birer karakter dizisi. Şimdi gelin yukarıda bahsettiğimiz len() fonksiyonunu kullanarak bu karakter dizilerinin uzunluğunu ölçelim.

print(len("firat_ozgul_1980")) #16
print(len("rT%65#$hGfUY56123")) #17

#Şimdi bu ikisinin toplamına bakalım;

print(len("firat_ozgul_1980") + len("rT%65#$hGfUY56123")) # 33

# Buradan alacağımız sonuç 33 olacaktır. Demek ki kullanıcı 40 karakter limitini aşmamış. O halde programımız bu kullanıcı adı ve parolayı kabul edebilir…
# Bu arada, belki farkettiniz, belki de farketmediniz, ama burada da çok önemli bir durumla karşı karşıyayız. Gördüğünüz gibi len() fonksiyonu bize sayı değerli bir veri gönderiyor. Gelin isterseniz bunu teyit edelim:

print(type(len("firat_ozgul_1980") + len("rT%65#$hGfUY56123"))) # <class 'int'>
# len() fonksiyonunun bize sayı değerli bir veri göndermesi sayesinde bu fonksiyondan elde ettiğimiz değerleri birbiriyle toplayabildik.

# Eğer len() fonksiyonu bize sayı değil de mesela karakter dizisi verseydi, bu fonksiyondan elde ettiğimiz değerleri yukarıdaki gibi doğrudan birbiriyle aritmetik olarak toplayamazdık. Öyle bir durumda, bu iki veriyi birbiriyle toplamaya çalıştığımızda, + işleci 16 ve 17 değerlerini birbiriyle toplamak yerine bu değerleri birbiriyle birleştirerek bize ‘1617’ gibi bir sonuç verecekti.
# Her zaman söylediğimiz gibi, Python’da veri tipi kavramını çok iyi anlamak ve o anda elimizde bulunan bir verinin hangi tipte olduğunu bilmek çok önemlidir. Aksi halde programlarımızda hata yapmamız kaçınılmazdır.

# Bu kodlar, istediğimiz şeyi gayet güzel yerine getiriyor. Ama sizce de yukarıdaki kodlarda çok rahatsız edici bir durum yok mu?
# Yukarıdaki verilerle işlem yapmak için her defasında bu verileri tek tek yazmak durumunda kaldık. Oysa bunları bir değişkende gayet rahat saklayabilir ve ihtiyacımız olduğu durumda sadece bu değişken adını çağırarak basitçe işlemimizi halledebilirdik.

# len() fonksiyonunun bazı kısıtlamalarından söz edelim. Dediğimiz gibi, bu fonksiyonu kullanarak karakter dizileri içinde toplam kaç adet karakter bulunduğunu hesaplayabiliyoruz. Yalnız bu len() fonksiyonunu sayıların uzunluğunu ölçmek için kullanamıyoruz.

#! >>>len(123456)

#!Traceback (most recent call last):
#!  File "<stdin>", line 1, in <module>
#!TypeError: object of type 'int' has no len()



#! ---- Degisken Tanımlaması ---
#Şimdi yukarıdaki işlemi degiskenler yardimiyla yapalım.

isim = "firat_ozgul_1980"
sifre = "rT%65#$hGfUY56123"

print(isim) # firat_ozgul_1980
print(sifre) # rT%65#$hGfUY56123

# Yukarıda görüldüğü üzere sadece degisken ismini kullanarak basitçe veriyi alabildik.

print(len(isim) + len(sifre)) # 33

#Böyle çok daha basit değil mi? Elbette böyle çok daha basit.

print(type(len(isim) + len(sifre))) # <class 'int'>

# veya

k_adi_uzunlugu = len(isim)
print(k_adi_uzunlugu) # 16

#* Örnek 1 ;

sayi1 = 10
sayi2 = 15
topla = sayi1 + sayi2
print(topla) # 25


#! --- Değişken adı belirleme kuralları ---
# Öncelikle şurdan başlayalım ; Aşağıda görmüş  olduğunuz isimler python programlama dilinde özel anlam ifade eden kelimelerdir. Bu yüzden bunları kullanamazsınız...Aşağıda yazan bütün anahtar kelimeleri ilerleyen süreçlerde göreceğiz.
 
#* ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Değişken adları bir sayı ile başlayamaz > 3_kilo_elma = "5 TL"
# Değişken adları aritmetik işleçlerle başlayamaz >  +deger = 4576
# Değişken adları ya bir alfabe harfiyle ya da _ işaretiyle başlamalıdır > _deger = 4576 veya > deger = 4576

# Değişken adları içinde Türkçe karakterler kullanabilirsiniz. Ancak ileride beklenmedik uyum sorunları çıkması ihtimaline karşı değişken adlarında Türkçe karakter kullanmaktan kaçınmak isteyebilirsiniz.
# (Naçizane tavsiyem : Farklı bir programlama dili daha öğrenmek istiyorsanız ilerleyen zamanlarda bu yüzden değişkenlerde asla türkçe karakter kullanmamayı alışkanlık haline getirin.)

#, Yukarıda kaç adet anahtar kelime var ? Hemen bakalım ;
import keyword
print(len(keyword.kwlist)) # 35

#*Örneği yazıyla süsleyelim ;
print("Yukarıda toplam :", len(keyword.kwlist), "anahtar kelime mevcut.") # 35


#! ---- Anahtar kelimeleri değişken adı olarak kullanırsak ne olur ? ---

#* Örnek 1 ;

type = 5
print(type) # 5

# Buraya kadar bir sorun yok "type" anahtar kelimesinin bir verinin türünü öğrenmek amaçlı kullanıldığını biliyoruz. Ancak yukarıda değişken olarak tanımladık ve şuanlık bize istediğimiz sonucu sorunsuz bir şekilde verdi. Peki ileride bir verinin tipini öğrenme ihtiyacı duyduğumuz zamanda sorunsuz çalışacak mı? Hemen kontrol edelim ;

isim = "Elvent"
#!print(type(isim))

#* Exception has occurred: TypeError
#* 'int' object is not callable
#*   File "C:\Python-Education", line 107, in <module>
#*     print(type(isim))
#*           ^^^^^^^^^^
#* TypeError: 'int' object is not callable

# o da ne ! işte bir hatayla karşılaştık. Ancak bu durumdan kurtulmak için 
#* del type
# kullanıp type tipini silebiliriz. Bu yüzden degiskenlerde asla anahtar kelimeler kullanmamaya özen gösteriyoruz.

# ! ---- Uygulama Örnekleri ----

#* Örnek 1 ;
#?- 1. Cumartesi - Pazar günleri çalışmıyoruz.
#?- 2. Dolayısıyla ayda 22 gün çalışıyoruz.
#?- 3. Evden işe gitmek için kullandığımız vasıtanın ücreti 1.5 TL
#?- 4. İşten eve dönmek için kullandığımız vasıtanın ücreti 1.4 TL
#* Aylık yol masrafımızı hesaplayabilmek için gidiş ve dönüş ücretlerini toplayıp, bunları çalıştığımız gün sayısıyla çarpmamız yeterli olacaktır. Elimizdeki bu bilgiere göre aylık yol masrafımızı hesaplamak için şöyle bir formül üretebiliriz.

calisma_gunu = 22
gidis_ucreti = 1.5
donus_ucreti = 1.4
masraf = (gidis_ucreti + donus_ucreti) * calisma_gunu
print("Aylık yol masrafım : ", masraf) #63.8
# Demek ki aylık yol masrafımız 63.8 TL imiş.

# Bu arada, yukarıdaki örnekte bir şey dikkatinizi çekmiş olmalı. Aritmetik işlemi yaparken bazı sayıları parantez içine aldık. Python’da aritmetik işlemler yapılırken alıştığımız matematik kuralları geçerlidir. Yani mesela aynı anda bölme, çıkarma, toplama ve çarpma işlemleri yapılacaksa işlem öncelik sırası önce bölme ve çarpma, sonra toplama ve çıkarma şeklinde olacaktır. Elbette siz parantezler yardımıyla bu işlem sırasını değiştirebilirsiniz.

# Bu anlattıklarımıza göre, eğer yukarıda yol masrafını hesaplayan programda parantezleri kullanmazsak, işlem öncelik kuralları gereğince Python önce 22 ile 1.5’i çarpıp, çıkan sonucu 1.4 ile toplayacağı için elde ettiğimiz sonuç yanlış çıkacaktır. Bizim burada doğru sonuç alabilmemiz için önce 1.5 ile 1.4’ü toplamamız, çıkan sonucu da 22 ile çarpmamız gerekiyor. Bu sıralamayı da parantezler yardımıyla elde ediyoruz.

#* Örnek 2;

#? 1 yılda kaç gün çalıştığımızı hesaplayalım. 

aylik_calisma_gunu = 22
toplam_ay = 12
toplam_calisma_gunu = aylik_calisma_gunu * toplam_ay
print("Bir yılda toplam", toplam_calisma_gunu, "gün çalışıyoruz.") #264

#* Örnek 3 ;
#? 1 Yıldaki toplam yol masrafımızı hesaplayalım;

aylik_calisma_gunu = 22 #* 1 ayda toplam 22 gün çalışıyoruz.
toplam_ay = 12 #* 1 yılda toplam 12 ay var.
gidis_ucreti = 1.5 #* işe giderken 1.5 tl ödüyoruz
donus_ucreti = 1.4 #* dönerken 1.4 tl ödüyoruz
gunluk_masraf = gidis_ucreti + donus_ucreti #* gidis ve donus ucretini topluyoruz
toplam_masraf = aylik_calisma_gunu * toplam_ay * gunluk_masraf #* calisma gunu, toplam ay ve günlük masrafı çarpıyoruz.
print(toplam_masraf) # 765.6

#* Örnek 4 ;
#? 1 yıl içerisinde kendimize ayırdığımız uyku vaktini saat ve gün olarak hesaplayalım ;
# Ortalama olarak günlük 8 saat uykuyu baz alalım.
import math #sayıyı yuvarlamak için kullanıyoruz, ileride göreceğiz.
bir_yil = 365
bir_gun_kac_saat = 24
gunluk_uyku = 8
toplam_uyku_saati = bir_yil * gunluk_uyku
toplam_uyku_gunu = toplam_uyku_saati / bir_gun_kac_saat
print(toplam_uyku_saati)
print(toplam_uyku_gunu) # Yuvarlanmamış hali "121.66666666666667"
print(math.floor(toplam_uyku_gunu))# Yuvarlanmış hali 121

#* Örnek 5 ; 'Bir dairenin alanını (yaklaşık olarak) hesaplayan bir program yazalım.
#* Bir dairenin alanını bulmak.
#? 1- Öncelikle çap adlı bir değişken tanımlayalım
cap = 16

#? 2- Bu değeri kullanarak dairemizin yarıçapını hesaplayabiliriz. Bunun için "cap" değişkeninin değerinin yarısını almamız yeterli olacaktır;
yaricap = cap /2

#? 3- Pi sayısını 3.14159 olarak alalım.
pi = 3.14159

#? Bir dairenin alan formulü (pi)r2'dir.
alan = pi * (yaricap * yaricap)
print(alan) # 201.06176

# Görüyorsunuz ya, değişkenler işimizi nasıl da kolaylaştırıyor. Eğer yukarıdaki programda değişken kullanmasaydık kodlarımız şöyle görünecekti:

print(3.14159 * ((16/2) * (16/2))) #201.06176

# Burada yarıçap değişkeninin karesini alabilmek için bu değeri kendisiyle çarptık. Aslında gayet mantıklı ve makul bir yöntem. Kare bulmak için değeri kendisiyle çarpıyoruz. Eğer bir sayının küpünü bulmak isteseydik o sayıyı üç kez kendisiyle çarpacaktık:

#* Bir sayının küpünü bulmak ;
print(3 * 3 * 3)

# Peki ya bir sayının mesela beşinci kuvvetini hesaplamak istersek ne yapacağız? O sayıyı beş kez kendisiyle mi çarpacağız? Bu ne kadar vasat bir yöntem, değil mi?
# Elbette bir sayının herhangi bir kuvvetini hesaplamak için o sayıyı kendisiyle kuvvetince çarpmayacağız. Python’da bu tür ‘kuvvet hesaplamaları’ için ayrı bir işleç (ve fonksiyon) bulunur.

# Öncelikle kuvvet hesaplarını yapmamızı sağlayan işleçten söz edelim.
#. Key : kuvvet hesabı yapmak, sayının kuvvetini hesaplamak.
# Python’da ** adlı bir işleç bulunur. Bu işlecin görevi bir sayının kuvvetini hesaplamamızı sağlamaktır. Örneğin bir sayının 2. kuvvetini, ya da başka bir deyişle karesini hesaplamak istersek şöyle bir kod yazabiliriz:
#. Key : bir sayının karesini hesaplamak.
print(12 ** 2)

# Burada 12 sayısının 2. kuvvetini, yani karesini hesapladık. Bu bilgiyi yukarıdaki formüle uygulayalım;

alan = pi * (yaricap ** 2)
print(alan) # 201.06176

#Bu işleci herhangi bir sayının herhangi bir kuvvetini hesaplamak için kullanabiliriz elbette. Mesela 23 sayısının küpünü (yani 3. kuvvetini) hesaplayalım:
#. Key : bir sayının küpünü hesaplamak

print(23 ** 3) # 12167

# Aynı işleçten, bir sayının karekökünü hesaplamak için de yararlanabilirsiniz. Neticede bir sayının 0.5’inci kuvveti, o sayının kareköküdür:
#. Key : bir sayının karekökünü hesaplamak.

print(144 ** 0.5) # 12.0

#! --- pow() fonksiyonu ---
# Gördüğünüz gibi, kuvvet hesaplama işlemleri için bu işleç son derece kullanışlı bir araç vazifesi görüyor. Ama eğer istersek aynı iş için özel bir fonksiyondan da yararlanabiliriz. Bu fonksiyonun adı pow().

print(pow(12, 2)) # 144
print(pow(23, 3)) # 12167
print(pow(144, 0.5)) # 12.0
# Gördüğünüz gibi, pow() fonksiyonunun ilk parametresi asıl sayıyı, ikinci parametresi ise bu sayının hangi kuvvetini hesaplamak istediğimizi gösteriyor. Bu arada, fonksiyonun parantezleri içinde belirttiğimiz parametreleri birbirinden virgül ile ayırdığımızı gözden kaçırmayın.

# Dediğimiz gibi, pow() fonksiyonu, pek kullanılmayan üçüncü bir parametre daha alır. Bu fonksiyonun üçüncü parametresi şöyle kullanılır. Dikkatlice bakın:

print(pow(16, 2, 2)) # 0 
#* Bu komut şu anlama gelir:
#*      16 sayısının 2’nci kuvvetini hesapla ve çıkan sayıyı 2’ye bölüp, bölme işleminden kalan sayıyı göster!
#* 16 sayısının 2. kuvveti 256 sayısıdır. 256 sayısını 2’ye böldüğümüzde, bölme işleminin kalanı 0’dır. Yani 256 sayısı 2’ye tam bölünür…

#* Örnek ;
print(pow(11, 3, 4)) # 3
# Demek ki, 11 sayısının 3. kuvveti olan 1331 sayısı 4’e bölündüğünde, bölme işleminden kalan sayı 3 imiş…
# Dediğimiz gibi, pow() fonksiyonu genellikle sadece iki parametre ile kullanılır. Üçüncü parametrenin kullanım alanı oldukça dardır.

#! --- Değişkenlere Dair Bazı İpuçları ---

#< --- Aynı Değere Sahip Değişkenler Tanımlama ---

# Şimdi size şöyle bir soru sormama izin verin: Acaba aynı değere sahip iki değişkeni nasıl tanımlayabiliriz? Yani mesela değeri 4 sayısı olan iki farklı değişkeni nasıl belirleyeceğiz?

# Aklınıza şöyle bir çözüm gelmiş olabilir:
a = 4
b = 4

# Böylece ikisi de 4 değerine sahip a ve b adlı iki farklı değişken tanımlamış olduk. Bu tamamen geçerli bir yöntemdir. Ancak Python’da bu işlemi yapmanın daha kolay bir yolu var. Bakalım:

a = b = 4
# Bu kodlar bir öncekiyle tamamen aynı işlevi görür. Yani her iki kod da 4 değerine sahip a ve b değişkenleri tanımlamamızı sağlar.

# Bu bilgiyi kullanarak mesela bir yıl içindeki her bir ayın çektiği gün sayısını ay adlarına atayabilirsiniz:

ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = haziran = eylul = kasim = 30
subat = 28

# Böylece bir çırpıda değeri 31 olan yedi adet değişken, değeri 30 olan dört adet değişken, değeri 28 olan bir adet değişken tanımlamış olduk. Bu değişkenlerin değerine nasıl ulaşacağınızı biliyorsunuz.
print(temmuz) # 31

# Bu değişkenleri nasıl bir program içinde kullanacağınız tamamen sizin hayal gücünüze kalmış. Mesela bu değişkenleri kullanarak aylara göre doğalgaz faturasını hesaplayan bir program yazabiliriz.

#* Örnek ;  
# Hemen son gelen doğalgaz faturasını (örn. Mart ayı) elimize alıp inceliyoruz ve bu faturadan şu verileri elde ediyoruz:

#? 1 - Mart ayı doğalgaz faturasına göre sayaçtan ölçülen hacim 346 m3. Demek ki bir ayda toplam 346 m3 doğalgaz harcamışız.
#? 2 - Fatura tutarı 273.87 TL imiş. Yani 346 m3 doğalgaz tüketmenin bedeli 273.87 TL. Buna göre değişkenlerimizi tanımlayalım:

aylik_sarfiyat = 346
fatura_tutari = 273.87

#? Bu bilgiyi kullanarak doğalgazın birim fiyatını hesaplayabiliriz. Formülümüz şöyle olmalı:

birim_fiyat = fatura_tutari / aylik_sarfiyat
print(birim_fiyat) # 0.7915317919075144
# Demek ki doğalgazın m3 fiyatı (vergilerle birlikte yaklaşık) 0.79 TL’ye karşılık geliyormuş.
# Bu noktada günlük ortalama doğalgaz sarfiyatımızı da hesaplamamız gerekiyor:

gunluk_sarfiyat = aylik_sarfiyat / mart
print(gunluk_sarfiyat) # 11.161290322580646
# Demek ki Mart ayında günlük ortalama 11 m3 doğalgaz tüketmişiz.

# Bütün bu bilgileri kullanarak Nisan ayında gelecek faturayı tahmin edebiliriz:
nisan_faturasi = birim_fiyat * gunluk_sarfiyat * nisan
print(nisan_faturasi) # 265.03548387096777

# Gördüğünüz gibi, aynı anda birden fazla değişken tanımlayabilmek işlerimizi epey kolaylaştırıyor.

#< --- Değişkenlerin Değerini Takas Etme ---

# Diyelim ki, işyerinizdeki personelin unvanlarını tuttuğunuz bir veritabanı var elinizde. Bu veritabanında şuna benzer ilişkiler tanımlı:
osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje Sorumlusu"

# İlerleyen zamanda işvereniniz sizden Osman ve Mehmet’in unvanlarını değiştirmenizi talep edebilir. Yani Osman’ı Proje Sorumlusu, Mehmet’i de Araştırma Geliştirme Müdürü yapmanızı isteyebilir sizden.

# Patronunuzun bu isteğini Python’da çok rahat bir biçimde yerine getirebilirsiniz. Dikkatlice bakın:

osman, mehmet = mehmet, osman
print(osman) # Proje Sorumlusu
print(mehmet) # Araştırma Geliştirme Müdürü