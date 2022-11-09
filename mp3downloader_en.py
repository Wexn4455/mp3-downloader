from pytube import YouTube
import os
from colorama import Fore, init

os.system("cls")   
os.system('title YouTube Mp3 Downloader ^| Wexn')

print(f"""{Fore.RED}
|=================================|
|                                 |
|              WEXN               |
|                                 |
|         Mp3 Downloader          |
|                                 |
|=================================|
""")

print("")
print("")
print(f"{Fore.YELLOW}Paste the link of the video you want to download.")
print("")

url = input(f"{Fore.BLUE}")
video = YouTube(url)
print("")

print(f"{Fore.YELLOW}Type Where You Want Videos to Download")
print("")
print(f"{Fore.GREEN}Example: {Fore.RED}\n\nC:\Users\YOURUSERNAME\Desktop")
print("")

dosya = input(f"{Fore.BLUE}")
print("")

out_path = video.streams.filter(only_audio=True).first().download(dosya)

new_name = os.path.splitext(out_path)

os.rename(out_path, new_name[0]+'.mp3')

print(f'{Fore.YELLOW}Audio You Want To Download: {Fore.RED}', video.title)
print("")
print(f"{Fore.GREEN}Downloading...")


print("")

print(f'{Fore.GREEN}Audio Downloaded Successfully!{Fore.RED}\n\nLocation: {Fore.BLUE}', dosya) 

print(f"{Fore.RESET}")