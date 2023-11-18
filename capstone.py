# Define the Capstone Menu
capstone_menu = [
    "1. Tampilkan Daftar Siswa",
    "2. Tambahkan Data Siswa baru",
    "3. Ubah Data Siswa",
    "4. Hapus Data Siswa",
    "5. Keluar"
]
student_list = [
    {'NPM': 12, "Nama": "Reza", "Asal": "Surabaya", "Alamat": "Semolowaru", "Nilai": 90},
    {'NPM': 15, "Nama": "Ahay", "Asal": "Malang", "Alamat": "Nginden", "Nilai": 85}
    ]

data_not_found = "Data does not exist"
option_selected_invalid = "The option you entered is not valid"
def display_student_list():
    if len(student_list) == 0:
        print(data_not_found)
    else:
        for student in student_list:
            for key in (student.keys()):
                print("{0}: {1}".format(key, student.get(key)))
            print("\n")

# CREATE DATA
def create_data():
    create_menu_selected = ""
    while create_menu_selected != 2:
        print("==== Menu Tambah Data Siswa ====")
        print("1. Tambahkan Data Siswa")
        print("2. Kembali Ke Menu Utama")
        create_menu_selected = int(input("Silakan Pilih Sub Menu [1 atau 2] : "))
        if create_menu_selected == 1:
            npm_siswa = input("Masukkan data NPM: ")
            while npm_siswa.isnumeric() == False:
                npm_siswa = input("NPM hanya terdiri dari Angka!\nSilahkan Masukkan NPM kembali: ")
            # check if there is any duplicate NPM
            if len(student_list) > 0:
                for student in student_list:
                    if int(npm_siswa) == student["NPM"]:
                        print("Data already exists")
                        break
            
            nama_siswa = input("Masukkan nama Siswa: ")
            asal_siswa = input("Masukkan asal daerah Siswa: ")
            alamat_siswa = input("Masukkan alamat tempat tinggal Siswa: ")
            nilai_siswa = input("Masukkan nilai Siswa: ")
            while nilai_siswa.isnumeric() == False:
                nilai_siswa = input("Nilai hanya terdiri dari Angka!\nSilahkan Masukkan Nilai kembali: ")

            user_option = ""
            while (user_option.upper() != 'Y') or (user_option.upper() == 'N'):
                print('''
                Anda akan memasukkan data berikut
                NPM: {}
                Nama: {}
                Asal: {}
                Alamat Tempat Tinggal: {}
                Nilai: {}
                '''.format(npm_siswa, nama_siswa, asal_siswa, alamat_siswa, nilai_siswa))
                user_option = input("Apakah Anda ingin Memasukkan Data ini? [Y/N]: ")
                if user_option.upper() == 'Y':
                    siswa_info = {'NPM': int(npm_siswa), 'Nama': nama_siswa, 'Asal': asal_siswa, 'Alamat': alamat_siswa, 'Nilai': int(nilai_siswa)}
                    student_list.append(siswa_info)
                    print("Data successfully saved")
                    break
                elif user_option.upper() == 'N':
                    print("Data tidak tersimpan")
                    break
                else:
                    print(option_selected_invalid)
        elif create_menu_selected == 2:
            menu()
        else:
            print(option_selected_invalid)

# READ DATA
def read_data():
    read_menu_selected = ""
    while read_menu_selected != 3:
        print("\n==== Menu Daftar Seluruh Siswa ====")
        print("1. Tampilkan seluruh data siswa")
        print("2. Cari siswa berdasarkan NPM")
        print("3. Kembali Ke Menu Utama")                                                                     
        read_menu_selected = int(input("Silakan Pilih Sub Menu Read Data [1-3] : "))
        if read_menu_selected == 1:
            display_student_list()
        elif read_menu_selected == 2:
            if len(student_list) == 0:
                print(data_not_found)
            else:
                npm_selected = input("Silahkan Masukkan NPM yang ingin Dilihat: ")
                while npm_selected.isnumeric() == False:
                    npm_selected = input("NPM hanya terdiri dari Angka!\nSilahkan Masukkan NPM kembali: ")

                for student in student_list:
                    if int(npm_selected) == student['NPM']:
                        for key in (student.keys()):
                            print("{0}: {1}".format(key, student.get(key)))
                        break
                    else:
                        print(data_not_found)
        elif read_menu_selected == 3:
            menu()
        else:
            print(option_selected_invalid)

