from flask import Flask, request, send_file
import os
import torch
from super_gradients.training import models
from super_gradients.common.object_names import Models

app = Flask(__name__)

dataset_params = {
    'data_dir': '/content/EEP_Detection-1',
    'train_images_dir': 'train/images',
    'train_labels_dir': 'train/labels',
    'val_images_dir': 'valid/images',
    'val_labels_dir': 'valid/labels',
    'test_images_dir': 'test/images',
    'test_labels_dir': 'test/labels',
    'classes': ['boots', 'gloves', 'helmet', 'human', 'vest']
}

best_model = models.get('yolo_nas_s', num_classes=len(dataset_params['classes']), checkpoint_path=r"app\model.pth")

def detect_objects_in_file(input_file_path, output_file_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    best_model.to(device)

    best_model.predict(input_file_path, output_file_path)

    return output_file_path


@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    try:
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        if file.mimetype not in ['image/jpeg', 'video/mp4']:
            return 'Unsupported file format'

        input_file_path = 'input.' + file.filename.split('.')[-1]
        file.save(input_file_path)

        output_file_path = 'output.' + file.filename.split('.')[-1]

        output_file_path = detect_objects_in_file(input_file_path, output_file_path)

        return send_file(output_file_path, mimetype=file.mimetype)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
