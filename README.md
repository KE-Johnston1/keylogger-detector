#  Keylogger Detection Toolkit

A modular, scenario-driven toolkit for detecting keylogger activity across multiple system layers. Built for clarity, transparency, and recruiter-readiness.

---

##  Quick Start

Clone the repo and run any module from the terminal:

```bash
python process_monitor.py
python startup_check.py
python network_monitor.py
python keystroke_scanner.py
python report_builder.py

Each module scans a specific log file and saves results to logs/.
Modules Overview
Module	Purpose	Output File
process_monitor.py	Flags suspicious running processes	logs/output.log
startup_check.py	Detects auto-run programs with keylogger traits	logs/startup_output.log
network_monitor.py	Scans outbound connections to suspicious IPs	logs/network_output.log
keystroke_scanner.py	Parses keystroke logs for stealthy behavior	logs/keystroke_output.log
report_builder.py	Combines all results into one summary	logs/final_report.log

Scenario
You suspect a keylogger is active on your system. This toolkit helps you investigate across process activity, startup entries, outbound connections, and keystroke behavior—then summarizes findings in one report.

Sample Logs
Each module uses a mock .log file stored in logs/. These simulate real-world data and are easy to swap out for live logs.

