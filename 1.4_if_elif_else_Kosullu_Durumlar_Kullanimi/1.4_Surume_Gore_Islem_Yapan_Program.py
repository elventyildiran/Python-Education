
#! ----- Sürüme Göre İşlem Yapan Program -----
#. Key : Sürüme göre işlem yapma, sürüm ayarları yapma, sürüm ayarlama, sürüme göre işlem yapan program.
# Bildiğiniz gibi, şu anda piyasada iki farklı Python serisi bulunuyor: Python2 ve Python3. Daha önce de söylediğimiz gibi, Python’ın 2.x serisi ile çalışan bir program Python’ın 3.x serisi ile muhtemelen çalışmayacaktır. Aynı şekilde bunun tersi de geçerlidir. Yani 3.x ile çalışan bir program 2.x ile büyük ihtimalle çalışmayacaktır.

# Bu durum, yazdığınız programların farklı Python sürümleri ile çalıştırılma ihtimaline karşı bazı önlemler almanızı gerektirebilir. Örneğin yazdığınız bir programda kullanıcılarınızdan beklentiniz, programınızı Python’ın 3.x sürümlerinden biri ile çalıştırmaları olabilir. Eğer programınız Python’ın 2.x sürümlerinden biri ile çalıştırılırsa kullanıcıya bir uyarı mesajı göstermek isteyebilirsiniz.

# Hatta yazdığınız bir program, aynı serinin farklı sürümlerinde dahi çalışmayı engelleyecek özellikler içeriyor olabilir. Örneğin print() fonksiyonunun flush adlı parametresi dile 3.3 sürümü ile birlikte eklendi. Dolayısıyla bu parametreyi kullanan bir program, kullanıcının 3.3 veya daha yüksek bir Python sürümü kullanmasını gerektirir. Böyle bir durumda, programınızı çalıştıran Python sürümünün en düşük 3.3 olmasını temin etmeniz gerekir.

# Peki bunu nasıl yapacaksınız?

# Burada aklınızda ilk olarak, kodlarınıza #!/usr/bin/env python3.3 veya #! python3.3 gibi bir satır eklemek gelmiş olabilir. Ama unutmayın, bu çözüm ancak kısıtlı bir işlevsellik sunabilir. Programımıza böyle bir satır eklediğimizde, programımızın Python’ın 3.3 sürümü ile çalıştırılması gerektiğini belirtiyoruz. Ama 3.3 dışı bir sürümle çalıştırıldığında ne olacağını belirtmiyoruz. Böyle bir durumda, eğer programımız 3.3 dışı bir sürümle çalıştırılırsa çökecektir. Bizim burada daha kapsamlı ve esnek bir çözüm bulmamız gerekiyor.

# Hatırlarsanız önceki derslerden birinde sys adlı bir modülden söz etmiştik. Bildiğiniz gibi, bu modül içinde pek çok yararlı değişken ve fonksiyon bulunuyor. Önceki derslerimizde, bu modül içinde bulunan exit() fonksiyonu ile stdout ve version değişkenlerini gördüğümüzü hatırlıyor olmalısınız. sys modülü içinde bulunan exit() fonksiyonunun programdan çıkmamızı sağladığını, stdout değişkeninin standart çıktı konumu bilgisini tuttuğunu ve version değişkeninin de kullandığımız Python sürümü hakkında bilgi verdiğini biliyoruz. İşte yukarıda bahsettiğimiz programda da bu sys modülünden yararlanacağız.

# Bu iş için, version değişkenine çok benzeyen version_info adlı bir değişkeni kullanacağız.

# Bu değişkenin nasıl kullanıldığına etkileşimli kabukta beraberce bakalım…

# sys modülü içindeki araçları kullanabilmek için öncelikle bu modülü içe aktarmamız gerektiğini biliyorsunuz:

#< import sys

# Şimdi de bu modül içindeki version_info adlı değişkene erişelim:

