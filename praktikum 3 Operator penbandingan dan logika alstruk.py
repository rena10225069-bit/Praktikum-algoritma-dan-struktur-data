# 1. Membuat variabel
nilai = 82
kehadiran = 90

# 2. Memeriksa masing-masing syarat
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("Nilai mahasiswa:", nilai)
print("Kehadiran mahasiswa:", kehadiran, "%")
print("Memenuhi syarat nilai:", syarat_nilai)
print("Memenuhi syarat kehadiran:", syarat_kehadiran)

# 3. Menggunakan operator and
print("Lulus praktikum (and):", syarat_nilai and syarat_kehadiran)

# 4. Mengubah nilai menjadi 70
nilai = 70
syarat_nilai = nilai >= 75

print("\nSetelah nilai diubah menjadi 70:")
print("Nilai mahasiswa:", nilai)
print("Memenuhi syarat nilai:", syarat_nilai)
print("Lulus praktikum (and):", syarat_nilai and syarat_kehadiran)

# 5. Menggunakan operator or
print("Lulus praktikum (or):", syarat_nilai or syarat_kehadiran)