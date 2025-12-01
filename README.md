<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=000000,300000,ff0000&height=220&section=header&text=ThreatVision&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Real-Time%20Cyber%20Threat%20Intelligence%20Map&descAlignY=60&descSize=20" width="100%"/>

  <p>
    <img src="https://img.shields.io/badge/Python-Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
    <img src="https://img.shields.io/badge/Frontend-LeafletJS-199900?style=for-the-badge&logo=leaflet&logoColor=white" />
    <img src="https://img.shields.io/badge/Data-Live_Feed-red?style=for-the-badge" />
  </p>

</div>

---

### 👁️ About The Project
**ThreatVision** is a Cyber Threat Intelligence (CTI) dashboard that visualizes global attacks in real-time. 

Unlike static maps, this tool fetches **live threat data** from open-source security feeds, geolocates the attacker's IP address, and plots the attack vector on an interactive dark-mode 3D map.

* **🔴 Live Data:** Pulls real-time SSH Brute Force attackers from `Blocklist.de`.
* **🗺️ Geolocation:** Converts raw IPs into GPS coordinates using the `IP-API` service.
* **⚡ High Performance:** Uses an asynchronous frontend loop to update the map without page reloads.

---

### 📡 Technical Architecture

| Component | Tech Used | Description |
| :--- | :--- | :--- |
| **Backend** | `Python (Flask)` | Fetches & filters threat feeds; serves JSON API. |
| **Frontend** | `HTML5 / JS` | Renders the dashboard and polls the API. |
| **Mapping** | `Leaflet.js` | Renders the interactive "Dark Matter" world map. |
| **Intel Source** | `Blocklist.de` | Provides the raw list of malicious IPs. |

---

### ⚙️ Installation & Usage

#### 1. Clone the Repository
```bash
git clone [https://github.com/devnand-47/ThreatVision.git](https://github.com/devnand-47/ThreatVision.git)
cd ThreatVision
