#! python3
# ex15.py - An insecure password locker program

PASSWORDS = {
    'email': 'F7min1BDDuvMJuxESSKHFhTxFTjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage' : '12345'
}

import sys, pyperclip
if len(sys.argv) < 1:
    print('Usage: python ex15.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

"""
Could create something similar to store all my stock answers to common questions (to avoid repeating myself) aka automated responses
"""
