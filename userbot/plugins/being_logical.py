import asyncio
import random

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.belo", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x = random.randrange(1, 96)

    if x == 1:

        await event.edit(
            '`"Sualtı baloncuklar və yağış damlaları bir-birinin tam əksidir."`'
        )

    if x == 2:

        await event.edit(
            '`"Bir silgi alsanız, sözün əsl mənasında səhvləriniz üçün pul ödəyəcəksiniz."`'
        )

    if x == 3:

        await event.edit(
            '`"Ən çox maraqlandığınız Şəxs sizi ən çox məhv etmək potensialına malikdir."`'
        )

    if x == 4:

        await event.edit(
            '`"İnsanlar ayı müstəmləkə halına gətirərsə, ehtimal ki, çəki zəifliyi yaşlıların özlərini daha güclü hiss etməsinə imkan verəcəyi üçün təqaüd evlərini cəlb edəcəkdir."`'
        )

    if x == 5:

        await event.edit(
            '`"Başlıqda “onu gözləyin” yazılmış hər hansı bir video sadəcə çox uzundur."`'
        )

    if x == 6:

        await event.edit(
            '`"İllərdəki yaşınız Günəşi neçə dəfə dövr etdiyinizdir, ancaq aylardakı yaşınız Ayın sizi neçə dəfə dövr etdiyinizdir."`'
        )

    if x == 7:

        await event.edit(
            '`"Yemək yeyərkən dilinizi dişləməyiniz, onilliklər boyu yaşadığınız təcrübə ilə belə hələ də vida edə biləcəyinizin mükəmməl bir nümunəsidir."`'
        )

    if x == 8:

        await event.edit(
            '`"Evinizin 93 Milyon mil məsafədəki simsiz bir Nüvə sintez reaktoru ilə işlədiyini söyləmək, damınızda günəş panelləri olduğunu söyləməkdən daha yaxşı səslənir."`'
        )

    if x == 9:

        await event.edit(
            '`"Ən sarsıdıcı hiss kimsə küçədə sənə gülümsəməsi və geri gülümsəyəcək qədər sürətli reaksiya verməməyindir."`'
        )

    if x == 10:

        await event.edit(
            '`"Dişlər diri-diri çürüməsinin qarşısını almaq üçün davamlı baxım tələb edir və bununla birlikdə min illər boyu fosil olaraq dəfn olunaraq həyatda qalmağı bacarırlar."`'
        )

    if x == 11:

        await event.edit('`"Qovluq qatlamaq istəmədiyiniz şeylər üçündür."`')

    if x == 12:

        await event.edit(
            '`"Səhər oyanmaq bəzən izləməyi dayandırmağa qərar verdiyin bok filmə davam etmək kimi hiss olunur."`'
        )

    if x == 13:

        await event.edit(
            '`"Hər şey yaxşı gedirsə, yəqin ki, bu gün xatırlamayacaqsınız."`'
        )

    if x == 14:

        await event.edit(
            '`"Real həyatda yeni insanlarla tanış olduqda, xəyal dünyanız üçün daha çox simvol açırsınız."`'
        )

    if x == 15:

        await event.edit(
            '`"Bəlkə də günəşdən qoruyucu kremini “xərçəng əleyhinə krem” olaraq dəyişdirsəydilər, daha çox insan onu istifadə edərdi."`'
        )

    if x == 16:

        await event.edit(
            '`"200 il əvvəl insanlar gələcəkdə insanların səssizcə şüşəyə vuraraq ünsiyyət quracağını heç düşünməzdilər."`'
        )

    if x == 17:

        await event.edit(
            '`"Valideynlər oğullarının nəyi yüklədiyindən, qızlarının nə yüklədiyindən narahatdırlar."`'
        )

    if x == 18:

        await event.edit(
            '`"Birininlə eyni yaşda olmağın, amma həyatında tamamilə fərqli bir mərhələdə olmağın necə dəli."`'
        )

    if x == 19:

        await event.edit(
            "`\"Ölmək istədiyinizi düşündüyünüzdə, həqiqətən ölmək istəmirsiniz, sadəcə belə yaşamaq istəmirsiniz. \"`"
        )

    if x == 20:

        await event.edit('`"Texniki cəhətdən heç kim heç vaxt boş bir otaqda olmayıb."`')

    if x == 21:

        await event.edit(
            '`"Soğan yeməyin bas ifaçısıdır. Yəqin ki, solo ləzzət almayacaqsan, amma olmasaydı darıxardın."`'
        )

    if x == 22:

        await event.edit(
            '`"Verdiyiniz hər qərar sizi bu cümləni oxumağa gətirib çıxardı."`'
        )

    if x == 23:

        await event.edit(
            '`"Verdiyiniz hər qərar sizi bu cümləni oxumağa gətirib çıxardı."`'
        )

    if x == 24:

        await event.edit(
            '`"Hamı sizdən çox çalışmağınızı istəyir, amma kimsə nə qədər çalışdığınızı eşitmək istəmir."`'
        )

    if x == 25:

        await event.edit(
            '`"Hamı sizdən çox çalışmağınızı istəyir, amma kimsə nə qədər çalışdığınızı eşitmək istəmir."`'
        )

    if x == 26:

        await event.edit(
            '`"Dişlərimizi çubuqdakı saçlarla və saçlarımızı çubuqdakı dişlərlə fırçalayırıq."`'
        )

    if x == 27:

        await event.edit(
            '`"Heç kim sənin yöndəmsiz anlarınızı xatırlamır, ancaq öz anlarını xatırlamaqla çox məşğul olurlar."`'
        )

    if x == 28:

        await event.edit(
            '`"Lal insanlar sadə fikirləri mümkün qədər mürəkkəb deməyə çalışırlar, ağıllı insanlar isə kompleks fikirləri mümkün qədər sadə deməyə çalışırlar."`'
        )

    if x == 29:

        await event.edit(
            "`\"Bəzi insanlar varlı olduqları üçün səndən daha yaxşı olduqlarını düşünürlər. Bəzi insanlar kasıb böyüdükləri üçün səndən daha yaxşı olduqlarını düşünürlər."`'
        )

    if x == 30:

        await event.edit(
            '`"Ən böyük istehza odur ki, kompüterlər və mobil telefonlar vaxta qənaət etmək üçün icad edilmişdir!"`'
        )

    if x == 31:

        await event.edit(
            '`"Bal ilk aşkar edildikdən sonra, ehtimal ki, insanların həşəratlardan əldə edilə bilən hər hansı bir palçıq dadına baxdıqları bir dövr var idi."`'
        )

    if x == 32:

        await event.edit(
            '`"Valideynləriniz sizi məyus etmək əvəzinə, sizi məyus etməyə başladıqda qocaldığınızı bilirsiniz."`'
        )

    if x == 33:

        await event.edit(
            '`"İnsanlar təcrübə ilə öyrənmək üçün nəzərdə tutulmuşdur, lakin təhsil sistemi belə təcrübə əldə etməməyi təmin etmişdir."`'
        )

    if x == 34:

        await event.edit(
            '`"Yanıb-sönməyə diqqət yetirərək daha yavaş yanıb-sönürsünüz ... Nəfəs almaq üçün eynidir."`'
        )

    if x == 35:

        await event.edit(
            '`"Trafik döymək üçün tələsik olan sürücülər ümumiyyətlə qarşısını almaq üçün trafik yaradan qəzalara səbəb olur."`'
        )

    if x == 36:

        await event.edit(
            '`"Bədii ədəbiyyatda evlənən personajlar sözün əsl mənasında bir-biri üçün düzəldilmişdir."`'
        )

    if x == 37:

        await event.edit(
            '`"Körpələr hər hansı bir dil ilə proqramlaşdırıla bilən təmiz bir sabit diskdir."`'
        )

    if x == 38:

        await event.edit(
            "`\"İnsana hər xəstəliyi müalicə edən, siçovullarda işləmədiyi üçün heç vaxt bilməyəcəyimiz bir möcüzə dərmanı ola bilər. \"`"
        )

    if x == 39:

        await event.edit(
            "`\"Kərgədanlar qorunmaq üçün bir buynuz böyütmək üçün inkişaf etdilər, lakin onları məhv etməyə vadar edən şey budur."`"
        )

    if x == 40:

        await event.edit(
            '`"Bəlkə vaxt yolçu tapa bilmirik, çünki hamımız 25-50 ildə ölürük."`'
        )

    if x == 41:

        await event.edit(
            '`"Yuxu ölümün sınaq versiyasıdır, hətta fəaliyyətinizə əsaslanan reklamlarla gəlir."`'
        )

    if x == 42:

        await event.edit(
            '`"Casus filmlərindəki ən real olmayan şey havalandırma sisteminin nə qədər təmiz olmasıdır!"`'
        )

    if x == 43:

        await event.edit(
            '`"Oyunlarda sərt rejimlərin kilidini açmaq üçün asan rejimlər vasitəsilə oynayırıq. Həyatda asan rejimlərin kilidini açmaq üçün sərt rejimləri oynayırıq."`'
        )

    if x == 44:

        await event.edit(
            '`"Səssiz insanlar uca səsli insanlardan daha ağıllı görünür, çünki axmaq düşüncələrini özlərində saxlayırlar."`'
        )

    if x == 45:

        await event.edit('`"Qrenlandiya həqiqətən yaşıl rəngə çevrilirsə, hamımız vidalandıq."`')

    if x == 46:

        await event.edit(
            '`"Kimsə xəyalınızda ağıllı bir şey söyləyirsə, bu əslində öz ağıllılığınızı göstərir."`'
        )

    if x == 47:

        await event.edit(
            '`"Məşhur film sitatları aktyorun hesabına yazılır və onları yazan faktiki yazıçı deyil."`'
        )

    if x == 48:

        await event.edit(
            '`"Heç kim sənə velosiped sürməyi öyrətmir. Bunu işləyənə qədər səni şıltaq edirlər."`'
        )

    if x == 49:

        await event.edit('`"Özünüzdən soruşun ki, beyin ikinci ikincisini niyə görməzlikdən gəlir."`')

    if x == 50:

        await event.edit(
            '`"Yəqin ki, bütün həyatınızın 80% -ni unutmusunuz və xatırladığınız xatirələrin əksəriyyəti əslində baş verənlərlə dəqiq deyil."`'
        )

    if x == 51:

        await event.edit(
            '`"Gələcəkdə uşaqlara video oyunlarında valideynlərinə qarşı qalib gəlmək çox çətin olacaq."`'
        )

    if x == 52:

        await event.edit(
            '`"Hər kəsin qüsuru var, özünüzü tanımırsınızsa, yenisi var."`'
        )

    if x == 53:

        await event.edit('`"Bir uşağı böyütmək əvəzləyicinizi yetişdirməkdir."`')

    if x == 54:

        await event.edit(
            "`\"'O'pen Qapalı dairə ilə başlayır və' C'lose açıq dairə ilə başlayır. \"`"
        )

    if x == 55:

        await event.edit(
            '`"Həmişə səndən heç bir səbəb olmadan nifrət edən biri var və indi də var."`'
        )

    if x == 56:

        await event.edit(
            '`"Patlamış qarğıdalı kəşf edildikdən sonra eyni təsirin olub olmadığını görmək üçün qovrulmuş bir çox təsadüfi toxum olmalı idi."`'
        )

    if x == 57:

        await event.edit(
            '`"Gecənin yuxusu nə qədər vacibdirsə, yuxuya getmək o qədər çətindir."`'
        )

    if x == 58:

        await event.edit(
            '`"Yeni bir stilistə istədikləri saç düzümünü düzgün təsvir edə bilənlər nə xoşbəxtdir."`'
        )

    if x == 59:

        await event.edit(
            "`\"Çox insan qazana bilmədikləri pulu sərf etmək, istəmədikləri şeyi almaq, bəyənmədikləri insanları təsirləndirmək üçün xərcləyir! \"`"
        )

    if x == 60:

        await event.edit(
            '`"Tema parkı işçiləri dəhşət və həyəcan qışqırıqları arasındakı fərqi yaxşı izah etməlidirlər."`'
        )

    if x == 61:

        await event.edit('`"6-dan 6: 30-a qədər saat 5: 50-dən 6: 20-dək yarım saat daha çox hiss olunur"`')

    if x == 62:

        await event.edit(
            '`"Lokavtdan əvvəl parolunuzu son giriş cəhdində əldə etmək, çoxumuzun yaşayacağı son anda bombanı tərksilah etmək üçün ən yaxın şeydir."`'
        )

    if x == 63:

        await event.edit(
            '`"Yataqdan əvvəl hekayə dinləyərək vaxtınızı dəyərləndirin."`'
        )

    if x == 64:

        await event.edit(
            '`"Bütün cinayətkarlar soymağı dayandırsaydılar, təhlükəsizlik sənayesi düşərdi, sonra soyğunçuluğa asanlıqla qayıda bilərdilər."`'
        )

    if x == 65:

        await event.edit('`"Bir ton balina həqiqətən yalnız yarım balinaya bənzəyir."`')

    if x == 66:

        await event.edit(
            '`"Qocalanda texniki cəhətdən köhnəlisən yenisən, cavan mənlik isə köhnə sənsən."`'
        )

    if x == 67:

        await event.edit(
            '`"Yəqin ki, İnternetdə paraşütlərə dair bir çox mənfi rəy tapa bilməyəcəksiniz."`'
        )

    if x == 68:

        await event.edit(
            '`"İnsanlar üçün ən çox sevgi və heyranlığı, artıq bunu qiymətləndirməyəcəkləri zaman göstəririk."`'
        )

    if x == 69:

        await event.edit(
            "`\"Minlərlə dəfə yatmağı öyrəndik, amma bunu çox yaxşı edə bilmirik və ya tutarlı ola bilmirik. \"`"
        )

    if x == 70:

        await event.edit(
            '`"İnsanlar düşmən mühiti olan başqa bir planetə köçmək üçün həvəslidirlər - yer üzünü qorumaqdan daha yaxşıdır."`'
        )

    if x == 71:

        await event.edit(
            "`\"Çox insanın həyatının ən xoşbəxt mərhələsi, beyinlərinin hələ tam inkişaf etməməsidir. \"`"
        )

    if x == 72:

        await event.edit('`"Ən təsirli zəngli saat dolu mesanedir."`')

    if x == 73:

        await event.edit(
            '`"Yəqin ki, milyonlarla insanla yanıb sönən sinxronizasiya etmisiniz."`'
        )

    if x == 74:

        await event.edit(
            '`"Əvvəlcə dərmanları heyvanlar üzərində sınadığımız üçün, siçovul dərmanı insan təbabətindən illər öndə olmalıdır."`'
        )

    if x == 75:

        await event.edit(
            '`"Bir istirahət günündən əvvəlki gecə həqiqi istirahət günündən daha razıdır."`'
        )

    if x == 76:

        await event.edit('`"Qatlamamaq üçün kağızı bir qovluğa qoyduq."`')

    if x == 77:

        await event.edit(
            '`"Bir yerdə, iki ən yaxşı dost ilk dəfə görüşür."`'
        )

    if x == 78:

        await event.edit(
            '`"Beynimiz eyni zamanda bizdən nifrət edir, bizi sevir, bizimlə maraqlanmır və hər hərəkətimizi mikro idarə edir."`'
        )

    if x == 79:

        await event.edit(
            '`"Kişi olmaq doğuş məsələsidir. Kişi olmaq yaş məsələsidir. Ancaq centlmen olmaq seçim məsələsidir."`'
        )

    if x == 80:

        await event.edit(
            '`"Tezliklə valideynlər hesablarını valideynlərindən gizlədən uşaqlardan daha çox sosial hesablarını övladlarından gizlədəcəklər."`'
        )

    if x == 81:

        await event.edit('`"Vikipediya internetin nəzərdə tutulduğu şeydir."`')

    if x == 82:

        await event.edit(
            '`"Tema parkı uzaqdan qışqırıq səsləri eşidə biləcəyiniz və narahat olmayacağınız yeganə yerdir."`'
        )

    if x == 83:

        await event.edit(
            '`"Simsiz telefon şarj cihazı, simli birinə nisbətən daha az hərəkət azadlığı təklif edir."`'
        )

    if x == 84:

        await event.edit(
            "`\"Sevmədiyiniz bir şeyi bəyəndiyinə görə dəfələrlə birini tənqid edirsinizsə, bəyənməyi dayandırmazlar. Sizi bəyənməyi dayandıracaqlar. \"`"
        )

    if x == 85:

        await event.edit(
            '`"Bir yerdə nənəsi həqiqətən dünyanın ən yaraşıqlı oğlanı olan bir nənə var."`'
        )

    if x == 86:

        await event.edit(
            '`"If someday human teleportation becomes real, people will still be late for work."`'
        )

    if x == 87:

        await event.edit(
            '`"Yengeç yeyən ilk insanlar, zirehli bir dəniz hörümçəyini yeməyə çalışmaq üçün həqiqətən ac olmuşlar"`'
        )

    if x == 88
                         
        await event.edit(
            '`"Yengeç yeyən ilk insanlar, zirehli bir dəniz hörümçəyini yeməyə çalışmaq üçün həqiqətən ac olmuşlar"`'
        )

    if x == 89:

        await event.edit(
            '`"Bir şey göndərdikdən sonra beyniniz birdən-birə oxumaqda mükəmməlləşir."`'
        )

    if x == 90:

        await event.edit(
            '`"Pleylistinizdə həmişə atladığınız, lakin heç vaxt çıxarmadığınız bir mahnı həmişə var."`'
        )

    if x == 91:

        await event.edit(
            '`"Gələn əsrdəki uşaqlar, ehtimal ki, bütün yaxşı istifadəçi adlarını götürdüyümüz üçün bizə nifrət edəcəklər."`'
        )

    if x == 92:

        await event.edit('`"Bubbles yağışın insanlar üçün nə olduğunu balıq tutmaq üçündür."`')

    if x == 93:

        await event.edit(
            '`"Nə qədər çox insanla tanış olsanız, valideynlərinizin sizi necə böyüdüyünü daha çox dərk edir və qiymətləndirirsiniz."`'
        )

    if x == 94:

        await event.edit('`"Vergül qısa bir fasilə, koma uzun bir fasilədir."`')

    if x == 95:

        await event.edit('`"Bir gün ya oyanmayacaqsan, ya da yatmayacaqsan."`')

    if x == 96:

        await event.edit(
            '`"Bermuda Üçbucağı bu simulyasiyanın çıxış portalı ola bilər."`'
        )

    if x == 97:

        await event.edit(
            '`"Dark Userbotdan 1 dənədi.)))"`'
        )
