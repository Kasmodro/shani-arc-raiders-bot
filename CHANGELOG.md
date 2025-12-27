# Changelog – Shani Bot
Alle relevanten Änderungen am Shani-Bot

[0.9.1] – 2025-12-27 (Update)
🛡️ Sicherheit & Voice-Feinschliff

• **Schutz des Squad-Limits:** User erhalten keine `manage_channels` Rechte mehr in Squad-Channels. Dies verhindert das manuelle Umgehen der 2er/3er Begrenzung.
• **Kanal-Status:** Ersteller können nun den Sprachkanal-Status setzen (z. B. "PvP", "Looten"), um ihre Aktivität anzuzeigen (`set_voice_channel_status`).
• **Moderation:** Squad-Besitzer behalten das Recht, andere User zu verschieben oder zu kicken (`move_members`).
• **Auto-Voice Open:** Einführung eines "Open Join"-Channels für Squads ohne Teilnehmerbegrenzung.

[0.9.0] – 2025-12-27
✨ System-Modernisierung & Feature-Erweiterung

• **Migration zu SQLite:** Komplette Umstellung der Server-Konfiguration von JSON auf eine robuste SQLite-Datenbank.
• **Auto-Voice 2.0:** Erweiterung des Squad-Systems auf wählbare Typen (2er, 3er).
• **Zentraler Status-Check:** Neuer Befehl `/shani_status` zeigt die gesamte Bot-Konfiguration auf einen Blick.
• **GitHub Integration:** Professionelle Repository-Struktur mit `README.md`, `.gitignore` und `requirements.txt`.

🛠️ Technische Optimierungen
• **Asynchrone Datenbankzugriffe:** Alle DB-Operationen laufen nun asynchron über Threads, um die Event-Loop nicht zu blockieren.
• **Performance-Schub für Twitch:** Umstellung auf eine persistente `aiohttp.ClientSession` und verbesserte Browser-Header für zuverlässigeres Scraping.
• **Professionelles Logging:** Einführung eines Datei-basierten Loggings (`bot.log`) statt einfacher Print-Ausgaben.
• **Echtzeit-Rename:** Automatische Umbenennung von Squad-Channels bei Namensänderungen der Besitzer.

🛡️ Fixes & Stabilität
• **Command-Cleanup:** Neues Skript `cleanup_commands.py` zur Behebung von doppelten Slash-Commands.
• **Intents:** Aktivierung des `message_content` Intents für bessere Command-Verarbeitung.
• **Voice-Stabilität:** Behebung von 404-Fehlern beim Löschen von Kanälen durch Entzerrung der Event-Logik.
• **Sicherheit:** `.gitignore` schützt nun `.env` und Datenbank-Dateien vor öffentlichem Upload.

---

[0.8.0] – 2025-12-26 Stand 14:00 Uhr
✨ Neues Feature: Raider-Setcard-System

• Einführung eines vollständigen Raider-Setcard-Systems für ARC Raiders
• Spieler können ein persönliches Profil erstellen und bearbeiten
• Fokus auf Squad-Matching ohne Preisgabe sensibler Daten

🛠️ Setcard-Funktionen (User)
• /setcard edit – interaktiver Editor (2-seitig, stabil)
• /setcard me – eigene Setcard anzeigen
• /setcard view – Setcard anderer Raider ansehen
• /setcard find – Raider-Suche mit Filtern (privat)
• Löschen der eigenen Setcard direkt im Editor

🛡️ Admin- & Mod-Funktionen
• /setcard set_channel – Setcard-Zielkanal festlegen
• /setcard mod_delete – Setcards von Usern entfernen
• Rechteprüfung & klare Fehlerausgaben bei fehlenden Channel-Rechten

⚙️ Technische Verbesserungen
• Umstellung auf SQLite mit WAL-Modus (stabil & performant)
• Vollständig überarbeitetes Discord-UI (keine Row-/Width-Crashes)
• Zwei-seitige View-Struktur für bessere Übersicht
• Sichere Interaction-Handling-Logik (kein „Bot denkt nach…“ mehr)
• Robustes Error-Handling & Debug-Logging

🔐 Datenschutz & Sicherheit
• Keine Verifizierung notwendig
• Keine externen Dienste
• Altersangaben nur als Altersgruppen
• Alle Angaben freiwillig und jederzeit änderbar

🐛 Fixes
• Mehrere Discord-UI-Crashes behoben (Row-/Width-/Options-Fehler)
• Slash-Command-Hänger („Anwendung reagiert nicht“) behoben
• Fehlende Channel-Rechte sauber abgefangen (403 Missing Access)

---

[0.7.0] – 2025-12-26
Added
• Konzept für Raider-Setcards (Spielerprofile)
• Planung für standardisierte Spielerinfos

---

[0.6.0] – 2025-12-26
Added
• Konzept „Missionshilfe“ für Anwender
• Fokus auf benutzerfreundliche Bot-Nutzung
• Vorbereitung einer Nutzer-Dokumentation

---

[0.5.0] – 2025-12-26
Changed
• Analyse des Twitch-Live-Systems
• Entfernung des Cooldown-Gedankens
• Neue Zieldefinition: Nur ein Live-Ping pro Stream

---

[0.4.0] – 2025-12-25
Fixed
• Analyse und Lösung von Discord-Permissions-Problemen
• Klärung von 403 Forbidden Fehlern

---

[0.3.0] – 2025-12-25
Added
• Automatische Erstellung von Sprachkanälen (Squads)
• Automatisches Verschieben des Channel-Erstellers

---

[0.2.0] – 2025-12-24
Added
• Öffentliche Bot-Applikation (Public Bot)
• OAuth2 / Invite-Flow geklärt
• Bot-Identität: Shani (Security & Missionshilfe)

---

[0.1.0] – 2025-12-24
Added
• Initialer Discord-Bot erstellt
• Betrieb auf Hetzner-Server
• Python-Virtualenv eingerichtet
