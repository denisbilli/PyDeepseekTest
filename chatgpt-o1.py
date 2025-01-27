import os


def find_large_files(folder_path, size_threshold=100 * 1024 * 1024):
    large_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold:
                    large_files.append((file_path, file_size))
            except OSError:
                print(f"Impossibile accedere al file: {file_path}")
    # Ordina i file dal più grande al più piccolo
    large_files.sort(key=lambda x: x[1], reverse=True)
    return large_files


def main():
    # Ottieni il percorso della cartella Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"Verifico i file nel Desktop: {desktop_path}")

    large_files = find_large_files(desktop_path)

    if large_files:
        print("File più grandi di 100 MB trovati:")
        for file_path, file_size in large_files:
            print(f"{file_path}: {file_size / (1024 * 1024):.2f} MB")
    else:
        print("Nessun file più grande di 100 MB trovato nel Desktop.")


if __name__ == "__main__":
    main()
