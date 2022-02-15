import json
import asyncio
import requests
import aiohttp
import os

userid = None
channel = None


my_secret = os.environ['key']

while not userid:
    userid = input("Enter the Discordian's Id: ")

headers = {
   'Authorization': my_secret,
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1011 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
   'Content-Type': 'application/json'
}

while True: 
  text = input("Enter messages you want to send: ")   
  requests.post('https://discord.com/api/v9/channels/%s/messages'%userid,     
  headers=headers, json={"content": text})