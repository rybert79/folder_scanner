from pathlib import Path
import argparse
import sys

# gtw bener atau salah tapi waktu ku coba udah bener
def ubah_format(angka: int) -> str:
    if angka >= 1_000_000_000:
        return str(round(angka / 1_000_000_000, 2)) + " GB"

    elif angka >= 1_000_000:
        return str(round(angka / 1_000_000, 2)) + " MB"

    elif angka >= 1_000:
        return str(round(angka / 1_000, 2)) + " KB"

    else:
        return str(angka) + " B"   

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="kaih tahu folder mana yan harus di scan", type=str)
parser.add_argument("-c", "--count", help="kasih tahu mau berapa file dengan file terbesar di tampilkan", type=int, default=3)
parser.add_argument("-p", "--pengurutan", help="pilih jenis pengurutan (asc/desc)", type=str, default="asc")
args = parser.parse_args()

if args.count > 10 or args.count < 1:
    print("[-] argument count harus lebih kecil dari 11 dan lebih besar dari 0")
    sys.exit(-1)

if args.pengurutan not in ["asc", "desc"]:
    print("[-] jenis pungurutan hanya ada asc/desc")
    sys.exit(-1)

p = Path(args.folder).expanduser()
all_folder = []
all_file = []
total_size = 0
jenis_pengurutan = "ascending" if args.pengurutan == "asc" else "descending" 

try:
    # nyari folder yang muncul langsung
    for item in p.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            all_folder.append(item)

        elif item.is_file() and not item.name.startswith("."):
            all_file.append(item)
            total_size += item.stat().st_size

except (FileNotFoundError, NotADirectoryError, PermissionError):
    print("[-] welll something went wrong")
    sys.exit(-1)

# cek apakah ada folder untuk intruksi selanjutnya
if not all_folder and not all_file:
    print("[-] folder kosong")
    sys.exit(-1)

# nyari file dengan menyelami direktory temuan sambil mencari ukuran folder awal
i = 0
try:
    while i < len(all_folder):
        for item in all_folder[i].iterdir():
            if item.is_dir() and not item.name.startswith("."):
                all_folder.append(item)

            elif item.is_file() and not item.name.startswith("."):
                all_file.append(item)
                total_size += item.stat().st_size
        i += 1
except (FileNotFoundError, NotADirectoryError, PermissionError):
    print("[-] welll something went wrong")
    sys.exit(-1)

terbesar = max(all_file, key=lambda file: file.stat().st_size)
terkecil = min(all_file, key=lambda file: file.stat().st_size)

# print informasi folder 
print(f"Directory \t: {p}")
print(f"largest files \t: {terbesar} : {ubah_format(terbesar.stat().st_size)}")
print(f"smallest files \t: {terkecil} : {ubah_format(terkecil.stat().st_size)}")
print(f"files scanned \t: {len(all_file)}")
print(f"total sized \t: {ubah_format(total_size)}")
print(f"\ntop {args.count} files diurut secara {jenis_pengurutan}:")

# mencetak file sesuai aturan pengurutan yang diberikan
for i in range(len(all_file)):
    if i == args.count:
        break

    if args.pengurutan == "asc":
        file_pilihan = min(all_file, key=lambda file: file.stat().st_size)
    else:
        file_pilihan = max(all_file, key=lambda file: file.stat().st_size)

    name = file_pilihan.name
    index = all_file.index(file_pilihan)

    print(f"{i + 1}. {name} : {ubah_format((all_file[index].stat().st_size))}")
    all_file.pop(index)
