from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re

# ==== ustawienia ====
BASE_URL = "https://wfil.uwr.edu.pl/lista-pracownikow/" # Adresy e-mail pobierane wyłącznie do celów edukacyjnych
NUM_EMAILS = 100
SCROLL_DELAY = 1

# ==== konfiguracja przeglądarki ====
options = Options()

driver = webdriver.Chrome(options=options)

# ==== cookies ====
driver.get(BASE_URL)
input("enter po cookies")

# ==== linki ====
soup = BeautifulSoup(driver.page_source, 'html.parser')
profile_links = soup.select("a.pracownik-litera")
full_links = [BASE_URL + link.get("href") for link in profile_links]

emails = []

for link in full_links:
    driver.get(link)
    time.sleep(SCROLL_DELAY)

    try:
        accordion_button = driver.find_element(By.CSS_SELECTOR, "button.accordion")
        accordion_button.click()
        time.sleep(SCROLL_DELAY)
    except Exception as e:
        print(f"błąd kliknięcia: {e}")

    profile_soup = BeautifulSoup(driver.page_source, 'html.parser')
    panel = profile_soup.select_one("div.panel")

    if panel:
        text = panel.get_text()
        found_emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        for email in found_emails:
            if email not in emails:
                emails.append(email)
                print(f"[+] znaleziono email: {email}")
                if len(emails) >= NUM_EMAILS:
                    break
    if len(emails) >= NUM_EMAILS:
        break

driver.quit()

print("\nzebrane adresy email:")
for email in emails:
    print(email)

# zapis
with open("emails.txt", "w", encoding="utf-8") as f:
    for email in emails:
        f.write(email + "\n")

print(f"\nzapisano {len(emails)} adresów do pliku 'emails.txt'")