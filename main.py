import os
import requests
#biblioteczka systemowa i do żądań http
#link do raw pastebina
url = "https://pastebin.pl/view/raw/0ce85bfa"
response = requests.get(url)
if response.status_code == 200:
    lines = response.text.splitlines()
else:
    print("Błąd podczas pobierania zawartości z adresu:", url)
    exit(1)

folder_path = r"XXX" #Twoja ścieżka do zapisania pliku (~150gb)

episode_title = ""
for line in lines:
    line = line.strip()
    if line:
        if line.startswith("http"):
            if episode_title and line.endswith(".mp4"):
                file_name = f"{episode_title}.mp4"
                file_path = os.path.join(folder_path, file_name)

                print(f"Pobieranie: {file_name}")

                response = requests.get(line)
                if response.status_code == 200:
                    with open(file_path, "wb") as file:
                        file.write(response.content)
                    print(f"Zapisano jako: {file_name}")
                else:
                    print(f"Błąd podczas pobierania: {line}")

                episode_title = ""
        else:
            episode_title = line

print("Pobieranie zakończone.")
