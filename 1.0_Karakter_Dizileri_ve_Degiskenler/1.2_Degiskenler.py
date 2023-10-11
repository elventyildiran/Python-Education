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

