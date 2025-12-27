# Shani Bot

Ein leistungsstarker Discord-Bot für die Verwaltung von Raider-Setcards, dynamische Auto-Voice Channels und Twitch-Live-Alerts ohne API-Key.

## 🚀 Features

### 🛠️ Raider-Setcards
*   **Individuelle Profile:** User können ihre Gaming-Infos (Embark ID, Plattform, Erfahrung, Spielstil) hinterlegen.
*   **Automatische Posts:** Setcards werden in einem konfigurierten Kanal gepostet und bei Änderungen automatisch aktualisiert.
*   **Suche:** Finde Mitspieler basierend auf Filtern wie Plattform, Alter oder Spielstil mit `/setcard find`.
*   **SQLite-Backend:** Schnelle und sichere Datenspeicherung.

### 🔊 Auto-Voice (Squad Channels)
*   **Dynamische Channels:** Beim Betreten eines "Join"-Channels wird automatisch ein neuer Voice-Channel ("Squad <User>") in einer Ziel-Kategorie erstellt.
*   **Berechtigungsverwaltung:** Der Ersteller erhält automatisch Rechte zum Verwalten des Channels.
*   **Automatischer Cleanup:** Leere Kanäle werden sofort gelöscht, um den Server sauber zu halten.
*   **Echtzeit-Rename:** Ändert ein User seinen Anzeigenamen, während er in seinem Squad-Channel ist, wird der Kanal sofort umbenannt.

### 🟣 Twitch Live-Alerts (No-API)
*   **Einfaches Setup:** Keine Registrierung bei der Twitch-API nötig. Einfach Kanal-URL angeben.
*   **Präzise Erkennung:** Nutzt intelligentes Scraping mit Stabilisierungs-Logik, um Mehrfach-Pings bei kurzen Verbindungsabbrüchen zu verhindern.
*   **Automatisches Editieren:** Wenn ein Stream endet, wird die Live-Nachricht automatisch in eine Offline-Meldung umgewandelt.

## 📋 Voraussetzungen
*   Python 3.8+
*   `discord.py`
*   `aiohttp`
*   `python-dotenv`
*   `PyNaCl` (optional, für Voice-Audio Support)

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

### Konfiguration
*   `/setcard set_channel <#kanal>`: Legt den Kanal für Setcards fest.
*   `/setup_autovoice <join-channel> <ziel-kategorie>`: Richtet das Auto-Voice System ein.
*   `/setup_twitchlive2 <kanal-url> <#announce-kanal> [rolle]`: Aktiviert Twitch-Alerts.

### User
*   `/setcard edit`: Erstellt oder bearbeitet die eigene Setcard.
*   `/setcard me`: Zeigt die eigene Setcard an.
*   `/setcard find`: Sucht nach anderen Spielern.

## 🧹 Fehlerbehebung (Doppelte Commands)
Falls Slash-Commands doppelt angezeigt werden, führe einmalig das Bereinigungs-Skript aus:
```bash
python3 cleanup_commands.py
```
Danach den Bot neu starten und Discord (Strg+R) aktualisieren.

## 📄 Lizenz
Dieses Projekt ist für den privaten Gebrauch auf Discord-Servern bestimmt.
