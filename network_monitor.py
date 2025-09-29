import os

def scan_network():
    suspicious_ips = ["185.12.45.67", "203.0.113.99"]
    flagged = []

    log_path = "logs/netstat.log"
    output_path = "logs/network_output.log"

    if not os.path.exists(log_path):
        print(f"[!] Network log not found: {log_path}")
        return

    with open(log_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            for ip in suspicious_ips:
                if ip in line:
                    flagged.append(line.strip())

    with open(output_path, "w") as out:
        if flagged:
            out.write("[!] Suspicious outbound connections detected:\n")
            for entry in flagged:
                out.write(f"    {entry}\n")
            print(f"[✓] {len(flagged)} suspicious connections saved to {output_path}")
        else:
            out.write("[✓] No suspicious outbound connections found\n")
            print(f"[✓] No suspicious connections found. Logged to {output_path}")

if __name__ == "__main__":
    scan_network()
