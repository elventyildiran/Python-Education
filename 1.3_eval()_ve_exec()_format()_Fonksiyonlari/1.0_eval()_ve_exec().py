#
#! ----- eval() ŞEYTANİ GÜÇLERİ OLAN BİR FONKSİYONDUR! -------

# Bunun neden böyle olduğunu hem biz anlatacağız, hem de zaten bu fonksiyonu tanıdıkça neden eval()’e karşı dikkatli olmanız gerektiğini kendiniz de anlayacaksınız.

# Dilerseniz işe basit bir eval() örneği vererek başlayalım:
#* ÖRNEK :

print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

veri = input("İşleminiz: ")
hesap = eval(veri)

print(hesap)

# İngilizcede evaluate diye bir kelime bulunur. Bu kelime, ‘değerlendirmeye tabi tutmak, işleme sokmak, işlemek’ gibi anlamlar taşır. İşte eval() fonksiyonundaki eval kelimesi bu evaluate kelimesinin kısaltmasıdır. Yani bu fonksiyonun görevi, kendisine verilen karakter dizilerini değerlendirmeye tabi tutmak ya da işlemektir. Peki bu tam olarak ne anlama geliyor?

# Aslında yukarıdaki örnek programı çalıştırdığımızda bu sorunun yanıtını kendi kendimize verebiliyoruz. Bu programı çalıştırarak, “İşleminiz: “ ifadesinden sonra, örneğin, 45 * 76 yazıp Enter tuşuna basarsak programımız bize 3420 çıktısı verecektir. Yani programımız hesap makinesi işlevini yerine getirip 45 sayısı ile 76 sayısını çarpacaktır. Dolayısıyla, yukarıdaki programı kullanarak her türlü aritmetik işlemi yapabilirsiniz. Hatta bu program, son derece karmaşık aritmetik işlemlerin yapılmasına dahi müsaade eder.

# Peki programımız bu işlevi nasıl yerine getiriyor? İsterseniz kodların üzerinden tek tek geçelim.

# Öncelikle programımızın en başına kullanım kılavuzuna benzer bir metin yerleştirdik ve bu metni print() fonksiyonu yardımıyla ekrana bastık.
# Daha sonra kullanıcıdan alacağımız komutları veri adlı bir değişkene atadık. Tabii ki kullanıcıyla iletişimi her zaman olduğu gibi input() fonksiyonu yardımıyla sağlıyoruz.

# Ardından, kullanıcıdan gelen veriyi eval() fonksiyonu yardımıyla değerlendirmeye tabi tutuyoruz. Yani kullanıcının girdiği komutları işleme sokuyoruz. Örneğin, kullanıcı 46 / 2 gibi bir veri girdiyse, biz eval() fonksiyonu yardımıyla bu 46 / 2 komutunu işletiyoruz. Bu işlemin sonucunu da hesap adlı başka bir değişken içinde depoluyoruz.

# Eğer burada eval() fonksiyonunu kullanmazsak, programımız, kullanıcının girdiği 45 * 76 komutunu hiçbir işleme sokmadan dümdüz ekrana basacaktır. Yani:

print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

veri = input("İşleminiz: ")

print(veri)

# Eğer programımızı yukarıdaki gibi, eval() fonksiyonu olmadan yazarsak, kullanıcımız 45 * 76 gibi bir komut girdiğinde alacağı cevap dümdüz bir 45 * 76 çıktısı olacaktır. İşte eval() fonksiyonu, kullanıcının girdiği her veriyi bir Python komutu olarak algılar ve bu veriyi işleme sokar. Yani 45 * 76 gibi bir şey gördüğünde, bu şeyi doğrudan ekrana yazdırmak yerine, işlemin sonucu olan 3420 sayısını verir.

# eval() fonksiyonunun, yukarıda anlattığımız özelliklerini okuduktan sonra, ‘Ne güzel bir fonksiyon! Her işimi görür bu!’ dediğinizi duyar gibiyim. Ama aslında durum hiç de öyle değil. Neden mi?

print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

veri = input("İşleminiz son: ")
hesap = eval(veri)

print(hesap)

# Şimdi yukarıdaki programı tekrar çalıştırın ve “İşleminiz: “ ifadesinden sonra şu cevabı verin:
print("Merhaba Python!")
# Bu komut şöyle bir çıktı vermiş olmalı:
#? Merhaba Python!
#? None

# Gördüğünüz gibi, yazdığımız program, kullanıcının girdiği Python komutunun işletilmesine sebep oldu. Bu noktada, ‘Eee, ne olmuş!’ demiş olabilirsiniz. Gelin bir de şuna bakalım. Şimdi programı tekrar çalıştırıp şu cevabı verin:

