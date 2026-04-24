Olet Python-automaatioavustaja Kontiolahden Työttömät ry:lle.

Tehtävänäsi on luoda yksinkertaisia, hyvin kommentoituja ja eettisiä Python-skriptejä, jotka tukevat yhdistyksen missiota (yksinäisyyden vähentäminen, ruokajako, tapahtumien seuranta, kirpputorin hallinta jne.).

Käytä aina python.md-tiedostoa ohjeena.

Tehtävä: {{query}}

Tässä on **päivitetty ja parannettu versio** `python.md`-tiedostosta. Olen pitänyt alkuperäisen hengen (yksinkertaisuus, luettavuus, vapaaehtoisystävällisyys) mutta tehnyt selkeitä parannuksia vuoden 2026 tilanteen ja yhdistyksen tarpeiden mukaan.

Muutokset lyhyesti:
- Ruff korvaa Blackin ja isortin (Ruff on nopeampi ja riittää useimmissa tapauksissa).
- Lisätty selkeä projektirakenne-esimerkki.
- Lisätty yhdistysspesifinen osio (tapahtumat YAML-muodossa, toistuvien tapahtumien tuki, suomenkielisyys).
- Yksinkertaistettu työkalujen käyttö vapaaehtoisille.
- Lisätty käytännön komentoja ja README-ohjeistus.
- Korostettu eettisyyttä ja GDPR-huomiota (ruokajako, kirpputori jne.).

---

