# 📊 Central Limit Theorem (CLT) – Simulation & Visualization  

This project demonstrates the **Central Limit Theorem (CLT)** using Python simulations, animations, and visualizations.  
It was developed during my **FOSSIP Summer Internship 2025** under the Faculty of Science, MSU Baroda.

The goal of this project is to show how the distribution of **sample means** approaches a **normal distribution** as the **sample size increases**, even when the original population is not normal.

---

## 🔍 **Overview**
The Central Limit Theorem states that:

> *When we draw repeated random samples of size n from any population with mean μ and variance σ², the distribution of the sample mean approaches a normal distribution as n → ∞.*

This project uses:
- Binomial sampling  
- Simulation of many sample means  
- Animation to visualize how the distribution evolves  
- Comparison with the theoretical normal curve  

---


---

## 🎥 **CLT Animation (Python Script)**  
The animation shows how the histogram of sample means becomes smoother and more normal as sample size increases.

Key features:
- Repeated sampling from a **Binomial(n=10, p=0.5)** distribution  
- Sample sizes: **5, 10, 30, 100, 500**  
- Overlays the **theoretical normal distribution**  
- Updated frame-by-frame animation  

---

## 🧮 **Key Concepts Demonstrated**

### ✔ Sampling distribution  
The distribution of sample means is computed from repeated binomial samples.

### ✔ Convergence to normality  
With larger sample sizes, the sampling distribution closely matches a normal curve.

### ✔ Reduced variance  
Variance of sample mean:  
\[
\sigma_{\bar{X}}^2 = \frac{\sigma^2}{n}
\]

### ✔ Visual intuition  
Histograms + normal curve overlays make it easy to see CLT in action.

---

## 🚀 **How to Run the Animation**

### **Run using Python**
1. Install required libraries:
```bash
pip install numpy matplotlib scipy

###*Run the script*###
python clt_animation.py