#< open("deneme.txt", "w")
#? İşleminiz son: open("deneme.txt", "w")  
#? <_io.TextIOWrapper name='deneme.txt' mode='w' encoding='cp1252'>
#? Merhaba Python!

# Bu cevap, bilgisayarınızda deneme.txt adlı bir dosya oluşturulmasına sebep oldu. Belki farkındasınız, belki farkında değilsiniz, ama aslında şu anda kendi yazdığınız program sizin kontrolünüzden tamamen çıktı. Siz aslında bir hesap makinesi programı yazmıştınız. Ama eval() fonksiyonu nedeniyle kullanıcıya rastgele Python komutlarını çalıştırma imkanı verdiğiniz için programınız sadece aritmetik işlemleri hesaplamak için kullanılmayabilir. Böyle bir durumda kötü niyetli (ve bilgili) bir kullanıcı size çok büyük zarar verebilir. Mesela kullanıcının, yukarıdaki programa şöyle bir cevap verdiğini düşünün:

#< __import__("os").system("dir")
#? Volume in drive C has no label.
#? Volume Serial Number is 066E-CC6C

#? Directory of C:\Python-Education

#? 10/23/2023  11:55 PM    <DIR>          .
#? 10/23/2023  11:55 PM                 0 deneme.txt
#? 10/23/2023  10:54 PM    <DIR>          Python-Education
#?               1 File(s)              0 bytes
#?               2 Dir(s)  699,600,424,960 bytes free

#! ÇOK ÖNEMLİ :
# Burada anlamadığınız şeyleri şimdilik bir kenara bırakıp, bu komutun sonuçlarına odaklanın. Gördüğünüz gibi, yukarıdaki programa bu cevabı vererek mevcut dizin altındaki bütün dosyaları listeleyebildik. Yani programımız bir anda amacını aştı. Artık bu aşamadan sonra bu programı şeytani bir amaca yönelik olarak kullanmak tamamen programı kullanan kişiye kalmış… Bu programın, bir web sunucusu üzerinde çalışan bir uygulama olduğunu ve bu programı kullananların yukarıdaki gibi masumane bir şekilde dizin içindeki dosyaları listeleyen bir komut yerine, dizin içindeki dosyaları ve hatta sabit disk üzerindeki her şeyi silen bir komut yazdığını düşünün… Yanlış yazılmış bir program yüzünden bütün verilerinizi kaybetmeniz işten bile değildir. (Bahsettiğim o, ‘bütün sabit diski silen komutu’ kendi sisteminizde vermemeniz gerektiğini söylememe gerek yok, değil mi?)

# Eğer SQL Injection kavramını biliyorsanız, yukarıdaki kodların yol açtığı güvenlik açığını gayet iyi anlamış olmalısınız. Zaten internet üzerinde yaygın bir şekilde kullanılan ve web sitelerini hedef alan SQL Injection tarzı saldırılar da aynı mantık üzerinden gerçekleştiriliyor. SQL Injection metoduyla bir web sitesine saldıran cracker’lar, o web sitesini programlayan kişinin (çoğunlukla farkında olmadan) kullanıcıya verdiği rastgele SQL komutu işletme yetkisini kötüye kullanarak gizli ve özel bilgileri ele geçirebiliyorlar. Örneğin SQL Injection metodu kullanılarak, bir web sitesine ait veritabanının içeriği tamamen silinebilir. Aynı şekilde, yukarıdaki eval() fonksiyonu da kullanıcılarınıza rastgele Python komutlarını çalıştırma yetkisi verdiği için kötü niyetli bir kullanıcının programınıza sızmasına yol açabilecek potansiyele sahiptir.

# Peki eval() fonksiyonunu asla kullanmayacak mıyız? Elbette kullanacağız. Bu fonksiyonun kullanımını gerektiren durumlarla da karşılaşabilirsiniz. Ama şunu asla aklınızdan çıkarmayın: eval() fonksiyonu her ne kadar son derece yetenekli ve güçlü bir araç da olsa yanlış ellerde yıkıcı sonuçlar doğurabilir. Program yazarken, eğer eval() kullanmanızı gerektiren bir durumla karşı karşıya olduğunuzu düşünüyorsanız, bir kez daha düşünün. eval() ile elde edeceğiniz etkiyi muhtemelen başka ve çok daha iyi yöntemlerle de elde edebilirsiniz. Üstelik performans açısından eval() pek iyi bir tercih değildir, çünkü bu fonksiyon (çoğu durumda farketmeseniz de) aslında yavaş çalışır. O yüzden, eval() fonksiyonunu kullanacağınız zaman, bunun artı ve eksilerini çok iyi tartın: Bu fonksiyonu kullanmak size ne kazandırıyor, ne kaybettiriyor?

