from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
from datetime import datetime
import time
import os

# Kiinteä tiedostonimi (ylikirjoitetaan aina)
OUTPUT_PATH = "/root/n8n/shared/stm-ajankohtaista.json"

def scrape_stm_ajankohtaista(output_file=OUTPUT_PATH):
    articles = []
    
    print(f"Aloitetaan STM ajankohtaista -scrapaus → tallennetaan: {output_file}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            bypass_csp=True,
            ignore_https_errors=True,           # joskus STM:llä sertifikaattihässäkkää
        )
        page = context.new_page()
        
        print("Ladataan https://stm.fi/ajankohtaista ...")
        success = False
        for attempt in range(1, 4):
            try:
                page.goto("https://stm.fi/ajankohtaista", 
                         wait_until="domcontentloaded", 
                         timeout=45000)
                page.wait_for_load_state("networkidle", timeout=35000)
                success = True
                break
            except PlaywrightTimeoutError:
                print(f"Latausyritys {attempt} epäonnistui → odotetaan 4s ja yritetään uudelleen...")
                time.sleep(4)
        
        if not success:
            print("Sivun lataus epäonnistui 3 kertaa → lopetetaan.")
            browser.close()
            return articles
        
        # Odota, että jotain uutissisältöä ilmestyy
        try:
            page.wait_for_selector(
                'div.portlet-content-container, article, li a[href*="/-/"], div[class*="news"]', 
                timeout=20000
            )
        except:
            print("Uutislistan odotus epäonnistui → yritetään silti jatkaa.")
        
        # Kerätään containerit
        portlet_containers = page.locator('div.portlet-content-container').all()
        print(f"Löytyi {len(portlet_containers)} kpl portlet-content-container")
        
        containers = portlet_containers
        if not containers:
            print("Ei portlet-containeria → kokeillaan fallback-selektoreita")
            containers = page.locator(
                'div[class*="news-list"], div[class*="portlet"], ul[class*="news"], section[class*="content"], main'
            ).all()
            if not containers:
                print("Ei vieläkään containeria → käytetään koko bodyä")
                containers = [page.locator('body')]
        
        for container in containers:
            items = container.locator(
                'article, li, div[class*="item"], div[class*="teaser"], div[class*="card"], a[href*="/-/"]'
            ).all()
            
            print(f"→ Löytyi {len(items)} potentiaalista uutista containerista")
            
            for item in items:
                try:
                    # Otsikko + linkki
                    title_loc = item.locator(
                        'h2 a, h3 a, h2, h3, a:has(h2), a:has(h3), a'
                    ).first
                    
                    if not title_loc.is_visible(timeout=800):
                        continue
                    
                    title = title_loc.inner_text(timeout=4000).strip()
                    if not title or len(title) < 6:
                        continue
                    
                    link = title_loc.get_attribute("href") or ""
                    if not link:
                        continue
                    if link.startswith("/"):
                        link = "https://stm.fi" + link
                    if not link.startswith("http"):
                        continue
                    
                    # Päivämäärä
                    date = ""
                    date_loc = item.locator(
                        'time, span[class*="date"], div[class*="date"], p[class*="meta"], .date'
                    ).first
                    if date_loc.count() > 0:
                        date = date_loc.inner_text(timeout=2000).strip()
                    
                    # Ingressi / lead
                    summary = ""
                    summary_loc = item.locator(
                        'p:not(:has(a)), div[class*="lead"], div[class*="summary"], .teaser-text, .description'
                    ).first
                    if summary_loc.count() > 0:
                        summary = summary_loc.inner_text(timeout=2000).strip()
                    
                    article = {
                        "title": title,
                        "url": link,
                        "date": date,
                        "summary": summary[:320],
                        "scraped_at": datetime.now().isoformat(),
                        "source": "stm.fi/ajankohtaista"
                    }
                    
                    articles.append(article)
                    print(f"OK: {title[:70]}...  ({date})")
                    
                except Exception as e:
                    print(f"Ohitetaan viallinen elementti ({str(e)[:80]})")
                    continue
        
        browser.close()
    
    # Tallennetaan → ylikirjoitetaan aina
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        print(f"\nValmis! {len(articles)} artikkelia tallennettu → {output_file}")
    except Exception as e:
        print(f"Tiedoston tallennus epäonnistui: {e}")
    
    return articles


if __name__ == "__main__":
    scrape_stm_ajankohtaista()
