
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


