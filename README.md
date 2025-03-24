=================================================================
LINUX
=================================================================


1. Zainstaluj yt-dlp (dla debian/ubuntu dostępne w repo apt):
    sudo apt-get install yt-dlp 
2. Zainstaluj środowisko uruchomieniowe python (dla debian/ubuntu dostępne w repo apt):
    sudo apt-get install python3
3. Sklonuj repozytorium:
    git clone https://github.com/b4suuu/yt-dlp-menu.git
4. Uruchamiamy:
    python3 yt-dlp-menu.py

Plik start.cmd służy tylko do szybkiego uruchamiania progamu pod windowsem (pkt 5 sekscja WINDOWS). Pod linuxem zbędny. 


==================================================================
WINDOWS
==================================================================


1. Pobierz yt-dlp:
https://github.com/yt-dlp/yt-dlp

Pobierz FFmpeg:
https://github.com/BtbN/FFmpeg-Builds/releases



2. DODANIE yt-dlp DO ZMIENNYCH ŚRODOWISKOWYCH:

    - Panel Sterowania, następnie "System" i w zakładce "Zaawansowane" klikamy przycisk Zmienne środowiskowe.
      Lub skorzystaj z systemowej szukajki, otworzyć Menu Start i wpisać “zmienne” (lub z paska zadań ikona szukania). Następnie wybrać "zmienne środowiskowe" z podpowiedzi.
    - Klikamy w "zmienne środowiskowe"
    - Po zaznaczeniu zmiennej PATH i wciśnięciu przycisku Edytuj otworzy się nowe okno.
    - Dodajemy nową ścieżkę klikając w przycisk “Przeglądaj”, a następnie wybieramy miejsce w którym znajduje się yt-dlp.
    - Potwierdzamy - wychodzimy.

3. Do uruchomienia programu będzie potrzebne środowisko uruchomieniowe pythona. Instalujemy je ze sklepu WINDOWS STORE w szukajce wpisując "python".

4. Po pobraniu yt-dlp-menu.py, url.txt, start.cmd uruchamiamy z konsoli poleceniem:
    python ./yt-dlp-menu.py    lub   python3 ./yt-dlp.menu.pl   zależnie jaką wersje pythona posiadamy w systemie.

5. (OPCJONALNY) Można skorzystać z pliku start.cmd  - jako opcja szybkiego wywołania programu za pomocą CMD 2-klikiem - edytując poprawną ścieżkę do yt-dlp-menu.py w środku start.cmd
