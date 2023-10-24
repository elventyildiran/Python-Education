# Python’da yazdığımız şeylerin ekrana çıktı olarak verilebilmesi için print() adlı özel bir fonksiyondan yararlanmamız gerekir.
# print() de tıpkı daha önce gördüğümüz type(), len() ve pow() gibi bir fonksiyondur. Fonksiyonları ilerde daha ayrıntılı bir şekilde inceleyeceğimizi söylemiştik hatırlarsanız. O yüzden fonksiyon kelimesine takılarak, burada anlattığımız şeylerin kafanızı karıştırmasına, moralinizi bozmasına izin vermeyin.

# print() fonksiyonunun görevi ekrana çıktı vermemizi sağlamaktır. Hemen bununla ilgili bir örnek verelim:

print("Python programlama dili")
# Bildiğiniz gibi burada gördüğümüz “Python programlama dili” bir karakter dizisidir. İşte print() fonksiyonunun görevi bu karakter dizisini ekrana çıktı olarak vermektir.

#< Nasıl Kullanılır?

# Yukarıda verdiğimiz örnekte ilk gözümüze çarpan şey, karakter dizisini print() fonksiyonunun parantezleri içine yazmış olmamızdır. Biz bir fonksiyonun parantezleri içinde belirtilen öğelere ‘parametre’ dendiğini geçen bölümde öğrenmiştik. Tıpkı öğrendiğimiz öteki fonksiyonlar gibi, print() fonksiyonu da birtakım parametreler alır.

# Bu arada print() fonksiyonunun parantezini açıp parametreyi yazdıktan sonra, parantezi kapatmayı unutmuyoruz. Python programlama diline yeni başlayanların, hatta bazen deneyimli programcıların bile en sık yaptığı hatalardan biri açtıkları parantezi kapatmayı unutmalarıdır.

# Elbette, eğer istersek burada doğrudan “Python programlama dili” adlı karakter dizisini kullanmak yerine, önce bu karakter dizisini bir değişkene atayıp, sonra da print() fonksiyonunun parantezleri içinde bu değişkeni kullanabiliriz. Yani:

dil = "Python programlama dili"
print(dil)

# Bu arada, hem şimdi verdiğimiz, hem de daha önce yazdığımız örneklerde bir şey dikkatinizi çekmiş olmalı. Şimdiye kadar verdiğimiz örneklerde karakter dizilerini hep çift tırnakla gösterdik. Ama aslında tek seçeneğimiz çift tırnak değildir. Python bize üç farklı tırnak seçeneği sunar:

#? 1. Tek tırnak (' ')
#? 2. Çift tırnak (" ")
#? 3. Üç tırnak (""" """)

# Dolayısıyla yukarıdaki örneği üç farklı şekilde yazabiliriz:
print('Python programlama dili')
print("Python programlama dili")
print("""Python programlama dili""")

# Yukarıdaki çıktıların arasında hiçbir fark yok. Peki çıktılarda fark yoksa neden üç farklı tırnak çeşidi var ?

# İsterseniz bu soruyu bir örnek üzerinden açıklamaya çalışalım. Diyelim ki ekrana şöyle bir çıktı vermek istiyoruz :

#* Python programlama dilinin adı "piton" yılanından gelmez

#Eğer bu cümleyi çift tırnaklar içinde gösterirsek programımız hata verecektir:

#- print("Python programlama dilinin adı aslında "piton" yılanından gelmez")

#err: File "<stdin>", line 1
#err:  print("Python programlama dilinin adı "piton" yılanından gelmez")
#err:                                ^
#err: SyntaxError: invalid syntax


# Bunun sebebi, cümle içinde geçen ‘piton’ kelimesinin de çift tırnaklar içinde gösterilmiş olmasıdır. Cümlenin, yani karakter dizisinin kendisi de çift tırnak içinde gösterildiği için Python, karakter dizisini başlatan ve bitiren tırnakların hangisi olduğunu ayırt edemiyor. Yukarıdaki cümleyi en kolay şu şekilde ekrana yazdırabiliriz:

print('Python programlama dilinin adı aslında "piton" yılanından gelmez.')
# Bu gayet başarılı ve sorunsuz bir koddur.

# Burada karakter dizisini tek tırnak içine aldık. Karakter dizisi içinde geçen ‘piton’ kelimesi çift tırnak içinde olduğu için, karakter dizisini başlatıp bitiren tırnaklarla ‘piton’ kelimesindeki tırnakların birbirine karışması gibi bir durum söz konusu değildir.

# Bir de şöyle bir örnek verelim: Diyelim ki aşağıdaki gibi bir çıktı elde etmek istiyoruz:
#? İstanbul'un 5 günlük hava durumu tahmini

# Eğer bu karakter dizisini tek tırnak işaretleri içinde belirtirseniz Python size bir hata mesajı gösterecektir:

#- print('İstanbul'un 5 günlük hava durumu tahmini')

#err: File "<stdin>", line 1
#err:  print('İstanbul'un 5 günlük hava durumu tahmini')
#err:                    ^
#err: SyntaxError: invalid syntax

