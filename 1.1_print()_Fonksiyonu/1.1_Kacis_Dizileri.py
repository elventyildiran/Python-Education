 #! ----- Kaçış Dizileri -----
 
 # Python’da karakter dizilerini tanımlayabilmek için tek, çift veya üç tırnak işaretlerinden faydalandığımızı geçen bölümde öğrenmiştik. Python bir verinin karakter dizisi olup olmadığına bu tırnak işaretlerine bakarak karar verdiği için, tek, çift ve üç tırnak işaretleri Python açısından özel bir önem taşıyor. Zira Python’ın gözünde bir başlangıç tırnağı ile bitiş tırnağı arasında yer alan her şey bir karakter dizisidir.
 
 # Örneğin ilk olarak bir “ işareti koyup ardından “elma şeklinde devam ettiğinizde, Python ilk tırnağı gördükten sonra karakter dizisini tanımlayabilmek için ikinci bir tırnak işareti aramaya başlar. Siz “elma” şeklinde kodunuzu tamamladığınızda ise Python bellekte “elma” adlı bir karakter dizisi oluşturur.
 
 # Bu noktada size şöyle bir soru sormama izin verin: Acaba tırnak işaretleri herhangi bir metin içinde kaç farklı amaçla kullanılabilir?
 
 # İsterseniz bu sorunun cevabını örnekler üzerinde vermeye çalışalım:
 
 #?     Ahmet, “Bugün sinemaya gidiyorum,” dedi.
 # Burada tırnak işaretlerini, bir başkasının sözlerini aktarmak için kullandık.
 
 #?     ‘book’ kelimesi Türkçede ‘kitap’ anlamına gelir.
 # Burada ise tırnak işaretlerini bazı kelimeleri vurgulamak için kullandık.
 
# Bir de şuna bakalım
#?      Yarın Adana’ya gidiyorum.
# Burada da tırnak işaretini, çekim eki olan ‘-(y)a’ ile özel isim olan ‘Adana’ kelimesini birbirinden ayırmak için kesme işareti görevinde kullandık.

 
 #! ----- Ters Taksim (\) -----
 # Yukarıda verdiğimiz örneklerde, çift tırnakla gösterdiğimiz karakter dizilerinin içinde de çift tırnak işareti kullanabilmek için birkaç farklı yöntemden yararlanabildiğimizi öğrenmiştik. Buna göre, eğer bir karakter dizisi içinde çift tırnak işareti geçiyorsa, o karakter dizisini tek tırnakla; eğer tek tırnak geçiyorsa da o karakter dizisini çift tırnakla tanımlayarak bu sorunun üstesinden gelebiliyorduk. Ama daha önce de söylediğimiz gibi, ‘kaçış dizileri’ adı verilen birtakım araçları kullanarak, mesela içinde çift tırnak geçen karakter dizilerini yine çift tırnakla tanımlayabiliriz.
 
 # Dilerseniz, kaçış dizisi kavramını açıklamaya geçmeden önce bununla ilgili birkaç örnek verelim. Bu sayede ne ile karşı karşıya olduğumuz, zihnimizde biraz daha belirginleşebilir:

#* Örnek 1 :
print('Yarın Adana\'ya gidiyorum.') # Yarın Adana'ya gidiyorum.

#* Örnek 2 : 
print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.") # "book" kelimesi Türkçede "kitap" anlamına gelir.

# Burada da cümle içinde çift tırnak işaretlerini kullandığımız halde, \ işaretleri sayesinde karakter dizilerini yine çift tırnakla tanımlayabildik.

print("Python programlama dilinin adı \"piton\" yılanından gelmez") # Python programlama dilinin adı "piton" yılanından gelmez


#* Örnek 3: 
print("Python 1990 yılında Guido Van Rossum \
tarafından geliştirilmeye başlanmış, oldukça \
güçlü ve yetenekli bir programlama dilidir.") # Python 1990 yılında Guido Van Rossum tarafından geliştirilmeye başlanmış, oldukça güçlü ve yetenekli bir programlama dilidir.

