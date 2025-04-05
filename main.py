import requests
import re

API_KEY = "your-api" <!--edit-->
DOMAIN = "your-domain" <!--edit-->
URL = f"https://api.eu.mailgun.net/v3/{DOMAIN}/messages"

# wczytanie adresów e-mail
with open("emails.txt", "r") as file:
    email_list = [line.strip() for line in file]

# wczytanie treści wiadomości z pliku i zamiana \n na <br>
with open("mail.txt", "r", encoding="utf-8") as mail_file:
    mail_content = mail_file.read().replace("\n", "<br>")


# HTML wiadomości ze stopka
html_content = f"""
<html>
    <body>
        <p>{mail_content}</p>
        <a href="your-domain"> <!--edit-->
            <img src="https://i.ibb.co[link]" alt="Stopka" border="0" style="max-width: 100%;"> <!--edit stopke maila np. korzystajac z i.ibb-->
        </a>
    </body>
</html>
"""


# Wysyłanie e-maili
for email in email_list:
    response = requests.post(
        URL,
        auth=("api", API_KEY),
        data={
            "from": "your-subject", <!--edit-->
            "to": email,
            "subject": "your-subject", <!--edit-->
            "text": mail_content,  # Treść w wersji tekstowej
            "html": html_content,  # Treść w wersji HTML ze stopka
            "o:tracking": "yes",  # śledzenia otwarć
            "o:tag": "test"  # tagu dla raportów
        }
    )

    print(f"Wysłano do {email}: {response.status_code} {response.text}")