# Bu hatanın sebebi ‘İstanbul’un’ kelimesi içinde geçen kesme işaretidir. Tıpkı bir önceki örnekte olduğu gibi, Python karakter dizisini başlatan ve bitiren tırnakların hangisi olduğunu kestiremiyor. Python, karakter dizisinin en başındaki tek tırnak işaretinin ardından ‘İstanbul’un’ kelimesi içindeki kesme işaretini görünce karakter dizisinin burada sona erdiğini zannediyor. Ancak karakter dizisini soldan sağa doğru okumaya devam edince bir yerlerde bir terslik olduğunu düşünüyor ve bize bir hata mesajı göstermekten başka çaresi kalmıyor. Yukarıdaki karakter dizisini en kolay şöyle tanımlayabiliriz:

print("İstanbul'un 5 günlük hava tahmini.")

# Yukarıdaki karakter dizilerini düzgün bir şekilde çıktı verebilmek için üç tırnak işaretlerinden de yararlanabiliriz:

print("""Python programlama dilinin adı "piton" yılanından gelmez""")
print("""İstanbul'un 5 günlük hava durumu tahmini.""")

# Bütün bu örneklerden sonra kafanızda şöyle bir düşünce uyanmış olabilir:
#Görünüşe göre üç tırnak işaretiyle her türlü karakter dizisini hatasız bir şekilde ekrana çıktı olarak verebiliyoruz. O zaman ben en iyisi bütün karakter dizileri için üç tırnak işaretini kullanayım!

# Elbette, eğer isterseniz pek çok karakter dizisi için üç tırnak işaretini kullanabilirsiniz. Ancak Python’da karakter dizileri tanımlanırken genellikle tek tırnak veya çift tırnak işaretleri kullanılır. Üç tırnak işaretlerinin asıl kullanım yeri ise farklıdır. Peki nedir bu üç tırnak işaretlerinin asıl kullanım yeri?

# Üç tırnak işaretlerini her türlü karakter dizisiyle birlikte kullanabiliyor olsak da, bu tırnak tipi çoğunlukla sadece birden fazla satıra yayılmış karakter dizilerini tanımlamada kullanılır. Örneğin şöyle bir ekran çıktısı vermek istediğinizi düşünün:


print("""[H]=========HARMAN========[-][o][x]
|                                 |
|     Programa Hoşgeldiniz!       |
|           Sürüm 0.8             |
|    Devam etmek için herhangi    |
|       bir düğmeye basın.        |
|                                 |
|=================================|""")

print("Veya")

print("""Python programlama dili Guido Van Rossum
adlı Hollandalı bir programcı tarafından 90’lı
yılların başında geliştirilmeye başlanmıştır. Çoğu
insan, isminin "Python" olmasına bakarak, bu programlama
dilinin, adını piton yılanından aldığını düşünür.
Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez.""")

# Siz yukarıdaki çıktıyı tek veya çift tırnak kullanarak nasıl ekrana yazdırabileceğinizi düşünedurun, biz önemli bir konuya geçiş yapalım!

#! --- Bir Fonksiyon Olarak print() ---

# Gördüğünüz gibi, print() fonksiyonunu şöyle kullanıyoruz:

print("Aramak istediğiniz kelimeyi yazın: ")

# Burada print() bir fonksiyon, “Aramak istediğiniz kelimeyi yazın:” adlı karakter dizisi ise bu fonksiyonun parametresidir. Daha önce len() adlı başka bir fonksiyon daha öğrenmiştik hatırlarsanız. Onu da şöyle kullanıyorduk:
len("elma")

# Burada da len() bir fonksiyon, “elma” adlı karakter dizisi ise bu fonksiyonun parametresidir. Aslında biçim olarak print() ve len() fonksiyonlarının birbirinden hiçbir farkı olmadığını görüyorsunuz.

# Daha önce söylediğimiz ve bu örneklerden de anladığımız gibi, bir fonksiyonun parantezleri içinde belirtilen öğelere parametre adı veriliyor.

# print() fonksiyonu, tıpkı pow() fonksiyonu gibi, birden fazla parametre alabilir:

print('Fırat', 'Özgül')

# Bu örnekte bizim için çıkarılacak çok dersler var. Bir defa burada print() fonksiyonunu iki farklı parametre ile birlikte kullandık. Bunlardan ilki Fırat adlı bir karakter dizisi, ikincisi ise Özgül adlı başka bir karakter dizisi. Python’ın bu iki karakter dizisini nasıl birleştirdiğine dikkat edin. print() fonksiyonu bu iki karakter dizisini çıktı olarak verirken aralarına da birer boşluk yerleştirdi. Ayrıca, geçen derste de vurguladığımız gibi, parametrelerin birbirinden virgül ile ayrıldığını da gözden kaçırmıyoruz.

# Gelin bununla ilgili bir iki örnek daha verelim elimizin alışması için