# Normal şartlar altında, bir karakter dizisini tanımlamaya tek veya çift tırnakla başlamışsak, karakter dizisinin kapanış tırnağını koymadan Enter tuşuna bastığımızda Python bize bir hata mesajı gösterir:

#* >>> print("Python 1990 yılında Guido Van Rossum
#err:  File "<stdin>", line 1
#err:    print("Python 1990 yılında Guido Van Rossum                                                ^
#err: SyntaxError: EOL while scanning string literal

# İşte \ kaçış dizisi bizim burada olası bir hatadan kaçmamızı sağlar. Eğer Enter tuşuna basmadan önce bu işareti kullanırsak Python tıpkı üç tırnak işaretlerinde şahit olduğumuz gibi, hata vermeden bir alt satıra geçecektir. Bu sırada, yani \ kaçış dizisini koyup Enter tuşuna bastığımızda >>> işaretinin … işaretine dönüştüğünü görüyorsunuz. Bu işaretin, Python’ın bize verdiği bir ‘Yazmaya devam et!’ mesajı olduğunu biliyorsunuz.

#! ----- Satır Başı (\n) -----

# Satır başı karakterine ‘yeni satır karakteri’ dendiği de olur.

#* Örnek 1:
baslik = "Türkiye'de Özgür Yazılımın Geçmişi"
print(baslik, "\n","-"*len(baslik), sep="")
#* Türkiye'de Özgür Yazılımın Geçmişi
#* ----------------------------------

print("Burası birinci satır.\nBurası ikinci satır.")
# Burası birinci satır.
# Burası ikinci satır.


# * ÖNEMLİ ÖRNEK :

# Diyelim ki bilgisayarınızın ‘C:\’ dizinindeki ‘nisan’ adlı bir klasörün içinde yer alan masraflar.txt adlı bir dosyayı yazdığınız bir program içinde kullanmanız gerekiyor. Mesela bu dosyayı, tam adresiyle birlikte kullanıcılarınıza göstermek istiyorsunuz.
print("C:\nisan\masraflar.txt")
#* C:
#* isan\masraflar.txt

# Gördüğünüz gibi, bu çıktıyı normal yollardan vermeye çalıştığımızda Python bize hiç de beklemediğimiz bir çıktı veriyor. Peki ama neden?

# Python’da karakter dizileri ile çalışırken asla aklımızdan çıkarmamamız gereken bir şey var: Eğer yazdığımız herhangi bir karakter dizisinin herhangi bir yerinde \ işaretini kullanmışsak, bu işaretten hemen sonra gelen karakterin ne olduğuna çok dikkat etmemiz gerekir. Çünkü eğer dikkat etmezsek, farkında olmadan Python için özel anlam taşıyan bir karakter dizisi oluşturmuş olabiliriz. Bu da kodlarımızın beklediğimiz gibi çalışmasını engeller.

#* ÖNEMLİ HATA ÖRNEĞİ ;
#?  open("C:\nisan\masraflar.txt")
#err: Traceback (most recent call last):
#err:  File "<stdin>", line 1, in <module>
#err: OSError: [Errno 22] Invalid argument: 'C:\nisan\\masraflar.txt'

# Eğer sorunun gözden kaçan bir kaçış dizisinden kaynaklandığını farkedemezseniz, bu sorunu çözebilmek için saatlerinizi ve hatta günlerinizi harcamak zorunda kalabilirsiniz. Çünkü yukarıdaki hata mesajı sorunun nedenine dair hiçbir şey söylemiyor. Ancak ve ancak yukarıdaki karakter dizisi içinde sinsice gizlenen bir \n kaçış dizisi olduğu gözünüze çarparsa bu sorunu çözme yolunda bir adım atabilirsiniz.

# Diyelim ki sorunun ‘\nisan’ ifadesinin başındaki \n karakterlerinin Python tarafından bir kaçış dizisi olarak algılanmasından kaynaklandığını farkettiniz. Peki bu sorunu nasıl çözeceksiniz?

