


def mark_img(img, blue_threshold=0, green_threshold=0, red_threshold=0):
    # Define the color thresholds for marking the image
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]
    # Create a boolean mask indicating pixels that satisfy the color thresholds
    thresholds = (img[:,:,0] < bgr_threshold[0]) | (img[:,:,1] < bgr_threshold[1]) | (img[:,:,2] < bgr_threshold[2])
    # Set the pixels that satisfy the thresholds to black
    img[thresholds] = [0,0,0]
    return img

