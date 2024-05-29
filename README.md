# Plate Number Recognition Project

This project is a Django-based web application that uses machine learning to recognize license plate numbers from images.

## Overview

The main component of this project is the `PlateNumberRecognitionView` class, which is a Django view that handles the recognition of license plate numbers.

When a POST request is made to the `/recognition/` endpoint, the `post` method of the `PlateNumberRecognitionView` class is called. This method retrieves the license plate image from the POST data, uses a machine learning model to recognize the license plate number, and then returns the recognized number.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment and activate it.
4. Install the required packages using `pip install -r requirements.txt`.
5. Run the Django server using `python manage.py runserver`.

## Usage

To use the application, navigate to the `/recognition/` endpoint in your web browser. Upload an image of a license plate, and then click the "Recognize" button. The recognized license plate number will be displayed on the screen.

## Troubleshooting

If you encounter a `TypeError: 'NoneType' object is not callable` error, this typically means that you're trying to call a function on an object that is `None`. In the context of this project, this error might occur if the `form_class` attribute in the `PlateNumberRecognitionView` class is not set to a form class.

To fix this error, you need to either define a `form_class` attribute in your `PlateNumberRecognitionView` class or override the `get_form_class` method to return a form class.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.
# Plate Number Recognition Project

This project is a Django-based web application that uses machine learning to recognize license plate numbers from images.

## Overview

The main component of this project is the `PlateNumberRecognitionView` class, which is a Django view that handles the recognition of license plate numbers.

When a POST request is made to the `/recognition/` endpoint, the `post` method of the `PlateNumberRecognitionView` class is called. This method retrieves the license plate image from the POST data, uses a machine learning model to recognize the license plate number, and then returns the recognized number.

## Installation

1. Clone the repository to your local machine. Run `git clone https://github.com/ndaga1603/License-Plate-Recognition.git` in terminal
2. Navigate to the project directory.
3. Create a virtual environment and activate it.
4. Install the required packages using `pip install -r requirements.txt`.
5. Run the Django server using `python manage.py runserver`.

## Usage

To use the application, navigate to the `/recognition/` endpoint in your web browser. Upload an image of a license plate, and then click the "Recognize" button. The recognized license plate number will be displayed on the screen.

## Troubleshooting
I actively upgrade the projectt, if you get any error while running the project, please feel free to contact me.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.