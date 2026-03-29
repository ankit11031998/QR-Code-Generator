# 🚀 Premium QR Code Generator

A modern, fast, and beautiful QR code generator built with **Flask** and **Python**. Features a sleek **Glassmorphism UI** with custom color customization!

![QR Code Generator](https://raw.githubusercontent.com/ankit11031998/QR-Code-Generator/main/static/preview.png) *(Note: Add your screenshot here!)*

## ✨ Features
- **Instant Generation:** Create QR codes for any URL in seconds.
- **Custom Colors:** Personalize your QR code with custom foreground and background colors.
- **Premium UI:** Modern, responsive design using Blur effects and Outfit typography.
- **Downloadable:** Saved as high-quality PNG images.
- **One-Click Deploy:** Ready for hosting on Render or Vercel.

## 🛠️ Technology Stack
- **Backend:** Python, Flask, `qrcode`, `Pillow`
- **Frontend:** HTML5, CSS3 (Glassmorphism), Google Fonts
- **Deployment:** Render (via `gunicorn`)

## 🚀 Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ankit11031998/QR-Code-Generator.git
   cd QR-Code-Generator
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## 📦 Deployment on Render
This project is configured with a `render.yaml` for instant deployment. 
- Just connect your GitHub repo to Render.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

---
Made with ❤️ by [ankit11031998](https://github.com/ankit11031998)
