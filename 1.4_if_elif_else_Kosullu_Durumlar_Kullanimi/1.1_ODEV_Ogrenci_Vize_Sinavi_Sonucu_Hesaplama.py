#
#- Ödev: Bir Vize Sınavı Sonucu Hesaplama

# Bir öğrencinin vize sınav sonucuna göre notunu hesaplayan bir program yazın. Program aşağıdaki kurallara göre çalışmalı:

#? * Kullanıcıdan vize sınav sonucunu (0-100 arasında bir tam sayı) alın.
#? * Sonucu kullanarak aşağıdaki not skalasına göre öğrencinin notunu belirleyin ve ekrana yazdırın:
#- * 90-100: AA
#- * 85-89: BA
#- * 80-84: BB
#- * 75-79: CB
#- * 70-74: CC
#- * 65-69: DC
#- * 60-64: DD
#- * 55-59: FD
#- * 0-54: FF
# Örneğin, kullanıcı 75 girdiğinde program "CB" notunu döndürmelidir. Programınızın, geçerli olmayan girişlere (0'dan küçük veya 100'den büyük) karşı da bir hata mesajı vermesi gerekebilir.
# Bu ödev, koşullu ifadeleri kullanarak bir sınav notu hesaplama programı oluşturmanızı sağlayacak ve bu tür temel programlama becerilerinizi geliştirmenize yardımcı olacaktır.


vize1 = int(input("1. vize notunuzu girin : "))
vize2 = int(input("2. vize notunuzu girin : "))
final = int(input("Final notunuzu girin : "))
ortalama = (vize1 + vize2 + final ) / 3

if ortalama >= 90:
    print("Tebrikler notunuz {} : AA".format(int(ortalama)))
elif 85 <= ortalama < 90:
    print("Tebrikler notunuz {} : BA".format(int(ortalama)))
elif 80 <= ortalama < 85:
    print("Tebrikler notunuz {} : BB".format(int(ortalama)))
elif 75 <= ortalama < 80:
    print("Tebrikler notunuz {} : CB".format(int(ortalama)))
elif 70 <= ortalama < 75:
    print("Tebrikler notunuz {} : CC".format(int(ortalama)))
elif 65 <= ortalama < 70:
    print("Tebrikler notunuz {} : DC".format(int(ortalama)))
elif 60 <= ortalama < 65:
    print("Tebrikler notunuz {} : DD".format(int(ortalama)))
elif 55 <= ortalama < 60:
    print("Tebrikler notunuz {} : FD".format(int(ortalama)))
elif 0 <= ortalama < 55:
    print("Biraz daha çalışmanız gerekiyor {} : FF".format(int(ortalama)))
else:
    print("Notlarınızı tekrar gözden geçirin, not girişiniz yanlış olabilir.")


#* Yukarıda yaptığımız işlemleri şimdi madde madde açıklayalım.

# 1 - Kullanıcıdan 1. vize notunu girmesi istenir ve bu değer vize1 değişkenine atanır.
# 2 - Kullanıcıdan 2. vize notunu girmesi istenir ve bu değer vize2 değişkenine atanır.
# 3 - Kullanıcıdan final notunu girmesi istenir ve bu değer final değişkenine atanır.
# 4 - Vize notlarının ve final notunun ortalaması ortalama değişkenine atanır. Ortalama hesaplaması, vize1, vize2 ve final notlarının toplamının 3'e bölünmesi ile yapılır.

# Kodun geri kalanı, öğrencinin ortalama notuna göre hangi harf notunu aldığını belirlemek için kullanılır. 
# İşte bu bölümün madde madde açıklaması:

# 1 - İlk olarak, if ifadesi ile öğrencinin ortalama notu 90'a eşit veya daha yüksek mi diye kontrol edilir. Eğer bu koşul sağlanıyorsa, "Tebrikler notunuz AA" yazdırılır.

# 2 - İkinci elif ifadesi ile öğrencinin ortalama notu 85 ile 90 arasında mı diye kontrol edilir. Eğer bu koşul sağlanıyorsa, "Tebrikler notunuz BA" yazdırılır. Bu kod, öğrencinin not aralıklarını kontrol ederek, ortalama notuna göre uygun harf notunu ekrana yazdırır. Diğer elif blokları benzer şekilde diğer not aralıklarını kontrol eder ve uygun harf notlarını verir. 

# 3 - Son else bloğu ise kullanıcının hatalı not girdiği durumu ele alır ve bir uyarı mesajı gösterir.

# Bu şekilde, program öğrencinin notlarını alır, ortalama notunu hesaplar ve uygun harf notunu verir, hatta kullanıcının hatalı not girdiğini kontrol eder.

# Not : Henüz hata denetimini ele almadığımız için, eğer öğrenci bir not girmezse program hata verecektir...