print("Python", "Programlama", "Dili")
print("Fırat", "Özgül", "Adana", 1980)


#! --- print() Fonksiyonunun Parametreleri ---

# Şimdiye kadar verdiğimiz örneklerde belki çok da belli olmuyordur, ama aslında print() fonksiyonu son derece güçlü bir araçtır. İşte şimdi biz bu fonksiyonun gücünü gözler önüne seren özelliklerini incelemeye başlayacağız. Bu bölümü dikkatle takip etmeniz, ilerde yapacağımız çalışmaları daha rahat anlayabilmeniz açısından büyük önem taşır.

#< --- sep ---

# Burada print() fonksiyonunu iki farklı parametre ile birlikte kullandık. Bu fonksiyon, kendisine verdiğimiz bu parametreleri belli bir düzene göre birbiriyle birleştirdi. Bu düzen gereğince print(), kendisine verilen parametreleri birleştirirken, parametreler arasına bir boşluk yerleştiriyor. Bunu daha net görmek için şöyle bir örnek daha verelim:

print("Python", "PHP", "C++", "C", "Erlang") # Python PHP C++ C Erlang

# Gördüğünüz gibi, print() fonksiyonu gerçekten de, kendisine verilen parametreleri birleştirirken, parametrelerin her biri arasına bir boşluk yerleştiriyor. Halbuki bu boşluğu biz talep etmedik! Python bize bu boşluğu eşantiyon olarak verdi. Çoğu durumda istediğimiz şey bu olacaktır, ama bazı durumlarda bu boşluğu istemeyebiliriz. Örneğin:

print("http://","www.", "istihza.", "com") # http:// www. istihza. com

# Ya da boşluk karakteri yerine daha farklı bir karakter kullanmak istiyor da olabiliriz. Peki böyle bir durumda ne yapmamız gerekir?

#İşte bu noktada bazı özel araçlardan yararlanarak print() fonksiyonunun öntanımlı davranış kalıpları üzerinde değişiklikler yapabiliriz.

# Hatırlarsanız, Python’da fonksiyonların parantezleri içindeki değerlere parametre adı verildiğini söylemiştik. Mesela print() fonksiyonunu bir ya da daha fazla parametre ile birlikte kullanabileceğimizi biliyoruz:

# Fonksiyonların bir de daha özel görünümlü parametreleri vardır. Mesela print() fonksiyonunun sep adlı özel bir parametresi bulunur. Bu parametre print() fonksiyonunda görünmese bile her zaman oradadır. Yani diyelim ki şöyle bir kod yazdık:
print("http://", "www.", "google.", "com")

# Burada herhangi bir sep parametresi görmüyoruz. Ancak Python yukarıdaki kodu aslında şöyle algılar:
print("http://", "www.", "google.", "com", sep=" ")

#.Key : sep parametresinin kullanımı, sep kullanımı, separator kullanımı.
# sep ifadesi, İngilizcede separator (ayırıcı, ayraç) kelimesinin kısaltmasıdır. Dolayısıyla print() fonksiyonundaki bu sep parametresi, ekrana basılacak öğeler arasına hangi karakterin yerleştirileceğini gösterir. Bu parametrenin öntanımlı değeri bir adet boşluk karakteridir (” “). Yani siz bu özel parametrenin değerini başka bir şeyle değiştirmezseniz, Python bu parametrenin değerini bir adet boşluk karakteri olarak alacak ve ekrana basılacak öğeleri birbirinden birer boşlukla ayıracaktır. Ancak eğer biz istersek bu sep parametresinin değerini değiştirebiliriz. Böylece Python, karakter dizilerini birleştirirken araya boşluk değil, bizim istediğimiz başka bir karakteri yerleştirebilir. Gelin şimdi bu parametrenin değerini nasıl değiştireceğimizi görelim:

#* Örnek 1:
print("http://", "www.","istihza.","com") # http:// www. istihza. com
print("http://", "www.","istihza.","com", sep="") # http://www.istihza.com

#* Örnek sep 2:
print("T", "C", sep=".") # T.C

#* Örnek sep 3:
print("T", "B", "M", "M", sep=".") # T.B.M.M

#* Örnek sep 4:
print("bir", "iki", "üç", "dört", sep=" mumdur ") # bir mumdur iki mumdur üç mumdur dört

#* Örnek sep 5:
print(1, 2, 3, 4, 5, sep="-") #1-2-3-4-5

# Ancak sep parametresine değer olarak yalnızca karakter dizilerini ve None adlı özel bir sözcüğü verebiliriz. (None sözcüğünden ileride söz edeceğiz):

#- print(1,2,3,4,5, sep=0)
#err: Exception has occurred: TypeError
#err: sep must be None or a string, not int
#err:    print(1,2,3,4,5, sep=0)
#err: TypeError: sep must be None or a string, not int
# Gördüğünüz gibi, sep parametresine bir sayı olan 0 değerini veremiyoruz.

# Peki bu parametreye None değeri verirsek ne olur? Bu parametreye None değeri verildiğinde, print() fonksiyonu bu parametre için öntanımlı değeri (yani bir adet boşluk) kullanır:

#* Örnek sep 6:
print('a', 'b', sep=None) #a b

# Eğer amacınız parametreleri birbirine bitiştirmekse, yani sep parametresinin öntanımlı değeri olan boşluk karakterini ortadan kaldırmaksa, sep parametresine boş bir karakter dizisi vermeniz gerektiğini biliyorsunuz:

#* Örnek sep 7:
print('a', 'b', sep='') #ab

#.Key : end parametresinin kullanımı, end kullanımı.
#< --- end ---

# Bir önceki bölümde şöyle bir laf etmiştik:
#       print() fonksiyonun sep adlı özel bir parametresi bulunur. Bu parametre print() fonksiyonunda görünmese bile her zaman oradadır.

# Aynı bu şekilde, print() fonksiyonunun end adlı özel bir parametresi daha bulunur. Tıpkı sep parametresi gibi, end parametresi de print() fonksiyonunda görünmese bile her zaman oradadır.

# print() fonksiyonu öntanımlı olarak, parametrelerin sonuna ‘satır başı karakteri’ ekler. Peki bu satır başı karakteri (veya ‘yeni satır karakteri’) denen şey de ne oluyor?

# Yani kısacası bir alt satıra geçmek oluyor.

#* Örnek end 1;
print("Hey Merhaba Dünya!", end=".") # Hey Merhaba Dünya!.

# Ama yukarıdaki örnekte bir sorun var; Eğer bir print() fonksiyonu kullanarak alt satırda bir yazı yazmak istersek ne yazıkki alt satıra geçemeyecek, Hey Merhaba Dünya!. yazısının yanından devam edecektir. Çünkü end parametresinin varsayılan değeri satır başına geçmek yani aslında her zaman orada "\n" vardır.
# Hemen test edelim;
print("Yeni bir satır") # Hey Merhaba Dünya!.Yeni bir satır

# Görüldüğü gibi yeni bir satıra geçmedi, bunun nedenini yukarıda belirttik.
print("bir", "iki", "üç", "dört", "on dört",
sep=" mumdur ", end=" mumdur\n")

#- Burada kodlarımızın sağa doğru çirkin bir şekilde uzamasını engellemek için “on dört” karakter dizisini yazıp virgülü koyduktan sonra Enter tuşuna basarak bir alt satıra geçtik. Bir alt satıra geçtiğimizde >>> işaretinin … işaretine dönüştüğüne dikkat edin. Python’da doğru kod yazmak kadar, yazdığımız kodların düzgün görünmesi de önemlidir. O yüzden yazdığımız her bir kod satırının mümkün olduğunca 79 karakteri geçmemesini sağlamalıyız. Eğer yazdığınız bir satır 79 karakteri aşıyorsa, aşan kısmı yukarıda gösterdiğimiz şekilde alt satıra alabilirsiniz.

#Yine tıpkı sep parametresi gibi, end parametresinin değeri de sadece bir karakter dizisi veya None olabilir.
# Eğer bu parametreye None değeri verirsek, tıpkı sep parametresinde olduğu gibi, print() fonksiyonu bu parametre için öntanımlı değeri (yani satır başı karakteri) kullanır.

#.Key : file parametresinin kullanımı, file kullanımı, dosyaya yazma, dosyaya veri yazmak, dosya işlemleri, dizin değiştirme işlemleri, dosya yolu değiştirme, dosya konumunu belirleme.
#< --- file ---

# print() fonksiyonunun sep ve end dışında üçüncü bir özel parametresi daha bulunur. Bu parametrenin adı file’dır. Görevi ise, print() fonksiyonuna verilen karakter dizisi ve/veya sayıların, yani parametrelerin nereye yazılacağını belirtmektir.

# Bu parametrenin öntanımlı değeri sys.stdout’tur. Peki bu ne anlama geliyor? sys.stdout, ‘standart çıktı konumu’ anlamına gelir. Peki ‘standart çıktı konumu’ ne demek?
# Standart çıktı konumu; bir programın, ürettiği çıktıları verdiği yerdir. Aslında bu kavramın ne demek olduğu adından da anlaşılıyor:
# Standart çıktı konumu = çıktıların standart olarak verildiği konum.
# Mesela Python öntanımlı olarak, ürettiği çıktıları ekrana verir. Eğer o anda etkileşimli kabukta çalışıyorsanız, Python ürettiği çıktıları etkileşimli kabuk üzerinde gösterir. Eğer yazdığınız bir programı komut satırında çalıştırıyorsanız, üretilen çıktılar komut satırında görünür. Dolayısıyla Python’ın standart çıktı konumu etkileşimli kabuk veya komut satırıdır. Yani print() fonksiyonu yardımıyla bastığınız çıktılar etkileşimli kabukta ya da komut satırında görünecektir.

# Ama eğer istersek print() fonksiyonunun, çıktılarını ekrana değil, bir dosyaya yazdırmasını da sağlayabiliriz. Mesela biz şimdi print() fonksiyonunun deneme.txt adlı bir dosyaya çıktı vermesini sağlayalım.


