import os
import random
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

emotion_in_spanish = {
    'anger': 'Ira',
    'disgust': 'Asco',
    'fear': 'Miedo',
    'happiness': 'Alegría',
    'sadness': 'Tristeza',
    'surprise': 'Sorpresa'
}


def get_random_image_from_emotion(emotion):
    """Get a random image from the specified emotion directory."""
    emotion_dir = os.path.join('parsed-dataset', 'test', emotion)
    if not os.path.exists(emotion_dir):
        raise FileNotFoundError(f"Directory not found: {emotion_dir}")

    image_files = os.listdir(emotion_dir)
    if not image_files:
        raise ValueError(f"No images found in {emotion_dir}")

    # Select a random image
    random_image = random.choice(image_files)
    image_path = os.path.join(emotion_dir, random_image)

    return image_path, emotion


def get_grid():
    """Create a grid of images with one image from each emotion."""
    emotions = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']

    # Get one random image from each emotion
    image_paths = []
    for emotion in emotions:
        try:
            image_path, emotion_name = get_random_image_from_emotion(emotion)
            image_paths.append((image_path, emotion_name))
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    if not image_paths:
        print("No images found for any emotion.")
        return None

    # Create a figure with a grid of images
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten()

    # Add each image to the grid
    for i, (image_path, emotion) in enumerate(image_paths):
        if i < len(axes):
            try:
                # Open and convert image
                img = Image.open(image_path)
                img_array = np.array(img)

                # Display image
                axes[i].imshow(img_array, cmap='gray' if len(
                    img_array.shape) == 2 else None)
                # axes[i].set_title(emotion_in_spanish.get(emotion).capitalize())
                axes[i].axis('off')
            except Exception as e:
                print(f"Error displaying image {image_path}: {e}")
                axes[i].text(0.5, 0.5, f"Error: {emotion}",
                             ha='center', va='center', transform=axes[i].transAxes)
                axes[i].axis('off')

    # Adjust layout and save
    plt.tight_layout()
    output_path = 'emotion_grid.png'
    plt.savefig(output_path)
    print(f"Grid image saved to {output_path}")

    return output_path


def main():
    """Main function to run the script."""
    try:
        output_path = get_grid()
        if output_path:
            # Display the grid
            plt.figure(figsize=(12, 8))
            img = plt.imread(output_path)
            plt.imshow(img)
            # plt.axis('off')
            # plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
