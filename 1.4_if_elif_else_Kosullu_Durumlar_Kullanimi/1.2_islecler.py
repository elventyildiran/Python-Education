# Bu bölümde, aslında pek de yabancısı olmadığımız ve hatta önceki derslerimizde üstünkörü de olsa değindiğimiz bir konuyu çok daha ayrıntılı bir şekilde ele alacağız. Burada anlatacağımız konu size yer yer sıkıcı gelebilir. Ancak bu konuyu hakkıyla öğrenmenizin, programcılık maceranız açısından hayati önemde olduğunu rahatlıkla söyleyebilirim.

# Bu bölümün konusu işleçler. Peki nedir bu ‘işleç’ denen şey?

# İngilizce’de operator adı verilen işleçler, sağında ve solunda bulunan değerler arasında bir ilişki kuran işaretlerdir. Bir işlecin sağında ve solunda bulunan değerlere ise işlenen (operand) adı veriyoruz.

#- Türkçede işleç yerine operatör, işlenen yerine de operant dendiğine tanık olabilirsiniz.


# Biz bu bölümde işleçleri altı başlık altında inceleyeceğiz:

#- 1 - Aritmetik İşleçler
#- 2 - Karşılaştırma İşleçleri
#- 3 - Bool İşleçleri
#- 4 - Değer Atama İşleçleri
#- 5 - Aitlik İşleçleri
#- 6 - Kimlik İşleçleri

# Gördüğünüz gibi, işlememiz gereken konu çok, gitmemiz gereken yol uzun. O halde hiç vakit kaybetmeden, aritmetik işleçlerle yolculuğumuza başlayalım.

#! ----- Aritmetik İşleçler -----

# Dedik ki, sağında ve solunda bulunan değerler arasında bir ilişki kuran işaretlere işleç (operator) adı verilir. Önceki derslerimizde temel işleçlerin bazılarını öğrenmiştik. İsterseniz bunları şöyle bir hatırlayalım:

#, + toplama

#, - çıkarma

#, * çarpma

#, / bölme

#, ** kuvvet

# Bu işleçlere aritmetik işleçler adı verilir. Aritmetik işleçler; matematikte kullanılan ve sayılarla aritmetik işlemler yapmamızı sağlayan yardımcı araçlardır.

# Dilerseniz bu tanımı bir örnekle somutlaştıralım:
print(45 + 33) # 78

# Burada 45 ve 33 değerlerine işlenen (operand) adı verilir. Bu iki değer arasında yer alan + işareti ise bir işleçtir (operator). Dikkat ederseniz + işleci 45 ve 33 adlı işlenenler arasında bir toplama ilişkisi kuruyor.

# Bir örnek daha verelim:
print(23 * 46) # 1058

# Burada da 23 ve 46 değerleri birer işlenendir. Bu iki değer arasında yer alan * işareti ise, işlenenler arasında bir çarpma ilişkisi kuran bir işleçtir.

# Ancak bir noktaya özellikle dikkatinizi çekmek istiyorum. Daha önceki derslerimizde de değindiğimiz gibi, + ve * işleçleri Python’da birden fazla anlama gelir. Örneğin yukarıdaki örnekte + işleci, işlenenler arasında bir toplama ilişkisi kuruyor. Ama aşağıdaki durum biraz farklıdır:

print("istihza" + ".com") # 'istihza.com'

# Burada + işleci işlenenler (“istihza” ve “.com”) arasında bir birleştirme ilişkisi kuruyor.

# Tıpkı + işlecinde olduğu gibi, * işleci de Python’da birden fazla anlama gelir. Bu işlecin, çarpma ilişkisi kurma işlevi dışında tekrar etme ilişkisi kurma işlevi de vardır. Yani:

print("hızlı " * 2) # 'hızlı hızlı'

# veya.........
print("-" * 30) #, ------------------------------

# Burada * işlecinin, sayılar arasında çarpma işlemi yapmak dışında bir görev üstlendiğini görüyoruz.
# Python’da bu tür farklar, yazacağınız programın sağlıklı çalışabilmesi açısından büyük önem taşır. O yüzden bu tür farklara karşı her zaman uyanık olmamız gerekiyor.


# + ve * işleçlerinin aksine / ve - işleçleri ise işlenenler arasında sadece bölme ve çıkarma ilişkisi kurar. Bu işleçler tek işlevlidir:

print(25 / 4 ) # 6.25

print(10 - 5) # 5

# Önceki derslerde gördüğümüz ve yukarıda da tekrar ettiğimiz dört adet temel aritmetik işlece şu iki aritmetik işleci de ekleyelim:

#! % modülüs
#! // taban bölme

# İlk önce modülüsün ne olduğunu ve ne işe yaradığını anlamaya çalışalım.

# Şu bölme işlemine bir bakın:
"""30| 4
     |---
-  28| 7
-------
  02
"""""

