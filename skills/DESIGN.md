
---
name: Kontiolahti Yhdistys
description: Minimalistinen design järjestöille – luotettava, yhteisöllinen ja digitalisoitu. Inspiroituna Kontiolahden Työttömien Yhdistys & Kontiotupa.
colors:
  primary: "#2E5B4D"      # Metsänvihreä – luottamus & luonto (Pohjois-Karjala)
  secondary: "#6B7280"    # Harmaa – neutraali metadata
  tertiary: "#F59E0B"     # Oranssi – aktiiviset call-to-action (tapahtumat)
  neutral: "#F8FAFC"      # Vaalea harmaa – tausta (lämpimän neutraali)
  on-primary: "#FFFFFF"   # Teksti vihreällä
  success: "#10B981"
  error: "#EF4444"
typography:
  h1:
    fontFamily: "Inter"        # Moderni sans-serif (Google Fonts)
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.2
  h2:
    fontFamily: "Inter"
    fontSize: 1.875rem
    fontWeight: 600
  body-lg:
    fontFamily: "Inter"
    fontSize: 1.125rem
    lineHeight: 1.6
  body-md:
    fontFamily: "Inter"
    fontSize: 1rem
    lineHeight: 1.5
  label-sm:
    fontFamily: "Inter"
    fontSize: 0.875rem
    fontWeight: 500
    textTransform: uppercase
rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-md}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: "1px"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  card:
    backgroundColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    shadow: "0 1px 3px rgba(0,0,0,0.1)"
---

## Overview

**Yhteisöllinen Minimalismi.** Design heijastaa Kontiolahden luontoa (vihreä luottamus) ja yhdistysarkeaa – selkeä, saavutettava ja skaalautuva web/app:ille (WP, n8n-botit, tapahtumasivut). Korkea kontrasti (WCAG AAA), mobiili-first.

Ei turhia koristeita: Keskity sisältöön (tapahtumat, jäsenet, docs).

## Colors

Paletti pohjoiskarjalainen & luotettava:
- **Primary (#2E5B4D):** Vihreä painikkeet/call-to-action (tapahtumat).
- **Secondary (#6B7280):** Tekstit/metadata (jäsenlistat).
- **Tertiary (#F59E0B):** Korostukset (uudet uutiset).
- **Neutral (#F8FAFC):** Tausta – rauhallinen lukemiseen.

Kontrasti: Primary/on-primary 12:1 (passes AAA).

## Typography

Inter-fontti (free Google Fonts) – luettava suomi/englanti.
- **H1/H2:** Isot otsikot tapahtumille.
- **Body:** Päivittäinen teksti (RSS-uutiset).
- Caps-labelit lomakkeisiin (Forms).

## Layout & Spacing

Grid/flexbox-pohjainen: 16px base (md-skala).
- Cards tapahtumille/repo:lle.
- Spacing: Tasainen rytmi.

## Components

**Button-primary:** Tapahtuma-ilmoittautuminen.
**Button-secondary:** Linkit (repo/docs).
**Card:** Uutinen/jäsen – neutral bg, vihreä hover.

Hover: Primary lighten 10% (ei animaatioita – vakaa).

## Do's and Don'ts

✅ **Do:** Käytä primary vihreää CTA:han. Korkea kontrasti.
✅ **Do:** Inter body-teksti, 1.5+ line-height.
❌ **Don't:** Kirkkaat värit (turkoosi/pinkki) – pysy neutraalissa.
❌ **Don't:** Monimutkaiset shadowit – flat/minimal.

**Käytä koodauksessa:** Tailwind/CSS vars näillä tokeneilla. Testaa `npx @google/design.md lint DESIGN.md`.
