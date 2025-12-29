# Shani Bot – ARC Raiders Discord Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Release: v1.0.0](https://img.shields.io/badge/Release-v1.0.0-green.svg)](https://github.com/Kasmodro/shani-arc-raiders-bot/releases)

Shani is a powerful Discord bot designed specifically for **ARC Raiders** communities. It streamlines squad management, player profiles, and stream notifications to enhance the gaming experience.

## ⚡ Quick Start
```bash
git clone https://github.com/Kasmodro/shani-arc-raiders-bot.git
cd shani-arc-raiders-bot
pip install -r requirements.txt
cp .env.example .env # Add your DISCORD_TOKEN to .env
python3 bot.py
```

## 🚀 Main Features
- **Auto Voice Channels:** Dynamic squad channels (2-player, 3-player, or open squads).
- **Raider Setcards:** Comprehensive player profiles for better squad matching.
- **Twitch Live Alerts:** Real-time stream notifications without the need for a Twitch API key.
- **Interactive UI:** Fully driven by Discord Slash Commands and Buttons for a modern experience.

---

Ein leistungsstarker Discord-Bot für die Verwaltung von Raider-Setcards, dynamische Auto-Voice Channels (2er, 3er, Open) und Twitch-Live-Alerts ohne API-Key. Mit vollständig interaktivem UI über Slash-Commands und Buttons.

## 🚀 Features Detail (Deutsch)

### ✨ Interaktive Benutzeroberfläche
*   **Zentrales Menü:** Der Befehl `/shani` ist der einzige Einstiegspunkt, den User und Admins brauchen. Alles lässt sich über Buttons und Menüs steuern.
*   **Geführtes Setup:** Admins können den Bot über das "Admin Setup" Menü konfigurieren (Rollen, Kanäle, Twitch) – kein Auswendiglernen von Befehlen nötig.

### 🛠️ Raider-Setcards
*   **Individuelle Profile:** User können ihre Gaming-Infos (Embark ID, Plattform, Erfahrung, Spielstil) hinterlegen.
*   **Interaktive Suche:** Finde Mitspieler direkt über das `/shani` Menü mit Filtern wie Spielstil, Plattform oder Erfahrung.
*   **Intelligentes Matching:** Die Suche versteht Teilbegriffe und erlaubt Mehrfachauswahl bei den Interessen.
*   **Automatische Posts:** Setcards werden in einem konfigurierten Kanal gepostet und bei Änderungen automatisch aktualisiert.

### 🔊 Auto-Voice 2.0 (Squad Channels)
*   **Drei Modi:** Dedizierte Join-Channels für **2er Squads**, **3er Squads** und **Open Squads** (unbegrenzt).
*   **Setcard-Integration:** Der Bot postet automatisch die Setcard des Squad-Leiters in den Textchat des Voice-Channels, damit beigetretene Spieler sofort wissen, mit wem sie spielen.
*   **Eingeschränkte Rechte:** User können das Squad-Limit nicht mehr manipulieren, behalten aber Moderationsrechte (Kicken/Moven) und können den **Voice-Status** setzen.
*   **Intelligenter Cleanup:** Aktiver Scan der Voice-Kategorie sorgt dafür, dass leere Kanäle sofort und zuverlässig gelöscht werden.

### 🟣 Twitch Live-Alerts (No-API)
*   **Einfaches Setup:** Keine Registrierung bei der Twitch-API nötig. Konfiguration bequem über das Admin-Menü.
*   **Automatisches Editieren:** Live-Nachrichten werden bei Stream-Ende automatisch in Offline-Meldungen umgewandelt.

### 🔐 Rollen- & Berechtigungssystem
*   **Hauptmenü:** Zentraler Einstiegspunkt über `/shani` mit rollenbasierter Button-Anzeige.
*   **Admin- & Mod-Rollen:** Konfigurierbare Rollen für erweiterten Zugriff auf Bot-Funktionen.
*   **Sichtbarkeit:** Administrative Befehle sind für normale User in Discord unsichtbar.

## 🛡️ Discord Permissions & Intents
Damit alle Funktionen reibungslos laufen, benötigt der Bot folgende Einstellungen im Discord Developer Portal:

### Privileged Gateway Intents
*   **Presence Intent:** Aus (nicht benötigt)
*   **Server Members Intent:** AN (für Rollenprüfung & Setcards)
*   **Message Content Intent:** AN (für Befehlsverarbeitung)

