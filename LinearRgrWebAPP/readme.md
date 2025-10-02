cat > README.md << 'EOF'
# FWI Prediction (Flask + scikit-learn)

A minimal Flask web app that predicts **Fire Weather Index (FWI)** from 10 inputs using a scikit-learn regression model with a `StandardScaler`.  
The UI is a compact, responsive grid so all fields are visible on one screen.

---

## ✨ Features
- Flask form → `/predict` (POST)
- Preprocessing with `StandardScaler`
- Lasso/Ridge (any sklearn regressor) for prediction
- Clean, no-scroll UI using CSS Grid

---


## 🛠️ Tech Stack
- **Python 3.x**
- **Flask** (cv2)
- **NumPy**
- **Pickle** 

---
## ✨ Output
<img width="1877" height="938" alt="webpage_linear model" src="https://github.com/user-attachments/assets/39f9f1dc-07de-4820-beef-326d98a4c639" />
