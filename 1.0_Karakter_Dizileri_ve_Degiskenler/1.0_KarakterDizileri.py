# Karakter dizileri bütün progrmacılık maceramız boyunca karşımıza çıkacak. O yüzden bu kavramı ne kadar erken öğrenirsek o kadar iyi.
#Peki bir verinin karakter dizisi olup olmamasının bize ne faydası var? Yani yukarıdaki cümle karakter dizisi olmuş olmamış bize ne?
# Python’da, o anda elinizde bulunan bir verinin hangi tipte olduğunu bilmek son derece önemlidir.  Çünkü bir verinin ait olduğu tip, o veriyle neler yapıp neler yapamayacağınızı belirler. Python’da her veri tipinin belli başlı özellikleri vardır. Dolayısıyla, elimizdeki bir verinin tipini bilmezsek o veriyi programlarımızda etkin bir şekilde kullanamayız.

#* Karakter Dizisi Örnekleri ;
# tek tırnak ile.
print('a')
print('Merhaba dünya!')

#Çift tırnak ile.
print("a")
print("Merhaba dünya!")

# Gördüğünüz gibi, tırnak içinde gösterilen tek karakterlik bir öğe de Python’da karakter dizisi sınıfına giriyor.

#* İçi boş bir karakter dizisi örneği :
print("")

#* İçinde boşluk karakteri barındıran bir karakter dizisi örneği ;
print(" ")

# Bu ikisi arasındaki farka dikkat ediyoruz: Python’da ‘boş karakter dizisi’ ve ‘bir adet boşluktan oluşan karakter dizisi’ birbirlerinden farklı iki kavramdır.

#!----- Karakter Dizilerinin Tiplerini Öğrenme ------
#. key : Bir verinin tipini öğrenme. type() fonksiyonu nasıl kullanılır ?

print(type("Elma")) # <class 'str'>

#Burada amacımız “Elma” adlı öğenin tipini denetlemek. Denetlenecek öğeyi type() fonksiyonunun parantezleri arasında belirttiğimize dikkat edin. (Fonksiyonların parantezleri içinde belirtilen değerlere teknik dilde parametre adı verilir.) 

# Yukarıdaki çıktıda bizi ilgilendiren kısım, sondaki ‘str’ ifadesi. Tahmin edebileceğiniz gibi, bu ifade string kelimesinin kısaltmasıdır. Bu kelimenin Türkçede karakter dizisi anlamına geldiğini söylemiştik. O halde yukarıdaki çıktıya bakarak, “Elma” öğesinin bir karakter dizisi olduğunu söyleyebiliyoruz.

#! ---- Karakter dizilerini + operatoruyle birleştirme -----

#* Örnek 1 :
print("yazbel" + ".com") # yazbel.com

#* Örnek 2 :
print("Elvent" + " " + "YILDIRAN") # Elvent YILDIRAN

# Burada iki karakter dizisi arasına bir adet boşluk karakteri yerleştirdik. Aynı etkiyi şu şekilde de elde edebilirsiniz:

#* Örnek 3 :
print("Elvent" + " YILDIRAN") # Elvent YILDIRAN

#Şimdi buradaki örneğe dikkat edin;
#* Örnek 4 :
print("www" "." "google" "." "com") # www.google.com
#karakter dizilerini birleştirmek için mutlaka + işareti kullanmak zorunda değilsiniz. Siz + işaretini kullanmasanız da Python sizin karakter dizilerini birleştirmek istediğinizi anlayacak kadar zekidir.

#Ancak "+" işareti kullandığımız zaman kodlarımız daha okunaklı hale geliyor, bu yüzden bu alışkanlıktan vazgeçmemek en iyisidir.

#! ---- Karakter Dizilerinde *(çarpı) işareti kullanmak ---

#* Örnek 1 :
print("w" * 3) # www

#* Örnek 2 :
print("uzak" + " " * 5 + "çok uzak....") # uzak     çok uzak....

# Gördüğünüz gibi, çok basit parçaları bir araya getirerek karmaşık çıktılar elde edebiliyoruz. Mesela son örnekte “uzak” adlı karakter dizisine önce 5 adet boşluk karakteri (" " * 5), ardından da “çok uzak…” adlı karakter dizisini ekleyerek istediğimiz çıktıyı aldık.

# Burada + ve * adlı iki yeni araç görüyoruz. Bunlar aslında sayılarla birlikte kullanılan birer aritmetik işleçtir. Normalde + işleci toplama işlemleri için, * işleci ise çarpma işlemleri için kullanılır. Ama yukarıdaki örneklerde, + işaretinin ‘birleştirme’; * işaretinin ise ‘tekrarlama’ anlamından ötürü bu iki işleci bazı durumlarda karakter dizileri ile birlikte de kullanabiliyoruz. Bunların dışında bir de - (eksi) ve / (bölü) işleçleri bulunur. Ancak bu işaretleri karakter dizileri ile birlikte kullanamıyoruz.


