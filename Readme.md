# Image Classification Web App

This project is a Streamlit-based web application for image classification using a pre-trained TensorFlow model.

## Features

- Upload and classify images
- Display classification results with confidence scores
- User-friendly interface

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/rishabh1125/Skin-Disease-Classificaiton.git
   cd Skin-Disease-Classificaiton
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download all models from dvc
   ```
   dvc pull
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run src/homepage.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Upload an image using the interface and view the classification results.

## Project Structure

- `src/`: Main application files
- `data/`: Sample images are stored here.
- `model/`: Directory containing the pre-trained TensorFlow models
- `requirements.txt`: List of Python dependencies
- `.dvc/`: DVC configuration files for data version control

## Data Version Control

This project uses DVC (Data Version Control) to manage large files and datasets. The remote storage is configured to use Google Drive.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
