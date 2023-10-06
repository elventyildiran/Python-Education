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

--Çok Önemli Bir Uyarı--

Bir önceki adımda anlattığımız gibi Python3’ü resmi sitesinden indirip kendiniz derlediniz. Gayet güzel. Ancak bu noktada çok önemli bir konuya dikkatinizi çekmek isterim. En baştan beri söylediğimiz gibi, Python programlama dili GNU/Linux işletim sistemlerinde çok önemli bir yere sahiptir. Öyle ki bu programlama dili, kullandığınız dağıtımın belkemiği durumunda olabilir.

Örneğin Ubuntu GNU/Linux dağıtımında pek çok sistem aracı Python ile yazılmıştır. Bu yüzden, sistemdeki öntanımlı Python sürümünün ne olduğu ve dolayısıyla python komutunun hangi Python sürümünü çalıştırdığı çok önemlidir. Çünkü sisteminizdeki hayati bazı araçlar, python komutunun çalıştırdığı Python sürümüne bel bağlamış durumdadır. Dolayısıyla sizin bu python komutunun çalıştırdığı Python sürümüne dokunmamanız gerekir.

Mesela eğer kullandığınız işletim sisteminde python komutu Python’ın 2.x sürümlerinden birini çalıştırıyorsa sembolik bağlar veya başka araçlar vasıtasıyla python komutunu Python’ın başka bir sürümüne bağlamayın. Bu şekilde bütün sistemi kullanılmaz hale getirirsiniz. Elbette eğer kurulum aşamasında tarif ettiğimiz gibi, Python3’ü make install yerine make altinstall komutu ile kurmaya özen gösterdiyseniz, sonradan oluşturduğunuz bağ dosyasını silip python komutunu yine sistemdeki öntanımlı sürüme bağlayabilirsiniz. Bu şekilde her şey yine eski haline döner. Ama eğer Python’ı make install komutuyla kurmanızdan ötürü sistemdeki öntanımlı Python sürümüne ait dosyaları kaybettiyseniz sizin için yapılacak fazla bir şey yok… Sistemi tekrar eski kararlı haline getirmek için kan, ter ve gözyaşı dökeceksiniz…

Aynı şekilde, kullandığınız dağıtımda python3 komutunun öntanımlı olarak belirli bir Python sürümünü başlatıp başlatmadığı da önemlidir. Yukarıda python komutu ile ilgili söylediklerimiz python3 ve buna benzer başka komutlar için de aynen geçerli.

Örneğin, Ubuntu GNU/Linux dağıtımında python komutu sistemde kurulu olan Python 2.x sürümünü; python3 komutu ise sistemde kurulu olan Python 3.x sürümünü çalıştırdığından, biz kendi kurduğumuz Python sürümleri için, sistemdeki sürümlerle çakışmayacak isimler seçtik. Mesela kendi kurduğumuz Python3 sürümünü çalıştırmak için py3 gibi bir komut tercih ettik.

İyi bir test olarak, Python programlama dilini kendiniz kaynaktan derlemeden önce şu komutun çıktısını iyice inceleyebilirsiniz:

    "ls -g {,/usr{,/local}}/bin | grep python"

Bu komut iki farklı Python sürümünün kurulu olduğu sistemlerde şuna benzer bir çıktı verir (çıktı kırpılmıştır):

    "dh_python2
    dh_python3
    pdb2.7 -> ../lib/python2.7/pdb.py
    pdb3.7 -> ../lib/python3.7/pdb.py
    py3versions -> ../share/python3/py3versions.py
    python -> python2.7
    python2 -> python2.7
    python2.7
    python3 -> python3.7
    python3.7 -> python3.7mu
    python3.7mu
    python3mu -> python3.7mu
    pyversions -> ../share/python/pyversions.py"

Yatık harflerle gösterdiğimiz kısımlara dikkat edin. Gördüğünüz gibi python ve python2 komutları bu sistemde Python’ın 2.7 sürümünü çalıştırıyor. python3 komutu ise Python’ın 3.7 sürümünü… Dolayısıyla yukarıdaki çıktıyı aldığımız bir sistemde kendi kurduğumuz Python sürümlerine ‘python’, ‘python2’ veya ‘python3’ gibi isimler vermekten kaçınmalıyız.

