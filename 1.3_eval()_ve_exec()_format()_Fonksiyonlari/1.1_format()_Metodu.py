#
#! ----- format() Metodu -----
# Python programlama dili içindeki çok temel bazı araçları incelediğimize göre, bu noktada Python’daki küçük ama önemli bir konuya değinelim bu bölümü kapatmadan önce.
#* Resme bakmak için linke git;
#? https://python-istihza.yazbel.com/_images/unknown_url.png

# Burada belli ki adres çubuğuna fdkgd.com diye bir URL yazmışız, ama böyle bir internet adresi olmadığı için, kullandığımız internet tarayıcısı bize şöyle bir mesaj vermiş:
#err: Hata! Google Chrome fdkgd.com sitesini bulamadı

# Şimdi de dadasdaf.com adresini arayalım…
# Yine böyle bir adres olmadığı için, bu defa tarayıcımız bize şöyle bir uyarı gösterecek:
#err: Hata! Google Chrome dadasdaf.com sitesini bulamadı

# Gördüğünüz gibi, hata mesajlarında değişen tek yer, aradığımız sitenin adresi. Yani internet tarayıcımız bu hata için şöyle bir taslağa sahip:
#err: Hata! Google Chrome ... sitesini bulamadı
# Burada … ile gösterdiğimiz yere, bulunamayan URL yerleştiriliyor. Peki böyle bir şeyi Python programlama dili ile nasıl yapabiliriz?

#. Key : Format metodu kullanımı, format kullanımı.
# Çok basit:
#* ÖRNEK ;
#Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

# #Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome", url, "sitesini bulamadı")

# Peki ya biz kullanıcının girdiği internet adresini mesela tırnak içinde göstermek istersek ne olacak? Yani örneğin şöyle bir çıktı vermek istersek:

#Bunun için yine karakter dizisi birleştirme yönteminden yararlanabilirsiniz:

#Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome", "'" + url + "'", "sitesini bulamadı")
#Burada, + işaretlerini kullanarak, kullanıcının girdiği adresin sağına ve soluna birer tırnak işaretini nasıl yerleştirdiğimize dikkat edin.

#Gördüğünüz gibi bu yöntem işe yarıyor, ama ortaya çıkan karakter dizisi de oldukça karmaşık görünüyor. İşte bu tür ‘karakter dizisi biçimlendirme’ işlemleri için Python bize çok faydalı bir araç sunuyor. Bu aracın adı format().

#Bu aracı şöyle kullanıyoruz:

#Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome {} sitesini bulamadı".format(url))

# Bir de bulunamayan internet adresini tırnak içine alalım:
print("Hata! Google Chrome '{}' sitesini bulamadı.".format(url))

# Görüyorsunuz ya, biraz önce karakter dizisi birleştirme yöntemini kullanarak gerçekleştirdiğimiz işlemi, çok daha basit bir yolla gerçekleştirme imkanı sunuyor bize bu format() denen araç…

# Peki format() nasıl çalışıyor?

# Bunu anlamak için şu basit örneklere bir bakalım:

print("{} ve {} iyi bir ikilidir".format("Python", "Django"))

# Elbette bu örnekleri şöyle de yazabilirdik:
metin = "{} ve {} iyi bir ikilidir"
metin.format("Python", "Django")

# Burada taslak metni doğrudan format() metoduna parametre olarak vermeden önce bir değişkene atadık. Böylece bu metni daha kolay bir şekilde kullanabildik.
