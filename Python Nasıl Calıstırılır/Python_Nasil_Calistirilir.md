--Python Nasıl Çalıştırılır?--
Bir önceki bölümde, Python’ı farklı platformlara nasıl kuracağımızı bütün ayrıntılarıyla anlattık. Bu bölümde ise kurduğumuz bu Python programını hem GNU/Linux’ta hem de Windows’ta nasıl çalıştıracağımızı göreceğiz. Öncelikle GNU/Linux kullanıcılarının Python’ı nasıl çalıştıracağına bakalım.

--GNU/Linux Kullanıcıları--
Geçen bölümlerde gördüğünüz gibi, Python3’ü GNU/Linux sistemleri üzerine farklı şekillerde kurabiliyoruz. Bu bölümde, her bir kurulum türü için Python3’ün nasıl çalıştırılacağını ayrı ayrı inceleyeceğiz.

--Kurulu Python3’ü Kullananlar--
Eğer sisteminizde zaten Python3 kurulu ise komut satırında yalnızca şu komutu vererek Python3’ü başlatabilirsiniz:
    |
    |
        python
    |
    |
Ancak daha önce de dediğimiz gibi, 10.06.2023 tarihi itibariyle pek çok GNU/Linux dağıtımında öntanımlı olarak Python2 kuruludur. Dolayısıyla python komutunu verdiğinizde çalışan sürüm muhtemelen Python2 olacaktır. Bu yüzden sistemimizde öntanımlı olarak hangi sürümün kurulu olduğuna ve python komutunun hangi sürümü başlattığına çok dikkat etmelisiniz.
Yine daha önce de söylediğimiz gibi, sisteminizde hem Python2 hem de Python3 zaten kurulu durumda olabilir. O yüzden yukarıdaki komutu bir de python3 şeklinde vermeyi deneyebilirsiniz.
Örneğin Ubuntu GNU/Linux dağıtımının 12.10 sürümünden itibaren python komutu Python2’yi; python3 komutu ise Python3’ü çalıştırıyor.

--Python3’ü Depodan Kuranlar--
Dediğimiz gibi, 10.06.2023 tarihi itibariyle GNU/Linux dağıtımlarında öntanımlı Python sürümü ağırlıklı olarak Python2’dir. Dolayısıyla python komutu Python’ın 2.x sürümlerini çalıştırır. Bu durumdan ötürü, herhangi bir çakışmayı önlemek için GNU/Linux dağıtımları Python3 paketini farklı bir şekilde adlandırma yoluna gider. Şu anda piyasada bulunan dağıtımların ezici çoğunluğu Python3 paketini ‘python3’ şeklinde adlandırıyor. O yüzden GNU/Linux kullanıcıları, eğer paket yöneticilerini kullanarak Python kurulumu gerçekleştirmiş iseler, komut satırında şu komutu vererek Python3’ü başlatabilirler:
    |
    |
    python3
    |
    |
Bu komutun ardından şuna benzer bir ekranla karşılaşmış olmalısınız:

    "yazbel@ubuntu:~$ # python3
    Python 3.7.0 (default, 10.06.2023, 12:24:55)
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux
    Type “help”, “copyright”, “credits” or “license” for more information.
    ">>> 

Eğer yukarıdaki ekranı gördüyseniz Python’la programlama yapmaya hazırsınız demektir. Değilse, geriye dönüp işlerin nerede ters gittiğini bulmaya çalışabilirsiniz.

Bu aşamada işlerin nerede ters gitmiş olabileceğine dair birkaç ipucu verelim:

    1- Python3 kurulurken paket yöneticinizin herhangi bir hata vermediğinden, programın sisteminize başarıyla kurulduğundan emin olun. Bunun için Python3’ün kurulu paketler listesinde görünüp görünmediğini denetleyebilirsiniz.

    2 - python3 komutunu doğru verdiğinize emin olun. Python programlama diline özellikle yeni başlayanların en sık yaptığı hatalardan biri python kelimesini yanlış yazmaktır. Python yerine yanlışlıkla pyhton, pyton veya phyton yazmış olabilirsiniz. Ayrıca python3 komutunun tamamen küçük harflerden oluştuğuna dikkat edin. Python ve python bilgisayar açısından aynı şeyler değildir.

    3- Kullandığınız dağıtımın Python3 paketini adlandırma politikası yukarıda anlattığımızdan farklı olabilir. Yani sizin kullandığınız dağıtım, belki de Python3 paketini farklı bir şekilde adlandırmıştır. Eğer durum böyleyse, dağıtımınızın yardım kaynaklarını (wiki, forum, irc, yardım belgeleri, kullanıcı listeleri, vb.) kullanarak ya da forum.yazbel.com adresinde sorarak Python3’ün nasıl çalıştırılacağını öğrenmeyi deneyebilirsiniz.

Gelelim Python3’ü kaynaktan derlemiş olanların durumuna…

--Python3’ü root Olarak Derleyenler--
Eğer Python3’ü önceki bölümlerde anlattığımız şekilde kaynaktan root hakları ile derlediyseniz python3 komutu çalışmayacaktır. Bunun yerine şu komutu kullanmanız gerekecek:

    python3.11.4
    
        ! Kurduğunuz Python3 sürümünün 3.11.4 olduğunu varsayıyorum. Eğer farklı bir Python3 sürümü kurduysanız, elbette başlatıcı komut olarak o sürümün adını 
        ! kullanmanız gerekecektir. Mesela: python3.0 veya python3.1. Bu arada python3.11.4 komutunda 3114 sayısının rakamları arasında bir adet nokta işareti olduğunu ! gözden kaçırmıyoruz…

Tıpkı paket deposundan kurulumda olduğu gibi, eğer yukarıdaki komut Python’ı çalıştırmanızı sağlamıyorsa, kurulum esnasında bazı şeyler ters gitmiş olabilir. Örneğin kaynaktan kurulumun herhangi bir aşamasında bir hata almış olabilirsiniz ve bu da Python’ın kurulumunu engellemiş olabilir.

Gördüğünüz gibi, Python’ı kaynaktan derleyenler Python programlama dilini çalıştırabilmek için Python’ın tam sürüm adını belirtiyor. Dilerseniz bu şekilde çalışmaya devam edebilirsiniz. Bunun hiçbir sakıncası yok. Ancak ben size kolaylık açısından, /usr/bin/ dizini altına py3 adında bir sembolik bağ yerleştirmenizi tavsiye ederim. Böylece sadece py3 komutunu vererek Python3’ü başlatabilirsiniz.

Peki bunu nasıl yapacağız?

Python kaynaktan derlendiğinde çalıştırılabilir dosya /usr/local/bin/ dizini içine Python3.7 (veya kurduğunuz Python3 sürümüne bağlı olarak Python3.0 ya da Python3.1) adıyla kopyalanır. Bu nedenle Python3’ü çalıştırabilmek için python3.7 komutunu kullanmamız gerekir. Python3’ü çalıştırabilmek için mesela sadece py3 gibi bir komut kullanmak istiyorsak yapacağımız tek şey /usr/local/bin/ dizini içindeki python3.7 adlı dosyaya /usr/bin dizini altından, py3 adlı bir sembolik bağ oluşturmak olacaktır. Bunun için ln komutunu kullanacağız:

    "ln -s /usr/local/bin/python3.7 /usr/bin/py3"

Tabii bu komutu yetkili kullanıcı olarak vermeniz gerektiğini söylememe herhalde gerek yoktur. Bu komutu verdikten sonra artık sadece py3 komutu ile Python programlama dilini başlatabilirsiniz.
