import os
import shutil

# def rename_images(path):
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more extensions if needed

#     print(f"Renaming images in '{path}'...")
#     for filename in os.listdir(path):
#         file_path = os.path.join(path, filename)
#         if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in image_extensions:
#             new_filename = generate_new_filename(path, filename)
#             new_file_path = os.path.join(path, new_filename)
#             try:
#                 os.rename(file_path, new_file_path)
#                 print(f"Renamed '{filename}' to '{new_filename}'")
#             except FileExistsError:
#                 print(f"A file with the name '{new_filename}' already exists.")

#     print("Finished renaming images.")

# def generate_new_filename(path, filename):
#     name, ext = os.path.splitext(filename)
#     counter = 1
#     new_filename = filename
#     while os.path.exists(os.path.join(path, new_filename)):
#         new_filename = f"{name}_{counter}{ext}"
#         counter += 1
#     return new_filename

def rename_images(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                folder_name = os.path.basename(root)
                file_name, file_ext = os.path.splitext(file)
                counter = 1
                new_file_name = f"{folder_name}_{counter}{file_ext}"
                new_file_path = os.path.join(root, new_file_name)

                while os.path.exists(new_file_path):
                    counter += 1
                    new_file_name = f"{folder_name}_{counter}{file_ext}"
                    new_file_path = os.path.join(root, new_file_name)

                original_file_path = os.path.join(root, file)
                shutil.move(original_file_path, new_file_path)
                print(f"Renamed: {file} -> {new_file_name}")

# rename files in the following path
# path = "C:\\Users\\billy\\Documents\\GitHub\\BinaryClassificationModel\\application\\data\\arts_data_backup\\train\\drawings"
# path = "C:\\Users\\billy\\Documents\\GitHub\\BinaryClassificationModel\\application\\data\\arts_data_backup\\train\\engraving"
# path = "C:\\Users\\billy\\Documents\\GitHub\\BinaryClassificationModel\\application\\data\\arts_data_backup\\train\\iconography"
# path = "C:\\Users\\billy\\Documents\\GitHub\\BinaryClassificationModel\\application\\data\\arts_data_backup\\train\\painting"
path = "C:\\Users\\billy\\Documents\\GitHub\\BinaryClassificationModel\\application\\data\\arts_data_backup\\train\\sculpture"
rename_images(path)