# Ayrıca eval() fonksiyonu kullanılacağı zaman, kullanıcıdan gelen veri bu fonksiyona parametre olarak verilmeden önce sıkı bir kontrolden geçirilir. Yani kullanıcının girdiği veri eval() aracılığıyla doğrudan değerlendirmeye tabi tutulmaz. Araya bir kontrol mekanizması yerleştirilir. Örneğin, yukarıdaki hesap makinesi programında kullanıcının gireceği verileri sadece sayılar ve işleçlerle sınırlandırabilirsiniz. Yani kullanıcınızın, izin verilen değerler harici bir değer girmesini engelleyebilirsiniz. Bu durumu somutlaştırmak için şöyle bir diyagram çizebiliriz:


#- (VERİ) > <eval()> > (ÇIKTI)

# Yukarıdaki diyagram eval() fonksiyonunun yanlış uygulanış biçimini gösteriyor. Gördüğünüz gibi, veri doğrudan eval() fonksiyonuna gidiyor ve çıktı olarak veriliyor. Böyle bir durumda, eval() fonksiyonu kullanıcıdan gelen verinin ne olduğuna bakmadan, veriyi doğrudan komut olarak değerlendirip işleteceği için programınızı kullanıcının insafına terketmiş oluyorsunuz.

#Aşağıdaki diyagram ise eval() fonksiyonunun doğru uygulanış biçimini gösteriyor:

#- (VERİ) > (KONTROL) > <eval()> > (ÇIKTI)

# Burada ise, veri eval() fonksiyonuna ulaşmadan önce kontrolden geçiriliyor. Eğer veri ancak kontrol aşamasından geçerse eval() fonksiyona ulaşabilecek ve oradan da çıktı olarak verilebilecektir. Böylece kullanıcıdan gelen komutları süzme imkanına sahip oluyoruz.

# Gördüğünüz gibi, Python eval() gibi bir fonksiyon yardımıyla karakter dizileri içinde geçen Python kodlarını ayıklayıp bunları çalıştırabiliyor. Bu sayede, mesela bize input() fonksiyonu aracılığıyla gelen bir karakter dizisi içindeki Python kodlarını işletme imkanına sahip olabiliyoruz. Bu özellik, dikkatli kullanıldığında, işlerinizi epey kolaylaştırabilir.

#! ---- exec() ------
# Python’da eval() fonksiyonuna çok benzeyen exec() adlı başka bir fonksiyon daha bulunur. eval() ile yapamadığımız bazı şeyleri exec() ile yapabiliriz. Bu fonksiyon yardımıyla, karakter dizileri içindeki çok kapsamlı Python kodlarını işletebilirsiniz.

# Örneğin eval() fonksiyonu bir karakter dizisi içindeki değişken tanımlama işlemini yerine getiremez. Yani eval() ile şöyle bir şey yapamazsınız:

#? eval("a = 45")

# Ama exec() ile böyle bir işlem yapabilirsiniz:

#? exec("a = 45")

# Böylece a adlı bir değişken tanımlamış olduk. # Kontrol edelim ;
#? print(a) # 45

# eval() ve exec() fonksiyonları özellikle kullanıcıdan alınan verilerle doğrudan işlem yapmak gereken durumlarda işinize yarar. Örneğin bir hesap makinesi yaparken eval() fonksiyonundan yararlanabilirsiniz.

# Aynı şekilde mesela insanlara Python programlama dilini öğreten bir program yazıyorsanız exec() fonksiyonunu şöyle kullanabilirsiniz:

d1 = """

Python'da ekrana çıktı verebilmek için print() adlı bir
fonksiyondan yararlanıyoruz. Bu fonksiyonu şöyle kullanabilirsiniz:

>>> print("Merhaba Dünya")

Şimdi de aynı kodu siz yazın!

>>> """

girdi = input(d1)

exec(girdi)

d2 = """

Gördüğünüz gibi print() fonksiyonu, kendisine
parametre olarak verilen değerleri ekrana basıyor.

Böylece ilk dersimizi tamamlamış olduk. Şimdi bir
sonraki dersimize geçebiliriz."""

print(d2)

# Burada exec() ile yaptığımız işi eval() ile de yapabiliriz. Ama mesela eğer bir sonraki derste ‘Python’da değişkenler’ konusunu öğretecekseniz, eval() yerine exec() fonksiyonunu kullanmak durumunda kalabilirsiniz.