# machine_learning_corporate

This repository contains two main features:
1. **Automatic Number Plate Recognition (ANPR)** - Python implementation using YOLOv8
2. **Sanjay Fuloria Chatbot** - AI chatbot that answers questions about Sanjay Fuloria using Claude Sonnet

## 🤖 Sanjay Fuloria Chatbot

A conversational AI chatbot powered by Claude Sonnet that can answer questions about Sanjay Fuloria's professional background, expertise, and projects.

### Features
- Interactive chat interface
- Questions about machine learning expertise
- Information about technical skills and projects
- Details about the ANPR system and other work

### Quick Start
```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY="your-api-key-here"

# Interactive mode
python chatbot_cli.py --interactive

# Ask a single question
python chatbot_cli.py --question "What is Sanjay's expertise?"

# Show available topics
python chatbot_cli.py --topics
```

See [CHATBOT_CONFIG.md](CHATBOT_CONFIG.md) for detailed setup instructions.

## 🚗 Automatic Number Plate Recognition (ANPR)

<p align="center">
<a href="https://www.youtube.com/watch?v=fyJB1t0o0ms">
    <img width="600" src="https://utils-computervisiondeveloper.s3.amazonaws.com/thumbnails/with_play_button/anpr_yolo2.jpg" alt="Watch the video">
    </br>Watch on YouTube: Automatic number plate recognition with Python, Yolov8 and EasyOCR !
</a>
</p>

## data

The video I used in this tutorial can be downloaded [here](https://www.pexels.com/video/traffic-flow-in-the-highway-2103099/).

## models

A Yolov8 pretrained model was used to detect vehicles.

A licensed plate detector was used to detect license plates. The model was trained with Yolov8 using [this dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4) and following this [step by step tutorial on how to train an object detector with Yolov8 on your custom data](https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide). 

The trained model is available in my [Patreon](https://www.patreon.com/ComputerVisionEngineer).

## dependencies

The sort module needs to be downloaded from [this repository](https://github.com/abewley/sort) as mentioned in the [video](https://youtu.be/fyJB1t0o0ms?t=1120).
