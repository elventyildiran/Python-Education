#! ----- Kimlik İşleçleri -----

# Python'da her şeyin (ya da başka bir deyişle her nesnenin) bir kimlik numarası(identity) vardır. Kabaca söylemek gerekirse, bu kimlik numarası denen şey esasında o nesnenin bellekteki adresini gösterir.

# Peki bir nesnenin kimlik numarasına nasıl ulaşırız ?

# Python'da bu işi yapmamızı sağlayacak id() adlı bir fonksiyon bulunur (İngilizcedeki identity(kimlik) kelimesinin kısaltması). Şimdi bir örnek üzerinde bu id() fonksiyonunu nasıl kullanacağımıza bakalım:

a = 100
print(id(a)) # 140735473708936
# Çıktıda gördüğümüz 140735473708936 sayısı a değişkeninin tuttuğu 100 sayısının kimlik numarasını gösteriyor.
# Bu kimlik numarası muhtemelen sizde daha farklı olacaktır.

# Bir de şu örneklere bakalım:

a = 50
print(id(a)) # 505494576

kardiz = "Elveda Zalim Dünya!"
id(kardiz) # 156735467821340

# Gördüğünüz gibi, Python’daki her nesnenin kimliği eşşiz, tek ve benzersizdir.

# Yukarıda verdiğimiz ilk örnekte bir a değişkeni tanımlayıp bunun değerini 100 olarak belirlemiş ve id(a) komutuyla da bu nesnenin kimlik numarasına ulaşmıştık. Yani:

a = 100
print(id(a)) # 140735473708936

# Bir de şu örneğe bakalım:

b = 100
print(id(b)) # 140735473708936

# Gördüğünüz gibi, Python a ve b değişkenlerinin değeri için aynı kimlik numarasını gösterdi. Bu demek oluyor ki, Python iki adet 100 sayısı için bellekte iki farklı nesne oluşturmuyor. İlk kullanımda önbelleğine aldığı sayıyı, ikinci kez ihtiyaç olduğunda bellekten alıp kullanıyor. Bu tür bir önbellekleme mekanizmasının gerekçesi performansı artırmaktır.


a = 1000
print(id(a)) # 1525614341424

b = 1000
print(id(b)) # 1525614341424

print(a is 1000) # True
print(b is 1000) # True

#! ÖNEMLİ :

# Python'da, küçük tamsayılar ve bazı sık kullanılan sabit nesneler için, kimlik aynı olabilir. Ancak bu davranış, Python'ın işlemci özelliklerine ve uygulama bağlıdır. Özellikle, Python bu optimizasyonu yapabilmek için -5 ile 256 arasındaki tamsayıları özel bir şekilde işler.

# Bu nedenle, yukarıdaki kodda a ve b değişkenleri 1000 değerine sahip olsa da, bu değerlerin kimliği aynı olmayabilir.

# Sonuçlar, Python sürümüne ve uygulamaya bağlı olarak farklılık gösterebilir. Python, bu tür optimize edilmiş nesneler için aynı kimliği kullanarak bellek kullanımını azaltmaya çalışır, ancak bu her zaman garantili değildir ve bu davranışa güvenmemek daha iyidir. Eğer kimliklerin aynı olup olmadığını kontrol etmek istiyorsanız, "is" anahtar kelimesini kullanabilirsiniz:

a = 1000
b = 1000
print(a is b)  # Bu, a ve b'nin aynı nesneyi gösterip göstermediğini kontrol eder. 
# True

# id(a) ve id(b) aynı kimliği (memory address) gösterir.
# a is 1000 ve b is 1000, her ikisi de True döndürür, çünkü a ve b 1000 değerini aynı nesne olarak temsil eder.


#! ----- is işleci -----
#.Key : is işleci kullanımı. Kimlik karşılaştırma.

# Kimlik (Identity): Her Python nesnesi, bellekteki benzersiz bir konumda saklanır ve bir kimliğe sahiptir. Bu kimlik, nesnenin bellekteki adresini temsil eder.

# "is" İşleci: iki nesnenin kimliklerini karşılaştırmak için kullanılır. İki nesnenin aynı kimliği paylaşıyorsa (yani aynı bellek adresini gösteriyorlarsa), "is" işleci True döndürür. Aksi halde, "is" işleci False döndürür.

# Örnek bir kullanım:

a = [1, 2, 3]
b = a  # a ve b aynı nesneyi gösterir

if a is b:
    print("a ve b aynı nesneyi gösterir.")
else:
    print("a ve b farklı nesneleri gösterir.")

# Bu kod, a ve b değişkenlerinin aynı nesneyi gösterip göstermediğini kontrol eder. Eğer aynı nesneyi gösteriyorlarsa, "a ve b aynı nesneyi gösterir." yazısı ekrana yazdırılır.

# "==" işlecinden farkı, "==" işleci iki nesnenin eşitliğini (değerlerinin eşit olup olmadığını) kontrol ederken, "is" işleci iki nesnenin kimliklerini (bellek adreslerini) kontrol eder. Bu nedenle, "is" işlecini özellikle aynı nesnenin aynı kimliğe sahip olup olmadığını kontrol etmek için kullanırız.


#! Peki bu "is" işleci çok kullanılan bir işleç mi?

# "is" işleci, Python programlamada sık sık kullanılan bir işleç değildir. Genellikle iki nesnenin aynı kimliği olup olmadığını kontrol etmek için kullanılır, ancak çoğu zaman iki nesnenin eşitliğini (değerlerinin aynı olup olmadığını) kontrol etmek için "==" işleci kullanılır.

# Python'da "is" işleci bazı özel durumlar için kullanışlı olabilir, özellikle aynı nesneyi gösterip göstermediğinizi kontrol etmek istediğinizde. Örneğin, bir nesne "None" mı yoksa başka bir değer mi içeriyor, bir nesnenin tipini kontrol etmek gibi durumlarda "is" işleci kullanılabilir. Ancak, genellikle iki nesnenin eşitliğini kontrol etmek için "==" işleci daha yaygın olarak kullanılır.

# Bu nedenle, "is" işlecini kullanırken dikkatli olmalısınız ve özel durumlar için tercih edilmelidir. Çoğu zaman, iki nesnenin eşitliğini kontrol etmek için "==" işlecini kullanmak daha uygun ve okunaklıdır.
