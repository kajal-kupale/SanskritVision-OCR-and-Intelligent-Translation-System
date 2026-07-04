
<div align="center">

# ✨SanskritVision
### AI-Powered Sanskrit OCR & Intelligent Translation System

<p align="center">
An AI-powered web application for extracting Sanskrit text from images, translating it into multiple languages, analyzing translation history, and generating intelligent reports.
</p>


</div>

---

# 📖 Project Description

**SanskritVision** is an AI-powered web application which is the system combines **Optical Character Recognition (OCR)**, **Artificial Intelligence**, and **Multilingual Translation** into one intelligent platform.

Users can upload Sanskrit text images or directly paste Sanskrit text, translate the extracted content into multiple languages, maintain translation history, visualize analytics, and generate downloadable reports through a modern web interface.

---

# 🎯 Project Objectives

- 📜 Extract Sanskrit text from images using OCR
- 🌍 Translate Sanskrit into multiple languages
- 🤖 Integrate Artificial Intelligence for better translation quality
- 📊 Analyze translation activities through interactive charts
- 📁 Store translation history
- 📄 Generate downloadable analysis reports
- 💻 Provide a clean and user-friendly interface

---

# 👥 Target Users
- Students: Learn and understand Sanskrit literature.
- Faculty & Researchers: Preserve ancient Sanskrit documents.
- Educational Institutions: AI-assisted language education.
- Sanskrit Enthusiasts: Improve accessibility to Sanskrit knowledge.
---

## ⚙️ Core Working

### 📷 OCR Text Extraction
Extracts printed Sanskrit text from uploaded images using **Tesseract OCR** and image preprocessing techniques for accurate text recognition.

---

### 🤖 AI Translation Engine
Integrates the **Google Gemini API** to perform intelligent multilingual translation, transliteration, and contextual Sanskrit text understanding.

---

### 🌐 Multilingual Processing
Processes Sanskrit text from both image uploads and manual input, translating it into multiple target languages while preserving contextual meaning.

---

### 💾 Database Management
Stores user profiles, translation history, OCR records, and analytics data securely using **MySQL** with **SQLAlchemy ORM**.

---

### 📊 Analytics & Reporting
Generates interactive dashboards with language usage statistics, translation activity, OCR insights, and downloadable PDF analysis reports.

---

### 🔐 User Authentication
Provides secure registration, login, profile management, session handling, and user-specific translation history using Flask authentication.

---

### 💻 Responsive Web Interface
Built with **Flask, HTML, CSS, JavaScript, and Jinja2**, offering an intuitive interface for OCR, translation, analytics, and history management across devices.

# 🖥️ System Modules and Generated Outputs

## 🔐 Login Page

![Login Page](screenshots/OCRlogin.png)

**Description:** Secure user authentication interface with email and password validation for accessing the SanskritVision platform.

---

## 📝 Register Page

![Register Page](screenshots/OCRregister.png)

**Description:** User registration page for creating a new account with secure credential management and profile initialization.

---

## 🏠 Dashboard

![Dashboard](screenshots/OCRhome.png)

**Description:** Central dashboard providing quick navigation to OCR, translation, analytics, history, profile, and reporting modules.

---

## 📷 OCR Image Translation

![OCR Image Translation](screenshots/OCRimage.png)

**Description:** Upload Sanskrit text images to extract text using Tesseract OCR and perform AI-powered multilingual translation.

---

## 🌐 AI Translation

![AI Translation](screenshots/OCRtranslate.png)

**Description:** Translate Sanskrit text entered manually into multiple languages using the Gemini API with intelligent language processing.

---

## 📜 Translation History

![Translation History](screenshots/OCRhistory.png)

**Description:** View and search previously translated records with source type, language, timestamp, and translation details.

---

## 📊 Analytics Dashboard

![Analytics Dashboard](screenshots/OCRAnalysis.png)

**Description:** Interactive dashboard displaying OCR usage, language distribution, translation statistics, and downloadable analytical reports.

---

## 👤 User Profile

![User Profile](screenshots/OCRprofile.png)

**Description:** Personalized user profile displaying account information and quick access to translation activities and system features.

---

## 🛠️ Technology Stack

### 🎨 Frontend

![HTML5](https://img.shields.io/badge/HTML5-Latest-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Latest-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Jinja2](https://img.shields.io/badge/Jinja2-Template-B41717?style=flat-square&logo=jinja&logoColor=white)

### ⚙️ Backend

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)

### 🤖 OCR & Artificial Intelligence

![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Tesseract OCR](https://img.shields.io/badge/Tesseract-OCR-4285F4?style=flat-square)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-8E75FF?style=flat-square&logo=google&logoColor=white)
![Deep Translator](https://img.shields.io/badge/Deep--Translator-Latest-34A853?style=flat-square)

### 📊 Reports & Visualization

![Chart.js](https://img.shields.io/badge/Chart.js-4.x-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-Latest-FF5722?style=flat-square)

### 💻 Development Tools

![Visual Studio Code](https://img.shields.io/badge/VS_Code-Latest-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-2.x-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Latest-181717?style=flat-square&logo=github&logoColor=white)

---


# 💻 System Requirements

## Software Requirements

- Python 3.13
- Visual Studio Code
- MySQL Server
- Tesseract OCR
- 8GB RAM (16GB recommended)



---

# ⚙️ Quick Setup

```bash
# Clone Repository
git clone https://github.com/kajal-kupale/SanskritVision-OCR-and-Intelligent-Translation-System.git

# Open Project Directory
cd SanskritVision-OCR-and-Intelligent-Translation-System

# Create Virtual Environment
python -m venv venv

# Activate Virtual Environment (Windows)
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Configure MySQL Database and Gemini API Key

# Run Application
python app.py
```

🌐 Open your browser and visit:

```
http://127.0.0.1:5000
```
---
>>>>>>> 8bef97af8e35eba6b1e8b5c3ab74b7d509005720