#* Örnek 1, varsayılan çıktı konumuna dosya açıp içine veri yazmak ;
import os
dosya = open("deneme.txt", "w", encoding='utf-8')
print("Yeni bir metin dosyası actim! (Bu 'deneme.txt' adlı dosya, '1.0_print_fonksyionu.py' dosyasının 237. satırından oluşturulmuştur.) ", file=dosya)
dosya.close()


#*Örnek 2, belirlediğimiz bir konuma dosya açıp içine veri yazmak ;

import os # os modülünü içe aktarıyoruz
belirli_dizin = r"C:\Python-Education\Python-Education\1.1_print() Fonksiyonu" # Hangi dizin?
dosya_yolu = os.path.join(belirli_dizin, "deneme.txt") # belirli_dizin'de "deneme.txt" adlı dosyamızı oluşturuyoruz.
dosya = open(dosya_yolu, "w",  encoding="utf-8") # Yukarıda bulunan belirli dizinde, "w" yazma kipinde, "utf-8" karakter kodlarını destekleyen "deneme.txt" adlı dosyamızı açıyoruzç
print("Dosyaya yazdığım ilk yazı!\n(Bu 'deneme.txt' adlı dosya, '1.0_print_fonksyionu.py' dosyasının 247. satırından oluşturulmuştur.)", file=dosya) # Yazma işlemini burada tamamlıyoruz.
dosya.close() # Dosyaya yazdırma işlemini tamamladık ve artık kapatıyoruz.

# Şimdi tek tek açıklayalım ;

#* 1 - İlk satır, os modülünü içe aktarır. os modülü, işletim sistemi işlevlerini kullanmanıza yardımcı olur.

#* 2 - İkinci satırda, belirli_dizin adlı bir değişken oluşturulur ve bu değişkene bir belirli bir dizin yolu atanır. Bu dizin, r ön eki ile bir "raw string" olarak tanımlanır. Bu, dizin içindeki özel karakterleri (örneğin ters eğik çizgileri) işaretlemek için kullanılır.

#* 3 - Üçüncü satırda, os.path.join() işlevi kullanılarak dosya_yolu adlı bir değişken oluşturulur. os.path.join() işlevi, belirli_dizin değişkeni ile "deneme.txt" adlı bir dosyanın yolu arasında birleşme işlemi yapar. Sonuç olarak, dosya_yolu değişkeni, belirli bir dizindeki "deneme.txt" dosyasının tam yolu olur.

#* 4- Dördüncü satırda, open() işlevi kullanılarak "deneme.txt" adlı bir dosya oluşturulur ve dosya adlı bir değişkene atanır. Aynı zamanda, dosyanın yazma modunda ("w") açılmasını sağlar ve dosya kodlaması olarak "utf-8" seçilir.

#* 5 - Beşinci satırda, print() işlemi kullanılarak "Dosyaya yazdığım ilk yazı!" metni, belirtilen dosyaya yazılır. file argümanı ile dosya adlı dosya nesnesi belirtilir, bu nedenle metin dosyasına yazılır.

#* 6 - Altıncı satırda, dosya.close() işlemi kullanılarak dosya kapatılır. Dosyanın açık tutulması gerektiğinde işlem tamamlandığında dosyanın kapatılması iyi bir uygulamadır.


# Tıpkı sep ve end parametreleri gibi, file parametresi de, siz görmeseniz bile her zaman print() fonksiyonunun içinde vardır. Yani diyelim ki şöyle bir komut verdik:

print("Tahir olmak da ayıp değil", "Zühre olmak da")
import sys
#Python bu komutu şöyle algılar;
print("Tahir olmak da ayıp değil", "Zühre olmak da", sep=" ", 
end="\n", file=sys.stdout)

# Yani kendisine parametre olarak verilen değerleri ekrana yazdırırken sırasıyla şu işlemleri gerçekleştirir:

    # Parametrelerin arasına birer boşluk koyar (sep=" "),
    # Ekrana yazdırma işlemi bittikten sonra parametrelerin sonuna satır başı karakteri ekler (end="\n")
    # Bu çıktıyı standart çıktı konumuna gönderir (file=sys.stdout).

# İşte biz yukarıda file parametresinin değeri olan standart çıktı konumuna başka bir değer vererek bu konumu değiştiriyoruz.

# Gelin isterseniz bununla ilgili bir örnek daha yapalım. Mesela kişisel bilgilerimizi bir dosyaya kaydedelim. Öncelikle bilgileri kaydedeceğimiz dosyayı oluşturalım:

#* Örnek 3, kişisel bilgilerimizi bir dosyaya kaydetmek.
f = open("kisisel_bilgilerim.txt", "w", encoding='utf-8')
print("Elvent YILDIRAN\nEdirne\nWindows","(Bu 'kisisel_bilgilerim.txt' adlı dosya, '1.0_print_fonksyionu.py' dosyasının 285. satırından oluşturulmuştur.)", file=f)
# İşimiz bittiğinde dosyayı kapatmayı unutmuyoruz. Böylece bütün bilgiler dosyaya yazılmış oluyor:
f.close()


