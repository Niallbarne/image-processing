from flask import Flask, request, jsonify
import csv
import os
from process import process_image, apply_colormap

# Initialize the Flask application
app = Flask(__name__)

# Path to the CSV file storing metadata about processed images
METADATA_FILE = "C:/Users/Sonali/OneDrive/Desktop/imageprocessing/image_metadata.csv"

def store_metadata(filename, processed_image_path, colormap_image_path, width, height, depth):
    """
    Store metadata information in the CSV file. If the file doesn't exist, it creates a new one with headers.
    
    Args:
        filename (str): The original filename of the uploaded image.
        processed_image_path (str): Path to the processed image.
        colormap_image_path (str): Path to the image with applied colormap.
        width (int): The width of the processed image.
        height (int): The height of the processed image.
        depth (int): The depth value associated with the image (mocked as 120 for now).
    """
    # Check if the CSV file already exists
    file_exists = os.path.exists(METADATA_FILE)
    
    # Open the file in append mode
    with open(METADATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers only if the file is empty (i.e., first entry)
        if not file_exists:
            writer.writerow(['filename', 'processed_image_path', 'colormap_image_path', 'width', 'height', 'depth'])
        
        # Store image metadata in the CSV file
        writer.writerow([filename, processed_image_path, colormap_image_path, width, height, depth])

@app.route('/')
def index():
    """
    Root route for the API.
    """
    return "Welcome to the Image Processing API. Use /process_data to upload and process images, or /filter_by_depth to filter images by depth range."

@app.route('/process_data', methods=['POST'])
def process_data():
    """
    Endpoint to process the uploaded image. It resizes the image, applies a colormap, and stores the metadata.

    Returns:
        JSON: A response containing the processed image paths and metadata.
    """
    # Extract the image file from the request
    file = request.files['image']
    filename = file.filename
    file.save(os.path.join("resized_images", filename))  # Save the uploaded image
    
    # Mock depth value (replace this with actual logic if needed)
    depth = 120  # Placeholder for depth value
    
    # Define the paths for processed and colormap images
    processed_image_path = os.path.join("resized_images", filename.replace(".jpg", "_processed.jpg"))
    colormap_image_path = os.path.join("resized_images", filename.replace(".jpg", "_colormap.jpg"))
    
    # Process the image (resize and apply colormap)
    process_image(os.path.join("resized_images", filename), processed_image_path, 150, 110)
    apply_colormap(processed_image_path, colormap_image_path)

    # Store metadata (including depth information)
    store_metadata(filename, processed_image_path, colormap_image_path, 150, 110, depth)
    
    # Return a response containing the processed data
    return jsonify({
        "message": "Image uploaded and processed successfully",
        "processed_image_path": processed_image_path,
        "colormap_image_path": colormap_image_path,
        "metadata_stored": "Yes",
        "height": 110,
        "width": 150
    }), 200

@app.route('/filter_by_depth', methods=['GET'])
def filter_by_depth():
    """
    Endpoint to filter images based on a depth range (depth_min and depth_max).
    
    Query Parameters:
        depth_min (int): The minimum depth value for filtering images.
        depth_max (int): The maximum depth value for filtering images.

    Returns:
        JSON: A response containing filtered images matching the depth range.
    """
    # Retrieve depth_min and depth_max from the query parameters
    depth_min = request.args.get('depth_min', type=int)
    depth_max = request.args.get('depth_max', type=int)

    # Return an error if either depth_min or depth_max is missing
    if depth_min is None or depth_max is None:
        return jsonify({"error": "Both 'depth_min' and 'depth_max' are required"}), 400
    
    # Read the CSV and filter the images based on depth
    filtered_images = []
    with open(METADATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            filename, processed_image_path, colormap_image_path, width, height, depth = row
            # If the depth is within the specified range, add it to the filtered list
            if depth_min <= int(depth) <= depth_max:
                filtered_images.append({
                    "filename": filename,
                    "processed_image_path": processed_image_path,
                    "colormap_image_path": colormap_image_path,
                    "depth": depth,
                    "width": width,
                    "height": height
                })
    
    # If no images are found within the depth range, return a message
    if not filtered_images:
        return jsonify({"message": "No images found for the given depth range"}), 404

    # Return the filtered images in the response
    return jsonify(filtered_images), 200

if __name__ == "__main__":
    # Start the Flask app
    app.run(debug=True)
