Image Processing API
This project is a Flask-based API for processing and analyzing images. It includes features such as resizing images, applying colormaps, and storing metadata for easy filtering and querying. The application is containerized using Docker for easy deployment.

Features
Image Resizing: Resize uploaded images to specified dimensions.
Colormap Application: Apply custom colormaps to images (e.g., heatmaps).
Metadata Storage: Store image details (filename, dimensions, depth, etc.) in a CSV file.
Depth-based Filtering: Filter images by their depth values using query parameters.
API Endpoints:
POST /process_data: Upload and process images.
GET /filter_by_depth: Retrieve images based on depth range

Technologies Used
Backend: Python, Flask
Image Processing: Pillow (PIL)
Containerization: Docker
Data Storage: CSV for metadata storage
Testing: Postman for API testing

imageprocessing/
├── app.py                  # Main Flask application
├── process.py              # Functions for image processing
├── cleaned_data.py         # (Optional) Utilities for data cleaning
├── data/
│   └── resized_images/     # Directory for processed images
├── Dockerfile              # Dockerfile for containerization
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Getting Started
Prerequisites
Python 3.8 or above
Docker (optional, for containerization)
Installation
Clone the repository:

git clone https://github.com/Niallbarne/image-processing.git
cd image-processing
Install dependencies:

pip install -r requirements.txt
Run the Flask application:

python app.py
Alternatively, use Docker:

docker build -t image-processing .
docker run -p 5000:5000 image-processing
API Usage
1. Process an Image
Endpoint: POST /process_data
Upload an image to process it.

Request:

Method: POST
Body: Multipart form with an image file.
Response:

{
    "message": "Image uploaded and processed successfully",
    "processed_image_path": "<path_to_resized_image>",
    "colormap_image_path": "<path_to_colormap_image>",
    "metadata_stored": "Yes",
    "height": 110,
    "width": 150
}
2. Filter by Depth
Endpoint: GET /filter_by_depth
Retrieve images based on depth range.

Request:

Method: GET
Query Parameters: depth_min, depth_max (e.g., /filter_by_depth?depth_min=100&depth_max=150).
Response:

[
    {
        "filename": "example.jpg",
        "processed_image_path": "<path_to_resized_image>",
        "colormap_image_path": "<path_to_colormap_image>",
        "depth": 120,
        "width": 150,
        "height": 110
    }
]
Testing the API with Postman
Open Postman.
For POST /process_data:
Set the method to POST.
Enter the URL: http://localhost:5000/process_data.
Add a form-data field:
Key: image
Value: Select an image file from your system.
Send the request and view the response.
For GET /filter_by_depth:
Set the method to GET.
Enter the URL: http://localhost:5000/filter_by_depth?depth_min=100&depth_max=150.
Send the request and view the filtered data.
Contributions
Feel free to submit issues or pull requests to improve this project!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Let me know if you'd like any modifications or additions!






