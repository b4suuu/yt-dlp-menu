import os
import subprocess
import platform

# Funkcja czyszcząca ekran
def clear_screen():
    system = platform.system().lower()
    if system == 'windows':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Mac

# Funkcja pobierania filmów
def download_video():
    if not os.path.isfile('url.txt'):
        print("Plik url.txt nie istnieje! Dodaj linki do playlisty lub utworów i spróbuj ponownie.")
        exit(1)

    with open('url.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        print(f"Pobieranie: {url}")
        subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                        '--merge-output-format', 'mp4', '-o', '%(playlist)s/%(title)s.%(ext)s', url])

    print("✅ Pobieranie zakończone!")

# Funkcja pobierania muzyki
def download_audio():
    if not os.path.isfile('url.txt'):
        print("Plik url.txt nie istnieje! Dodaj linki do playlisty lub utworów i spróbuj ponownie.")
        exit(1)

    with open('url.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        print(f"Pobieranie: {url}")
        subprocess.run(['yt-dlp', '-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3',
                        '--audio-quality', '0', '-o', '%(playlist)s/%(title)s.%(ext)s', url])

    print("✅ Pobieranie zakończone!")

# Funkcja pobierania klipu wideo
def download_video_clip():
    if not os.path.isfile('url.txt'):
        print("Plik url.txt nie istnieje! Dodaj linki do playlisty lub utworów i spróbuj ponownie.")
        exit(1)

    start_time = input("Podaj czas rozpoczęcia klipu (np. 00:01:30): ")
    end_time = input("Podaj czas zakończenia klipu (np. 00:02:45): ")

    with open('url.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        print(f"Pobieranie klipu wideo z: {url} od {start_time} do {end_time}")
        subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                        '--merge-output-format', 'mp4', '-o', '%(playlist)s/%(title)s_clip.%(ext)s',
                        '--download-sections', f'*{start_time}-{end_time}', url])

    print("✅ Pobieranie klipu wideo zakończone!")

# Funkcja pobierania klipu audio
def download_audio_clip():
    if not os.path.isfile('url.txt'):
        print("Plik url.txt nie istnieje! Dodaj linki do playlisty lub utworów i spróbuj ponownie.")
        exit(1)

    start_time = input("Podaj czas rozpoczęcia klipu (np. 00:01:30): ")
    end_time = input("Podaj czas zakończenia klipu (np. 00:02:45): ")

    with open('url.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        print(f"Pobieranie klipu audio z: {url} od {start_time} do {end_time}")
        subprocess.run(['yt-dlp', '-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3',
                        '--audio-quality', '0', '-o', '%(playlist)s/%(title)s_clip.%(ext)s',
                        '--download-sections', f'*{start_time}-{end_time}', url])

    print("✅ Pobieranie klipu audio zakończone!")

# Funkcja aktualizacji yt-dlp (działa tylko na Windows)
def update_yt_dlp():
    system = platform.system().lower()
    if system == 'windows':
        print("Aktualizowanie yt-dlp...")
        subprocess.run(['yt-dlp', '--update'])
        print("✅ Aktualizacja zakończona!")
    else:
        print("Aktualizacja yt-dlp jest dostępna tylko na systemie Windows.")

# Menu wyboru
def main():
    clear_screen()  # Czyszczenie ekranu w zależności od systemu
    print("WYBIERZ OPCJE:")
    print("")
    print("1. Pobierz całe wideo")
    print("2. Pobierz całe audio")
    print("3. Pobierz klip wideo")
    print("4. Pobierz klip audio")
    print("5. Wyjście")
    print("")
    # Tylko na Windowsie pojawi się opcja aktualizacji
    system = platform.system().lower()
    if system == 'windows':
        print("6. Aktualizacja")

    print("")

    choice = input("WYBIERZ OPCJE: ")

    if choice == '1':
        download_video()
    elif choice == '2':
        download_audio()
    elif choice == '3':
        download_video_clip()
    elif choice == '4':
        download_audio_clip()
    elif choice == '5':
        print("Wyjście...")
        exit(0)
    elif choice == '6' and system == 'windows':
        update_yt_dlp()
    else:
        print("Nieprawidłowy wybór!")
        exit(1)

if __name__ == '__main__':
    main()