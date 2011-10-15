import os
import Image as PILImage

class Image(object):
    MAX_SIZEX = 1000 # this is the maximum width of the images
    MAX_SIZEY = 1000 # this is the maximum height of the images
    
    types = {'image/jpeg' : '.jpeg'}

    def __init__(self, file):
        self.fp = file.pop('fp')
        self.uid = file.pop('uid')
        self.filename = file.pop('filename')
        self.filesize = file.pop('size')
        self.mimetype = file.pop('mimetype')
        
        self.contents = self.fp.read()
        
        self.directory = 'reprap/static/img/issue_images/' + self.uid + '/'
        self.create_dir()
        
        self.base_filename = self.directory + 'base' + self.types[self.mimetype]
        self.create_base_image()
        
        image = PILImage.open(self.base_filename) # open the input file
        (width, height) = image.size # get the size of the input image

        ratio = 1. * self.MAX_SIZEX / self.MAX_SIZEY
        top = left = 0; right, bottom = image.size
        if width > height * ratio:
            # crop the image on the left and right side
            new_width = int(height * ratio)
            left = width / 2 - new_width / 2
            right = left + new_width
        elif width < height * ratio:
            # crop the image on the top and bottom
            new_height = int(width * ratio)
            top = height / 2 - new_height / 2
            bottom = top + new_height
        
        if width != height * ratio:
            image = image.crop((left, top, right, bottom))
        
        self.image = image

    def create_dir(self):
        os.mkdir(self.directory)
        
    def create_base_image(self):
        with open(self.base_filename, 'w+') as fh:
            fh.write(self.contents)
            
    def resize(self, size):
        temp_img = self.image.copy()
        width = size[0]; height = size[1]
        
        self.tile_filename = self.directory + \
                             'tile' + \
                             self.types[self.mimetype]
        temp_img = temp_img.resize((width, height), PILImage.ANTIALIAS)
        temp_img.save(self.tile_filename, "JPEG", quality = 100) # save the image
    
    def thumbnail(self, size):
        temp_img = self.image.copy()
        width = size[0]; height = size[1]
        
        self.thumbnail_filename = self.directory + \
                                  'thumbnail' + \
                                  self.types[self.mimetype]
        temp_img.thumbnail((width, height), PILImage.ANTIALIAS)
        temp_img.save(self.thumbnail_filename, "JPEG", quality = 80) # save the image