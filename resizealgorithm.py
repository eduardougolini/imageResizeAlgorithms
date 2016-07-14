import time
from skimage import io
from skimage import novice
from matplotlib import pyplot
from skimage.transform import resize

max_image_size = 400
new_width = None
new_height = None
image_path = "INSERT IN HERE THE PATH TO IMAGE TO BE RESIZED"
output_path = "INSERT IN HERE THE PATH WHERE RESIZED IMAGE IS GOING TO BE"

def set_new_image_size():
    global new_width
    global new_height
    
    image_properties = novice.open(image_path)
    
    if image_properties.width > image_properties.height:
        height_percentage = image_properties.height * 100 / image_properties.width
        new_width = int(max_image_size)
        new_height = int(new_width / 100 * height_percentage)
    elif image_properties.height > image_properties.width:
        width_percentage = image_properties.width * 100 / image_properties.height
        new_height = int(max_image_size)
        new_width = int(new_height / 100 * width_percentage)
    # Feel free to add a dealing for equal image dimensions
        

def resize_with_skimage():
    function_start_time = time.time()
    start_time = time.time()
    
    image = io.imread(image_path)
    print("Time to load image using skimage = " + str(time.time() - start_time))
    

    start_time = time.time()
    
    output_image = resize(image, (new_height, new_width))
    print("Time to resize image using skimage = " + str(time.time() - start_time))
    
    
    start_time = time.time()
    pyplot.imsave(output_path, output_image)
    print("Time to save image using skimage = " + str(time.time() - start_time))

    print("Total time of function execution = " + str(time.time() - function_start_time))
    
if __name__ == "__main__":
    set_new_image_size()
    resize_with_skimage()
    