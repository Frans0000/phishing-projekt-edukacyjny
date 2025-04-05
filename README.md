# Phishing Projekt Edukacyjny

Ten projekt to edukacyjna symulacja ataku phishingowego, mająca na celu zwiększenie świadomości użytkowników na temat zagrożeń w sieci i zobaczenia skali problemu. Stworzony w celach dydaktycznych.
Zebrane statystyki będą dosyć dokładne, bo będzie wiadomo ile osób w ogóle otworzyło maila i następnie ile z nich weszło na podaną w próbie phishingowej strone.

## Główne funkcje

- **Strona phishingowa** hostowana za pomocą **GitHub Pages**
- Monitorowanie wejść z użyciem **Google Analytics**
- **Mailgun API** do rozsyłania symulowanych wiadomości e-mail oraz podglądu który z adresów otworzył maila
- **Cloudflare** zarządzania DNS
- Skrypt w **Pythonie + Selenium**:
    - main.py który rozsyła maile za pomocą mailgun
    - emailScraper.py do pobierania ogólnodostępnych adresów (w przykładzie uwr)
- Przykładowy mail

## Ważne

Projekt **nie ma na celu rzeczywistego wyłudzania danych**. Wszelkie dane użyte w projekcie np. adresy e-mail pochodzą z ogólnodostępnych, publicznych źródeł. 
Projekt powinien być wykorzystywany wyłącznie w środowisku testowym lub edukacyjnym, z zachowaniem zasad etycznych i prawnych.

## Co potrzebujesz

Jedyne czego potrzebujesz w tym projekcie to zakupienie własnej domeny. Reszta narzędzi jest za darmo.

### Hosting strony na GitHub Pages

Aby opublikować stronę edukacyjną za pomocą GitHub Pages:

1. Upewnij się, że plik HTML ma nazwę **`index.html`**.
2. Stwórz nowe repozytorium na GitHub - musi być publiczne w wersji darmowej.
3. Wrzuć do repozytorium plik `index.html`
4. Przejdź do **Settings** w repozytorium.
5. W menu po lewej stronie wybierz zakładkę **Pages**.
6. W sekcji **Build and deployment**:
   - Ustaw **Source** na `Deploy from a branch`
   - Wybierz **Branch**: `main`, a folder: `/ (root)`
7. Kliknij **Save**.
8. Po chwili GitHub wygeneruje adres strony
9. W custom domain wklej nazwę swojej domeny, żeby strona była pod wykupionym adresem.

Więcej informacji: [https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

## Konfiguracja Google Analytics

Aby dodać śledzenie wejść na stronę za pomocą Google Analytics:

1. Przejdź na stronę: [https://analytics.google.com/](https://analytics.google.com/)
2. W kolumnie **Usługa (Property)** kliknij **Utwórz usługę**:
   - Podaj nazwę (np. `Phishing Edukacyjny`)
   - Wybierz odpowiednią strefę czasową i walutę
3. Wybierz **"Strona WWW"** jako źródło danych.
4. Po utworzeniu usługi otrzymasz identyfikator śledzenia w formacie: G-XXXXXXXXXX.
5. Wklej go w odpowiednie miejsca w pliku **`index.html`**.

## Konfiguracja Mailgun

1. Zarejestruj się na stronie: [https://www.mailgun.com/](https://www.mailgun.com/).
2. Po zalogowaniu przejdź do zakładki **Sending → Domains**.
3. Kliknij **"Add New Domain"**.
   - Przykład: `twojadomena.pl`
   - Możesz wybrać tryb **custom domain**
4. Mailgun wyświetli wymagane rekordy DNS:
   - **TXT** 
   - **MX**
   - **CNAME**
5. Dodaj te rekordy w panelu DNS swojej domeny (np. w Cloudflare).
6. Po kilku minutach (lub godzinach) domena zostanie zweryfikowana.
7. Przejdź do **Settings → API Keys** i skopiuj swój:
   - **Private API Key** (format: `key-xxxxxxxxxxxxxxxxxxxx`)
8. Umieść go w odpowiednim miejscu w pliku **`main.py`**.

## Konfiguracja Cloudflare (zarządzanie DNS i bezpieczeństwo)

Cloudflare to darmowe narzędzie do zarządzania DNS, ochrony domeny. 
W tym projekcie jest wykorzystana do zarządzania DNS.

### Krok po kroku:

1. Zarejestruj się na stronie: [https://cloudflare.com/](https://cloudflare.com/).
2. Kliknij **"Add a Site"** i wpisz swoją domenę.
3. Wybierz darmowy plan **Free** i kliknij **Continue**.
4. Cloudflare zeskanuje Twoje rekordy DNS i pokaże je do edycji.
5. Po zatwierdzeniu otrzymasz **nowe nameserwery**, np.: dahlia.ns.cloudflare.com kevin.ns.cloudflare.com
6. Przejdź do panelu swojego rejestratora domen (np. seohost.pl) i **zamień obecne nameserwery** na te z Cloudflare.
7. Poczekaj na propagację DNS (czasami kilka minut, czasami do 24h).

Konfiguracja cloudflare przykład:
![image](https://github.com/user-attachments/assets/f5c36474-4c2f-4087-8390-d41c206b0031)



### Rekordy DNS do GitHub Pages

Aby Twoja strona z GitHub Pages działała pod własną domeną:

- Jeśli używasz subdomeny (np. `www.twojadomena.pl`):
  - **Typ**: `CNAME`
  - **Nazwa**: `www`
  - **Wartość**: `twoja-nazwa.github.io`

- Jeśli chcesz użyć domeny głównej (`twojadomena.pl`):
  - **Typ**: `A`
  - **Nazwa**: `@`
  - **Wartości**: (IP GitHub Pages – wpisz każdy jako osobny rekord)
    - `185.199.108.153`
    - `185.199.109.153`
    - `185.199.110.153`
    - `185.199.111.153`
---

### Rekordy DNS do Mailgun

Po dodaniu domeny w Mailgun, otrzymasz zestaw rekordów (np. `TXT`, `MX`, `CNAME`) — dodaj je dokładnie tak, jak podaje Mailgun:

- **TXT**: do weryfikacji i SPF/DKIM
- **MX**: dla odbioru e-maili (opcjonalnie)
- **CNAME**: dla śledzenia kliknięć i otwarć

Po poprawnym dodaniu, Mailgun sam zweryfikuje domenę i będzie gotowe do wysyłki.

---

## Preview strony z komunikatem
![image](https://github.com/user-attachments/assets/efce5e29-26df-49da-9598-0f5b03babdcf)

