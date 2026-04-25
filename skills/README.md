# 📁 skills
**Kehitysvaiheessa**

**Osaamisopas ja ohjekirjasto** – nkmls/demos-repositorio

Tämä kansio sisältää **skillit** (ohjeistukset), joita tekoäly automaattisesti käyttää eri workflowissa (erityisesti n8n:ssä).

---

## 🎯 Käyttötarkoitus

- **Yhtenäinen tapa tehdä asioita** – värit, tyyli, sävy ja prosessit ovat aina samat.
- **Tekoäly osaa hakea ohjeet itse** – kun joku kysyy jotain, AI lukee tarvittavat skill-tiedostot GitHubista ja tekee työn juuri oikein.
- **Helppo oppia uusille jäsenille ja työntekijöille** – et tarvitse tietää kaikkea etukäteen, riittää kun tiedät mistä etsiä.
- **Modulaarinen** – yksi skill kerrallaan, helppo päivittää ilman että rikot jotain muuta.

Tämä on kuin **yhteinen muistiinpanojen kirja**, jota sekä ihmiset että tekoäly käyttävät päivittäin.

---

## 🚀 Esimerkkejä aloittelijoille ja uusille jäsenille

| Esimerkkitilanne – mitä haluat tehdä?                  | Mitä skillejä AI käyttää automaattisesti                  | Mitä saat lopputuloksena? |
|-----------------------------------------------|-----------------------------------------------------------|---------------------------|
| Haluan tehdä kauniin landing pagen            | `DESIGN.md` + `HTML.md`                                   | Valmis HTML-koodi oikeilla väreillä ja mobiili-first |
| Kirpputorille tulee uusi tuote                | `KIRPPUTORI.md` + `VIESTINTA.md` + `DESIGN.md`           | Lämmin tuoteilmoitus + kuvaus + Teams-viesti |
| Järjestän kahvitilaisuuden Kontiotuvalla     | `KONTIOTUPA.md` + `TAPAHTUMAT.md` + `VIESTINTA.md`       | Ilmoitus someen + tilavarausohjeet |
| Tarvitsen Python-skriptin ruokajaon hallintaan | `PYTHON.md` + `TAPAHTUMAT.md`                           | Valmis, helppolukuinen koodi |
| Haluan kirjoittaa kannustavan viestin jäsenelle | `VIESTINTA.md` + `KONTIOTUPA.md`                        | Lämpimän ja inklusiivisen tekstin |
| Tarvitsen virallisen toimintasuunnitelman osan | `TOIMINTASUUNNITELMA.md` + `VIESTINTA.md`               | Virallista mutta ihmisläheistä tekstiä |

**Vinkki uusille:**  
Aloita aina lukemalla ensin **[DESIGN.md](./DESIGN.md)** – se kertoo miten kaikki näyttää ja kuulostaa täällä.

---

## 📋 Kaikki skill-tiedostot

| Tiedosto                        | Mihin käytetään? |
|---------------------------------|------------------|
| **[DESIGN.md](./DESIGN.md)**    | Värit, fontit, painikkeet, kontrasti – **pakollinen kaikissa visuaalisissa jutuissa** |
| **[HTML.md](./HTML.md)**        | Landing paget, sivut ja Tailwind-koodaus |
| **[KIRPPUTORI.md](./KIRPPUTORI.md)** | Töpinän Tori -kirpputorin kaikki ohjeet |
| **[KONTIOTUPA.md](./KONTIOTUPA.md)** | Kontiotupa-kahvit, kerhot ja tilavaraukset |
| **[PYTHON.md](./PYTHON.md)**    | Python-koodaus ja skriptit |
| **[ROUTE.md](./ROUTE.md)**      | **AI:n reititin** – kertoo mitkä skillit tarvitaan |
| **[TAPAHTUMAT.md](./TAPAHTUMAT.md)** | Tapahtumien suunnittelu ja tiedotus |
| **[TOIMINTASUUNNITELMA.md](./TOIMINTASUUNNITELMA.md)** | Virallinen toimintasuunnitelma 2026 |
| **[VIESTINTA.md](./VIESTINTA.md)** | Lämpimän ja kannustavan viestinnän säännöt |

---

## 🔧 Miten tämä käytännössä toimii?

1. Joku lähettää viestin (Telegram, lomake tms.).
2. n8n-workflow käynnistyy.
3. Tekoäly lukee ensin `ROUTE.md`:n.
4. AI päättää mitkä skill-tiedostot tarvitaan.
5. Se hakee ne automaattisesti GitHubista (raw-linkeillä).
6. Lopuksi AI tekee tehtävän juuri oikealla tyylillä.

Sinun ei tarvitse tietää teknisiä yksityiskohtia – riittää kun teet asiat tämän kansion ohjeiden mukaan.



Lisää kysymyksiä? Avaa [Issue](https://github.com/nkmls/demos/issues) tai pingaa repo.
