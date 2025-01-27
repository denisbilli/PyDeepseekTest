import os
import shutil
from datetime import datetime


def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Errore durante l'ottenimento della dimensione del file {file_path}: {e}")
        return 0


def convert_to_megabytes(bytes_value):
    try:
        mb = bytes_value / (1024 * 1024)  # Converti in MB
        return round(mb, 2)
    except ZeroDivisionError:
        return 0


def get_large_files(desktop_path, min_size=100):  # min_size in MB
    large_files = []
    for root, dirs, files in os.walk(desktop_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size_mb = convert_to_megabytes(get_file_size(file_path))
            if file_size_mb > min_size:
                large_files.append({
                    'name': file,
                    'path': file_path,
                    'size': file_size_mb
                })
    # Ordina i file grandi in base alla dimensione (dal più grande al più piccolo)
    large_files.sort(key=lambda x: -x['size'])
    return large_files


if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")  # Percorso del Desktop
    print(f"Inizio a cercare i file grandi nel percorso: {desktop_path} \n")
    print("Ricerca in corso...", end="\n\n")

    large_files = get_large_files(desktop_path)

    if not large_files:
        print("Nessun file oltre 100 MB trovato nel Desktop.")
    else:
        print(f"Elenco dei file con dimensione superiore a 100 MB trovati nel Desktop:\n")
        for index, file in enumerate(large_files, start=1):
            # size_str = shutil.filesize(file['path'])  # Utilizza filesize per ottenere la dimensione formattata
            size_str = file['size']  # corretto: bastava usare la "size" già calcolata sopra
            print(
                f"{index}. {file['name']} - Posizione: {os.path.relpath(file['path'], desktop_path)} - Dimensione: {size_str}")

    print("\nScript completato. Ora:", datetime.now().strftime("%H:%M:%S"))