Sözün özü, bir GNU/Linux kullanıcısı olarak sistemdeki öntanımlı hiçbir Python sürümünü silmemeli, öntanımlı sürüme ulaşan komutları değiştirmemelisiniz. Eğer mesela sisteminizde python3 komutu halihazırda bir Python sürümünü çalıştırıyorsa, siz yeni kurduğunuz Python sürümüne ulaşmak için öntanımlı adla çakışmayacak başka bir komut adı kullanın. Yani örneğin sisteminizde python3 komutu Python’ın 3.7 sürümünü çalıştırıyorsa, siz yeni kurduğunuz sürümü çalıştırmak için py3 gibi bir sembolik bağ oluşturun. Bırakın öntanımlı komut (python, python3 vb.) öntanımlı Python sürümünü çalıştırmaya devam etsin.

Asla unutmayın. Siz bir programcı adayı olarak, program yazacağınız işletim sistemini enine boyuna tanımakla yükümlüsünüz. Dolayısıyla işletim sisteminizi kararsız hale getirecek davranışları bilmeli, bu davranışlardan kaçınmalı, yanlış bir işlem yaptığınızda da nasıl geri döneceğinizi bilmelisiniz. Hele ki bir programı kaynaktan derlemeye karar vermişseniz…

Bu ciddi uyarıyı da yaptığımıza göre gönül rahatlığıyla yolumuza devam edebiliriz.

--Python3’ü Ev Dizinine Kuranlar--

Eğer Python3’ü kısıtlı kullanıcı hakları ile derleyip ev dizininize kurduysanız yukarıdaki komutlar Python’ı çalıştırmanızı sağlamayacaktır. Python3’ü ev dizinine kurmuş olan kullanıcılar Python3’ü çalıştırabilmek için, öncelikle komut satırı aracılığıyla Python3’ü kurdukları dizine, oradan da o dizin altındaki bin/ klasörüne ulaşacak ve orada şu komutu verecek:

    ./python3.7
Diyelim ki Python3’ü $HOME/python adlı dizine kurdunuz. Önce şu komutla $HOME/python/bin adlı dizine ulaşıyoruz:

    cd $HOME/python/bin
Ardından da şu komutu veriyoruz:

    ./python3.7
    Komutun başındaki ./ işaretinin ne işe yaradığını artık adınız gibi biliyorsunuz…
    Elbette ben burada kurduğunuz Python sürümünün 3.7 olduğunu varsaydım. Eğer farklı bir sürüm kurduysanız yukarıdaki komutu ona göre yazmanız gerekiyor.

Eğer isterseniz bu şekilde çalışmaya devam edebilirsiniz. Ancak her defasında Python’ın kurulu olduğu dizin altına gelip orada ./python3.7 komutunu çalıştırmak bir süre sonra eziyete dönüşecektir. İşlerinizi kolaylaştırmak için şu işlemleri takip etmelisiniz:

1. ev dizininizin altında bulunan .profile (veya kullandığınız dağıtıma göre .bash_profile ya da .bashrc) adlı dosyayı açın.

2. Bu dosyanın en sonuna şuna benzer bir satır yerleştirerek Python’ı çalıştırmamızı sağlayan dosyanın bulunduğu dizini yola ekleyin:

    export PATH=$PATH:$HOME/python/bin/

3. $HOME/python/bin/ satırı Python3’ün çalıştırılabilir dosyasının hangi dizin altında olduğunu gösteriyor. Ben burada Python3’ün çalıştırılabilir dosyasının $HOME/python/bin dizini içinde olduğunu varsaydım. O yüzden de $HOME/python/bin/ gibi bir satır yazdım. Ama eğer Python3’ün çalıştırılabilir dosyası sizde farklı bir dizindeyse bu satırı ona göre yazmalısınız.

4. Kendi sisteminize uygun satırı dosyaya ekledikten sonra dosyayı kaydedip çıkın. Dosyada yaptığımız değişikliğin etkin hale gelebilmesi için şu komutu verin:

    source .profile

Elbette eğer sizin sisteminizdeki dosyanın adı .bash_profile veya .bashrc ise yukarıdaki komutu ona göre değiştirmelisiniz.

5. Daha sonra $HOME/python/bin/python3.7 adlı dosyaya $HOME/python/bin/ dizini altından mesela py3 gibi bir sembolik bağ verin:

    ln -s $HOME/python/bin/python3.7 $HOME/python/bin/py3

6. Bilgisayarınızı yeniden başlatın.

7. Artık hangi konumda bulunursanız bulunun, şu komutu vererek Python3’ü başlatabilirsiniz:

    py3

Burada da eğer yukarıdaki komut Python3’ü çalıştırmanızı sağlamıyorsa, bazı şeyleri eksik veya yanlış yapmış olabilirsiniz. Yardım almak için forum.yazbel.com adresine uğrayabilirsiniz.

Python3’ü başarıyla kurup çalıştırabildiğinizi varsayarak yolumuza devam edelim.