#* HATA ÖRNEĞİ ÇÖZÜM
#? open("C:\\nisan\masraflar")

# Tabii tutarlılık açısından karakter dizisi içindeki bütün ters taksim işaretlerini çiftlemek mantıklı olacaktır:
#? #? open("C:\\nisan\\masraflar")

#! ----- Sekme (\t) -----
#Python’da \ işareti sadece ‘n’ harfiyle değil, başka harflerle de birleşebilir. Örneğin \ işaretini ‘t’ harfiyle birleştirerek yine özel bir anlam ifade eden bir kaçış dizisi elde edebiliriz:

#* ÖRNEK 1:
print("Elvent\tYILDIRAN") # Elvent  YILDIRAN

# Burada \t adlı kaçış dizisi, “abc” ifadesinden sonra sanki Tab (sekme) tuşuna basılmış gibi bir etki oluşturarak “def” ifadesini sağa doğru itiyor. Bir de şu örneğe bakalım:
#* ÖRNEK 2:
print("bir", "iki", "üç", sep="\t") # bir     iki     üç

#* ÖRNEK 3:

print(*"123456789", sep="\t") # 1       2       3       4       5       6       7       8       9

#! ----- Zil Sesi (\a) -----
# \ işaretinin birleştiğinde farklı bir anlam türettiği bir başka harf de ‘a’ harfidir. \ işareti ‘a’ harfiyle birleşerek !bip! benzeri bir zil sesi üretilmesini sağlayabilir:
print("\a")

# İsterseniz yukarıdaki komutu şu şekilde yazarak, kafa şişirme katsayısını artırabilirsiniz:
print("\a" * 10)
# Bu şekilde !bip! sesi 10 kez tekrar edilecektir. Ancak bu kaçış dizisi çoğunlukla sadece Windows üzerinde çalışacaktır. Bu kaçış dizisinin GNU/Linux üzerinde çalışma garantisi yoktur. Hatta bu kaçış dizisi bütün Windows sistemlerinde dahi çalışmayabilir. Dolayısıyla bu kaçış dizisinin işlevine bel bağlamak pek mantıklı bir iş değildir.


#! ----- Aynı Satır Başı (\r) -----

# Bu kaçış dizisi, bir karakter dizisinde aynı satırın en başına dönülmesini sağlar. Bu kaçış dizisinin işlevini tanımına bakarak anlamak biraz zor olabilir. O yüzden dilerseniz bu kaçış dizisinin ne işe yaradığını bir örnek üzerinde göstermeye çalışalım:

#* ÖRNEK 1:
print("Merhaba\rZalim Dünya!") # Zalim Dünya!

# Burada olan şey şu: Normal şartlar altında, print() fonksiyonu içine yazdığımız bir karakter dizisindeki bütün karakterler soldan sağa doğru tek tek ekrana yazdırılır:
print("Merhaba Zalim Dünya!") # Merhaba Zalim Dünya!

# Ancak eğer karakter dizisinin herhangi bir yerine \r adlı kaçış dizisini yerleştirirsek, bu kaçış dizisinin bulunduğu konumdan itibaren aynı satırın başına dönülecek ve \r kaçış dizisinden sonra gelen bütün karakterler satır başındaki karakterlerin üzerine yazacaktır. Şu örnek daha açıklayıcı olabilir:

#* ÖRNEK 2:
print("Merhaba\rDünya") # Dünyaba
# Burada, “Merhaba” karakter dizisi ekrana yazdırıldıktan sonra \r kaçış dizisinin etkisiyle satır başına dönülüyor ve bu kaçış dizisinden sonra gelen “Dünya” karakter dizisi “Merhaba” karakter dizisinin üzerine yazıyor. Tabii “Dünya” karakter dizisi içinde 5 karakter, “Merhaba” karakter dizisi içinde ise 7 karakter olduğu için, “Merhaba” karakter dizisinin son iki karakteri (“ba”) dışarda kalıyor. Böylece ortaya “Dünyaba” gibi bir şey çıkıyor.


