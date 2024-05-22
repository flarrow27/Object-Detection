# Real-Time Object Recognition Using ResNet50 and OpenCV

This project demonstrates real-time object recognition using the ResNet50 deep learning model and OpenCV. The ResNet50 model, pre-trained on the ImageNet dataset, is used to predict object classes from video frames captured by a webcam or from a video file.

## Requirements

- Python
- OpenCV
- Keras
- TensorFlow
- Pre-trained ResNet50 model (downloaded automatically by Keras)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/real-time-object-recognition.git
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python keras tensorflow
   ```

3. Run the script:

   ```bash
   python object_recognition.py
   ```

## Usage

1. When the script is executed, it will access the webcam or the specified video file.
2. Each frame from the video source will be processed by the ResNet50 model for object recognition.
3. The predicted object class along with its confidence score will be displayed on each frame.
4. Press 'q' to exit the application.

## Contributing

Contributions to this project are welcome! Feel free to submit bug reports, feature requests, or pull requests via GitHub.

## Acknowledgements

- Thanks to the developers of OpenCV, Keras, and TensorFlow for their amazing libraries.
- Special thanks to the creators of the ResNet50 model for providing a powerful pre-trained model for object recognition.

## Contact

For any inquiries or support, please contact jabinjoshua.s@gmail.com

---

Enjoy real-time object recognition with ResNet50 and OpenCV!
