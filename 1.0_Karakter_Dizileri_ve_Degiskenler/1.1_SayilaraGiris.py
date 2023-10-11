 #! ----- Sayılara Giriş -----

# Dedik ki, Python’da birtakım veri tipleri bulunur ve karakter dizileri de bu veri tiplerinden yalnızca biridir. Veri tipi olarak karakter dizilerinin dışında, biraz önce aritmetik işleçler vesilesiyle sözünü ettiğimiz, bir de ‘sayı’ (number) adlı bir veri tipi vardır.
# Herhalde sayıların ne anlama geldiğini tarif etmeye gerek yok. Bunlar bildiğimiz sayılardır

#* Örnekler
print(23)
print(4567)
print(2.3)
print(10+2j) # Karmaşık sayılar.

# Python’da sayıların farklı alt türleri bulunur. Mesela tamsayılar, kayan noktalı sayılar, karmaşık sayılar…
# Yukarıdaki örnekler arasında geçen 23 ve 4567 birer tamsayıdır. İngilizcede bu tür sayılara integer adı verilir

# 2.3 ise bir kayan noktalı sayıdır (floating point number veya kısaca float). Bu arada kayan noktalı sayılarda basamak ayracı olarak virgül değil, nokta işareti kullandığımıza dikkat edin.
# En sonda gördüğümüz 10+2j sayısı ise bir karmaşık sayıdır (complex). Ancak eğer matematikle yoğun bir şekilde uğraşmıyorsanız karmaşık sayılar pek karşınıza çıkmaz.

#* Şimdi bazı basit matematik işlemleri yapalım ;

print(23 + 27) # 50
print(25*25) # 625
print(5 / 2) # 2.5
print(10 - 7) # 3

# Yukarıdaki örneklerde kullandığımız aritmetik işleçlerden biraz önce bahsetmiştik. O yüzden bunlara yabancılık çektiğinizi zannetmiyorum. Ama biz yine de bu işleçleri ve görevlerini şöylece sıralayalım:

# + Toplama
# - Çıkarma
# * Çarpma
# / Bölme

# Yukarıdaki örneklerde bir şey dikkatinizi çekmiş olmalı: Karakter dizilerini tanımlarken tırnak işaretlerini kullandık. Ancak sayılarda tırnak işareti yok. Daha önce de dediğimiz gibi, tırnak işaretleri karakter dizilerinin ayırt edici özelliğidir. Python’da tırnak içinde gösterdiğiniz her şey bir karakter dizisidir

print(34567)

print("34567")
# Çıktıya baktığımız zaman aslında her şey yolunda gibi, evet gerçektende yolunda. Ancak yukarıda birisi sayıyken, diğeri karakter dizesidir. Şimdi buna bakalım ;

print(type(34567)) # <class 'int'>
print(type("34567"))# <class 'str'>

# Gördüğünüz gibi, 34657 sayısını tırnak içine aldığımızda bu sayı artık sayı olma özelliğini yitiriyor ve bir karakter dizisi oluyor. Şu anda bu çok önemsiz bir ayrıntıymış gibi gelebilir size, ama aslında son derece önemli bir konudur bu.

#* Örnek 1 ;
print(23 + 65) # 88
#yukarıda iki sayıyı birbiryle topladık ve 88 sonucunu elde ettik.

print("23" + "65") # 2365
#Burada aslında iki karakter dizisini birleştirdik ve "2365" sonucunu aldık.
