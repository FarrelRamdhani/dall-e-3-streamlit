# Dall E Streamlit

This is a Streamlit app that generates images using DALL-E 3 based on user input prompts and specified image dimensions.

## Prerequisites

Before running the app, make sure you
- Python 3.6 or above
- Streamlit library

## Setup

1. Clone the repository or download the source code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
- For Window  
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the App

1. Make sure you are in the project directory and the virtual environment is activated.

2. Run the following command to start the Streamlit app:
   ```
   streamlit run app.py
    ```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by navigating to `http://localhost:8501` in your browser.

## Usage

1. Enter your desired prompt in the text area provided. The prompt will be used to generate the image.

2. Adjust the width and height of the image using the sliders. The width and height can be set in increments of 128 pixels, ranging from 128 to 1024 pixels.

3. Click the "Generate Image" button to generate the image based on your prompt and specified dimensions.

4. The generated image will be displayed below the button.

## Troubleshooting

- If you encounter any issues related to missing dependencies, make sure you have activated the virtual environment and installed the required libraries mentioned in the "Setup" section.

- If the app doesn't load or you see an error message, check the terminal or command prompt for any error logs or traceback information. Make sure the `app.py` file is located in the project directory.

## Contributing

If you would like to contribute to this project, please follow these
1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository.

5. Submit a pull request to the main repository, explaining your changes and their benefits.

## License

This project is licensed under the [MIT License](LICENSE).