#< --- flush ----

# Bildiğiniz gibi, print() gibi bir komut verdiğimizde Python, yazdırmak istediğimiz bilgiyi standart çıktı konumuna gönderir. Ancak Python’da bazı işlemler standart çıktı konumuna gönderilmeden önce bir süre tamponda bekletilir ve daha sonra bekleyen bu işlemler topluca standart çıktı konumuna gönderilir. Peki ilk başta çok karmaşıkmış gibi görünen bu ifade ne anlama geliyor?

# Aslında siz bu olguya hiç yabancı değilsiniz. file parametresini anlatırken verdiğimiz şu örneği tekrar ele alalım:

#? f = open("kisisel_bilgilerim.txt", "w")
# Bu komutla kişisel_bilgilerim.txt adlı bir dosyayı yazma kipinde açtık. Şimdi bu dosyaya bazı bilgiler ekleyelim:

#? print("Elvent YILDIRAN", file=f)
# Bu komutla kişisel_bilgilerim.txt adlı dosyaya ‘Elvent YILDIRAN’ diye bir satır eklemiş olduk.

# Şimdi bilgisayarınızda oluşan bu kişisel_bilgiler.txt dosyasını açın. Gördüğünüz gibi dosyada hiçbir bilgi yok. Dosya şu anda boş görünüyor. Halbuki biz biraz önce bu dosyaya ‘Elvent YILDIRAN’ diye bir satır eklemiştik, değil mi?

# Python bizim bu dosyaya eklemek istediğimiz satırı tampona kaydetti. Dosyaya yazma işlemleri sona erdiğinde ise Python, tamponda bekleyen bütün bilgileri standart çıktı konumuna (yani bizim durumumuzda f adlı değişkenin tuttuğu kişisel_bilgilerim.txt adlı dosyaya) boşaltacak.

# Dosyaya başka bilgiler de yazalım:

#? print("Adana", file=f)

# Dosyaya yazacağımız şeyler bu kadar. Artık yazma işleminin sona erdiğini Python’a bildirmek için şu komutu veriyoruz:

#? f.close()

# Böylece dosyamızı kapatmış olduk. Şimdi kişisel_bilgiler.txt adlı dosyaya çift tıklayarak dosyayı tekrar açın. Orada ‘Elvent YILDIRAN’, ‘Edirne’ ve ‘Windows’ satırlarını göreceksiniz.

# Gördüğünüz gibi, gerçekten de Python dosyaya yazdırmak istediğimiz bütün verileri önce tamponda bekletti, daha sonra dosya kapatılınca tamponda bekleyen bütün verileri dosyaya boşalttı. İşte flush parametresi ile, bahsettiğimiz bu boşaltma işlemini kontrol edebilirsiniz. Şimdi dikkatlice inceleyin:

f = open("yeni_bilgiler.txt", "w", encoding='utf-8')
print("flush parametresini kullanmayı öğreniyorum!\n", "(Bu 'yeni_bilgiler.txt' adlı dosya, '1.0_print_fonksyionu.py' dosyasının 319. satırından oluşturulmuştur.)", file=f, flush=True)

# Gördüğünüz gibi, burada flush adlı yeni bir parametre kullandık. Bu parametreye verdiğimiz değer True. Şimdi dosyaya çift tıklayarak dosyayı açın. Gördüğünüz gibi, henüz dosyayı kapatmadığımız halde bilgiler dosyaya yazıldı. Bu durum, tahmin edebileceğiniz gibi, flush parametresine True değeri vermemiz sayesindedir. Bu parametre iki değer alabilir: True ve False. Bu parametrenin öntanımlı değeri False’tur. Yani eğer biz bu parametreye herhangi bir değer belirtmezsek Python bu parametrenin değerini False olarak kabul edecek ve bilgilerin dosyaya yazılması için dosyanın kapatılmasını bekleyecektir. Ancak bu parametreye True değerini verdiğimizde ise veriler tamponda bekletilmeksizin standart çıktı konumuna gönderilecektir.

# Yazdığınız bir programda, yapmak istediğiniz işin niteliğine göre, bir dosyaya yazmak istediğiniz bilgilerin bir süre tamponda bekletilmesini veya hiç bekletilmeden doğrudan dosyaya yazılmasını isteyebilirsiniz. İhtiyacınıza bağlı olarak da flush parametresinin değerini True veya False olarak belirleyebilirsiniz.


#? ------ Birkaç Pratik Bilgi ------

# Buraya gelene kadar print() fonksiyonu ve bu fonksiyonun parametreleri hakkında epey söz söyledik. Dilerseniz şimdi de, programcılık maceranızda işinize yarayacak, işlerinizi kolaylaştıracak bazı ipuçları verelim.

