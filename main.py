import os
from os.path import join

COPY = os.environ.get('COPY') or False
VALIDATE = os.environ.get('VALIDATE')

base_dir = 'parsed-dataset'

emotions = {'sadness': [], 'happiness': [], 'fear': [],
            'anger': [], 'disgust': [], 'surprise': []}

if COPY:
    dataset = 'test'
    # dataset = 'train'
    # dataset = 'valid'
    # Create folders
    for emotion in emotions.keys():
        if not os.path.exists(join(base_dir, dataset, emotion)):
            os.mkdir(join(base_dir, dataset, emotion))

    # Get images file names
    images_names = os.listdir(dataset)

    # Copy images
    for image_name in images_names:
        emotion = image_name.split('.')[0].split('_')[-1]
        os.system('cp ' + join(dataset, image_name) + ' ' + join(
            base_dir, dataset, emotion, image_name))

if VALIDATE:
    for dataset in ['test', 'train', 'valid']:
        count = 0
        for emotion in emotions.keys():
            images_in_emotion = os.listdir(join(base_dir, dataset, emotion))
            count += len(images_in_emotion)

        original_count = len(os.listdir(dataset))

        print({'dataset': dataset, 'new_count': count,
              'original_count': original_count})
