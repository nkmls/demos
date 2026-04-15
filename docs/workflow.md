# n8n Workflowt – Kontiolahden Työttömät ry

Tämä dokumentti kuvaa kaikki aktiiviset ja kehitteillä olevat n8n-workflowt.  
Workflowt on suunniteltu tukemaan yhdistyksen toimintasuunnitelmaa 2026.

## 1. Ajankohtaisten asioiden seuranta ja sisäinen tiedottaminen

### 1.1 Kela Ajankohtaiset (Kela ajankohtaiset rss.json)
**Idea:**  
Hakee automaattisesti Kelan ajankohtaiset tiedotteet JSON-muodossa → analysoi Grok:lla → muotoilee sisäiseksi tiedotteeksi → lähettää Microsoft Teamsiin hallituksen ja Kontiotuvan kanavalle.

**Käyttötarkoitus:**  
Hallitus ja työntekijät saavat tiivistetyn, yhdistyksen näkökulmasta relevantin selonteon Kelan muutoksista (etuudet, säädökset, ohjeet).

**Avainkomponentit:**
- HTTP Request → Kela JSON
- Aggregate
- Grok LLM Chain (JSON-muotoinen vastaus: Otsikko, ingressi, sisältö, slug)
- Microsoft Teams – viestin lähetys

---

### 1.2 STM Ajankohtaiset (stm-ajankohtaista.json)
**Idea:**  
Samankaltainen workflow Sosiaali- ja terveysministeriön ajankohtaisista tiedotteista.

**Ero Kela-workflow'hun:**
- Käyttää RSS/JSON-lähdettä STM:ltä
- Sisältää Filter-noden (vain päiväyksellä varustetut tiedotteet)

---

### 1.3 Kontiolahden Kunta (Kontiolahden kunta rss.json)
**Idea:**  
Seuraa Kontiolahden kunnan toimielinten kokousasioita Dynasty-järjestelmästä RSS-syötteen kautta.

**Tarkoitus:**  
Pitää hallitus ajan tasalla kunnan päätöksistä, jotka voivat vaikuttaa työttömiin tai yhdistyksen toimintaan (esim. palvelut, avustukset, tilat).

---

## 2. Jäsenhankinta ja viestintä

### 2.1 Jäsenliittyminen + Uutiskirje (webhook-jäsenet-kirje.json)
**Idea:**  
WordPress-lomakkeesta tuleva webhook käsittelee liittymishakemuksia.

**Toiminta:**
- Käyttäjä voi valita: "Haluan liittyä jäseneksi" ja/tai "Haluan jäsenkirjeen"
- Switch-logiikka (eri reitit jäsenyydelle ja kirjeelle)
- Tallentaa tiedot OneDrive Excel -taulukkoon
- Mahdollisuus lähettää erilaisia tervetuloviestejä riippuen valinnoista

**Tila:** Aktiivinen

---

## 3. Sisällön ja tiedonhallinta

### 3.1 Kontiotupa Facebook Posts (Kontotupa Facebook posts.json)
**Idea:**  
Hakee Kontiotupan Facebook-sivun viimeisimmät postaukset → muuntaa ne embeddingeiksi → tallentaa Qdrant-vektori tietokantaan.

**Tarkoitus:**
- Mahdollistaa semanttisen haun vanhoista Facebook-postauksista
- Tukee tulevia RAG (Retrieval-Augmented Generation) -ratkaisuja
- Käyttää Ollama embeddings + Qdrant

---

## Yhteiset piirteet workfloweissa

- Useimmissa käytetään **xAI Grok** -mallia sisällön analysointiin ja muotoiluun
- Vastausmuoto on standardoitu JSON: `{ "Otsikko", "ingressi", "sisältö", "slug" }`
- Viestit lähetetään Microsoft Teamsiin sisäiseen kanavaan ("Tiedotteet ja tapahtumat")
- Suurin osa workfloweista on manuaalisesti käynnistettäviä (Manual Trigger), mutta voidaan muuttaa cron-aikatauluiksi

## Kehitysideat / Seuraavat workflowt

- Automaattinen kuukausittainen jäsenkirje 
- Töpinän tori – AI-avusteinen inventaario ja some-postaus



---


---

