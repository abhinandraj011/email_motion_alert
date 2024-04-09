# Motion Detection and Email Notification

This Python script detects motion using the camera feed and sends email notifications with images when motion is detected.

## Features

- **Motion Detection**: Analyzes the camera feed for changes between frames to detect motion.
- **Email Notification**: Sends email notifications with images when motion is detected.
- **Threaded Execution**: Uses threading to perform email sending and folder cleaning tasks concurrently with motion detection.
- **Image Storage**: Stores images of detected motion in a folder for reference.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install dependencies:

    ```bash
    pip install opencv-python
    ```

4. Set up email configuration:
    - Update the `emailing.py` file with your email credentials (SMTP server, sender email, receiver email, etc.).

5. Run the script:

    ```bash
    python motion_detection.py
    ```

## Usage

1. **Camera Selection**: Modify the `video=cv2.VideoCapture(0)` line to use the main camera (0) or the secondary camera (1).
2. **Frame Adjustment**: Adjust the `time.sleep(1)` line to allow the camera to load properly.
3. **Motion Sensitivity**: Modify the `cv2.threshold(delta_frame,60, 255, cv2.THRESH_BINARY)[1]` line to adjust motion sensitivity.
4. **Notification Configuration**: Customize the email notification settings in the `send_email` function.

## File Structure

- `motion_detection.py`: Main Python script for motion detection and email notification.
- `emailing.py`: Python script containing email sending functionality.
- `images/`: Directory containing images of detected motion.

## Dependencies

- OpenCV (cv2)

## Contributing

Contributions are welcome! If you'd like to improve the project or add new features, feel free to fork the repository and submit a pull request.
