# 🚀 Autonomous AI Audiobook Production Pipeline (2026)

A production-ready AI backend system for automated market research, outline creation, TTS optimization, and localization of audiobooks.

## 📋 System Overview
This system automates the entire lifecycle of an audiobook release in four distinct phases:
1. **Niche Research:** Autonomous market analysis to identify trend topics with high willingness-to-pay (saved in `ergebnis.txt`).
2. **Structural Design:** Generation of a publisher-ready chapter structure (`01_Gliederung.txt`).
3. **Content Scripting:** Production of fluent, engaging narrations specifically optimized for Text-to-Speech (TTS) engines like Play.ht (`02_Skript_DE.txt` – completely free of disruptive stage directions, brackets, or formatting errors).
4. **Global Localization:** Fully automated translation of the scripts into core global markets, including English (`03_Skript_EN.txt`) and Spanish (`04_Skript_ES.txt`), while preserving the natural narrative rhythm.

## 🛠️ Technical Highlights & Engineering Approach
* **Robust Architecture:** Fully compatible with modern Python versions (including early Python 3.14 pre-releases).
* **Fault-Tolerant API Routing:** Leverages the hybrid `g4f` framework for stable, registration-free API handling without the risk of API-key rate limits or blocks.
* **Platform-Independent Encoding:** Safeguarded against Windows-specific character encoding errors (umlauts) through consistent UTF-8 file I/O handling.

## 💻 Installation & Execution
```bash
# 1. Clone or download this repository
# 2. Install the required dependency
pip install g4f

# 3. Run the pipeline
python agent_test.py