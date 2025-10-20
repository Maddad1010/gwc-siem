"""
Simple contributor script for gwc-siem.
Created by: Shreekant-Bharti
Date: October 2025
Purpose: Adds a readable contribution log for transparency.
"""

def contribution_log():
    contributors = [
        {"name": "Shreekant-Bharti", "role": "Open Source Contributor", "feature": "Documentation or usability improvement"}
    ]
    
    print("GWC-SIEM Contribution Log")
    print("--------------------------")
    
    for c in contributors:
        print(f"Contributor: {c['name']}")
        print(f"Role: {c['role']}")
        print(f"Feature: {c['feature']}")
        print("--------------------------")

if __name__ == "__main__":
    contribution_log()
