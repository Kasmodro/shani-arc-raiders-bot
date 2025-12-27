# Shani Bot

Ein leistungsstarker Discord-Bot für die Verwaltung von Raider-Setcards, dynamische Auto-Voice Channels (2er, 3er, Open) und Twitch-Live-Alerts ohne API-Key.

## 🚀 Features

### 🛠️ Raider-Setcards
*   **Individuelle Profile:** User können ihre Gaming-Infos (Embark ID, Plattform, Erfahrung, Spielstil) hinterlegen.
*   **Automatische Posts:** Setcards werden in einem konfigurierten Kanal gepostet und bei Änderungen automatisch aktualisiert.
*   **Suche:** Finde Mitspieler basierend auf Filtern wie Plattform, Alter oder Spielstil mit `/setcard find`.
*   **SQLite-Backend:** Schnelle und sichere Datenspeicherung.

### 🔊 Auto-Voice 2.0 (Squad Channels)
*   **Drei Modi:** Dedizierte Join-Channels für **2er Squads**, **3er Squads** und **Open Squads** (unbegrenzt).
*   **Eingeschränkte Rechte:** User können das Squad-Limit nicht mehr manipulieren, behalten aber Moderationsrechte (Kicken/Moven) und können den **Voice-Status** setzen.
*   **Intelligenter Cleanup:** Aktiver Scan der Voice-Kategorie sorgt dafür, dass leere Kanäle sofort und zuverlässig gelöscht werden.
*   **Echtzeit-Rename:** Automatische Namensanpassung bei Display-Name-Wechsel.

### 🟣 Twitch Live-Alerts (No-API)
*   **Einfaches Setup:** Keine Registrierung bei der Twitch-API nötig.
*   **Automatisches Editieren:** Live-Nachrichten werden bei Stream-Ende automatisch in Offline-Meldungen umgewandelt.

### 🔐 Rollen- & Berechtigungssystem
*   **Hauptmenü:** Zentraler Einstiegspunkt über `/shani` mit rollenbasierter Button-Anzeige.
*   **Admin- & Mod-Rollen:** Konfigurierbare Rollen für erweiterten Zugriff auf Bot-Funktionen.
*   **Sichtbarkeit:** Administrative Befehle sind für normale User in Discord unsichtbar.

## 📋 Voraussetzungen
*   Python 3.12+
*   `discord.py`
*   `aiohttp`
*   `python-dotenv`
*   `PyNaCl` (für Voice Support)

## ⚙️ Installation

1.  **Repository klonen:**
    ```bash
    git clone https://github.com/Kasmodro/shani-bot-beta.git
    cd shani-bot
    ```

2.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Konfiguration:**
    Erstelle eine `.env` Datei im Hauptverzeichnis:
    ```env
    DISCORD_TOKEN=DEIN_BOT_TOKEN
    ```

4.  **Bot starten:**
    ```bash
    python3 bot.py
    ```

## 🛠️ Wichtige Befehle

### Konfiguration (Nur Admins)
*   `/shani_setup_roles`: Legt Admin- und Mod-Rollen fest.
*   `/shani_status`: Zeigt die gesamte Bot-Konfiguration auf einen Blick.
*   `/setup_autovoice`: Konfiguriert die Join-Channels und die Ziel-Kategorie.

### User
*   `/shani`: Öffnet das interaktive Hauptmenü.
*   `/setcard edit / me / find`: Verwaltung der Raider-Setcards.

## 🧹 Fehlerbehebung (Doppelte Commands)
Falls Slash-Commands doppelt angezeigt werden, führe einmalig das Bereinigungs-Skript aus:
```bash
python3 cleanup_commands.py
```
Danach den Bot neu starten und Discord (Strg+R) aktualisieren.

## 📄 Lizenz
Dieses Projekt ist für den privaten Gebrauch auf Discord-Servern bestimmt.