# Burada 02 sayısı bölme işleminin kalanıdır. İşte modülüs denen işleç de bölme işleminden kalan bu değeri gösterir. Yani:

print(30 % 4 ) # 2

# Gördüğünüz gibi modülüs işleci (%) gerçekten de bölme işleminden kalan sayıyı gösteriyor… Peki bu bilgi ne işimize yarar?

# Mesela bu bilgiyi kullanarak bir sayının tek mi yoksa çift mi olduğunu tespit edebiliriz:

sayi = int(input("Bir sayı girin : "))
if sayi % 2 ==  0:
    print("Sayi çift sayıdır.")
else:
    print("Sayı tek sayıdır.")

# Eğer bir sayı 2’ye bölündüğünde kalan değer 0 ise o sayı çifttir. Aksi halde o sayı tektir.

# Elbette modülüs işlecini bir sayının yalnızca 2’ye tam bölünüp bölünmediğini denetlemek için kullanmıyoruz. Bu işleci kullanarak herhangi bir sayının herhangi bir sayıya tam bölünüp bölünmediğini de denetleyebilirsiniz. Örneğin:

print(45 % 4) # 1

print(36 % 9) # 0

# Bu bilgiyi kullanarak mesela şöyle bir program yazabilirsiniz:

bolunen = int(input("Bir sayı girin : "))
bolen = int(input("Bir sayı daha girin : "))

sablon = "{} sayısı {} sayısına tam".format(bolunen, bolen)

if bolunen % bolen == 0:
    print(sablon, "bölünüyor!")
else:
    print(sablon, "bölünmüyor!")

# Programımız, kullanıcının girdiği ilk sayının ikinci sayıya tam bölünüp bölünmediğini hesaplıyor ve sonuca göre kullanıcıyı bilgilendiriyor. Bu kodlarda özellikle şu satıra dikkat edin:

#< if bölünen % bölen == 0:

# Programımızın temelini bu kod oluşturuyor. Çünkü bir sayının bir sayıya tam bölünüp bölünmediğini bu kodla belirliyoruz. Eğer bir sayı başka bir sayıya bölündüğünde kalan değer, yani modülüs 0 ise, o sayı öbür sayıya tam bölünüyor demektir.

# Ayrıca bir sayının son basamağını elde etmek için de modülüsten yararlanabilirsiniz. Herhangi bir tamsayı 10’a bölündüğünde kalan (yani modülüs), bölünen sayının son basamağı olacaktır:

print(65 % 10) # 5 
print(543 % 10) # 3

# Programlama tecrübeniz arttıkça, aslında modülüsün ne kadar faydalı bir araç olduğunu kendi gözlerinizle göreceksiniz.

# Modülüs işlecini örnekler eşliğinde ayrıntılı bir şekilde incelediğimize göre sıra geldi taban bölme işlecini açıklamaya…

# Öncelikle şu örneği inceleyelim
print(5 / 2) # 2.5

# Burada, bildiğimiz bölme işlecini (/) kullanarak basit bir bölme işlemi yaptık. Elde ettiğimiz sonuç doğal olarak 2.5.

# Matematikte bölme işleminin sonucunun kesirli olması durumuna ‘kesirli bölme’ adı verilir. Bunun tersi ise tamsayılı bölme veya taban bölmedir. Eğer herhangi bir sebeple kesirli bölme işlemi değil de taban bölme işlemi yapmanız gerekirse // işlecinden yararlanabilirsiniz:

