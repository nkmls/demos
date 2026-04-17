# Ollama Embeddings & Vektoritietokanta

Tämä dokumentti kuvaa, miten käytämme **Ollamaa** ja **Qdrant** vektoritietokantaa n8n-automaatioissa Kontiolahden Työttömät ry:ssä.

## Miksi embeddings?

Käytämme tekstin embeddings-malleja, jotta voimme:
- Hakea semanttisesti samankaltaisia sisältöjä (esim. jäsenhakemuksia, lahjoituskuvauksia)
- Rakentaa älykkäitä AI-agentteja
- Parantaa hakutoimintoja Kontiotuvan ja Töpinän torin datasta
- Generoida parempia vastauksia Grok-mallilla kontekstin avulla

## Tekninen stack

- **Ollama** – Paikallinen LLM + embeddings-mallit
- **Qdrant** – Vektoritietokanta (Dockerissa)
- **n8n** – Integraatio ja workflow’t
- **xAI Grok** – Päämalli (täydennyksenä)

## Käytössä olevat embeddings-mallit

| Malli                        | Koko     | Käyttötarkoitus                          | Status     |
|-----------------------------|----------|------------------------------------------|------------|
| `nomic-embed-text`          | ~137M    | Yleinen tekstin embedding (suositus)     | Käytössä   |
| `mxbai-embed-large`         | 335M     | Parempi laatu suomenkieliselle tekstille | Testaus    |
| `all-MiniLM-L6-v2`          | 23M      | Nopea kevyt embedding                    | Vaihtoehto |

**Suositus:** Aloita mallilla `nomic-embed-text`

## Docker-konfiguraatio (qdrant + ollama)

Katso `docker-compose.yml` tiedostosta palvelut:
- `qdrant` – Vektoritietokanta
- `ollama` – Paikallinen LLM-palvelu (embeddings + chat)

## n8n-integraatioesimerkit

### 1. Tekstin embedding + tallennus Qdrantiin
- Node: HTTP Request → Ollama Embeddings endpoint
- Node: Qdrant Vector Store (upsert)

### 2. Semanttinen haku
- Käyttäjä syöttää kysymyksen
- Muunnetaan embeddingiksi
- Haetaan samankaltaisia dokumentteja Qdrantista
- Lähetetään konteksti Grok:lle

→ katso [workflow.md](./docs/workflow.md) |

## Asennusohjeet

1. Lisää `ollama/qdrant` palvelu `docker-compose.yml`:iin ja aja komento:
```bash
   docker compose  docker-compose.yml up -d

2. Pullaa haluttu malli:
```bash
docker exec -it ollama ollama pull nomic-embed-text


