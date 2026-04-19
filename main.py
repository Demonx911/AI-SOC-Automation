# ================================
# WazuhGuard AI - SOC Automation
# ================================

import re
import time
import subprocess
import requests

# ========= CONFIG =========
LOG_FILE = "auth.log"   # your log file

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"

AUTO_MODE = True   # True = auto block, False = manual alert
# ==========================


# 📩 Send Telegram Alert
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except:
        print("[!] Telegram send failed")


# 🚫 Block IP
def block_ip(ip):
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        print(f"[+] Blocked IP: {ip}")
    except:
        print("[!] Failed to block IP")


# 🧠 AI Analysis (simple formatted)
def ai_analysis(attack, ip):
    return f"""
🧠 AI Analysis

Attack: {attack}
IP: {ip}
Risk: HIGH

Explanation:
Suspicious activity detected from this IP.

Recommendation:
- Disable root login
- Use SSH keys
- Monitor logs regularly
"""


# 🔍 Detect Attacks
def detect_attack(line):
    
    # SSH Brute Force
    if "Failed password" in line:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            return "SSH Brute Force", match.group(1)

    # Port Scan (basic detection)
    if "nmap" in line.lower():
        return "Port Scan", "unknown"

    return None, None


# ================= MAIN =================
def main():
    print("[+] WazuhGuard AI started...")

    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # move to end of file

        while True:
            line = f.readline()

            if not line:
                time.sleep(1)
                continue

            attack, ip = detect_attack(line)

            if attack:
                print(f"[!] Detected: {attack} from {ip}")

                # Decision
                if AUTO_MODE:
                    block_ip(ip)
                    action = "Blocked"
                else:
                    action = "Manual Action Required"

                # 🚨 Alert
                alert_msg = f"""
🚨 ALERT: {attack}
IP: {ip}
Action: {action}
"""
                send_telegram(alert_msg)

                # 🧠 AI Analysis
                ai_msg = ai_analysis(attack, ip)
                send_telegram(ai_msg)


# Run
if __name__ == "__main__":
    main()
