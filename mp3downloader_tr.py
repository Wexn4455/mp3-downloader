from pytube import YouTube
import os
from colorama import Fore, init

os.system("cls")   
os.system('title YouTube Mp3 Yükleyici ^| Wexn')

print(f"""{Fore.RED}
|=================================|
|                                 |
|              WEXN               |
|                                 |
|          Mp3 İndirici           |
|                                 |
|=================================|
""")

print("")
print("")
print(f"{Fore.YELLOW}İndirmek İstediğin Videonun Linkini Yapıştır.")
print("")

url = input(f"{Fore.BLUE}")
video = YouTube(url)
print("")

print(f"{Fore.YELLOW}Videoların İndirilmesini İstediğin Yeri Göster")
print("")
print(f"{Fore.GREEN}Örnek: {Fore.RED}\n\nC:\Users\KULLANICIADIN\Desktop")
print("")

dosya = input(f"{Fore.BLUE}")
print("")

out_path = video.streams.filter(only_audio=True).first().download(dosya)

new_name = os.path.splitext(out_path)

os.rename(out_path, new_name[0]+'.mp3')

print(f'{Fore.YELLOW}İndirmek İstediğin Ses: {Fore.RED}', video.title)
print("")
print(f"{Fore.GREEN}Yükleniyor...")


print("")

print(f'{Fore.GREEN}Ses Başarıyla İndirildi!{Fore.RED}\n\nLokasyon: {Fore.BLUE}', dosya) 

print(f"{Fore.RESET}")