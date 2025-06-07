import hashlib
import datetime

def find_pin(checksum, number):
        result = hashlib.md5(number.encode()).hexdigest()
        if result == checksum:
            t2 = datetime.datetime.now()
            tt = t2 - t1
            print(f"PIN ditemukan: {number} (MD5: {checksum}) - Waktu pencarian: {tt}")
            return True
        return False

def main():
        global t1
        print("Program Pencari PIN dari Hash MD5")
        print("--------------------------------")

        # Input dari user
        user_input = input("Masukkan hash MD5 yang ingin dicari (pisahkan dengan koma jika banyak): ")
        checksums = [md5.strip().lower() for md5 in user_input.split(",")]

        t1 = datetime.datetime.now()
        found = False

        for checksum in checksums:
            if len(checksum) != 32 or not all(c in "0123456789abcdef" for c in checksum):
                print(f"Hash tidak valid: {checksum} (harus 32 karakter hexadecimal)")
                continue

            print(f"\nMencari PIN untuk hash: {checksum}")

            for i in range(0, 10000):
                pin = f"{i:04d}"  # Format 4 digit dengan leading zero
                if find_pin(checksum, pin):
                    found = True
                    break

        if not found:
            t2 = datetime.datetime.now()
            print(f"\nTidak ditemukan PIN yang cocok untuk hash yang diberikan. Waktu pencarian: {t2 - t1}")

if __name__ == "__main__":
        main()