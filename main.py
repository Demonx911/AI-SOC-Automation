# WazuhGuard AI - SOC Automation Script
# Detects attacks, sends alerts, blocks IP, and provides AI analysis

import re
import subprocess
import requests

# ================= CONFIG =================
LOG_FILE = "auth.log"  # change if needed

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

AUTO_MODE = True  # True = auto block, False = alert only

OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"

# ==========================================

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def block_ip(ip):
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        return True
    except:
        return False

def ai_analysis(attack_type, ip):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"Explain {attack_type} attack from IP {ip} and give prevention steps"
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except:
        return "AI analysis failed"

def detect_attack(line):
    # Simple SSH brute force detection
    if "Failed password" in line:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            return "SSH Brute Force", match.group(1)

    return None, None

# ================= MAIN =================

def main():
    print("[+] Monitoring logs...")

    with open(LOG_FILE, "r") as f:
        for line in f:
            attack, ip = detect_attack(line)

            if attack:
                print(f"[!] Detected {attack} from {ip}")

                if AUTO_MODE:
                    block_ip(ip)
                    action = "Blocked"
                else:
                    action = "Manual action required"

                alert_msg = f"""
🚨 ALERT: {attack}
IP: {ip}
Action: {action}
"""

                send_telegram(alert_msg)

                ai_result = ai_analysis(attack, ip)

                send_telegram(f"🧠 AI Analysis:\n{ai_result}")

# Run
if __name__ == "__main__":
    main()
