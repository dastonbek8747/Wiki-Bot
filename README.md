# 📚 Wiki-Bot — Telegram Wikipedia Boti

**aiogram** asosida yozilgan Telegram bot: yuborilgan matn bo'yicha o'zbek tilidagi Wikipedia maqolasini topib beradi.

---

## ✨ Imkoniyatlar

- 🔎 **Qidiruv:** har qanday matn → Wikipedia maqolasi xulosasi
- 🇺🇿 **O'zbek tili:** `wikipedia.set_lang("uz")`
- 🆘 **/start** komandasi: yordam xabari
- 🛡 **Xato boshqaruvi:** maqola topilmasa yoki bir nechta mos kelsa — tushunarli javob

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| **Python 3.10+** | Asosiy til |
| **aiogram 3.x** | Telegram bot |
| **wikipedia** | Wikipedia API |
| **python-dotenv** | Token boshqaruvi |

---

## ⚙️ O'rnatish

```bash
git clone https://github.com/dastonbek8747/Wiki-Bot.git
cd Wiki-Bot
python -m venv venv
source venv/bin/activate
pip install aiogram wikipedia python-dotenv
```

Tokenni sozlang:

```bash
cp .env.example .env
```

```env
BOT_TOKEN=123456:ABC...
```

> 🔒 Tokenni **kodga yozmang** — faqat `.env` orqali.

---

## ▶️ Ishga tushirish

```bash
python bot.py
```

Telegram'da botga istalgan so'z yozing — maqola xulosasini oladi.

---

## 📁 Loyiha tuzilishi

```
Wiki-Bot/
├── bot.py             # Bot handler'lari
├── config.py          # Token yuklash
├── wiki.py            # Wikipedia namunasi
├── Pipfile
├── tests/
└── .env.example
```

---

## 📄 Litsenziya

Litsenziya ko'rsatilmagan.