# Şimdi size şöyle bir soru sormama izin verin: Acaba aşağıdaki gibi bir çıktıyı nasıl elde ederiz?
#* L.i.n.u.x

# Aklınıza hemen şöyle bir cevap gelmiş olabilir:
print("L", "i", "n", "u", "x", sep=".") # L.i.n.u.x

# Evet, bu tamamen geçerli bir yanıttır ancak oldukça uğraştırıcı ve zaman kaybettiricidir. Bunu çözmenin çok daha basit bir yolu vardır.
# Dikkatle bakın ;
print(*"Linux", sep=".") # L.i.n.u.x

# yıldız (*) parametresi karakterlerin arasında birer boşluk bırakmamıza yarıyor.
print(*"Linux") # L i n u x

# Dediğimiz gibi, bir fonksiyona parametre olarak verdiğimiz bir karakter dizisinin başına eklediğimiz yıldız işareti, bu karakter dizisini tek tek öğelerine ayırıp, bu öğeleri yine tek tek ve sanki her bir öğe ayrı bir parametreymiş gibi o fonksiyona gönderdiği için doğal olarak yıldız işaretini ancak, birden fazla parametre alabilen fonksiyonlara uygulayabiliriz.

# Örneğin len() fonksiyonu sadece tek bir parametre alabilir 
len("Galatasaray") # 11

# Bu fonksiyonu birden fazla parametre ile kullanamayız.

# Yıldızlı parametreleri bir fonksiyona uygulayabilmemiz için o fonksiyonun birden fazla parametre alabilmesinin yanısıra, yapısının da yıldızlı parametre almaya uygun olması gerekir. Mesela open(), type() ve biraz önce bahsettiğimiz len() fonksiyonlarının yapısı yıldızlı parametre almaya uygun değildir. Dolayısıyla yıldızlı parametreleri her fonksiyonla birlikte kullanamayız, ama print() fonksiyonu yıldızlı parametreler için son derece uygun bir fonksiyondur.

# < ----- sys.stdout’u Kalıcı Olarak Değiştirmek -----

# Önceki başlıklar altında verdiğimiz örneklerden de gördüğünüz gibi, print() fonksiyonunun file parametresi yardımıyla Python’ın standart çıktı konumunu geçici olarak değiştirebiliyoruz. Ama bazı durumlarda, yazdığınız programlarda, o programın işleyişi boyunca standart dışı bir çıktı konumu belirlemek isteyebilirsiniz. Yani standart çıktı konumunu geçici olarak değil, kalıcı olarak değiştirmeniz gerekebilir. Mesela yazdığınız programda bütün çıktıları bir dosyaya yazdırmayı tercih edebilirsiniz. Elbette bu işlemi her defasında file parametresini, çıktıları yazdırmak istediğiniz dosyanın adı olarak belirleyerek yapabilirsiniz. Tıpkı şu örnekte olduğu gibi:

f = open("dosya.txt", "w", encoding='utf-8')
print("Fırat Özgül", file=f)
print("Adana", file=f)
print("Ubuntu", file=f)
f.close()

# Gördüğünüz gibi, her defasında file parametresine f değerini vererek işimizi hallettik. Ama bunu yapmanın daha pratik bir yöntemi var. Dilerseniz yazdığınız programın tüm işleyişi boyunca çıktıları başka bir konuma yönlendirebilirsiniz. Bunun için hem şimdiye kadar öğrendiğimiz, hem de henüz öğrenmediğimiz bazı bilgileri kullanacağız.

# İlk önce şöyle bir kod yazalım:

import sys

# Bu kod yardımıyla sys adlı özel bir ‘modülü’ programımıza dahil etmiş, yani içe aktarmış olduk. Peki ‘modül’ nedir, ‘içe aktarmak’ ne demek?
# sys modülü içinde pek çok önemli değişken ve fonksiyon bulunur. Ancak bir modül içindeki değişken ve fonksiyonları kullanabilmek için o modülü öncelikle programımıza dahil etmemiz, yani içe aktarmamız gerekiyor. Bunu import komutuyla yapıyoruz:

# sys modülü içinde bulunan pek çok değişken ve fonksiyondan biri de stdout adlı değişkendir. Bu değişkenin değerine şöyle ulaşabilirsiniz:

print(sys.stdout) # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

# Bu çıktıdaki name=’<stdout>’ kısmına dikkat edin. Bu ifadeye birazdan geri döneceğiz. Biz şimdi başka bir şeyden söz edelim.

# Hatırlarsanız etkileşimli kabuğu nasıl kapatabileceğimizi anlatırken, etkileşimli kabuktan çıkmanın bir yolunun da şu komutları vermek olduğunu söylemiştik:

#? import sys; sys.exit()

# Bu komutu tek satırda yazmıştık, ama istersek şöyle de yazabiliriz elbette:
#? import sys
#? sys.exit()

# Dedik ya, sys modülü içinde pek çok değişken ve fonksiyon bulunur. Nasıl stdout sys modülü içindeki değişkenlerden biri ise, exit() de sys modülü içinde bulunan fonksiyonlardan biridir.

