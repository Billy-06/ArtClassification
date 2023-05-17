import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgba2rgb, gray2rgb

dataset_dir = 'training set'

# Initialize empty lists to store the images and corresponding labels
images = []
labels = []

# Iterate through each class folder
for class_name in os.listdir(dataset_dir):
    class_dir = os.path.join(dataset_dir, class_name)
    
    # Iterate through each image in the class folder
    for image_name in os.listdir(class_dir):
        image_path = os.path.join(class_dir, image_name)
        
        # Load the image
        image = imread(image_path)
        
        # Convert image to RGB format if it has an alpha channel or grayscale
        if image.shape[-1] == 4:  # RGBA image
            image = rgba2rgb(image)
        elif len(image.shape) == 2:  # Grayscale image
            image = gray2rgb(image)
        
        # Remove the alpha channel if present
        image = image[:, :, :3]
        
        # Resize the image while maintaining the aspect ratio
        resized_image = resize(image, (300, 300), mode='reflect')
        
        # Append the resized image to the images list
        images.append(resized_image)
        
        # Append the corresponding label to the labels list
        labels.append(class_name)
        
# Convert the lists to numpy arrays
images = np.array(images)
labels = np.array(labels)

# Perform label encoding on the target labels
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)

# Split the dataset into training and validating sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.1, random_state=42)

# Reshape the image arrays for input to DecisionTreeClassifier
X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

# Initialize the decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

dir(clf)

clf.metrics

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred, normalize='true')

# Plot the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
disp.plot()
plt.title('Normalized Confusion Matrix')
plt.show()
