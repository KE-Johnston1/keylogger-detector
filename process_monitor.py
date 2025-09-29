def scan_processes():
    suspicious_keywords = ["keylogger", "logger", "stealth", "capture"]
    flagged = []

    try:
        with open("logs/ps.log", "r") as file:
            lines = file.readlines()
            for line in lines:
                for keyword in suspicious_keywords:
                    if keyword in line.lower():
                        flagged.append(line.strip())

        if flagged:
            print("[!] Suspicious processes detected:")
            for entry in flagged:
                print(f"    {entry}")
        else:
            print("[✓] No suspicious processes found")

    except FileNotFoundError:
        print("[!] ps.log not found")

if __name__ == "__main__":
    scan_processes()
