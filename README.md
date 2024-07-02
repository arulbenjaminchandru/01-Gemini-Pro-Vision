# Gemini Pro Vision Image Recognition with Streamlit

This repository contains a Streamlit application that uses the Gemini Pro Vision API to recognize and describe the content of an uploaded image based on a customizable prompt text box.

## Features

- Upload an image and get a description based on a prompt.
- Customize the prompt to get specific descriptions.
- Simple and user-friendly web interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/gemini-pro-vision-streamlit.git
    cd gemini-pro-vision-streamlit
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory of the project and add your Gemini Pro Vision API key:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the application.

3. Upload an image and enter a prompt to get a description based on the prompt.

## Code Overview

The main components of the application are:

- **`app.py`**: The main application file that contains the Streamlit code.
- **`requirements.txt`**: The file that lists the Python dependencies for the project.

## Example

1. Upload an image:
    ![Upload Image](screenshots/upload_image.png)

2. Enter a prompt:
    ![Enter Prompt](screenshots/enter_prompt.png)

3. View the generated information:
    ![Generated Information](screenshots/generated_information.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/)
- [Gemini Pro Vision](https://gemini-vision.com/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

