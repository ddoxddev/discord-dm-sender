import tls_client
import time
import datetime
import os

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

def get_timestamp():
    time_idk = datetime.datetime.now().strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp

class DiscordSession:
    def __init__(self, client_identifier="chrome112", token="YOUR_TOKEN_HERE"):
        self.session = tls_client.Session(client_identifier=client_identifier, random_tls_extension_order=True)
        self.token = token
        self.headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US',
            'authorization': self.token, 
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/1222747973205758002/1224417703100551169',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9037 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Calcutta',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDM3Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMzcgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODA3MDAsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ1MzY5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        }

    def post(self, url, headers, data):
        return self.session.post(url, headers=headers, data=data)

    def start_private_message(self, recipient_id):
        data = {
            'recipient_id': recipient_id
        }
        response = self.post('https://discord.com/api/v9/users/@me/channels', headers=self.headers, data=data)
        if response.status_code == 200:
            return response.json()['id']
        else:
            print(f'{get_timestamp()} {red} An Error Occurred : {response.status_code} - {response.text}')
            return None

class DmSender:
    def __init__(self, discord_session):
        self.discord_session = discord_session

    def send_message(self, channel_id, message):
        data = {
            'content': message
        }
        response = self.discord_session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=self.discord_session.headers, data=data)
        if response.status_code == 200:
            print(f"{get_timestamp()} {green} Successfully Sent Message : {message}")
            return True  # Return True on success
        else:
            print(f'{get_timestamp()} {red} An Error Occurred : {response.status_code} - {response.text}')
            return False  

def main():
    token = "Your Token here"
    discord_session = DiscordSession(token=token)
    dm_sender = DmSender(discord_session)

    channel_id = Your channel_id here
    message = "Message here" 

    message_count = 0 

    while True:
        if dm_sender.send_message(channel_id, message):  
            message_count += 1 

        if message_count % 1 == 0:
            print(f"{get_timestamp()} {blue} Total messages sent: {message_count}")

        time.sleep(1800) 

if __name__ == "__main__":
    os.system("cls")
    main()
