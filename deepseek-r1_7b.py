import os
import glob
import json # aggiunta perché mancante, anche se il codice per cui veniva usata è inutile

# Path delDesktop
## desktop_path = os.path.join(os.sep, 'Users', 'tvoeuser', 'Documenti', 'Desktop')  # Modifica according to your user path
desktop_path = os.path.join(os.sep, 'Users', 'denisbilli', 'Desktop')  # corretta con nome utente e tolto "Documenti"

# Ricerca tutti i file .txt nella cartella Desktop
large_files = []
## for filename in glob.glob(desktop_path + r'\*'): # corretto sotto in quanto la barra è al contrario
for filename in glob.glob(desktop_path + r'/*'):
    if os.path.isfile(filename):
        file_size = os.path.getsize(filename) // (1024 * 1024)  # KB diviso 1024 per ottenere MB
        if file_size > 100:
            large_files.append((filename, file_size))

# Ordina i file da più grandi a più piccoli
large_files.sort(key=lambda x: -x[1])

# Mostra il risultato
print("File grandi (> 100 MB) sul Desktop:")
for file in large_files:
    print(f"- {file[0]} ({file[1]:.2f} MB)")

# il codice sottostante, per quanto interessante, non è stato richiesto ed è quindi inutile

# Opzione per esportare i risultati in un file.txt
# def export_to_file(files, filename="large_files.txt"):
#     with open(filename, 'a') as f:
#         json.dump(files, f, indent=2)
#
# print("\nSe vuoi salvare i risultati in un file, imposta un valore per 'filename' e premi invio.")
