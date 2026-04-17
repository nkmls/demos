# demos


Tämä repository sisältää **Kontiolahden Työttömät ry:n** ja **Kontiotuvan** digitaalisen kehityksen materiaalia, sekä muita omia projektejani.

Kaikki automaatiot, Docker-stackit, lomakkeet ja dokumentaatio yhdessä paikassa.

## 📁 Repositoryn rakenne

| Kansio          | Sisältö |
|-----------------|--------|
| `data/`         | (sisäinen) |
| `docs/`         | Dokumentaatio ja prosessikuvaukset |
| `html/`         | WordPress-lomakkeet ja HTML-sivut |
| `n8n/`          | n8n-spesifiset asetukset ja custom-nodet |
| `qdrant/`       | Vektoritietokanta AI-agentteja varten |
| `scripts/`      | Apuskriptit ja työkalut |
| `workflows/`    | n8n workflow JSON-tiedostot → katso [workflow.md](./docs/workflow.md) |
| `ollama/`      | Ollama asetukset |


## 🌐 Verkkopalvelut ja kanavat

- **Kontiotupa** → [kontiotupa.fi](https://kontiotupa.fi)
- **Kontiolahden Työttömät ry** → [kontiolahdentyottomat.fi](https://kontiolahdentyottomat.fi)
- **YouTube – Kontiotupa** → [@kontiotupa](https://www.youtube.com/@kontiotupa)
- **YouTube – Lumi AI** → [@lumi-ai.online](https://www.youtube.com/@lumi-ai.online)
- **Lehmon Pallo ry** → [lehpa.fi](https://lehpa.fi)

**Lisää linkkejä** → katso [LINKIT.md](./docs/linkit.md)

## 🛠️ Tekninen stack

- **n8n** (self-hosted) + PostgreSQL + Qdrant 
- **Caddy** (reverse proxy + HTTPS)
- **Microsoft 365** (Outlook, OneDrive, Calendar, Excel, Forms)
- **xAI Grok API**
- **WordPress**
- **Ollama** embeddings → katso [ollama.md](./docs/ollama.md)

## Tavoitteet

- Automatisoida yhdistyksen arkea (jäsenhankinta, Töpinän tori, ruokajakelu, tapahtumat)
- Kehittää monistettavia ratkaisuja muille yhdistyksille
- Yhdistää teknologiaa ja yhteisöllisyyttä

---

**Ylläpitäjä:** **[Niko Mölsä** – Varapuheenjohtaja & ICT-vastaava  
**Status:** Kehitysvaihe (vapaaehtoistyö)  
**Päivitetty:** 15.4.2026

**Lisenssi:** MIT License
