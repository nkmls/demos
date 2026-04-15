
# stm.py - ajetaan sunnuntai klo 8:15
15 8 * * 0 cd /root/stm && source /root/playwright-venv/bin/activate && python3 stm.py >> /root/stm/stm.log 2>&1

# kela.py - ajetaan sunnuntai klo 00:00
0 0 * * * cd /root/n8n/shared && source /root/playwright-venv/bin/activate && python3 kela.py >> /root/n8n/shared/scrape_kela.log 2>&1
