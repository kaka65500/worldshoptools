#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════╗
║         WORLDSHOPTOOLS - Ethical Hacking Tool        ║
║              Professional Security Suite             ║
╚══════════════════════════════════════════════════════╝
"""

import os
import sys
from modules.scanner import NetworkScanner
from modules.encoder import Encoder
from modules.password import PasswordTools
from modules.web import WebTools
from modules.utils import colors, clear_screen, print_banner

def display_menu():
    """Affiche le menu principal"""
    clear_screen()
    print_banner()
    print(f"\n{colors.CYAN}{'='*55}{colors.RESET}")
    print(f"{colors.YELLOW}[1]{colors.RESET} {colors.GREEN}Network Scanner{colors.RESET} - Scan ports, DNS, Whois")
    print(f"{colors.YELLOW}[2]{colors.RESET} {colors.GREEN}Encoder/Decoder{colors.RESET} - Hash, Base64, ROT13, URL")
    print(f"{colors.YELLOW}[3]{colors.RESET} {colors.GREEN}Password Tools{colors.RESET} - Generator, Strength Check")
    print(f"{colors.YELLOW}[4]{colors.RESET} {colors.GREEN}Web Tools{colors.RESET} - Headers, URL Validator")
    print(f"{colors.YELLOW}[5]{colors.RESET} {colors.RED}Exit{colors.RESET}")
    print(f"{colors.CYAN}{'='*55}{colors.RESET}\n")

def network_menu():
    """Menu Network Scanner"""
    while True:
        clear_screen()
        print_banner()
        print(f"\n{colors.CYAN}=== NETWORK SCANNER ==={colors.RESET}\n")
        print(f"{colors.YELLOW}[1]{colors.RESET} Port Scanner")
        print(f"{colors.YELLOW}[2]{colors.RESET} DNS Lookup")
        print(f"{colors.YELLOW}[3]{colors.RESET} Whois Lookup")
        print(f"{colors.YELLOW}[4]{colors.RESET} Back to Menu\n")
        
        choice = input(f"{colors.GREEN}Choose option: {colors.RESET}").strip()
        
        if choice == '1':
            scanner = NetworkScanner()
            scanner.port_scan()
        elif choice == '2':
            scanner = NetworkScanner()
            scanner.dns_lookup()
        elif choice == '3':
            scanner = NetworkScanner()
            scanner.whois_lookup()
        elif choice == '4':
            break
        else:
            print(f"{colors.RED}Invalid option!{colors.RESET}")
            input("Press Enter to continue...")

def encoder_menu():
    """Menu Encoder/Decoder"""
    while True:
        clear_screen()
        print_banner()
        print(f"\n{colors.CYAN}=== ENCODER/DECODER ==={colors.RESET}\n")
        print(f"{colors.YELLOW}[1]{colors.RESET} Base64 Encode/Decode")
        print(f"{colors.YELLOW}[2]{colors.RESET} Hash (MD5, SHA1, SHA256)")
        print(f"{colors.YELLOW}[3]{colors.RESET} ROT13 Cipher")
        print(f"{colors.YELLOW}[4]{colors.RESET} URL Encode/Decode")
        print(f"{colors.YELLOW}[5]{colors.RESET} Back to Menu\n")
        
        choice = input(f"{colors.GREEN}Choose option: {colors.RESET}").strip()
        
        if choice == '1':
            encoder = Encoder()
            encoder.base64_tool()
        elif choice == '2':
            encoder = Encoder()
            encoder.hash_tool()
        elif choice == '3':
            encoder = Encoder()
            encoder.rot13_tool()
        elif choice == '4':
            encoder = Encoder()
            encoder.url_tool()
        elif choice == '5':
            break
        else:
            print(f"{colors.RED}Invalid option!{colors.RESET}")
            input("Press Enter to continue...")

def password_menu():
    """Menu Password Tools"""
    while True:
        clear_screen()
        print_banner()
        print(f"\n{colors.CYAN}=== PASSWORD TOOLS ==={colors.RESET}\n")
        print(f"{colors.YELLOW}[1]{colors.RESET} Password Generator")
        print(f"{colors.YELLOW}[2]{colors.RESET} Password Strength Checker")
        print(f"{colors.YELLOW}[3]{colors.RESET} Back to Menu\n")
        
        choice = input(f"{colors.GREEN}Choose option: {colors.RESET}").strip()
        
        if choice == '1':
            pwd = PasswordTools()
            pwd.generate_password()
        elif choice == '2':
            pwd = PasswordTools()
            pwd.check_strength()
        elif choice == '3':
            break
        else:
            print(f"{colors.RED}Invalid option!{colors.RESET}")
            input("Press Enter to continue...")

def web_menu():
    """Menu Web Tools"""
    while True:
        clear_screen()
        print_banner()
        print(f"\n{colors.CYAN}=== WEB TOOLS ==={colors.RESET}\n")
        print(f"{colors.YELLOW}[1]{colors.RESET} HTTP Headers Check")
        print(f"{colors.YELLOW}[2]{colors.RESET} URL Validator")
        print(f"{colors.YELLOW}[3]{colors.RESET} Back to Menu\n")
        
        choice = input(f"{colors.GREEN}Choose option: {colors.RESET}").strip()
        
        if choice == '1':
            web = WebTools()
            web.check_headers()
        elif choice == '2':
            web = WebTools()
            web.validate_url()
        elif choice == '3':
            break
        else:
            print(f"{colors.RED}Invalid option!{colors.RESET}")
            input("Press Enter to continue...")

def main():
    """Fonction principale"""
    try:
        while True:
            display_menu()
            choice = input(f"{colors.GREEN}Choose option: {colors.RESET}").strip()
            
            if choice == '1':
                network_menu()
            elif choice == '2':
                encoder_menu()
            elif choice == '3':
                password_menu()
            elif choice == '4':
                web_menu()
            elif choice == '5':
                print(f"\n{colors.YELLOW}Goodbye! 👋{colors.RESET}\n")
                sys.exit(0)
            else:
                print(f"{colors.RED}Invalid option!{colors.RESET}")
                input("Press Enter to continue...")
    except KeyboardInterrupt:
        print(f"\n{colors.YELLOW}\nExiting...{colors.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
