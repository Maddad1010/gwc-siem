<img width="1536" height="1024" alt="ChatGPT Image Sep 29, 2025, 02_16_49 AM" src="https://github.com/user-attachments/assets/17e7065e-791d-473f-9066-cdbde083e32e" />

# gwc-siem 🛡️

A **mini-SIEM** for home labs and Hacktoberfest contributions. Parses common logs (auth, nginx), detects simple security events (SSH brute force, HTTP 5xx bursts), stores alerts in SQLite, and exposes them via **FastAPI API**, **CLI**, and a **lightweight dashboard**.

---

## ✨ Features

* **Log ingestion:** Upload `auth.log` or Nginx access logs via API or UI
* **Parsers:** Convert raw lines → structured `Event` objects
* **Detections:** Sliding-window brute-force & 5xx-burst rules (thresholds configurable in YAML)
* **Storage:** SQLite for easy portability
* **Dashboard:** Static HTML + JS fetch alerts from API
* **CLI:** Local batch scanning for sample logs or offline use

---

## 🚀 Quickstart

### 1. Clone & Setup

```bash
git clone https://github.com/<your-username>/gwc-siem.git
cd gwc-siem
```

---

### 🪟 Windows Setup Guide

If you’re on **Windows**, follow these steps instead of the Linux/macOS commands:

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/gwc-siem.git
   cd gwc-siem
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   (If `requirements.txt` is missing, you can manually install common dependencies like FastAPI and Uvicorn)

   ```bash
   pip install fastapi uvicorn sqlite-utils
   ```

4. **Run the API**

   ```bash
   uvicorn api.main:app --reload
   ```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)
Upload sample logs from `sample_data/` using the upload form.
Alerts will appear in a table below.

---

### 2. Use CLI

```bash
python cli/app.py --file sample_data/auth.log --kind auth
```

This parses, detects alerts, and writes them to `seclog.db`.
You can fetch them via API:

```bash
curl http://127.0.0.1:8000/alerts?limit=10 | jq
```

---

## 🧩 Core Components

| Component                           | Description                            |
| ----------------------------------- | -------------------------------------- |
| **API (`api/`)**                    | `/ingest`, `/alerts`, `/health`        |
| **Parsers (`core/parsers/`)**       | Auth + Nginx → `Event`                 |
| **Detections (`core/detections/`)** | Brute force + HTTP 5xx burst → `Alert` |
| **Storage (`storage/`)**            | SQLite + helper functions              |
| **Web (`web/index.html`)**          | Upload form + table renderer           |
| **CLI (`cli/`)**                    | Batch scanning tool                    |

---

## 🧑‍💻 Contributing

1. **Fork & clone** the repository
2. **Create a new branch** for your contribution
3. **Set up local environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install fastapi uvicorn pytest sqlite-utils
   ```
4. **Run tests**

   ```bash
   pytest -q
   ```
5. **Open a Pull Request** referencing an issue (see [CONTRIBUTING.md](CONTRIBUTING.md))

---

## 📌 Roadmap

* [ ] Apache access log parser
* [ ] GeoIP blocklist rule
* [ ] Prometheus `/metrics` endpoint
* [ ] Docker Compose example with log mounts
* [ ] Alert notifiers (Slack, Discord)

---

## 🛡️ Security

See [SECURITY.md](SECURITY.md).
For severe issues, please disclose privately.

---

## 📄 License

MIT © 2025 ghostmkg

---

## 📢 Join Our Community

Be a part of our growing community and stay connected 🚀

* 🗨️ [Join us on Discord](https://discord.gg/YMJp48qbwR)
* 📢 [Join our Telegram](https://t.me/gwcacademy)
* 💼 [Follow our LinkedIn Page](https://www.linkedin.com/company/gwc-academy/)
* 💬 [Join our WhatsApp Community](https://whatsapp.com/channel/0029ValnoT1CBtxNi4lt8h1s)
* 📺 [Subscribe on YouTube](https://www.youtube.com/c/growwithcode?sub_confirmation=1)
* 🐦 [Follow on Twitter](https://x.com/goshwami_manish)
* 📸 [Follow on Instagram](https://www.instagram.com/grow_with_code)

---

## ☕ Support the Project

If you like this project and want to support future development, consider buying me a coffee:

<a href="https://www.buymeacoffee.com/mgoshwami1c">
  <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="mgoshwami1c">
</a>

<br><br/>
