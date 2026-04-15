#!/usr/bin/env python3
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import datetime

def scrape_kela():
    url = "https://www.kela.fi/ajankohtaista?page=1&pageSize=20"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Moderni user-agent
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        })
        
        print(f"[{datetime.now()}] Haetaan sivua: {url}")
        page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Odota että uutiskortit latautuvat
        page.wait_for_selector('div[data-testid="topical-element-wrapper"]', timeout=30000)
        
        results = []
        
        cards = page.query_selector_all('div[data-testid="topical-element-wrapper"]')
        print(f"Löytyi {len(cards)} korttia")
        
        for card in cards:
            try:
                link_elem = card.query_selector('a')
                title_elem = card.query_selector('h3 span') or card.query_selector('h3')
                date_elem = card.query_selector('.kds-text-muted')
                type_elem = card.query_selector('.kelafi-badge')
                
                linkki = link_elem.get_attribute('href') if link_elem else ''
                if linkki and not linkki.startswith('http'):
                    linkki = 'https://www.kela.fi' + (linkki if linkki.startswith('/') else '/' + linkki)
                
                otsikko = title_elem.inner_text().strip() if title_elem else ''
                paiva = date_elem.inner_text().strip() if date_elem else ''
                tyyppi = type_elem.inner_text().strip() if type_elem else ''
                
                if otsikko:
                    results.append({
                        "linkki": linkki,
                        "otsikko": otsikko,
                        "paiva": paiva,
                        "tyyppi": tyyppi,
                        "haettu": datetime.now().isoformat()
                    })
            except:
                continue  # jos joku kortti epäonnistuu, jatka
        
        browser.close()
        
        # Tallenna JSON
        output_dir = Path("/root/n8n/shared")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / "kela_ajankohtaista.json"
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"[{datetime.now()}] Tallennettu {len(results)} uutista tiedostoon {output_file}")
        return len(results)

if __name__ == "__main__":
    scrape_kela()
