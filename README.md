# ehima-Securenet
AI-powered Wireshark Traffic Analyzer For 3MTT Showcase
# Ehima SecureNet 🔐  
AI-Powered Network Traffic Analyzer using Wireshark Logs  

## 👩🏽‍💻 Built by: Ehi Mercy Adams  
3MTT Cohort 3 | Cybersecurity Track  

---

## 📌 Project Overview

Ehima SecureNet is a lightweight, beginner-friendly tool that uses artificial intelligence to analyze network traffic logs captured via Wireshark. It identifies suspicious patterns and flags potentially malicious behavior like brute-force attacks, data exfiltration, or unusual IP activity — all using open-source tools.

This project was built as part of the 3MTT June Showcase to demonstrate how AI can be used in practical cybersecurity workflows.

---

## 🚨 Problem Statement

Small businesses and individuals often struggle to monitor their network traffic effectively due to lack of tools, time, or technical knowledge. Most threats go unnoticed until damage is done.

---

## ✅ Solution

Ehima SecureNet bridges that gap by using:
- Wireshark to capture live traffic
- Python to parse and preprocess logs
- Scikit-learn to classify traffic as either normal or suspicious
- Matplotlib (optional) to visualize flagged connections

---

## 🧠 How AI Is Used

A machine learning model (Logistic Regression) was trained on labeled traffic datasets to recognize patterns of suspicious behavior. When a new `.pcap` log is loaded, the model analyzes fields like source IP, port, packet size, and frequency to predict whether the traffic is benign or malicious.

---

## 🧰 Tools & Technologies

- 🐍 Python 3.x  
- 📡 Wireshark  
- 📦 Scikit-learn  
- 📊 Pandas, NumPy  
- 📈 Matplotlib (for optional visualization)

---

## 📁 Project Structure
