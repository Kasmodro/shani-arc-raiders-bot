# 🔐 Permissions Overview – Shani Discord Bot

This document explains why Shani requires certain Discord permissions and how they are used.

---

## 🎙 Voice & Squad Management

Required for dynamic squad channels and auto-voice features:

- **Manage Channels** (create / delete / rename squad channels)
- **Move Members** (move users into their squad channels)
- **Connect / Speak** (voice participation if required)

---

## 🧩 Interactive UI & Slash Commands

Required for modern Discord interactions:

- **Send Messages**
- **Embed Links**
- **Read Message History**
- **Add Reactions**

---

## 🧵 Threads, Forums & Setcards

Used for player profiles, forum posts, and cleanup:

- **Manage Threads**
- **Manage Messages** (bot-owned messages only)

---

## 🛡 Security Notes

- ❌ Administrator permission is **NOT required**
- ✅ Permissions can be limited per channel or category
- 🔐 The bot only manages content it creates itself
- 🔑 Secrets (tokens) are never stored in the repository

---

## ⚠ Common Permission Issues

- **Bot cannot delete channels** → missing **Manage Channels**
- **Bot cannot move users** → missing **Move Members**
- **Slash commands not responding** → missing **Send Messages** or **Read Message History**

---

If you encounter issues, verify both **server-level** and **channel-level** permissions.