#< sys.version_info

# Bu komut bize şöyle bir çıktı verir:
#- sys.version_info(major=3, minor=11, micro=4, releaselevel='final', serial=0)

# Gördüğünüz gibi, bu değişken de bize tıpkı version adlı değişken gibi, kullandığımız Python sürümü hakkında bilgi veriyor.

# Ben yukarıdaki komutu Python3’te verdiğinizi varsaydım. Eğer yukarıdaki komutu Python3 yerine Python2’de verseydik şöyle bir çıktı alacaktık:

#- sys.version_info(major=|major2|, minor=|minor2|, micro=|micro2|, releaselevel='final', serial=0)

# version_info ve version değişkenlerinin verdikleri çıktının birbirlerinden farklı yapıda olduğuna dikkat edin. version değişkeni, version_info değişkeninden farklı olarak şöyle bir çıktı verir:

#- '3.7.0 (default, 10.06.2023, 12:24:55)
#- [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux'


#< sys.version

#- '3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]'

# version_info değişkeninin verdiği çıktı bizim şu anda yazmak istediğimiz programa daha uygun. Bunun neden böyle olduğunu biraz sonra siz de anlayacaksınız.

# Gördüğünüz gibi, version_info değişkeninin çıktısında major ve minor gibi bazı değerler var. Çıktıdan da rahatlıkla anlayabileceğiniz gibi, major, kullanılan Python serisinin ana sürüm numarasını; minor ise alt sürüm numarasını verir. Çıktıda bir de micro adlı bir değer var. Bu da kullanılan Python serisinin en alt sürüm numarasını verir.

# Bu değere şu şekilde ulaşıyoruz :
#< sys.version_info.major
#- 3

# Öteki değerlere de aynı şekilde ulaşıyoruz:
#< sys.version_info.minor
#< sys.version_info.micro

# İşte bu çıktılardaki major (ve yerine göre bununla birlikte minor ve micro) değerini kullanarak, programımızın hangi Python sürümü ile çalıştırılması gerektiğini kontrol edebiliriz. Şimdi programımızı yazalım:

import sys
_2x_metni = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""

_3x_metni = "Programa hoşgeldiniz."

if sys.version_info.major < 3:
    print(_2x_metni)
else:
    print(_3x_metni)
    
# Gelin isterseniz öncelikle bu kodları biraz inceleyelim.

# İlk olarak modülümüzü içe aktarıyoruz. Bu modül içindeki araçları kullanabilmemiz için bunu yapmamız şart:

#< import sys

# Ardından Python’ın 2.x sürümlerinden herhangi birini kullananlar için bir uyarı metni oluşturuyoruz:

#< _2x_metni = """
#< Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
#< Programı çalıştırabilmek için sisteminizde Python'ın
#< 3.x sürümlerinden biri kurulu olmalı."""

# Bildiğiniz gibi Python’da değişken adları bir sayıyla başlamaz. O yüzden değişken isminin başına bir tane alt çizgi işareti koyduğumuza dikkat edin.

# Bu da Python3 kullanıcıları için:

#< _3x_metni = "Programa hoşgeldiniz."

# Artık sürüm kontrolü kısmına geçebiliriz. Eğer major parametresinin değeri 3’ten küçükse _2x_metnini yazdırıyoruz. Bunun dışındaki bütün durumlar için ise _3x_metnini basıyoruz:

#< if sys.version_info.major < 3:
#<    print(_2x_metni)
#< else:
#<    print(_3x_metni)

# Gördüğünüz gibi, kullanılan Python sürümünü kontrol etmek ve eğer program istenmeyen bir Python sürümüyle çalıştırılıyorsa ne yapılacağını belirlemek son derece kolay.

# Yukarıdaki çok basit bir kod parçası olsa da bize Python programlama diline ve bu dilin farklı sürümlerine dair son derece önemli bazı bilgiler veriyor.

