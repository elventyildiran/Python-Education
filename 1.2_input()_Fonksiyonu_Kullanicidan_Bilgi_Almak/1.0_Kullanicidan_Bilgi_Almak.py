
#! ----- input() Fonksiyonu Kullanarak Kullanıcıdan Bilgi Almak -----

# Python'da input() fonksiyonu, kullanıcıdan metin tabanlı verileri almak için kullanılan bir işlevdir. Bu işlev, kullanıcıdan bir metin girişi isteyerek bir dize (string) değerini döndürür. input() işlevi, kullanıcıdan bilgi almak ve bu bilgiyi Python programlarına dahil etmek için oldukça yaygın bir şekilde kullanılır.

#. Key : input() kullanımı, input kullanımı, kullanıcıdan veri almak, kullanıcıdan bilgi almak, input() fonksiyonu kullanımı, input fonksiyonu kullanımı.
# input() işlevi şu şekilde kullanılır :
#* ÖRNEK 1:

kullanici_girisi = input("Bir metin girin : ")

# Yukarıdaki kod, kullanıcıya "Bir metin girin: " mesajını gösterir ve kullanıcının girişini bekler. Kullanıcı bir şey yazdığında, bu giriş bir dize olarak kullanici_girisi adlı değişkene atanır. Kullanıcı girişi genellikle metin veya sayılar gibi verileri almak için kullanılır ve daha sonra programın bu verileri işlemesine olanak tanır.

print("Girilen metin : " + kullanici_girisi)

#* ÖRNEK 2: 
isim = input("Adınızı girin : ")
print("Merhaba, " + isim + "!")

# Yukarıdaki örnek, kullanıcıdan isim girişi alır ve bu ismi bir selamla birleştirip ekrana yazar.


#! ----- Tip Dönüşümleri -----

# Diyelim ki kullanıcıdan aldığı sayının karesini hesaplayan bir program yazmak istiyoruz. Öncelikle şöyle bir şey deneyelim:

#? sayi = input("Lütfen bir sayı girin : ")

#Girilen sayıın karesini bulmak için sayı değişkeninin 2. kuvvetini alıyoruz. Aynı şeyi pow() fonksiyonu ile de yapabileceğimizi biliyorsunuz. Örn : pow(sayi, 2)
#? print("Girdiğiniz sayının karesi: ", sayi ** 2)

# Bu kodları çalıştırdığımız zaman, programımız kullanıcıdan bir sayı girmesini isteyecek, ancak kullanıcı bir sayı girip Enter tuşuna bastığında şöyle bir hata mesajıyla karşılaşacaktır:

#err: Traceback (most recent call last):
#err:   File "test.py", line 5, in <module>
#err:     print("Girdiğiniz sayının karesi: ", sayi ** 2)
#err: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# Hata mesajına baktığınızda, ‘TypeError’ ifadesinden, bunun veri tipine ilişkin bir hata olduğunu tahmin edebilirsiniz. Eğer İngilizce biliyorsanız yukarıdaki hata mesajının anlamını rahatlıkla çıkarabilirsiniz. İngilizce bilmeseniz de en sondaki ‘str’ ve ‘int’ kelimeleri size karakter dizisi ve sayı adlı veri tiplerini hatırlatacaktır. Demek ki ortada veri tiplerini ilgilendiren bir sorun var…

# Peki burada tam olarak neler dönüyor?

#  Hatırlayacaksınız, geçen derslerden birinde len() fonksiyonunu anlatırken şöyle bir şey söylemiştik:
# Biz henüz kullanıcıdan nasıl veri alacağımızı bilmiyoruz. Ama şimdilik şunu söyleyebiliriz: Python’da kullanıcıdan herhangi bir veri aldığımızda, bu veri bize bir karakter dizisi olarak gelecektir.

# Gelin isterseniz yukarıda anlattığımız durumu teyit eden bir program yazalım:

#* Örnek 1 :

# Kullanıcıdan herhangi bir veri girmesini istiyoruz:

sayi = input("Herhangi bir veri girin : ")

#Kullanıcının girdiği verinin tipini değişkene atıyoruz:
tip = type(sayi)

# Son olarak kulllanıcının girdiği verinin tipini ekrana basıyoruz.
print("Girdiğiniz verinin tipi: ", tip) #? Girdiğiniz verinin tipi:  <class 'str'>

# Bu programı çalıştırdığımızda ne tür bir veri girersek girelim, girdiğimiz verinin tipi str, yani karakter dizisi olacaktır. Demek ki gerçekten de, kullanıcıdan veri almak için kullandığımız input() fonksiyonu bize her koşulda bir karakter dizisi veriyormuş.

#- Python’da, o anda elinizde bulunan bir verinin hangi tipte olduğunu bilmek son derece önemlidir. Çünkü bir verinin ait olduğu tip, o veriyle neler yapıp neler yapamayacağınızı belirler.

# Şu anda karşı karşıya olduğumuz durum da buna çok güzel bir örnektir. Eğer o anda elimizde bulunan verinin tipini bilmezsek tıpkı yukarıda olduğu gibi, o veriyi programımızda kullanmaya çalışırken programımız hata verir ve çöker.

