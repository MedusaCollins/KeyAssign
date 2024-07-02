# KeyAssign

type: text,
value: string,
typingDelay: float, 
repeatPress: bool,
duration: [int, int],


tpye: script,
import: string,
repeatPress: bool,
duration: [int, int],

## Yapılacaklar
- [x] imports ismi plugins ile değiştirilecek.
- [ ] Config alanında bulunan repeatPress özelliğinin iyileştirmeleri yapılacak, şu anda bazı durumlarda(a tuşuna bastığımızda birden çok işlemi gerçekleştirmesi gibi) hatalar olabiliyor.
- [ ] Bir Popup librarysi yazılacak, bu library input alanı olan ve olmayan olarak 2 farklı popup'a sahip olacak, bunun yanı sıra ise return değerini gösterebileceğimiz bir output alanı olacak.
- [ ] Tuşa basılı tuttuğumuzda kullanıcıya hangi tuşa ne kadar bastığını gösteren bir popup menüsü yazılacak, bu popup menüsü global config üzerinden açılıp kapatılabilecek.
- [ ] Global config dosyası yazılacak; bu dosya sayesinde kullanıcının bazı popup ayarları(Tuşa ne kadar süre basılı tuttuğu...) vb...
- [ ] Programı terminal üzerinden başlatırken kullanıcıdan çeşitli argümanlar alabilmemiz sağlanacak(Örn: python3 main.py --config=global_config.json)(Bazı argümanlar; -h, -v, -set[config, library, imports, profile("Bütün dosyaları kopyalar")], -get[config, library, imports, profile("Bütün dosyaları kopyalar")] , -debug, -config[configFileName]) 
- [ ] Bazı örnek scriptler yazılacak, bu scriptlerin amacı kullanıcıya programın nasıl kullanılacağını göstermek olacak.
- [ ] Web sitesi yazılacak, bu websitesi üzerinden hem programın tanıtımı yapılacak hem de kullanıcıların config dosyalarını hazırlayabileceği bir arayüz sağlanacak(3D klavye animasyonlarına sahip olacak).
- [ ] Config yapısı birden fazla tuş kombinasyonuna uygun hale getirilecek, bu sayede "CTRL + A" gibi kombinasyonlar yapılabilir hale gelecek.
- [ ] Vimmotions benzeri bir yapı kurulacak, bu sayede config dosyasına belirli bir şey yazmadan direkt olarak anlık tuş basışlarını belirli bir tuşa atayabileceğiz.
