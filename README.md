<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b3d91,100:1ea7fd&height=200&section=header&text=Aravind%20Kumar%20Arunagiri&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Industrial%20AI%20Engineer%20%E2%80%A2%20Predictive%20Maintenance%20%E2%80%A2%20Physics-Informed%20ML&descAlignY=60&descSize=16" width="100%" alt="banner"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3200&pause=900&color=1EA7FD&center=true&vCenter=true&width=720&lines=Turning+vibration+%26+pressure+signals+into+early+warnings;PINNs+%C2%B7+Digital+Twins+%C2%B7+Predictive+Maintenance;Rotating+machinery+%C2%B7+Water+infrastructure+%C2%B7+Industrial+AI)](https://git.io/typing-svg)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aravind%20Kumar%20Arunagiri-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aravind-kumar-arunagiri-iaiml)
[![ISO 18436-1](https://img.shields.io/badge/ISO%2018436--1-Cat%20II%20Vibration%20Analyst-1f6feb?style=for-the-badge)](#-credentials)
[![Location](https://img.shields.io/badge/Bengaluru-India-orange?style=for-the-badge&logo=googlemaps&logoColor=white)](#)

</div>

---

## 👋 About Me

I'm an **Industrial AI Engineer** with **8+ years** across mechanical and aeronautical engineering, signal processing and machine learning. I build systems that listen to machines: **acquire the signal, understand the physics, and predict the failure before it happens.**

- 🏭 Building predictive-maintenance systems for **pumping stations** on the **iPUMPNET** platform at **Pump Academy Pvt. Ltd.**
- 🚰 Production deployments for water utilities: **BWSSB (Bengaluru)** and **BMC (Mumbai)**
- 🔬 Focus: the intersection of **signal processing × machine learning**, meaning ML *on* vibration, MCSA/ESA, acoustic and process data
- 🧠 Exploring **physics-informed neural networks**, **digital twins** and **RAG-based diagnostic assistants** for industrial fault diagnosis

---

## 🛠️ What I Work On

| Area | What it looks like in practice |
|---|---|
| **Condition Monitoring** | FFT / spectral analysis, vibration diagnostics, MCSA & ESA for motor health, acoustic emission |
| **Predictive Maintenance** | Failure prediction, health index, RUL estimation, anomaly detection on rotating machinery and hydraulic systems |
| **Physics-Informed ML** | Multi-Task PINNs, LSTM / Prophet forecasting, digital-twin modelling of pumps |
| **Pump Station Optimisation** | Q-H curve analysis, SCADA-based efficiency evaluation, energy-optimal pump scheduling |
| **Diagnostic Intelligence** | Knowledge layers and RAG pipelines that turn model output into readable diagnostic reports |
| **Data Engineering** | DAQ ingestion (TDMS), cleaning and ETL pipelines, MySQL storage |

---

## 🧰 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

**Signal & domain:** FFT · STFT · Shannon entropy · envelope analysis · MCSA / ESA · acoustic emission · ISO 13374 · Q-H curves · SCADA
**Modelling:** LSTM · Prophet · PINNs · autoencoders · anomaly detection · health index & RUL

---

## 🚀 Featured Project

### 🔧 [AODD Pump Condition Monitoring: FFT and Entropy Analysis](https://github.com/AAravind-sys/REPO-NAME)

Analysis notebooks for an **air-operated double diaphragm (AODD) pump** test setup. Because the pump is a pulsating machine, raw pressure signals are converted to frequency spectra and the energy in the **failure-related frequency band** is tracked over running hours. Data comes from bench tests with deliberately induced diaphragm cracks on two pumps.

```text
 DAQ (.tdms) ─► timestamps ─► clean + MySQL ─► running-state filter ─► windowed FFT ─► spectra + band energy
                                                                     └─► Shannon entropy (2nd health indicator)
```

`Python` `FFT` `Shannon entropy` `MySQL` `TDMS` `Jupyter`

---

## 🏗️ Selected Industrial Work

- **BMC Sewage Water:** LSTM fault identification, knowledge layer and a RAG-based AI diagnosis tool with continuous model improvement
- **BMC Water:** energy optimisation, model-based pump scheduling, and hydraulic / electrical / mechanical analytics
- **BWSSB Cauvery Water Supply Scheme:** combinatorial pump scheduling to minimise specific power consumption across pump combinations
- **Dover India:** AODD pump failure prediction, hydraulic cylinder seal failure via acoustic data, winch gear failure via vibration
- **Lucas TVS:** ESA-based motor health monitoring

---

## 🎓 Credentials

- 🏅 **ISO 18436-1 Category II**, Vibration Analyst
- 📊 **GATE AIR 444**
- 🎓 **ME**, Engineering Design · **BE**, Aeronautical Engineering
- 🎤 Research presented at **IEEMA 2026 (Mumbai)** and **AWWA India 2025**
- 📄 Co-authored preprint on **physics-informed ML for pump health monitoring**

---

## 🌱 Currently Building

- 🔹 A cleaner, deployable **pump-health pipeline** (containerised, served through an API)
- 🔹 Public, documented repos for **PINN-based pump digital twins**, **industrial fault-diagnosis RAG**, and an **ESA / vibration signal toolkit**
- 🔹 Building a small language model from scratch to understand the stack end to end

---

## 📊 GitHub Stats

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=AAravind-sys&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="stats"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AAravind-sys&layout=compact&theme=tokyonight&hide_border=true" alt="top languages"/>

</div>

---

## 🤝 Let's Connect

I'm always happy to talk about **predictive maintenance, vibration analytics, physics-informed ML and water-infrastructure AI**.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aravind-kumar-arunagiri-iaiml)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1ea7fd,100:0b3d91&height=100&section=footer" width="100%" alt="footer"/>

</div>
