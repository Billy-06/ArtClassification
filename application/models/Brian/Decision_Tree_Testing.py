import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score, precision_recall_curve, auc
from sklearn.metrics._plot.confusion_matrix import ConfusionMatrixDisplay
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgba2rgb, gray2rgb
from sklearn.preprocessing import label_binarize


# Set the path to the test dataset directory
test_dir = 'test set'

# Initialize empty lists to store the test images and corresponding labels
test_images = []
test_labels = []

# Iterate through each class folder in the test directory
for class_name in os.listdir(test_dir):
    class_dir = os.path.join(test_dir, class_name)
    
    # Iterate through each image in the class folder
    for image_name in os.listdir(class_dir):
        image_path = os.path.join(class_dir, image_name)
        
        # Load the test image
        test_image = imread(image_path)
        
        # Convert image to RGB format if it has an alpha channel or grayscale
        if test_image.shape[-1] == 4:  # RGBA image
            test_image = rgba2rgb(test_image)
        elif len(test_image.shape) == 2:  # Grayscale image
            test_image = gray2rgb(test_image)
        
        # Remove the alpha channel if present
        test_image = test_image[:, :, :3]
        
        # Resize the test image to the same size used during training
        resized_test_image = resize(test_image, (300, 300), mode='reflect')
        
        # Append the resized test image to the test images list
        test_images.append(resized_test_image)
        
        # Append the corresponding label to the test labels list
        test_labels.append(class_name)

# Convert the test lists to numpy arrays
test_images = np.array(test_images)
test_labels = np.array(test_labels)

# Perform label encoding on the test labels using the same label encoder used during training
test_labels_encoded = label_encoder.transform(test_labels)

# Reshape the test image array for input to the DecisionTreeClassifier
test_images = test_images.reshape(test_images.shape[0], -1)

# Make predictions on the test set using the trained classifier
test_predictions = clf.predict(test_images)

# Compute the confusion matrix
cm = confusion_matrix(test_labels_encoded, test_predictions)

# Plot the confusion matrix as a table
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
disp.plot(include_values=True, cmap='Blues', xticks_rotation='vertical')
plt.title('Confusion Matrix (Test Set)')
plt.show()

# Binarize the test labels
binarized_labels = label_binarize(test_labels_encoded, classes=np.unique(test_labels_encoded))

# Compute precision, recall, and F1-score for each class
precision = dict()
recall = dict()
f1_scores = dict()

for class_idx in range(len(np.unique(test_labels_encoded))):
    class_name = str(class_idx)
    class_predictions = [1 if pred == class_idx else 0 for pred in test_predictions]
    class_labels = binarized_labels[:, class_idx]

    true_positives = np.sum(np.logical_and(class_predictions, class_labels))
    false_positives = np.sum(np.logical_and(class_predictions, np.logical_not(class_labels)))
    false_negatives = np.sum(np.logical_and(np.logical_not(class_predictions), class_labels))

    precision[class_name] = true_positives / (true_positives + false_positives + 1e-9)  # Add a small epsilon to avoid division by zero
    recall[class_name] = true_positives / (true_positives + false_negatives + 1e-9)  # Add a small epsilon to avoid division by zero
    f1_scores[class_name] = 2 * (precision[class_name] * recall[class_name]) / (precision[class_name] + recall[class_name] + 1e-9)  # Add a small epsilon to avoid division by zero

# Plot the F1-score curve for each class
plt.figure()
for class_idx in range(len(np.unique(test_labels_encoded))):
    class_name = str(class_idx)
    plt.plot(recall[class_name], f1_scores[class_name], marker='o', label=class_name)

plt.xlabel('Recall')
plt.ylabel('F1-Score')
plt.title('F1-Score Curve')
plt.legend()
plt.grid(True)
plt.show()