# Eğer bu programı Python’ın 3.x sürümlerinden biri ile çalıştırdıysanız şu çıktıyı alacaksınız:

#- Programa hoşgeldiniz.

# Ama eğer bu programı Python’ın 2.x sürümlerinden biri ile çalıştırdıysanız, beklentinizin aksine, şöyle bir hata mesajı alacaksınız:

#- File "test.py", line 5
#- SyntaxError: Non-ASCII character '\xc4' in file test.py on line 6, but no
#- encoding declared; see http://www.python.org/peps/pep-0263.html for details

# Biz _2x_metni adlı değişkenin ekrana basılmasını beklerken Python bize bir hata mesajı gösterdi. Aslında siz bu hata mesajına hiç yabancı değilsiniz. Bunu daha önce de görmüştünüz. Hatırlarsanız önceki derslerimizde karakter kodlamalarından bahsederken, Python’ın 2.x sürümlerinde öntanımlı karakter kodlamasının ASCII olduğundan söz etmiştik. Bu yüzden programlarımızda Türkçe karakterleri kullanırken bazı ilave işlemler yapmamız gerekiyordu.

# Burada ilk olarak karakter kodlamasını UTF-8 olarak değiştirmemiz gerekiyor. Bunun nasıl yapılacağını biliyorsunuz. Programımızın ilk satırına şu kodu ekliyoruz:

# -*- coding: utf-8 -*-

# Bu satır Python3 için gerekli değil. Çünkü Python3’te öntanımlı karakter kodlaması zaten UTF-8. Ama Python2’de öntanımlı karakter kodlaması ASCII. O yüzden Python2 kullanıcılarını da düşünerek UTF-8 kodlamasını açıkça belirtiyoruz. Böylece programımızın Python’ın 2.x sürümlerinde Türkçe karakterler yüzünden çökmesini önlüyoruz.

# Ama burada bir problem daha var. Programımız Türkçe karakterler yüzünden çökmüyor çökmemesine ama, bu defa da Türkçe karakterleri düzgün göstermiyor:

# - Python'Ä±n 2.x sÃ¼rÃ¼mlerinden birini kullanÄ±yorsunuz.
#- ProgramÄ± Ã§alÄ±ÅŸtÄ±rabilmek iÃ§in sisteminizde Python'Ä±n
#- 3.x sÃ¼rÃ¼mlerinden biri kurulu olmalÄ±.

# Programımızı Python’ın 2.x sürümlerinden biri ile çalıştıranların uyarı mesajını düzgün bir şekilde görüntüleyebilmesini istiyorsanız, Türkçe karakterler içeren karakter dizilerinin en başına bir ‘u’ harfi eklemelisiniz. Yani _2x_metni adlı değişkeni şöyle yazmalısınız:

_2x_metni = u"""
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
#. Key : Türkçe karakter sorunu, türkçe karakter düzeltme, türkçe karakterler gözükmüyor.
# Bu karakter dizisinin en başına bir ‘u’ harfi ekleyerek bu karakter dizisini ‘unicode’ olarak tanımlamış olduk. Eğer ‘unicode’ kavramını bilmiyorsanız endişe etmeyin. İlerde bu kavramdan bolca söz edeceğiz. Biz şimdilik, içinde Türkçe karakterler geçen karakter dizilerinin Python2 kullanıcıları tarafından düzgün görüntülenebilmesi için başlarına bir ‘u’ harfi eklenmesi gerektiğini bilelim yeter.

# Eğer siz bir Windows kullanıcısıysanız ve bütün bu işlemlerden sonra bile Türkçe karakterleri düzgün görüntüleyemiyorsanız, bu durum muhtemelen MS-DOS komut satırının kullandığı yazı tipinin Türkçe karakterleri gösterememesinden kaynaklanıyordur. Bu problemi çözmek için MS-DOS komut satırının başlık çubuğuna sağ tıklayıp ‘özellikler’ seçeneğini seçerek yazı tipini ‘Lucida Console’ olarak değiştirin. Bu işlemin ardından da komut satırında şu komutu verin:

#< chcp 1254
# Böylece Türkçe karakterleri düzgün görüntüleyebilirsiniz.

# MS-DOS’taki Türkçe karakter problemi hakkında daha ayrıntılı bilgi için https://web.archive.org/web/20150516030259/http://www.istihza.com/py2/python-programlarini-kaydetmek.html#ms-dos-ta-turkce-karakter-problemi adresindeki makalemizi inceleyebilirsiniz.

# Şimdiye kadar anlattıklarımızdan öğrendiğiniz gibi, sys modülü içinde sürüm denetlemeye yarayan iki farklı değişken var. Bunlardan biri version, öbürü ise version_info.

# Python3’te bu değişkenlerin şu çıktıları verdiğiniz biliyoruz:

#! version:

#- '3.7.0 (default, 10.06.2023, 12:24:55)
#- [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux'

#! version_info:
# - sys.version_info(major=3, minor=11, micro=4, releaselevel='final', serial=0)

# Gördüğünüz gibi, çıktıların hem yapıları birbirinden farklı, hem de verdikleri bilgiler arasında bazı farklar da var. Mesela version değişkeni, kullandığımız Python sürümünün hangi tarih ve saatte, hangi işletim sistemi üzerinde derlendiği bilgisini de veriyor. Ancak kullanılan Python sürümünün ne olduğunu tespit etmek konusunda version_info biraz daha pratik görünüyor. Bu değişkenin bize major, minor ve micro gibi parametreler aracılığıyla sunduğu sayı değerli verileri işleçlerle birlikte kullanarak bu sayılar üzerinde aritmetik işlemler yapıp, kullanılan Python sürümünü kontrol edebiliyoruz.

# version değişkeni bize bir karakter dizisi verdiği için, bu değişkenin değerini kullanarak herhangi bir aritmetik işlem yapamıyoruz. Mesela version_info değişkeniyle yukarıda yaptığımız büyüktür-küçüktür sorgulamasını version değişkeniyle tabii ki yapamayız.

# Yukarıdaki örnekte seriler arası sürüm kontrolünü nasıl yapacağımızı gördük. Bunun için kullandığımız kod şuydu:

#< if sys.version_info.major < 3:
#<      ...


# Burada kullanılan Python serisinin 3.x'ten düşük olduğu durumları sorguladık. Peki aynı serinin farklı sürümlerini denetlemek istersek ne yapacağız ? Mesela Python'ın 3.2 sürümünü sorgulamak istersek nasıl bir kod kullanacağız ?

# Bunun için şöyle bir şey yazabiliriz :

#< if sys.version_info.major ==  3 and sys.version_info.minor == 2:
#<      ...

# Gördüğünüz gibi burada version_info değişkeninin hem major hem de minor parametrelerini kullandık. Ayrıca hem ana sürüm, hem de alt sürüm için belli bir koşul talep ettiğimizden ötürü and adlı Bool işlecinden de yararlandık. Çünkü koşulun gerçekleşmesi, ana sürümün 3 ve alt sürümün 2 olmasına bağlı.

# ukarıdaki işlem için version değişkenini de kullanabilirdik. Dikkatlice bakın:

#< if "3.2" in sys.version:
#<      ...

# Bildiğiniz gibi, version değişkeni Python’ın 3.x sürümlerinde şuna benzer bir çıktı veriyor:

#- '3.7.0 (default, 10.06.2023, 12:24:55)
#- [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux'

# İşte biz burada in işlecini kullanarak, version değişkeninin verdiği karakter dizisi içinde ‘3.2’ diye bir ifade aradık.
# Bu konuyu daha iyi anlamak için kendi kendinize bazı denemeler yapmanızı tavsiye ederim. Ne kadar çok örnek kod yazarsanız, o kadar çok tecrübe kazanırsınız