# Her zaman üstüne basa basa söylediğimiz gibi, aritmetik işlemler yalnızca sayılarla yapılır. Karakter dizileri ile herhangi bir aritmetik işlem yapılamaz. Dolayısıyla, input() fonksiyonundan gelen veri bir karakter dizisi olduğu için ve biz de programımızda girilen sayının karesini hesaplamak amacıyla bu fonksiyondan gelen verinin 2. kuvvetini, yani karesini hesaplamaya çalıştığımız için programımız hata verecektir.

# Ancak bazen öyle durumlarla karşılaşırsınız ki, programınız hiçbir hata vermez, ama elde edilen sonuç aslında tamamen beklentinizin dışındadır. Mesela şu basit örneği inceleyelim:

sayı1 = input("Toplama işlemi için ilk sayıyı girin: ")
sayı2 = input("Toplama işlemi için ikinci sayıyı girin: ")

print(sayı1, "+", sayı2, "=", sayı1 + sayı2) # 12 + 34 = 1234

# Bu kodları çalıştırdığımızda şöyle bir manzarayla karşılaşırız: #? # 12 + 34 = 1234

# input() fonksiyonunun alttan alta neler çevirdiğini bu örnek yardımıyla çok daha iyi anladığınızı zannediyorum. Gördüğünüz gibi yukarıdaki program herhangi bir hata vermedi. Ama beklediğimiz çıktıyı da vermedi. Zira biz programımızın iki sayıyı toplamasını istiyorduk. O ise kullanıcının girdiği sayıları yan yana yazmakla yetindi. Yani bir aritmetik işlem yapmak yerine, verileri birbiriyle bitiştirdi. Çünkü, dediğim gibi, input() fonksiyonunun kullanıcıdan aldığı şey bir karakter dizisidir. Dolayısıyla bu fonksiyon yukarıdaki gibi bir durumla karşılaştığı zaman karakter dizileri arasında bir birleştirme işlemi gerçekleştirir. Tıpkı ilk derslerimizde etkileşimli kabukta verdiğimiz şu örnekte olduğu gibi:

print("23" + "23") #? 2323


#Bu son örnekten ayrıca şunu çıkarıyoruz: Yazdığınız bir programın herhangi bir hata vermemesi o programın doğru çalıştığı anlamına gelmeyebilir. Dolayısıyla bu tür durumlara karşı her zaman uyanık olmanızda fayda var.

# Peki yukarıdaki gibi durumlarla karşılaşmamak için ne yapacağız?

# İşte bu noktada devreye tip dönüştürücü adını verdiğimiz birtakım fonksiyonlar girecek.

#! ----- int() -----

# Dediğimiz gibi, input() fonksiyonundan gelen veri her zaman bir karakter dizisidir. Dolayısıyla bu fonksiyondan gelen veriyle herhangi bir aritmetik işlem yapabilmek için öncelikle bu veriyi bir sayıya dönüştürmemiz gerekir. Bu dönüştürme işlemi için int() adlı özel bir dönüştürücü fonksiyondan yararlanacağız. 

karakter_dizisi = "23"
sayi = int(karakter_dizisi)
print(sayi) #? 23
print(type(sayi)) #? <class 'int'>

# Burada öncelikle “23” adlı bir karakter dizisi tanımladık. Ardından da int() fonksiyonunu kullanarak bu karakter dizisini bir tamsayıya (integer) dönüştürdük. İsminden de anlayacağınız gibi int() fonksiyonu İngilizce integer (tamsayı) kelimesinin kısaltmasıdır ve bu fonksiyonun görevi bir veriyi tamsayıya dönüştürmektir.



#! ----- str() ------

# karakter dizisi olmayan verileri karakter dizisine dönüştürmemiz de mümkündür. Bu işlem için str() adlı başka bir tip dönüştürücüden yararlanıyoruz:

sayi = 1
karakter_dizisi = str(sayi)
print(karakter_dizisi)
print(type(karakter_dizisi)) #? <class 'str'>


#! ----- float() -----

# Hatırlarsanız ilk bölümlerde sayılardan söz ederken tamsayıların (integer) dışında kayan noktalı sayıların (float) da olduğundan söz etmiştik. İşte eğer bir tamsayıyı veya sayı değerli bir karakter dizisini kayan noktalı sayıya dönüştürmek istersek float() adlı başka bir dönüştürücüden yararlanacağız:

a = 23
float(a) #? 23.0

#! ----- complex() -----

# Sayılardan söz ederken, eğer matematikle çok fazla içli dışlı değilseniz pek karşılaşmayacağınız, ‘karmaşık sayı’ adlı bir sayı türünden de bahsetmiştik. Karmaşık sayılar Python’da ‘complex’ ifadesiyle gösteriliyor. Mesela şunun bir karmaşık sayı olduğunu biliyoruz:

print(type(12+0j)) #? <class 'complex'>


#! int()
# Sayı değerli bir karakter dizisini veya kayan noktalı sayıyı tamsayıya (integer) çevirir.

#! float()
# Sayı değerli bir karakter dizisini veya tamsayıyı kayan noktalı sayıya (float) çevirir.

#! str()
# Bir tamsayı veya kayan noktalı sayıyı karakter dizisine (string) çevirir.

#! complex()
# Herhangi bir sayıyı veya sayı değerli karakter dizisini karmaşık sayıya (complex) çevirir.