### Bot Permissions (OAuth2 Scope: `bot` + `applications.commands`)
*   **Manage Channels:** Erstellen/Löschen der Squad-Kanäle
*   **Move Members:** Verschieben in neue Squads
*   **Manage Roles:** Rollenprüfung beim Setup
*   **Send Messages / Embed Links:** Benachrichtigungen & Setcards
*   **Connect / Speak:** Voice-Support

⚠️ **Only grant the permissions listed above. Administrator permissions are not required.**

## 📋 Voraussetzungen
*   Python 3.12+
*   `discord.py`
*   `aiohttp`
*   `python-dotenv`
*   `PyNaCl` (für Voice Support)

## ⚙️ Installation

1.  **Repository klonen:**
    ```bash
    git clone https://github.com/Kasmodro/shani-arc-raiders-bot.git
    cd shani-arc-raiders-bot
    ```

2.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Konfiguration (.env Datei):**
    Der Bot benötigt einen Discord-Token, um online zu gehen. Diesen speicherst du sicher in einer Datei namens `.env`.
    
    *   Verwende die Vorlage [.env.example](.env.example) als Basis:
        ```bash
        cp .env.example .env
        ```
    *   Öffne die Datei (z. B. mit `nano .env`) und füge deinen Bot-Token ein:
        ```env
        DISCORD_TOKEN=DEIN_BOT_TOKEN_HIER_EINSETZEN
        ```
    *   *Hinweis:* Die `.env` Datei wird von Git ignoriert, damit dein Token nicht öffentlich auf GitHub landet.

4.  **Bot starten:**
    ```bash
    python3 bot.py
    ```

## 🖥️ Automatischer Start (Systemd Service)
Damit der Bot nach einem Server-Neustart automatisch startet, empfiehlt sich die Einrichtung als System-Service:

1.  **Service-Datei erstellen:** `sudo nano /etc/systemd/system/shani.service`
2.  **Inhalt einfügen** (Pfade anpassen!):
    ```ini
    [Unit]
    Description=Shani Discord Bot
    After=network.target

    [Service]
    Type=simple
    User=DEIN_USER
    WorkingDirectory=/home/DEIN_USER/shani-arc-raiders-bot
    ExecStart=/usr/bin/python3 bot.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
3.  **Aktivieren:**
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable shani.service
    sudo systemctl start shani.service
    ```

## 🛠️ Bedienung

### Für Admins
Nutze `/shani` und klicke auf **"Admin Setup"**. Dort kannst du schrittweise Rollen, Kanäle und Twitch konfigurieren.

### Für User
Nutze `/shani`, um deine **Setcard zu bearbeiten** oder nach **Raidern zu suchen**.

## 🧹 Fehlerbehebung (Doppelte Commands)
Falls Slash-Commands doppelt angezeigt werden, führe einmalig das Bereinigungs-Skript aus:
```bash
python3 cleanup_commands.py
```
Danach den Bot neu starten und Discord (Strg+R) aktualisieren.

## 🤝 Community & Forks

This project is intentionally open-source.

You are **explicitly allowed and encouraged** to:
- fork this repository
- modify the code
- run your own version of the bot
- adapt it for your own Discord community

No permission is required — just keep the original license and credits.

Forks do **not** grant any official support or endorsement.

If you build something cool on top of it, feel free to share it with the community 🚀

## 🛡️ Disclaimer

This bot is provided **"as is"**, without warranty of any kind.

Server owners and administrators are **fully responsible** for:
- how the bot is configured
- which permissions it is granted
- how it is used within their Discord server

The author is **not liable** for:
- moderation issues
- data loss
- misuse by server members
- Discord ToS violations caused by misconfiguration
- actions taken by Discord moderators or automated systems

Use at your own risk.

### 🇩🇪 Haftungsausschluss (Kurzfassung)

Die Nutzung des Bots erfolgt **auf eigene Verantwortung**.

Server-Admins sind selbst dafür verantwortlich, welche Rechte der Bot erhält und wie er eingesetzt wird. Der Entwickler übernimmt keine Haftung für Fehlkonfigurationen, Missbrauch oder Regelverstöße auf dem Server.

## 📄 Lizenz
Dieses Projekt ist unter der **MIT-Lizenz** lizenziert. Weiterverwendung oder Anpassungen sind ausdrücklich erlaubt, solange der ursprüngliche Autor genannt wird.

---
### 🆘 Support
*   **Bug reports & feature requests:** [GitHub Issues](https://github.com/Kasmodro/shani-arc-raiders-bot/issues)
*   **Setup questions & discussion:** [Discord Server](https://discord.gg/UhhJtFteun)