#! ----- Düşey Sekme (\v) -----
# Eğer \ işaretini ‘v’ harfiyle birlikte kullanırsak düşey sekme denen şeyi elde ederiz. Hemen bir örnek verelim:

print("Düşey\vsekme")
# Yalnız bu \v adlı kaçış dizisi her işletim sisteminde çalışmayabilir. Dolayısıyla, birden fazla platform üzerinde çalışmak üzere tasarladığınız programlarınızda bu kaçış dizisini kullanmanızı önermem.

#! ----- İmleç Kaydırma (\b) -----
# \ kaçış dizisinin, biraraya geldiğinde özel bir anlam kazandığı bir başka harf de b’dir. \b kaçış dizisinin görevi, imleci o anki konumundan sola kaydırmaktır. Bu tanım pek anlaşılır değil. O yüzden bir örnek verelim:

#* ÖRNEK 1 :
print("yahoo.com\b") # yahoo.com
#  Bu kodu çalıştırdığınızda herhangi bir değişiklik görmeyeceksiniz. Ama aslında en sonda gördüğümüz \b kaçış dizisi, imleci bir karakter sola kaydırdı. Dikkatlice bakın:


#* ÖRNEK 2:
print("yahoo.com\b.uk") # yahoo.co.uk

# Gördüğünüz gibi, \b kaçış dizisinin etkisiyle imleç bir karakter sola kaydığı için, ‘com’ kelimesinin son harfi silindi ve bunun yerine \b kaçış dizisinden sonra gelen .uk karakterleri yerleştirildi. Dolayısıyla biz de şu çıktıyı aldık: yahoo.co.uk



# * ÖRNEK 3:
# Bildiğiniz gibi, print() fonksiyonu, kendisine verilen parametreler arasına birer boşluk yerleştirir

print('istihza', '.', 'com') # istihza . com

# Biz bu öğeleri birbirine bitiştirmek için şöyle bir yol izleyebileceğimizi biliyoruz:
print('istihza', '.', 'com', sep='') # istihza.com

# İşte aynı etkiyi \b kaçış dizisini kullanarak da elde edebiliriz:

print('istihza', '\b.', '\bcom') # istihza.com

#! ----- Küçük Unicode (\u) -----

# Belki sağda solda ‘UNICODE’ diye bir şey duymuşsunuzdur. Eğer şimdiye kadar böyle bir şey duymadıysanız veya duyduysanız bile ne olduğunu bilmiyorsanız hiç ziyanı yok. Birkaç bölüm sonra bunun ne anlama geldiğini bütün ayrıntılarıyla anlatacağız. Biz şimdilik sadece şunu bilelim: UNICODE, karakterlerin, harflerin, sayıların ve bilgisayar ekranında gördüğümüz öteki bütün işaretlerin her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir. Bu sistemde, ‘kod konumu’ (code point) adı verilen bu numaralar özel bir şekilde gösterilir. Örneğin ‘ı’ harfi UNICODE sisteminde şu şekilde temsil edilir:

#* u+0131

# Aynı şekilde ‘a’ harfi bu sistemde şu kod konumu ile gösterilir:

#* u+0061

# Python programlama dilinde ise, yukarıdaki kod konumu düzeni şöyle gösterilir:

#* \\u0131

# Gördüğünüz gibi, Python UNICODE sistemindeki her bir kod konumunu gösterebilmek için, önce \u şeklinde bir kaçış dizisi tanımlıyor, ardından UNICODE sisteminde + işaretinden sonra gelen sayıyı bu kaçış dizisinin hemen sağına ekliyor. Gelin kendi kendimize birkaç deneme çalışması yapalım:

#* ÖRNEKLER :
print("\u0130") # İ
print("\u0070") # p


#! ----- Etkisizleştirme (r) -----

