# ⚡ Screen OCR Auto-Clicker

This is a Python-based automation script that uses **Tesseract OCR**, **OpenCV**, and **PyAutoGUI** to detect text (numbers) from a specific area of the screen in real-time.  
When a target number (default `0`) appears, the script automatically triggers a mouse click.  
It’s ideal for automation, quick response systems, and visual screen monitoring tasks.

---

## 🧩 Requirements

- Python 3.8 or higher  
- Tesseract OCR (installed and accessible from your system)  

### Python Dependencies

Install the required packages with:

```bash
pip install pillow pytesseract pyautogui opencv-python numpy mouse
