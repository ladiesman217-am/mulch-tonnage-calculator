# 🌿 Mulch Tonnage Calculator

This Streamlit app helps you quickly convert **square feet of 3-inch mulch coverage** into **tons of material** — ideal for landscape estimating and supply planning.

---

## ⚙️ How It Works
1. Enter the total **area in square feet**.  
2. Choose your mulch type:
   - Light (~400 lb/yd³)
   - Medium (~500 lb/yd³)
   - Heavy (~600 lb/yd³)
3. The calculator instantly shows the **tons of mulch required** for a 3-inch depth.

---

## 🧮 Formula
\[
\text{Tons} = \frac{\text{Area (sq ft)} \times 0.25 \text{ ft}}{27} \times \frac{\text{Weight per yd³}}{2000}
\]

Or simplified:
> **Tons = Area ÷ 432 (for medium mulch)**

---

## 🚀 Run the App Locally
If you want to run it on your computer:
```bash
pip install streamlit
streamlit run mulch_tonnage_calculator.py
