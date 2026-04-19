# 🛡️ WazuhGuard AI

### 🚀 AI-Powered SOC Automation | Detection • Response • Intelligence

![Banner](docs/banner.png)

---

## 🚨 Problem

Security Operations Centers (SOC) face:

* Alert fatigue from thousands of logs
* Slow manual incident response
* Lack of intelligent attack understanding

---

## 💡 Solution

**WazuhGuard AI** is an automated SOC system that:

* Detects attacks using Wazuh SIEM
* Sends real-time alerts via Telegram
* Automatically mitigates threats (IP blocking)
* Uses AI to explain attacks and suggest fixes

---

## 🎯 Key Outcomes

* ⚡ Reduced response time from minutes → seconds
* 🚫 Automatic threat mitigation
* 🧠 Intelligent attack explanation
* 📩 Instant alerting system

---

## 🧪 Lab Environment

| Component     | Technology Used             |
| ------------- | --------------------------- |
| Attacker      | Kali Linux                  |
| Target System | Ubuntu Server (Wazuh Agent) |
| SIEM          | Wazuh Manager               |
| Automation    | Python                      |
| Alerting      | Telegram Bot API            |
| AI Engine     | openrouter Ai               |

---

## 🧠 Architecture

![Architecture](docs/architecture.png)


🔍 Flow Diagram
```text
Attacker (Kali Linux)
        ↓
Wazuh Agent (Target System)
        ↓
Wazuh Manager (Detection Server)
        ↓
Python Alert Handler
        ↓
        ┌───────────────────────────────┐
        │ Can Auto Fix the Attack?      │
        └───────────────────────────────┘
             ↓ YES                         ↓ NO
 ┌────────────────────────┐      ┌────────────────────────────┐
 │ Auto Mitigation        │      │ Telegram Alert              │
 │ (Block IP / Fix Issue) │      │ (Manual Action Required)    │
 └────────────────────────┘      └────────────────────────────┘
             ↓                              ↓
             └──────────────┬───────────────┘
                            ↓
                  AI Analysis Engine
                            ↓
        ┌──────────────────────────────────────┐
        │ Explanation + Summary + Guidance     │
        │ (How to fix the issue manually)      │
        └──────────────────────────────────────┘
```

1. Attacker initiates an attack (e.g., brute force or network scan)  
2. Wazuh detects suspicious activity  
3. Python alert handler processes the event  
4. The system evaluates whether automatic mitigation is possible  

- If YES → the attack is blocked automatically  
- If NO → a Telegram alert is sent for manual intervention  

5. AI analyzes the attack and provides:
   - Explanation  
   - Summary  
   - Step-by-step remediation guidance 

---

## 🔁 Workflow

1. Attacker launches attack (SSH brute force / scan)
2. Wazuh detects malicious activity
3. Alert forwarded to Python handler
4. Telegram bot sends instant alert
5. System auto-blocks attacker IP
6. AI analyzes attack and generates explanation
7. If auto-fix fails → AI provides manual guidance

---
## 💣 Attack Simulation

### ⚡ Auto-Mitigation (Automatically Fixed)

These attacks can be detected and mitigated automatically by the system:

- 🔐 SSH Brute Force Attack  
- 🌐 Network Scanning (Nmap)  
- 🚫 Multiple Failed Login Attempts  

✔️ Detected by Wazuh  
✔️ Attacker IP blocked automatically (iptables)  
✔️ Telegram alert sent  
✔️ AI explanation generated  


### ⚠️ Non-Automatable Attacks (Manual Intervention Required)

These attacks require human intervention and AI guidance:

- 🔓 Privilege Escalation Attack  
- 🧬 Advanced Persistent Threats (APT)  
- ⚙️ Misconfigurations or Insider Attacks  

✔️ Detected by Wazuh  
✔️ Telegram alert sent  
❌ Auto-fix not possible  
🧠 AI provides:
   - Attack explanation  
   - Risk assessment  
   - Step-by-step remediation guidance  

---

### 🧠 Smart Handling Logic

The system intelligently decides:

- If the attack is simple → auto mitigation  
- If the attack is complex → alert + AI guidance  

This ensures no attack is ignored, even when automation is not possible.

---

### 📸 Demo

### 💣 Attack Simulation (Kali Linux)

![ip](docs/kali_ip.png) ![Attack](docs/attack.png)

---

### 🎯 Target System (Agent)

![ip](docs/Agent_ip.png)

---

### 🔍 Detection (Wazuh)

![wazuh](docs/detection.png)

---
### 📩  Alert (Telegram)

![Telegram](docs/TelegramAlert(2).png)

---
### 🚫 Auto Mitigation

![ip block](docs/ip_block.png)

---
### 🧠 AI Analysis

![Telegram](docs/Telegramalert.png)

---


### ⚠️ Non-Automatable Attacks (Manual Intervention Required)

Some attacks require human decision-making and cannot be safely automated.

Example:
- Privilege escalation
- Insider threats

![ip](docs/Agent_ip.png) ![ip](docs/agent.png) 

---

![privilage](docs/privilage.png)

---

## 🔄 Workflow

Attack → Detection → Alert → Response (Auto / Manual)

---

## 📊 Results


| Feature             | Status | Impact                          |
| ------------------- | ------ | ------------------------------- |
| Real-time Detection | ✅      | Immediate threat visibility     |
| Auto Response       | ✅      | Reduced response time to seconds|
| Telegram Alerts     | ✅      | Instant notification system     |
| AI Explanation      | ✅      | Better incident understanding   |
---

## 🛠️ Tech Stack

- Wazuh SIEM  
- Python  
- Linux (iptables)  
- Telegram Bot API  
- OpenRouter API (LLM-based analysis)  

---

## 💣 Attacks Simulated

- SSH Brute Force Attack  
- Privilege Escalation  
- Unauthorized Access Attempts  


---

## ⚙️ Installation

```bash
git clone https://github.com/Demonx911/AI-SOC-Automation.git
cd AI-SOC-Automation
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the automation script:

```bash
python3 main.py
```

## 🚨 Example Alert

```
🚨 ALERT: SSH Brute Force Detected  
IP: 192.168.1.10  
Action: Blocked  
Status: Mitigated  
```

---

## 🧠 AI Analysis Output

```
Attack Type: SSH Brute Force  
Risk Level: High  
Explanation: Multiple login attempts detected  
Recommendation: Use SSH keys, disable root login  
```

---

## 🧠 Skills Demonstrated

* SIEM (Wazuh)
* Incident Response Automation
* Threat Detection & Analysis
* Python Scripting
* API Integration
* AI in Cybersecurity

---

## ⚠️ Disclaimer

This project is for **educational and ethical cybersecurity research purposes only**.

---

## 👨‍💻 Author

**Asker (Demonx911)**
Cybersecurity Researcher | SOC Analyst | AI Security Enthusiast

---