# Python’da \ işaretinin dışında temel bir kaçış dizisi daha bulunur. Bu kaçış dizisi ‘r’ harfidir. Şimdi bu kaçış dizisinin nasıl kullanılacağını ve ne işe yaradığını inceleyelim:

# Şöyle bir çıktı vermek istediğimizi düşünün:

#?      Kurulum dizini: C:\aylar\nisan\toplam masraf

# Bildiğimiz yoldan bu çıktıyı vermeye çalışırsak neler olacağını adınız gibi biliyorsunuz:

#? print("Kurulum dizini: C:\aylar\nisan\toplam masraf")
#- Kurulum dizini: C:ylar
#- isan        oplam masraf

# Eğer Windows üzerinde çalışıyorsanız bu komutu verdikten sonra bir !bip! sesi de duymuş olabilirsiniz…

# Python tabii ki, karakter dizisi içinde geçen ‘\aylar’, ‘\nisan’, ve ‘\toplam masraf’ ifadelerinin ilk karakterlerini yanlış anladı! \a, \n ve \t gibi ifadeler Python’ın gözünde birer kaçış dizisi. Dolayısıyla Python \a karakterlerini görünce bir !bip! sesi çıkarıyor, \n karakterlerini görünce satır başına geçiyor ve \t karakterlerini görünce de Tab tuşuna basılmış gibi bir tepki veriyor. Sonuç olarak da yukarıdaki gibi bir çıktı üretiyor.

# Daha önce bu durumu şöyle bir kod yazarak engellemiştik:
#? print("Kurulum dizini: C:\\aylar\\nisan\\toplam masraf")

# Burada, \ işaretlerinin her birini çiftleyerek sorunun üstesinden geldik. Yukarıdaki yöntem doğru ve kabul görmüş bir çözümdür. Ama bu sorunun üstesinden gelmenin çok daha basit ve pratik bir yolu var. Bakalım:

print(r"Kurulum dizini: C:\aylar\nisan\toplam masraf") # Kurulum dizini: C:\aylar\nisan\toplam masraf

#Gördüğünüz gibi, karakter dizisinin baş kısmının dış tarafına bir adet r harfi yerleştirerek sorunun üstesinden geliyoruz. Bu kaçış dizisinin, kullanım açısından öteki kaçış dizilerinden farklı olduğuna dikkat edin. Öteki kaçış dizileri karakter dizisinin içinde yer alırken, bu kaçış dizisi karakter dizisinin dışına yerleştiriliyor.

#* ÖRNEK 1:
print(r"Kaçış dizileri: \, \n, \t, \a, \\, r") # Kaçış dizileri: \, \n, \t, \a, \\, r


# ! ----- Sayfa Başı (\f) -----

#\f artık günümüzde pek kullanılmayan bir kaçış dizisidir. Bu kaçış dizisinin görevi, özellikle eski yazıcılarda, bir sayfanın sona erip yeni bir sayfanın başladığını göstermektir. Dolayısıyla eski model yazıcılar, bu karakteri gördükleri noktada mevcut sayfayı sona erdirip yeni bir sayfaya geçer.

#Bu kaçış dizisinin tam olarak ne işe yaradığını test etmek için şu kodları çalıştırın:

f = open("deneme.txt", "w")
print("deneme\fdeneme", file=f)
f.close()

# Şimdi bu kodlarla oluşturduğunuz deneme.txt adlı dosyayı LibreOffice veya Microsoft Word gibi bir programla açın. ‘deneme’ satırlarının iki farklı sayfaya yazdırıldığını göreceksiniz. Bu arada, eğer Microsoft Word dosyayı açarken bir hata mesajı gösterirse, o hata mesajına birkaç kez ‘tamam’ diyerek hata penceresini kapatın. Dosya normal bir şekilde açılacaktır.

