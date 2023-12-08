import cv2
import numpy as np
import os

def region_of_interest(img, vertices, color3=(255,255,255), color1=255):
    # Create a mask with the same shape as the image
    mask = np.zeros_like(img)
    # Check if the image has multiple channels (i.e., color image) or a single channel (i.e., grayscale image)
    if len(img.shape) > 2:
        color = color3
    else:
        color = color1
    # Fill the region of interest defined by the vertices with the specified color
    cv2.fillPoly(mask, vertices, color)
    # Perform bitwise AND operation between the image and the mask to get the region of interest
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def mark_img(img, blue_threshold=0, green_threshold=0, red_threshold=0):
    # Define the color thresholds for marking the image
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]
    # Create a boolean mask indicating pixels that satisfy the color thresholds
    thresholds = (img[:,:,0] < bgr_threshold[0]) | (img[:,:,1] < bgr_threshold[1]) | (img[:,:,2] < bgr_threshold[2])
    # Set the pixels that satisfy the thresholds to black
    img[thresholds] = [0,0,0]
    return img

# Open the video file
cap = cv2.VideoCapture('C:/Users/daisy/Desktop/Document/vscodetest/image/1212.mp4')

# Create a directory to store the result images if it doesn't exist
if not os.path.exists('results'):
    os.makedirs('results')

frame_count = 0

while(cap.isOpened()):
    # Read the next frame from the video
    ret, image = cap.read()
    
    if not ret:
        break
    
    # Get the height and width of the image
    height, width = image.shape[:2]

    # Define the region of interest vertices
    vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=np.int32)
    # Extract the region of interest from the image
    roi_img = region_of_interest(image, vertices, (0,0,255))

    # Create a copy of the region of interest image for marking
    mark = np.copy(roi_img)
    # Mark the image by setting pixels below the color thresholds to black
    mark = mark_img(roi_img)

    # Create a boolean mask for pixels that satisfy the color threshold for red
    color_thresholds = (mark[:,:,0] == 0) & (mark[:,:,1] == 0) & (mark[:,:,2] > 200)
    # Set the pixels that satisfy the color threshold to red
    image[color_thresholds] = [0,0,255]

    # Display the resulting image
    cv2.imshow('results', image)
    
    # Save the result image to a file
    cv2.imwrite(os.path.join('results', f'frame_{frame_count}.jpg'), image)
    frame_count += 1
    
    # Wait for key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the results image on the screen
    cv2.imshow('Result Image', image)
    cv2.waitKey(1)

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
