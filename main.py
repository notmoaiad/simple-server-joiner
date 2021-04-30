from colorama import Fore, Style, init
import requests
from json import loads
from os import system
from time import sleep
init(convert=True)

def get_time():
    try:
        return int(input("waiting time in seconds:"))
    except TypeError:
        print(f"{Fore.RED}The input must be numbers!")
        get_time()


def main():

    successs = 0

    try:
        with open("tokens.txt", "r", encoding="utf-8") as f:
            tokens = [token.strip().replace("\"","") for token in f.readlines()]

    except FileNotFoundError:
        try:
            system("Echo. > tokens.txt")

        except :
            system("nano tokens.txt")

        with open("tokens.txt", "r", encoding="utf-8") as f:
            tokens = [token.strip().replace("\"","") for token in f.readlines()]


    if not tokens:
        print(f"{Fore.RED}Please fill the tokens.txt file first.")
        return

    print(f"{Fore.GREEN}{len(tokens)} token has loaded.")

    invite_code = input(f"{Style.RESET_ALL}give me the server invite link: ")


    invite_code = invite_code if "/" not in invite_code else invite_code.split("/")[-1]

    guild_data_request = requests.get("https://discordapp.com/api/v6/invites/" + invite_code)
    print("guild_data_request.status_code", guild_data_request.status_code)
    if guild_data_request.status_code == 200:
        guild_data = loads(guild_data_request.content)
        if guild_data["code"] == 10006:
            print(f"{Fore.RED} ERROR: I can't find this server")
            
            system("pause")
            main()
        else:
            guild_name = guild_data["guild"]["name"]
            guild_id = guild_data["guild"]["id"]
            print(f"{Fore.GREEN}Server Name: {guild_name}\n Server ID: {guild_id}")
            time = get_time()
            print(f"{Style.RESET_ALL}")
            for token in tokens:
                requests.post(f"https://discordapp.com/api/v6/invites/"+invite_code,headers={'authorization':token})
                successs += 1
                sleep(time)

    else:
        print(f"{Fore.RED}ERROR: I can't find this server or you got ratelemited...")
        
        system("pause")

        main()

if __name__ == '__main__':
    main()