# Dediğimiz gibi, bu kaçış dizisi artık pek kullanılmıyor. Ama yine de bu kaçış dizisine karşı da uyanık olmalısınız. Çünkü bu kaçış dizisi de beklemediğiniz çıktılar almanıza yol açabilir. Mesela şu örneğe bir bakalım:

"\fırat"

'\x0cırat'

# Gördüğünüz gibi, siz aslında ‘\fırat’ yazmak isterken, Python bu kelimenin baş tarafındaki \f karakter dizisini bir kaçış dizisi olarak değerlendirip ona göre bir çıktı verdi.

# Bütün bu anlattıklarımızın ardından, kaçış dizilerinin, birleştirildikleri karakterlerin farklı bir anlam yüklenmesini sağlayan birtakım işaretler olduğunu anlıyoruz. Örneğin \ işareti ‘ (tek tırnak) işareti ile bir araya gelerek, tek tırnak işaretinin karakter dizisi tanımlama dışında başka bir anlam yüklenmesini sağlıyor. Aynı şekilde yine \ işareti “ (çift tırnak) işareti ile birleşerek çift tırnak işaretinin de karakter dizisi tanımlama dışında bir anlama kavuşmasını sağlıyor. Böylece tırnak işaretlerini karakter dizileri içinde rahatlıkla kullanabiliyoruz.

# Ya da yine \ işareti ‘n’ harfi ile bir araya gelip, bu harfin satır başına geçilmesini sağlayan bir kaçış dizisi oluşturmasını mümkün kılıyor. Veya aynı işaret ‘t’ harfiyle birleşip, öğeler arasında sekme oluşturulmasını sağlayabiliyor. Bu araçlar sayesinde ekrana yazdırdığımız bir metnin akışını kontrol etme imkanına kavuşuyoruz.

#! ----- Kaçış Dizilerine Toplu Bakış -----

# Biraz sonra bu önemli konuyu kapatacağız. Ama dilerseniz kapatmadan önce, bu bölümde öğrendiğimiz kaçış dizilerini şöyle bir topluca görelim:


# ? Kaçış Dizisi ve Anlamı

#? \’

#Karakter dizisi içinde tek tırnak işaretini kullanabilmemizi sağlar.

#? \”

#Karakter dizisi içinde çift tırnak işaretini kullanabilmemizi sağlar.

#? \\

# Karakter dizisi içinde \ işaretini kullanabilmemizi sağlar.

#? \n

# Yeni bir satıra geçmemizi sağlar.

#? \t

# Karakterler arasında sekme boşluğu bırakmamızı sağlar.

#? \u

# UNICODE kod konumlarını gösterebilmemizi sağlar.

#? \U

# UNICODE kod konumlarını gösterebilmemizi sağlar.

#? \N

# Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar.

#? \x

# Onaltılı sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar.

#? \a

# Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesini sağlar.

#? \r

# Aynı satırın başına dönülmesini sağlar.

#? \v

# Destekleyen sistemlerde düşey sekme oluşturulmasını sağlar.

#? \b

# İmlecin sola doğru kaydırılmasını sağlar

#? \f

# Yeni bir sayfaya geçilmesini sağlar.

#? r

# Karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.

# Kaçış dizileriyle ilgili son olarak şunu söyleyebiliriz: Kaçış dizileri, görmezden gelebileceğiniz, ‘öğrenmesem de olur,’ diyebileceğiniz önemsiz birtakım işaretler değildir. Bu konu boyunca verdiğimiz örneklerden de gördüğünüz gibi, kaçış dizileri, kullanıcıya göstereceğiniz metinlerin biçimini doğrudan etkiliyor. Bütün bu örnekler, bu kaçış dizilerinin yersiz veya yanlış kullanılmasının ya da bunların bir metin içinde gözden kaçmasının, yazdığınız programların hata verip çökmesine, yani programınızın durmasına sebep olabileceğini de gösteriyor bize.

# Böylece bir bölümü daha bitirmiş olduk. Artık Python’la ‘gerçek’ programlar yazmamızın önünde hiçbir engel kalmadı.