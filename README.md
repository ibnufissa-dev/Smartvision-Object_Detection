# SmartVision Bottle Detection

SmartVision is a custom object detection project using YOLO to detect bottles in real time through a webcam.

## Project Features

- Custom bottle dataset
- Manual image annotation
- YOLO model training
- Train / validation / test dataset split
- Real-time webcam detection
- Custom trained model using best.pt
- Git and GitHub version control

## Dataset

Total images: 31

Dataset split:

- Train: 21 images
- Validation: 6 images
- Test: 4 images

Object class:

- Bottle

## Model

Model used: YOLO11n

Training settings:

- Epochs: 20
- Image size: 320
- Batch size: 4

## Training Results

- mAP50: approximately 0.906
- mAP50-95: approximately 0.666

## Real-Time Detection

The trained best.pt model was tested using the laptop webcam and successfully detected the custom bottle object in real time.

## Run Detection

```bash
yolo predict model=best.pt source=0 show=True