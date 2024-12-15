import os
import shutil

def copy_folder_content(source_folder, destination_folder):
    try:
        for item in os.listdir(source_folder):
            source_item_path = os.path.join(source_folder, item)
            destination_item_path = os.path.join(destination_folder, item)

            if os.path.isfile(source_item_path):
                # Faylı kopyaladığımız hissə
                with open(source_item_path, 'rb') as src_file:
                    with open(destination_item_path, 'wb') as dest_file:
                        dest_file.write(src_file.read())
            elif os.path.isdir(source_item_path):
                os.mkdir(destination_item_path)
                copy_folder_content(source_item_path, destination_item_path)
    except Exception as e:
        print(f"Error while copying folder content: {e}")

def main():
    inpath = input("Kopyalamaq istədiyiniz folderin yerləşdiyi yer: ")
    outpath = input("Köçürmək istədiyimiz yer: ")

    try:
        # Şərtlərin yoxlanılması
        if not os.path.exists(inpath):
            print("Error: bu qovluğ mövcud deyil.")
            return

        if not os.path.isdir(inpath):
            print("Error: seçilmiş olan obyekt qovluq deyil.")
            return

        if os.path.exists(outpath):
            print("Error: bu qovluğ mövcuddur.")
            return

        # Yeni qovluq yaratmaq
        os.makedirs(outpath)
        print(f"Qovluq yaradıldı: {outpath}")

        # Qovluğun tərkibini kopyalamaq
        copy_folder_content(inpath, outpath)
        print("Qovluğun məzmunu köçürüldü.")

    except Exception as e:
        print(f"Gözlənilməz xəta baş verdi: {e}")

if __name__ == "__main__":
    main()
