function start() {
    var kezdoKep = document.getElementById('kezdokep');
    mutasd(kezdokep);
}

function mutasd(element) {
    document.getElementById('kiemelt-kep').style.backgroundImage = "url(" + element.src + ")";
    document.getElementById('kiemelt-nev').innerText = element.alt;
    switch (element.alt) {
        case "Denevér":
            document.getElementById('kiemelt-leiras').innerText =
                'A denevérek különleges emlősök. Mellső végtagjaik ugyanis bőrszárnyakat mozgatnak. A denevérek ugyanúgy képesek a repülésre, mint a madarak. A hazai denevérek mindegyike hasznos rovarpusztító.';
            break;
        case "Imádkozó sáska":
            document.getElementById('kiemelt-leiras').innerText =
                'Az imádkozó sáska magas fűszálakra helyezi kokonját, azaz a petéit tartalmazó kis száraz falú tartályt. A magas fűszál oldalán a kokon védve van a földön haladó egyéb rovaroktól, és a tócsák sem áztatják el, ha esik az eső.';
            break;
        case "Levelibéka":
            document.getElementById('kiemelt-leiras').innerText =
                'Életmódjában a többi békától annyiban különbözik, hogy amíg azok kivétel nélkül a talajszint lakói vagy vízben élnek, addig a levelibéka a növényzeten tartózkodik, ott vadászik mindenféle apró rovarra. Néha a nagy jegenyefák legmagasabb csúcsáról hangzik a hímek jellezetes brekegése. Ilyenkor az állatok hatalmasra fújják a torkukon feszülő hanghólyagjukat, amely rezonátorként működve felerősíti a levegőrezgéseket.';
            break;
        case "Mocsári teknős":
            document.getElementById('kiemelt-leiras').innerText =
                'A mocsári teknősök szívesen kalandoznak el a víz mellől. Táplálkozni viszont elsősorban a vízben szoktak. Ragadozók, étrendjükön vízben élő rovarlárvák, ebihalak, - és ha el tudják fogni őket - kisebb halak szerepelnek. Tojásaikat a nőstények május végén rakják le. A kis teknősök szeptemberre fejlődnek ki, azonban csak a következő év tavaszán bújnak elő.';
            break;
        case "Mókus":
            document.getElementById('kiemelt-leiras').innerText =
                'A mókus az erdő légtornásza. Miközben fáról fára ugrik, hosszú farkával kormányoz. A mászásban éles, hegyes karmai segítik. Rágcsáló állat. Ám a magok és gyümölcsök mellett a madarak tojásait is elfogyasztja.';
            break;
        case "Pávaszem":
            document.getElementById('kiemelt-leiras').innerText =
                'Bársonyos piros szárnyain kör alakú szemfoltot visel. Fekete alapszínű, fehér pontokkal tarkított elágazó tövisekkel bíró hernyója a csalánon él. Általánosan elterjedt, s mivel hernyója gyomnövényzeten (csalánon) él, kevéssé veszélyeztetett. Az imágók áttelelnek, s márciustól októberig rendszeresen megfigyelhetőek.';
            break;
        case "Sün":
            document.getElementById('kiemelt-leiras').innerText =
                'A sünök rovarevő emlősállatok. Tömzsi testüket felül tüskék borítják. Hasuk, fejük és lábaik azonban szőrösek. A nőstény sünök 4-5 kicsinyüket nyáron hozzák a világra.';
            break;
        case "Szalamandra":
            document.getElementById('kiemelt-leiras').innerText =
                'A foltos szalamandra árnyas, nyirkoserdőkben él. Lábai gyengék, hosszú farkának kígyózó mozgásával halad előre. Hazánkban is honos, védett állat.';
            break;
        case "Szarvasbogár":
            document.getElementById('kiemelt-leiras').innerText =
                'A legnagyobb testű bogarunk, a nőstények 25-50, a hímek 30-80, ritkán 100 mm-re is megnőnek. Magyarország idősebb tölgyeseiben fordul elő. Lárvája tölgyek elhalt, korhadó gyökerében, tuskójában fejlődik 3-5 évig. Az imágók júniusban jelennek meg, napközben tápnövényeiken tartózkodnak, illetve azok nedvező sérüléseiből táplálkoznak.';
            break;
        case "Ürge":
            document.getElementById('kiemelt-leiras').innerText =
                'Az ürge a száraz völgyek, legelők, domboldalak lakója. A szemes gabonát pusztítja. Mégis hasznos, mert a hasznos nagyobb ragadozómadaraknak táplálékul szolgál (rétisas, héják, ölyvek).';
            break;
        case "Vakond":
            document.getElementById('kiemelt-leiras').innerText =
                'A vakond szinte egész életét a föld alatt tölti. Rendkívül jó szaglású, kiválóan ásó emlősállat. Bársonyos, barnásfekete bundájáról a föld azonnal lepereg. A vakond falánk rovarevő, táplálékát föld alatti kamráiba gyűjti.';
            break;
        case "Csodabogyó":
            document.getElementById('kiemelt-leiras').innerText =
                'Kissé szúrós lombját, nem valódi levelek, hanem módosult hajtások, fillokládiumok alkotják. Tavasszal hozza apró, zöldessárga virágait, melyek nem kimondottan látványosak. Ősszel fejlődnek ki dekoratív, matt hatású piros termései.';
            break;
        case "Hóvirág":
            document.getElementById('kiemelt-leiras').innerText =
                'Egyik legszebb lágyszárú növényünk a hóvirág. Egészen korán, enyhébb teleken már február közepén kihajt. A tavasz hírnökének is nevezik, mert az egyik legkorábban virágzó növény. A földben telelő hagymából bújik ki minden évben. Virága nem különül el csésze- és sziromlevélre, fehér lepellevelekből áll.';
            break;
        case "Leánykökörcsin":
            document.getElementById('kiemelt-leiras').innerText =
                'A leánykökörcsin a száraz gyepek egyik legkorábban nyíló virága. Még fakó tetszhalott állapotban várják a legelők és sztyepprétek a melegebb időt, amikor a leánykökörcsin sűrűn szőrözött, bundás virágkelyhei beharangozzák a tavasz érkezését.';
            break;
        case "Kornistarnics":
            document.getElementById('kiemelt-leiras').innerText =
                'A nyár második felétől akár ősz közepéig az ország egész területén találkozhatunk vele. Kiszáradó kékperjés láprétek, hegyvidéki üde kaszálók, szőrfűgyepek lakója. Érdekesség, hogy a kornistárnics kizárólagos tápnövénye a szürkés hangyaboglárkának, amely boglárkalepke a kornistárnics virágzatára petézik.';
            break;
        case "Tavaszi hérics":
            document.getElementById('kiemelt-leiras').innerText =
                'Hazánkban dombvidéki és hegyvidéki élőhelyeken, napsütötte pusztafüves lejtőkön, száraz sziklagyepekben, lösz- és homoki gyepekben, irtásréteken és legelőkön, karsztbokorerdőkben és ligetes, melegkedvelő tölgyesekben találkozhatunk vele. Erősen mérgező, így a legelő állatok kerülik.';
            break;
        case "Tündérrózsa":
            document.getElementById('kiemelt-leiras').innerText =
                'A fehér tündérrózsával tavakban, holtágakban, tápanyagban gazdag, iszapos talajú álló- vagy lassan folyó vizekben találkozhatunk. A víz tisztán tartásában fontos szerepük van, mivel víz felszínén elterülő leveleik beárnyékolják a vízfelszínt, így csökkentik az esetleges algásodás kialakulását.';
            break;
        case "Turbán liliom":
            document.getElementById('kiemelt-leiras').innerText =
                'A turbánliliom 50–120 cm magas sudár növény. Alsó levelei örvösek, a felsők átellenesek vagy váltogatva állók, hosszúkás lándzsásak. Hónaljukban nincsenek sarjhagymák. 5–10 virága fejlődik, amelyek fürtösen helyezkednek el és változatos megjelenésűek.';
            break;
        default:
            document.getElementById('kiemelt-leiras').innerText = "";
    }
}