#* 1 - 1. Python’da modüller import komutu ile içe aktarılır. Örneğin sys adlı modülü içe aktarmak için import sys komutunu veriyoruz.
#* 2 - Modüller içinde pek çok faydalı değişken ve fonksiyon bulunur. İşte bir modülü içe aktardığımızda, o modül içindeki bu değişken ve fonksiyonları kullanma imkanı elde ederiz.
#* 3 - sys modülü içindeki değişkenlere bir örnek stdout; fonksiyonlara örnek ise exit() fonksiyonudur. Bir modül içindeki bu değişken ve fonksiyonlara ‘modül_adı.değişken_ya_da_fonksiyon’ formülünü kullanarak erişebiliriz. Örneğin:

#? sys.stdout
#? sys.exit()

# Hadi tekrar işimize dönelim ;

import sys
f = open("sys_stdout_konum_degisti.txt", "w", encoding='utf-8')
# Bu kodun anlamını biliyorsunuz. Burada dosya.txt adlı bir dosyayı yazma kipinde açmış olduk. Tahmin edebileceğiniz gibi, çıktılarımızı ekran yerine bu dosyaya yönlendireceğiz.

sys.stdout = f

# Bildiğiniz gibi, sys.stdout değeri Python’ın çıktıları hangi konuma vereceğini belirliyor. İşte biz burada sys.stdout’un değerini biraz önce oluşturduğumuz f adlı dosya ile değiştiriyoruz. Böylece Python bütün çıktıları f değişkeni içinde belirttiğimiz dosya.txt adlı dosyaya gönderiyor.

print("Bakalım sys.stdout'un standart çıktı konumu gerçekten değişti mi?\n", "(Bu 'sys_stdout_konum_degisti.txt' adlı dosya, '1.0_print_fonksyionu.py' dosyasının 404. satırından oluşturulmuştur.)",)

# Evet gerçektende istediğimiz yere verdi, bu satırdan sonra yazılan her şey yukarıda adı geçen "sys_stdout_konum_degisti.txt" adlı dosyaya yazılacaktır.

# Gördüğünüz gibi, burada file parametresini kullanmadığımız halde çıktılarımız ekrana değil, ys_stdout_konum_degisti.txt adlı bir dosyaya yazdırıldı. Peki ama bu nasıl oldu? Aslında bunun cevabı çok basit: Biraz önce sys.stdout = f komutuyla sys.stdout’un değerini f değişkeninin tuttuğu dosya ile değiştirdik. Bu işlemi yapmadan önce sys.stdout’un değeri şuydu hatırlarsanız:

#? <_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1254'>
# Ama sys.stdout = f komutundan sonra her şey değişti. Kontrol edelim:
print(sys.stdout, flush=True)

# Gördüğünüz gibi, özgün stdout çıktısındaki name=’<stdout>’ değeri name=sys_stdout_konum_degisti.txt’ olmuş. Dolayısıyla artık bütün çıktılar sys_stdout_konum_degisti.txt adlı dosyaya gidiyor…

# Bu arada, yukarıdaki çıktıda görünen name, mode ve encoding değerlerine şu şekilde ulaşabilirsiniz:

# ? sys.stdout.name
# ? sys.stdout.mode
# ? sys.stdout.encoding

# Burada sys.stdout.name komutu standart çıktı konumunun o anki adını verecektir. sys.stdout.mode komutu ise standart çıktı konumunun hangi kipe sahip olduğunu gösterir. Standart çıktı konumu genellikle yazma kipinde (w) bulunur. sys.stdout.encoding kodu ise standart çıktı konumunun sahip olduğu kodlama biçimini gösterir. 

# Peki standart çıktı konumunu, etkileşimli kabuktan çıkmadan veya programı kapatmadan eski haline döndürmenin bir yolu var mı? Elbette var. Dikkatlice bakın:

import sys
f = open("sys_stdout_konum_degisti.txt", "w")
sys.stdout, f = f, sys.stdout
print("deneme", flush=True)
f, sys.stdout = sys.stdout, f
print("deneme")

# Aslında burada anlayamayacağınız hiçbir şey yok. Burada yaptığımız şeyi geçen bölümlerde değişkenlerin değerini nasıl takas edeceğimizi anlatırken de yapmıştık. Hatırlayalım:

osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje Sorumlusu"
osman, mehmet = mehmet, osman

# Bu kodlarla Osman ve Mehmet’in unvanlarını birbiriyle takas etmiştik. İşte yukarıda yaptığımız şey de bununla aynıdır. sys.stdout, f = f, sys.stdout dediğimizde f değerini sys.stdout’a, sys.stdout’un değerini ise f’ye vermiş oluyoruz. f, sys.stdout = sys.stdout, f dediğimizde ise, bu işlemin tam tersini yaparak her şeyi eski haline getirmiş oluyoruz. Python’ın bize sunduğu bu kolaylıktan faydalanarak değişkenlerin değerini birbiriyle kolayca takas edebiliyoruz. 