```markdown
# Python Kehityskäytännöt – Kontiolahden Työttömät ry

Tämä asiakirja määrittelee standardit ja parhaat käytännöt Python-skriptien kehittämiseen yhdistyksessämme.  
**Tavoitteena** on koodin **luettavuus**, **ylläpidettävyys** ja **helppo ymmärrettävyys** myös vapaaehtoisille, joilla ei ole vahvaa ohjelmointitaustaa.

Koodi tukee yhdistyksen missiota:  
yksinäisyyden vähentäminen, tapahtumien organisointi, ruokajako, kirpputorin hallinta, ilmoittautumiset ym.

## 1. Ydinperiaatteet (Zen of Python)

- **Yksinkertainen on parempi kuin monimutkainen.**
- Koodia luetaan paljon useammin kuin kirjoitetaan → **luettavuus ensin**.
- Käytä kuvaavia, mielellään suomenkielisiä muuttujia ja funktioiden nimiä.
- Pidä funktiot pieninä: yksi funktio – yksi selkeä tehtävä.
- Suosi eksplisiittistä koodia "taikuuden" sijaan.
- Sisällytä aina debug-lokitus (`logging`).

## 2. Koodityyli & Työkalut (2026)

Käytä seuraavia työkaluja:

| Työkalu     | Käyttötarkoitus                          | Komento-esimerkki                  |
|-------------|------------------------------------------|------------------------------------|
| **Ruff**    | Linting + formaus (korvaa Flake8, isort ja Blackin monessa tapauksessa) | `ruff check .` ja `ruff format .` |
| **Mypy**    | Staattinen tyypintarkistus               | `mypy .`                           |
| **Pytest**  | Testaus (myöhemmin, ei pakollinen aluksi)| `pytest`                           |

### Konfiguraatio (pyproject.toml)

Kaikki asetukset keskitetään yhteen tiedostoon:

```toml
[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
ignore = []

[tool.ruff.format]
quote-style = "double"

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
```

## 3. Tyypitys (Type Hinting)

Kaikki uusi koodi sisältää tyypit – ne toimivat itsestäänselvänä dokumentaationa.

Esimerkki:
```python
from datetime import date
from typing import List, Dict

def hae_tulevat_tapahtumat(paivat_eteenpain: int = 30) -> List[Dict]:
    ...
```

## 4. Ympäristön hallinta

- **Älä koskaan** asenna paketteja globaalisti.
- Käytä aina virtuaaliympäristöä:
  ```bash
  python -m venv .venv
  # Windows:
  .venv\Scripts\activate
  # Linux / Mac:
  source .venv/bin/activate
  ```
- Suositeltu riippuvuuksien hallinta: `pip` + `requirements.txt` (yksinkertaisin) tai `uv` edistyneemmille.
- Älä commita `.venv`-kansiota GitHubiin.

## 5. Tietoturva ja eettisyys

- **Älä** kovakoodaa salaisuuksia (sähköpostiosoitteet, API-avaimet jne.).
- Käytä `.env`-tiedostoa (`python-dotenv`).
- **GDPR-huomio**: Älä tallenna turhia henkilötietoja. Ruokajaossa ja kirpputorilla anonymisoi tiedot aina kun mahdollista.
- Päivitä riippuvuudet säännöllisesti: `pip list --outdated`.

## 6. Projektirakenne (suositus)

Yksinkertainen ja selkeä rakenne pienelle yhdistykselle:

```
kontiolahti_automaatio/
├── .venv/                  # Virtuaaliympäristö (ÄLÄ commitaa)
├── .env                    # Salaiset asetukset (ÄLÄ commitaa)
├── pyproject.toml
├── README.md               # Selkeät suomenkieliset käyttöohjeet
├── requirements.txt        # Riippuvuudet
├── data/                   # Tietokannat, listat (ruokajako.csv, kirpputori.yaml...)
├── tapahtumat/
│   ├── __init__.py
│   ├── tapahtuma_ilmoittaja.py
│   └── tapahtumat.yaml     # Tapahtumat helposti muokattavassa muodossa
├── utils/                  # Yhteiset apufunktiot (logging, päivämääräapu jne.)
├── tests/                  # Testit (myöhemmin)
└── kirpputori/             # Kirpputoriin liittyvät skriptit
```

## 7. Tapahtumien ja datan hallinta (yhdistysspesifi)

- **Älä** kovakoodaa tapahtumia suoraan `.py`-tiedostoon.
- Käytä mieluiten `tapahtumat.yaml`-tiedostoa (helppo muokata tekstieditorilla).
- Tue **toistuvia tapahtumia** (Äijäryhmä, bingo, vauva-treffit jne.) – suunnittele tulevaisuudessa funktio, joka generoi tapahtumia säännöllisesti.
- Esimerkki YAML-rakenne:
  ```yaml
  - nimi: "Äijäryhmä"
    paikka: "Kontiotupa"
    toistuvuus: "joka kuukauden 1. torstai"
    kuvaus: "..."
  ```

## 8. Luokat, funktiot ja dokumentointi

- Käytä Google-tyylisiä docstringejä monimutkaisemmissa funktioissa.
- Poikkeukset: Ole tarkka → `except ValueError:` eikä `except Exception:`.
- Jokaisessa pääskriptissä:
  - Selkeä otsikko ja kuvaus docstringissä (suomeksi).
  - `if __name__ == "__main__": main()`

## 9. Testaus ja debuggaus

- Sisällytä aina `logging`-moduuli (INFO-taso + virheet).
- Aloita kevyesti: `print()` + logging.
- Myöhemmin: kirjoita testit `tests/`-hakemistoon.

## 10. Käyttöönotto vapaaehtoisille (yksinkertainen ohje)

1. Kloonaa repositorio.
2. Luo virtuaaliympäristö ja aktivoi se.
3. `pip install -r requirements.txt`
4. Muokkaa tarvittaessa `tapahtumat.yaml` tai `.env`.
5. Aja esim. `python tapahtumat/tapahtuma_ilmoittaja.py`

**Muista**: Koodin tarkoitus on helpottaa vapaaehtoisten arkea – ei tehdä siitä vaikeampaa.

---

Tämä versio on valmis käytettäväksi. Se on pidetty **helppolukuisena** ja **käytännönläheisenä**, mutta sisältää modernit 2026-suositukset (erityisesti Ruff).

Haluatko, että teen vielä pienempiä säätöjä (esim. lisään esimerkin `tapahtumat.yaml`:sta tai `requirements.txt`:stä)? Vai siirrytäänkö suoraan luomaan paranneltu `tapahtuma_ilmoittaja.py` tämän uuden ohjeistuksen mukaisesti?
