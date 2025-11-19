# Program Validasi Username

username = input("Masukkan username: ")

if len(username) < 5:
    print("Username tidak valid: minimal 5 karakter")
elif " " in username:
    print("Username tidak valid: tidak boleh mengandung spasi")
elif not username[0].isalpha():
    print("Username tidak valid: karakter pertama harus huruf")
else:
    print("Username valid")
