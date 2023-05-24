import os
from PIL import Image

def write_yolo_label(image_path, category, output_dir):
    image_name = str(os.path.splitext(os.path.basename(image_path))[0])
    label_name = image_name + ".txt"
    label_path = os.path.join(output_dir, label_name)

    image = Image.open(image_path)
    image_width, image_height = image.size

    # convert the image_width and image_height to floats that are between 0 and 1 (YOLO format)
    # depending on the image size, the coordinates of the center of the image will be between 0 and 1
    image_width = image_width / image_width
    image_height = image_height / image_height
    

    with open(label_path, "w") as label_file:
        label_file.write(f"{category} {image_width/2} {image_height/2} {image_width} {image_height}")

def process_images(path, output_dir):
    categories = {
        "sculpture": 0,
        "drawings": 1,
        "iconography": 2,
        "engraving": 3,
        "painting": 4
    }

    print("Processing images...")
    for root, dirs, files in os.walk(path):
        for file in files:
            image_path = os.path.join(root, file)
            category = categories.get(os.path.basename(root))
            if category is not None:
                write_yolo_label(image_path, category, output_dir)
    
    print("Done!")

# Example usage
path = "C:/Users/billy/Documents/GitHub/BinaryClassificationModel/application/data/arts_data_backup/train"
output_dir = "C:/Users/billy/Documents/GitHub/BinaryClassificationModel/application/data/arts_data/labels/train"
process_images(path, output_dir)