print(5 // 2) # 2

# Gördüğünüz gibi, // işleci sayesinde bölme işleminin sonucu kesirli değil, tamsayı olarak elde ediliyor.

# Yukarıda yaptığımız taban bölme işlemi şununla aynı anlama gelir:

print(5 / 2) # 2

# Daha açık ifade etmemiz gerekirse :
a = 5 / 2
print(a) # 2.5
print(int(a)) # 2

# Burada olan şu: 5 / 2 işleminin sonucu bir kayan noktalı sayıdır (2.5). Bunu şu şekilde teyit edebiliriz:

a = 5 / 2
print(type(a)) # <class 'float'>

# Buradaki float çıktısının floating point number, yani kayan noktalı sayı anlamına geldiğini biliyorsunuz.c

# Bu kayan noktalı sayının sadece tabanını elde etmek için bu sayıyı tamsayıya (integer) çevirmemiz yeterli olacaktır. Yani:
print(int(a)) # 2

#! ---- round() fonksiyonu -----
#. Key sayı yuvarlama, round() kullanımı, round fonksiyonu kullanımı
# Bu arada yeri gelmişken round() adlı bir gömülü fonksiyondan bahsetmeden geçmeyelim. Eğer bir sayının değerini yuvarlamanız gerekirse round() fonksiyonundan yararlanabilirsiniz. Bu fonksiyon şöyle kullanılır:

print(round(2.55)) # 3

# Gördüğünüz gibi, round() fonksiyonuna parametre olarak bir sayı veriyoruz. Bu fonksiyon da bize o sayının yuvarlanmış halini döndürüyor. Bu fonksiyonu kullanarak yuvarlanacak sayının noktadan sonraki hassasiyetini de belirleyebilirsiniz. Örneğin:

print(round(2.55,1)) # 2.5
# Burada ikinci parametre olarak 1 sayısını verdiğimiz için, noktadan sonraki bir basamak görüntüleniyor. Bir de şuna bakalım:

print(round(2.68, 1)) # 2.7


# Burada da yuvarlama işlemi yapılırken noktadan sonra bir basamak korunuyor. Eğer 1 sayısı yerine 2 sayısını kullanırsanız, yukarıdaki örnek şu çıktıyı verir:

print(round(2.68, 2)) # 2.68
# round() fonksiyonunun çalışma prensibini anlamak için kendi kendinize örnekler yapabilirsiniz.

#.Key : Bir sayının karesini hesaplamak.
# işleci (**) idi. Mesela bu işleci kullanarak bir sayının karesini hesaplayabileceğimizi biliyorsunuz:
print(25 ** 2) #325

#. Key : Bir sayının karekökünü hesaplamak. Karekök hesaplama
# Bir sayının 2. kuvveti o sayının karesidir. Bir sayının 0.5. kuvveti ise o sayının kareköküdür:
print(625 ** 0.5) # 25.0

# Bu arada, eğer karekökün kayan noktalı sayı cinsinden olması hoşunuza gitmediyse, bu sayıyı int() fonksiyonu ile tam sayıya çevirebileceğinizi biliyorsunuz.

# Kuvvet hesaplamaları için ** işlecinin yanısıra pow() adlı bir fonksiyondan da yararlanabileceğimizi öğrenmiştik:

print(pow(25, 2)) # 625

# Bildiğiniz gibi pow() fonksiyonu aslında toplam üç parametre alabiliyor:

print(pow(25, 2, 5)) # 0

# Bu işlemin şununla aynı anlama geliyor:

print((25 ** 2) % 5) # 0
# Yani pow(25, 2, 5) gibi bir komut verdiğimizde, 25 sayısının 2. kuvvetini alıp, elde ettiğimiz sayının 5’e bölünmesinden kalan sayıyı hesaplamış oluyoruz.

#! ----- Karşılaştırma İşleçleri -----
#.Key : Karşılaştırma işleçleri, karşılaştırma operatorleri

#- == Eşittir
#- != Eşit değildir
#- >  Büyüktür
#- <  Küçüktür
#- >= Büyük eşittir
#- <= Küçük eşittir.

# Bu işleçlerin hiçbiri size yabancı değil, zira bunların hepsini aslında daha önceki derslerde verdiğimiz örneklerde kullanmıştık

parola = "xyz05"
soru = input("paroılanız : ")

if soru == parola:
    print("Doğru parola!")
elif soru != parola:
    print("Yanlış parola!")

# Burada soru değişkeniyle kullanıcıdan alınan verinin, programın başında tanımladığımız parola değişkeninin değerine eşit olup olmadığını sorguluyoruz. Buna göre, eğer kullanıcıdan gelen veri parolayla eşleşiyorsa (if soru == parola), kullanıcıyı parolanın doğru olduğu konusunda bilgilendiriyoruz (print("doğru parola!")). Ama eğer kullanıcıdan gelen veri parolayla eşleşmiyorsa (elif soru != parola), o zaman da kullanıcıya parolanın yanlış olduğunu bildiriyoruz (print("yanlış parola!")).

# Yukarıdaki örnekte == (eşittir) ve != (eşit değildir) işleçlerinin kullanımını örneklendirdik. Öteki karşılaştırma işleçlerinin de nasıl kullanıldığını biliyorsunuz. Basit bir örnek verelim:
    
sayı = input("sayı: ")

if int(sayı) <= 100:
    print("sayı 100 veya 100'den küçük")

elif int(sayı) >= 100:
    print("sayı 100 veya 100'den büyük")


#! ----- Bool İşleçleri -----
#.Key bool kullanımı. bool nasıl kullanılır ?
# Nedir bu bool denen şey?

# Bilgisayar bilimi iki adet değer üzerine kuruludur: 1 ve 0. Yani sırasıyla True ve False. Bilgisayar biliminde herhangi bir şeyin değeri ya True, ya da False’tur. İşte bu True ve False olarak ifade edilen değerlere bool değerleri adı verilir (George Boole adlı İngiliz matematikçi ve filozofun adından). Türkçe olarak söylemek gerekirse, True değerinin karşılığı Doğru, False değerinin karşılığı ise Yanlış’tır.

# Örneğin :
a = 1

# Burada a adlı bir değişken tanımladık. Bu değişkenin değeri 1. Şimdi bu değişkenin değerini sorgulayalım:
# a değeri 1'e eşit mi ?
print(a == 1)  # True

# Gördüğünüz gibi, a == 1 sorgusu True (Doğru) çıktısı veriyor. Çünkü a değişkeninin değeri gerçekten de 1. Bir de şunu deneyelim:
print(a == 2) # False

# Burada da a değişkeninin değerinin 2 sayısına eşdeğer olup olmadığını sorguladık. a değişkeninin değeri 2 olmadığı için de Python bize False (Yanlış) çıktısı verdi.

# Gördüğünüz gibi, bool işleçleri herhangi bir ifadenin doğruluğunu veya yanlışlığını sorgulamak için kullanılabiliyor. Buna göre, eğer bir sorgulamanın sonucu doğru ise True, eğer yanlış ise False çıktısı alıyoruz.

# Bool işleçleri sadece yukarıda verdiğimiz örneklerdeki gibi, salt bir doğruluk-yanlışlık sorgulamaya yarayan araçlar değildir. Bilgisayar biliminde her şeyin bir bool değeri vardır. Bununla ilgili genel kuralımız şu: 0 değeri ve boş veri tipleri False’tur. Bunlar dışında kalan her şey ise True’dur.

# Bu durumu bool() adlı özel bir fonksiyondan yararlanarak teyit edebiliriz:

print(bool(3)) # True

print(bool("Elma")) # True

print(bool(" ")) # True

print(bool("  ")) # True

print(bool("asdasd")) # True

print(bool(0)) # False

print(bool("")) # False

# Gördüğünüz gibi, gerçekten de 0 sayısının ve boş karakter dizilerinin bool değeri False’tur. Geri kalan her şey ise True’dur.

#- 0’ın bir sayı, “0”’ın ise bir karakter dizisi olduğunu unutmayın. Sayı olan 0’ın bool değeri False’tur, ama karakter dizisi olan “0”’ın değeri True’dur.

# Yukarıdaki örneklere göre, içinde herhangi bir değer barındıran karakter dizileri (0 hariç) True çıktısı veriyor. Burada söylediğimiz şey bütün veri tipleri için geçerlidir. Eğer herhangi bir veri tipi herhangi bir değer içermiyorsa o veri tipi False çıktısı verir.

# Peki bu bilgi bizim ne işimize yarar? Yani mesela boş veri tiplerinin False, içinde bir veri barındıran veri tiplerinin ise True olması bizim için neden bu kadar önemli? Bunu birazdan açıklayacağız. Ama önce isterseniz, bool değerleri ile ilgili çok önemli bir konuya değinelim.

# Belki kendiniz de farketmişsinizdir; bool değerleri Python’da koşul belirten if, elif ve else deyimlerinin de temelini oluşturur. Şu örneği ele alalım mesela:

isim = input("İsminiz : ")

if isim == "Ferhat":
    print("ne güzel bir isim bu")
else:
    print(isim, "ismini pek sevmem!")
    
# Burada if isim == "Ferhat" dediğimizde, aslında Python’a şu emri vermiş oluyoruz:

# Eğer isim == "Ferhat" ifadesi True ise…

# Bunu teyit etmek için şöyle bir kod yazabilirsiniz:

isim = input("İsminiz : ")
print(isim == "Ferhat")

# Eğer burada kullanıcı ‘Ferhat’ ismini girecek olursa programımız True çıktısı verir. Ama eğer kullanıcı başka bir isim girerse bu kez False çıktısını alırız. İşte koşul bildiren deyimler, karar verme görevini, kendilerine verilen ifadelerin bool değerlerine bakarak yerine getirir. Dolayısıyla yukarıdaki örneği şu şekilde Türkçeye çevirebiliriz:

# Eğer isim == "Ferhat" ifadesinin bool değeri True ise, Ne güzel bir isim bu! çıktısı ver! Ama eğer isim == "Ferhat" ifadesinin bool değeri True dışında herhangi bir şey ise (yani False ise), … ismini pek sevmem! çıktısı ver!


# Hatırlarsanız içi boş veri tiplerinin bool değerinin her zaman False olacağını söylemiştik.
# Herhangi bir değere sahip veri tiplerinin bool değeri ise her zaman True olur (0 hariç).


# İçi boş veri tiplerinin bool değerinin her zaman False olacağı bilgisini kullanarak şöyle bir uygulama yazabiliriz:

kullanici = input("Kullanıcı adınız : ")

if bool(kullanici) == True:
    print("Teşekkürler!")
else:
    print("Kullanıcı adı alanı boş bırakılamaz!")

# Burada şöyle bir emir verdik:
# “Eğer kullanıcı değişkeninin bool değeri True ise Teşekkürler! çıktısı ver! Değilse Kullanıcı adı alanı boş bırakılamaz! uyarısını göster!

# Yalnız bu noktada şöyle bir uyarı yapalım. Yukarıdaki komutlar sözdizimi açısından tamamen doğru olsa da, etrafta yukarıdakine benzer bir kullanımı pek görmezsiniz. Aynı iş için genellikle şöyle bir şeyler yazılır:

kullanici = input("Kullanıcı adınız : ")

if kullanici:
    print("Teşekkürler")
else:
    print("Kullanici adı boş bırakılamaz!")

# Gördüğünüz gibi, if bool(kullanıcı) == True: kodunu if kullanıcı: şeklinde kısaltabiliyoruz. Bu ikisi tamamen aynı anlama gelir. Yani ikisi de ‘kullanıcı değişkeninin bool değeri True ise…’ demektir.

# Bool işleçleri, bool değerlerinden birini elde etmemizi sağlayan işleçlerdir. Bu işleçler şunlardır:

#! ----- and işleci -----
#. Key : and işleci kullanımı, and kullanımı.
# Önce and ile başlayalım…

# Türkçe söylemek gerekirse and ‘ve’ anlamına gelir. Peki bu and ne işimize yarar? Çok basit bir örnek verelim:
# Hatırlarsanız geçen bölümde koşullu durumlara örnek verirken şöyle bir durumdan bahsetmiştik:

# Diyelim ki Google’ın Gmail hizmeti aracılığıyla bir e.posta hesabı aldınız. Bu hesaba gireceğiniz zaman Gmail size bir kullanıcı adı ve parola sorar. Siz de kendinize ait kullanıcı adını ve parolayı sayfadaki kutucuklara yazarsınız. Eğer yazdığınız kullanıcı adı ve parola doğruysa hesabınıza erişebilirsiniz. Ama eğer kullanıcı adınız ve parolanız doğru değilse hesabınıza erişemezsiniz. Yani e.posta hesabınıza erişmeniz, kullanıcı adı ve parolayı doğru girme koşuluna bağlıdır.

# Burada çok önemli bir nokta var. Kullanıcının Gmail sistemine girebilmesi için hem kullanıcı adını hem de parolayı doğru yazması gerekiyor. Yani kullanıcı adı veya paroladan herhangi biri yanlış ise sisteme giriş mümkün olmayacaktır.

# Yukarıdaki durumu taklit eden bir programı, şu ana kadar olan bilgilerimizi kullanarak şöyle yazabiliyoruz

kullanici_adi = input("Kullanici adı : ")
parola = input("Parolanız :")

if kullanici_adi == "aliveli":
    if parola == "1234567":
        print("Sisteme giriş başarıyla sağlandı.")
    else:
        print("Yanlış kullanıcı adı veya parola.")
else:
    print("Yanlış kullanıcı adı veya parola.")

# Burada yeni bir bilgiyle daha karşılaşıyoruz. Gördüğünüz gibi, burada if deyimlerini iç içe kullandık. Python’da istediğiniz kadar iç içe geçmiş if deyimi kullanabilirsiniz. Ancak yazdığınız bir programda eğer üçten fazla iç içe if deyimi kullandıysanız, benimsediğiniz yöntemi yeniden gözden geçirmenizi tavsiye ederim. Çünkü iç içe geçmiş if deyimleri bir süre sonra anlaşılması güç bir kod yapısı ortaya çıkarabilir. Neyse… Biz konumuza dönelim.

# Yukarıdaki yazdığımız programda kullanıcının sisteme giriş yapabilmesi için hem kullanıcı adını hem de parolayı doğru girmesi gerekiyor. Kullanıcı adı ve paroladan herhangi biri yanlışsa sisteme girişe izin verilmiyor. Ancak yukarıdaki yöntem dolambaçlıdır. Halbuki aynı işlevi yerine getirmenin, Python’da çok daha kolay bir yolu var. Bakalım:

kullanici_adi = input("Kullanici adı : ")
parola = input("Parolanız :")

if kullanici_adi == "aliveli" and parola == "1234567":
    print("Giriş başarıyla sağlandı.")
else:
    print("Kullanıcı adı veya parola hatalı!")
    
# Burada and işlecini nasıl kullandığımızı görüyorsunuz. Bu işleci kullanarak iki farklı ifadeyi birbirine bağladık. Böylece kullanıcının sisteme girişini hem kullanıcı adının hem de parolanın doğru olması koşuluna dayandırdık.

# Peki and işlecinin çalışma mantığı nedir? Dediğim gibi, and Türkçede ‘ve’ anlamına geliyor. Bu işleci daha iyi anlayabilmek için şu cümleler arasındaki farkı düşünün:

# a - Toplantıya Ali ve Veli katılacak.
# b - Toplantıya Ali veya Veli katılacak.

# İlk cümlede ‘ve’ bağlacı kullanıldığı için, bu cümlenin gereğinin yerine getirilebilmesi, hem Ali’nin hem de Veli’nin toplantıya katılmasına bağlıdır. Sadece Ali veya sadece Veli’nin toplantıya katılması durumunda bu cümlenin gereği yerine getirilememiş olacaktır.

# İkinci cümlede ise toplantıya Ali ve Veli’den herhangi birisinin katılması yeterlidir. Toplantıya sadece Ali’nin katılması, sadece Veli’nin katılması veya her ikisinin birden katılması, bu cümlenin gereğinin yerine getirilebilmesi açısından yeterlidir.

# İşte Python’daki and işleci de aynı bu şekilde işler.

#! ----- or işleci -----
#.Key : or kullanımı, or işleci kullanımı.
# Tıpkı and gibi bir bool işleci olan or’un Türkçede karşılığı ‘veya’dır. Yukarıda ‘Toplantıya Ali veya Veli katılacak.’ cümlesini tartışırken aslında bu or kelimesinin anlamını açıklamıştık. Hatırlarsanız and işlecinin True çıktısı verebilmesi için bu işleçle bağlanan bütün önermelerin True değerine sahip olması gerekiyordu. or işlecinin True çıktısı verebilmesi için ise or işleciyle bağlanan önermelerden herhangi birinin True çıktısı vermesi yeterli olacaktır. 

# and ve or işleçlerini öğrendiğimize göre, bir sınavdan alınan notların harf karşılıklarını gösteren bir uygulama yazabiliriz:

x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")

elif x >= 90 and x <= 100:
    print("A aldınız.")

elif x >= 80 and x <= 89:
    print("B aldınız.")

elif x >= 70 and x <= 79:
    print("C aldınız.")

elif x >= 60 and x <= 69:
    print("D aldınız.")

elif x >= 0 and x <= 59:
    print("F aldınız.")

# Bu programda eğer kullanıcı 100’den büyük ya da 0’dan küçük bir sayı girerse Böyle bir not yok uyarısı alacaktır. 0-100 arası notlarda ise, her bir not aralığına karşılık gelen harf görüntülenecektir. 

# Hatta yukarıdaki kodları şöyle de yazabilirsiniz:

x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")

#90 sayısı x'ten küçük veya x'e eşit,
#x sayısı 100'den küçük veya 100'e eşit ise,
#Yani x, 90 ile 100 arasında bir sayı ise
elif 90 <= x <= 100:
    print("A aldınız.")

#80 sayısı x'ten küçük veya x'e eşit,
#x sayısı 89'dan küçük veya 89'a eşit ise,
#Yani x, 80 ile 89 arasında bir sayı ise
elif 80 <= x <= 89:
    print("B aldınız.")

elif 70 <= x <= 79:
    print("C aldınız.")

elif 60 <= x <= 69:
    print("D aldınız.")

elif 0 <= x <= 59:
    print("F aldınız.")
    
# Bu kodlar bir öncekiyle aynı işi yapar. Yorumlardan da göreceğiniz gibi, bu iki kod arasında sadece mantık farkı var.

# Hatta, daha da ileri giderek aynı kodu çok daha basit hale getirmek isterseniz, aşağıdaki koda bakabilirsiniz.:

x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")

elif x >= 90:
    print("A aldınız.")

elif x >= 80:
    print("B aldınız.")

elif x >= 70:
    print("C aldınız.")

elif x >= 60:
    print("D aldınız.")

elif x >= 0:
    print("F aldınız.")
    

#! ----- not işleci kullanımı -----
#. Key : not işleci kullanımı, not kullanımı.

# Bu kelimenin İngilizce’deki anlamı ‘değil’dir. Bu işleci şöyle kullanıyoruz:

a = 23
print(not a) # False

a = ""
print(not a) # True

# Bu işleç, özellikle kullanıcı tarafından bir değişkene veri girilip girilmediğini denetlemek için kullanılabilir. Örneğin:

parola = input("Parolanız :  ")

if not parola:
    print("Parola boş bırakılamaz!")
    
# Eğer kullanıcı herhangi bir parola belirlemeden doğrudan Enter tuşuna basacak olursa parola değişkeninin değeri boş bir karakter dizisi olacaktır. Yani parola = "". Boş veri tiplerinin bool değerinin False olacağını biliyoruz. Dolayısıyla, yukarıdaki gibi bir örnekte, kullanıcı parolayı boş geçtiğinde not parola kodu True verecek ve böylece ekrana “Parola boş bırakılamaz!” karakter dizisi yazdırılacaktır. Eğer yukarıdaki örneğin mantığını kavramakta zorluk çekiyorsanız şu örnekleri incelemenizi öneririm:

parola = ""
print(bool(parola)) # False

print(bool(not parola)) # True

parola = "1234"
print(bool(parola)) # True

print(bool(not parola)) # False

# Aslında yukarıdaki örneklerde şuna benzer sorular sormuş gibi oluyoruz:

parola = ""
bool(parola) #parola boş bırakılmamış, değil mi?
# False #Hayır, parola boş bırakılmış.

bool(not parola) #parola boş bırakılmış, değil mi?
# True #Evet, parola boş bırakılmış

# Kendi kendinize pratik yaparak bu işlecin görevini daha iyi anlayabilirsiniz.

# Böylece kısmen çetrefilli bir konu olan bool işleçlerini de geride bırakmış olduk. Sırada değer atama işleçleri var

#! ----- Değer Atama İşleçleri -----
#. Key : Değer atama işleci, değer atama operatorleri kullanımı.

#- += işleci

# Bu işlecin ne işe yaradığını anlamak için şöyle bir örnek düşünün:

a = 23

# a  değerine mesela 5 ekleyip bu değeri 28’e eşitlemek için ne yapmamız lazım? Tabii ki şunu:

a = a + 5
print(a) # 28

# Burada yaptığımız şey çok basit: a değişkeninin taşıdığı değere 5 ilave ediyoruz ve daha sonra bu değeri tekrar a değişkenine atıyoruz. Aynı işlemi çok daha kolay bir şekilde de yapabiliriz:

a = 23
a += 5
print(a) # 28

# Bu kod, yukarıdakiyle tamamen aynı anlama gelir. Ama bir önceki koda göre çok daha verimlidir. Çünkü a += 5 kodunda Python a değişkeninin değerini sadece bir kez kontrol ettiği için, işlemi a = a + 5 koduna göre daha hızlı yapacaktır.







#- -= işleci

#  Bir önceki += işleci toplama işlemi yapıp, ortaya çıkan değeri tekrar aynı değişkene atıyordu. -= işleci de buna benzer bir işlem gerçekleştirir:
a = 23
a -= 5
print(a) # 18

# Yukarıdaki kullanım şununla tamamen aynıdır:

a = 23
a = a - 5
print(a) # 18

# Ancak tıpkı += işlecinde olduğu gibi, -= işleci de alternatifine göre daha hızlı çalışan bir araçtır.


#- /= işleci

# Bu işlecin çalışma mantığı da yukarıdaki işleçlerle aynıdır:

a = 30
a /= 3
print(a) # 10

# Yukarıdaki işlem de şununla tamamen aynıdır:

a = 30
a = a / 3
print(a) # 10





#- *= işleci

# Bu da ötekiler gibi, çarpma işlemi yapıp, bu işlemin sonucunu aynı değişkene atar:

a = 20
a *= 2
print(a) # 40

# Yukarıdaki işlemin aynısı

a = 20
a = a * 2
print(a) # 40






#- %= işleci

# Bu işlecimiz ise bölme işleminden kalan sayıyı aynı değişkene atar:

a = 40
a %= 3
print(a) # 1

# Bu işleç de şuna eşdeğerdir:

a = 40
a = a % 3
print(a) # 1






#-  **= işleci

# Bu işlecin ne yaptığını tahmin etmek zor değil. Bu işlecimiz, bir sayının kuvvetini hesapladıktan sonra çıkan değeri aynı değişkene atıyor:

a = 12
a **= 2
print(a) # 144

# Eş değeri

a = 12
a = a ** 2
print(a)








#- //= işleci

# Değer atama işleçlerinin sonuncusu olan //= işlecinin görevi ise taban bölme işleminin sonucunu aynı değişkene atamaktır:

a = 5
a //= 2
print(a) # 2


# Eşdeğeri:
a = 5
a = a // 2
print(a) # 2


# Bu işleçler arasından, özellikle += ve -= işleçleri işinize bir hayli yarayacak.

# Bu arada eğer bu işleçleri kullanırken mesela += mi yoksa =+ mı yazacağınızı karıştırıyorsanız, şöyle düşünebilirsiniz:

a = 5
a += 5
print(a) # 10

# Burada, değeri 5 olan bir a değişkenine 5 daha ekleyip, çıkan sonucu tekrar a değişkenine atadık. Böylece değeri 10 olan bir a değişkeni elde ettik. += işlecinin doğru kullanımı yukarıdaki gibidir. Bir de yukarıdaki örneği şöyle yazmayı deneyelim:

a = 5
a =+ 5
print(a) # 5


# Burada + işleci ile = işlecinin yerini değiştirdik.

# a =+ 5 satırına dikkatlice bakın. Aslında burada yaptığımız şeyin a = +5 işlemi olduğunu, yani a değişkenine +5 gibi bir değer verdiğimizi göreceksiniz. Durum şu örnekte daha net görünecektir:

a = 5
a =- 5
print(a) # -5

# Gördüğünüz gibi, a =- 5 yazdığımızda, aslında yaptığımız şey a değişkenine -5 değerini vermekten ibarettir. Yani a = -5.












#- := işleci
#. Key, := işleci kullanımı, walrus işleci kullanımı, walrus kullanımı.
#! Walrus operatörü olarak da bilinen bu işleç, Python’un 3.8 versiyonu ile eklenmiştir. Bundan önceki versiyonlarda bulunmamaktadır ve çalışmayacaktır. SyntaxError hatası verecektir.

# Bu işleç biraz garip gözüküyor olabilir. Ne yaptığını bakarak kestirmek de biraz zor. En iyisi bir örnekle başlayalım:

giriş = len(input("Adın ne? "))

if giriş < 4:
    print("Adın kısaymış.")
elif giriş < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")
    
# Gördüğünüz gibi girilen karakter dizisinin uzunluğuna göre ekrana bir çıktı yazdırmaktayız. Python3.8’e sahipseniz vereceğimiz örnekleri kendiniz de deneyebilirsiniz. Bir de := işleci ile bu kodu nasıl yazabileceğimize bakalım:

if (giris := len(input("Adın ne?")) ) < 4:
    print("Adın kısaymış.")
elif giris < 6:
    print("Adın biraz uzunmuş")
else:
    print("Adın çok uzunmuş.")
    
    
# Burada giriş değişkenine değer atamayı if ifadesinin içinde yaptık. Normalde böyle bir işlemi = ile yapamazdık :
#< if ( giriş = len(input("Adın ne? ")) ) < 4:
#< SyntaxError: invalid syntax

# Fark edebileceğiniz gibi walrus operatörü bizi bir satır fazladan yazmaktan kurtardı. Kullanıcıdan alınan bilginin giriş değişkenine nasıl atandığına dikkat edin. giriş değişkeninden sonra := işlecini kullanıyoruz ve aynı zamanda değişken atamasını yaptığımız bölümün tamamını parantez içine alıyoruz. Peki bu parantezi koymaz isek ne olur? Gelin bir örnek ile de onu deneyelim:

if giris := len(input("Adın ne?")) < 4:
    print(giris)

# Eğer bu kodu çalıştırsanız ekrana True yazıldığını veya hiçbir şey yazılmadığını görebilirsiniz. Oysa önceki parantez kullandığımız kodda giriş değişkeni bir int’di. Bu örneğimizde ise ilk önce len(input("Adın ne? "))  < 4 kısmı çalışıyor ve bunun sonucu daha sonra giriş değişkenimize atanıyor. Bu yüzden giriş değişkenimiz True veya False, yani bir bool oluyor. Eğer giriş değişkeni True olursa ekrana yazılıyor, ancak eğer False olursa ekrana yazılmıyor. Çünkü if ifadesinin değeri de False oluyor. if ifadesinin kontrol ettiği yer len(input("Adın ne? "))  < 4 kısmı olduğu için if deyiminin içine girilmiyor.

# Çok önemli bir işleç olmayabilir ama bazen aynı fonksiyonu iki defa çağırmak yerine bir defa çağırmak gibi kolaylıklar sağlamaktadır. 

#* Walrus operatoru örneği 1 :

#! Walrus kullanılmadan
yas = int(input("Lütfen yaşınızı girin: "))
if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")
    
# Bu kod, kullanıcının yaşını kontrol eder ve ehliyet alıp alamayacağını belirler. Walrus operatörünü kullanarak bu kodu daha kısa hale getirebiliriz:

#! Walrus kullanılarak
if (yas := int(input("Lütfen yaşınızı girin: ")) ) >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")

# Burada walrus operatörü, yaş değerini kullanıcıdan alırken aynı anda yas değişkenine atar. Bu sayede tek satırda hem değeri alırız hem de yaş kontrolünü yaparız.

#* Walrus basit örneği 2:

sayi = 5
if sayi > 0:
    print("Sayı pozitif.")
else:
    print("Sayı sıfır veya negatif.")
    
# Bu kod, bir sayının pozitif olup olmadığını kontrol eder. Şimdi bu kodu walrus operatörü kullanarak daha kısa hale getirelim:

if (sayi := 5) > 0:
    print("Sayı pozitif.")
else:
    print("Sayı sıfır veya negatif.")
    



#! ----- Aitlik İşleçleri -----
#- in
#. Key : in işleci kullanımı
# Aitlik işleçleri, bir karakter dizisi ya da sayının, herhangi bir veri tipi içinde bulunup bulunmadığını sorgulamamızı sağlayan işleçlerdir.

# Python’da bir tane aitlik işleci bulunur. Bu işleç de in işlecidir. Bu işleci şöyle kullanıyoruz:

a = "abcd"
print("a" in a) # True

print("f" in a) # False

# Gördüğünüz gibi, in adlı bu işleç, bir öğenin, veri tipi içinde geçiyorsa True çıktısı, eğer geçmiyorsa False çıktısı alıyoruz.

# Henüz bu in işlecini verimli bir şekilde kullanmamızı sağlayacak araçlardan yoksunuz. Ancak birkaç sayfa sonra öğreneceğimiz yeni araçlarla birlikte bu işleci çok daha düzgün ve verimli bir şekilde kullanabilecek duruma geleceğiz.

