import os
import Image as PILImage

class Image(object):
    MAX_SIZEX = 1000 # this is the maximum width of the images
    MAX_SIZEY = 1000 # this is the maximum height of the images
    TILE_SIZEX = 200 # this is the maximum width of the tile images
    TILE_SIZEY = 200 # this is the maximum height of the tile images
    THUMBNAIL_SIZEX = 50 # this is the maximum width of the thumbnail images
    THUMBNAIL_SIZEY = 50 # this is the maximum height of the thumbnail images
    
    image_names = {'base' : 'base',
                   'tile' : 'tile',
                   'thumbnail' : 'thumbnail'}
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
        
        self.base_filename = self.directory + self.image_names['base'] + self.types[self.mimetype]
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
        
        self.create_tile_image(image)
        self.create_thumbnail_image(image)

    def create_dir(self):
        os.mkdir(self.directory)
        
    def create_base_image(self):
        with open(self.base_filename, 'w+') as fh:
            fh.write(self.contents)
            
    def create_tile_image(self, image):
        temp_img = image.copy()

        self.tile_filename = self.directory + \
                             self.image_names['tile'] + \
                             self.types[self.mimetype]
        temp_img = temp_img.resize((self.TILE_SIZEX, self.TILE_SIZEY), PILImage.ANTIALIAS)
        temp_img.save(self.tile_filename, "JPEG", quality = 100) # save the image
    
    def create_thumbnail_image(self, image):
        temp_img = image.copy()

        self.thumbnail_filename = self.directory + \
                                  self.image_names['thumbnail'] + \
                                  self.types[self.mimetype]
        temp_img.thumbnail((self.THUMBNAIL_SIZEX, self.THUMBNAIL_SIZEY), PILImage.ANTIALIAS)
        temp_img.save(self.thumbnail_filename, "JPEG", quality = 80) # save the image