import os
import matplotlib.pyplot as plt
import cv2

data_dir = "/content/drive/MyDrive/Dataset"
yes_path = os.path.join(data_dir, "yes")
no_path = os.path.join(data_dir, "no")

def load_sample_images(folder, sample_size=5):
    images = []
    filenames = os.listdir(folder)[:sample_size]
    for filename in filenames:
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
        images.append((img, filename))
    return images

yes_samples = load_sample_images("/content/drive/MyDrive/Dataset/brain_tumor_dataset/yes")
no_samples = load_sample_images("/content/drive/MyDrive/Dataset/brain_tumor_dataset/no")

def display_images(image_list, title):
    plt.figure(figsize=(12, 8))
    for i, (img, filename) in enumerate(image_list):
        plt.subplot(1, len(image_list), i + 1)
        plt.imshow(img)
        plt.title(filename)
        plt.axis("off")
    plt.suptitle(title)
    plt.show()

display_images(yes_samples, "Brain Tumor (YES)")
display_images(no_samples, "Brain Tumor (NO)")
