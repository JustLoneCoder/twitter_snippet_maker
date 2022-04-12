import os, sys
from PIL import Image

twitter_defined_size = (1200, 675)
not_too_bright_rgb_color = (157, 169, 179)

def DoSomethingWithImage():
    ''' 
    This image takes a captured or a snippet image and superimpose it on a background 
    that is the desired dimension for a tweet post

    Just put the script and the image in the same folder and give the script the name 
    of the image, an appropriate width, and a new name or don't give it a new name if you
    wish to crach the old picture. 

    This function takes 3 arguments. 
    (REQUIRED) first is the name of the image you wish to run this function on. 
    (REQUIRED) The second is an appropriate width you think is fit to be a twitter image post. 
    (OPTIONAL) The third is the new name of the image that is going to be saved, or leave it
    empty if you wish to replace the old image.  
    '''

    # asigning the passed arguments
    try:
        image_name = str(sys.argv[1])
        image = Image.open(image_name)
    except FileNotFoundError:
        print("No such file found!")
        return
    except IndexError:
        print("Please give the file's name!")
        return

    try:
        desired_width = int(sys.argv[2])

    except ValueError:
        print("width must be an integer!")
        return
    except IndexError:
        print("Please give a width that you see fit!")
        return

    try:
        saved_name = str(sys.argv[3])

    except IndexError:
        saved_name = image_name
    
    # Dealing with current working directory
    cwd = os.getcwd()

    # Doing the superimpose operation
    image_width = image.size[0]
    image_height = image.size[1]

    new_width = desired_width
    new_height = int((image_height / image_width) * new_width)

    image = image.resize((new_width, new_height))

    size = twitter_defined_size
    layer = Image.new('RGB', size, not_too_bright_rgb_color)

    # A fancy way to define the center of the background
    center = tuple(map(lambda x:(x[0] - x[1]) // 2, zip(size, image.size)))

    layer.paste(image, center)
    layer.save(saved_name)

    layer.show()


if __name__ == '__main__':
    DoSomethingWithImage()
   