# UPDATE DATA
def update_data():
    update_menu_selected = ""
    while update_menu_selected != 2:
        print("==== Menu Ubah Data Siswa ====")
        print("1. Ubah Data Siswa")
        print("2. Kembali Ke Menu Utama")
        update_menu_selected = int(input("Silakan Pilih Sub Menu [1 atau 2] : "))
        if update_menu_selected == 1:
            if len(student_list) == 0:
                print(data_not_found)
            else:
                display_student_list()
                npm_selected = input("Silahkan Masukkan NPM yang ingin Diubah: ")
                while npm_selected.isnumeric() == False:
                    npm_selected = input("NPM hanya terdiri dari Angka!\nSilahkan Masukkan NPM kembali: ")
                
                for student in student_list:
                    if int(npm_selected) == student['NPM']:
                        # show the students information
                        print("Informasi Siswa")
                        for key in student.keys():
                            print("{0}: {1}".format(key, student.get(key)))
                        
                        column_selected = input("Tuliskan nama kolom yang ingin diubah: ")
                        while column_selected.title() not in list(student.keys()):
                            column_selected = input("Kolom yang Anda masukkan tidak ada!\nSilahkan masukkan kembali: ")
                        
                        new_data = input("Anda akan mengubah data {}, silahkan tuliskan data baru: ".format(column_selected.title()))
                        user_option = ""
                        while (user_option.upper() != 'Y') or (user_option.upper() == 'N'):
                            user_option = input("Apakah Anda ingin Mengubah Data ini? [Y/N]: ")
                            if user_option.upper() == 'Y':                               
                                if column_selected == 'Nilai':
                                    new_data = int(new_data)
                                student.update({column_selected.title(): new_data})
                                print("Data successfully updated")
                                break
                            elif user_option.upper() == 'N':
                                print("Data tidak Terhapus")
                                break
                            else:
                                print(option_selected_invalid)
                    else:
                        continue # continue to the iteration to keep finding the NPM
        elif update_menu_selected == 2:
            menu()
        else:
            print(option_selected_invalid)

# DELETE DATA
def delete_data():
    delete_menu_selected = ""
    while delete_menu_selected != 2:
        print("==== Menu Hapus Data Siswa ====")
        print("1. Hapus Data Siswa")
        print("2. Kembali Ke Menu Utama")
        delete_menu_selected = int(input("Silakan Pilih Sub Menu [1 atau 2] : "))
        if delete_menu_selected == 1:
            if len(student_list) == 0:
                print(data_not_found)
            else:
                display_student_list()
                npm_selected = input("Silahkan Masukkan NPM yang ingin Dihapus: ")
                while npm_selected.isnumeric() == False:
                    npm_selected = input("NPM hanya terdiri dari Angka!\nSilahkan Masukkan NPM kembali: ")
        
                for student in student_list:
                    if int(npm_selected) == student['NPM']:
                        user_option = ""
                        while (user_option.upper() != 'Y') or (user_option.upper() == 'N'):
                            user_option = input("Apakah Anda ingin Menghapus Data ini? [Y/N]: ")
                            if user_option.upper() == 'Y':
                                student_list.pop(student_list.index(student))
                                print("Data successfully deleted")
                                break
                            elif user_option.upper() == 'N':
                                print("Data tidak dihapus")
                                break
                            else:
                                print(option_selected_invalid)
                        break
                    else:
                        continue # continue to the iteration to keep finding the NPM
        elif delete_menu_selected == 2:
            menu()
        else:
            print(option_selected_invalid)

def menu():
    menu_selected = ""
    while menu_selected != 5:
        print("SELAMAT DATANG!!\n==== Database Aplikasi Data Siswa ====")
        for menu in capstone_menu:
            print(menu)
        menu_selected = int(input("Silahkan Pilih Menu [Tulis angka 1-5]: "))
        
        if menu_selected == 1:
            read_data()
        elif menu_selected == 2:
            create_data()
        elif menu_selected == 3:
            update_data()
        elif menu_selected == 4:
            delete_data()
        elif menu_selected == 5:
            print("Thank you!")
            quit()
        else:
            print(option_selected_invalid)

menu()
