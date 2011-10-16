slide = function(node, direction) {
    step_size = 150;
    
    image_gallery = node.parentNode;
    gallery_children = image_gallery.children;
    image_slide = undefined;
    $.each(gallery_children, function(id, childNode) {
        if(childNode.className == "image_slide") {
            image_slide = childNode;   
        }
    });
    left = image_slide.style.left == "" ? "0px" : image_slide.style.left;
    left_int = parseInt(left);
    
    index = image_slide.children.length - 1;
    farthestRightElement = image_slide.children[index];
    rightEdgeOffset = farthestRightElement.offsetLeft + farthestRightElement.offsetWidth;
    gallery_width = image_gallery.offsetWidth;
    
    if(direction == "left") {
        step = step_size;
        new_left = left_int + step;
        if(new_left > 0) {
            new_left = left_int;
        }
    }
    else {
        step = -1 * step_size;
        new_left = left_int + step;
        if ((new_left + rightEdgeOffset) < gallery_width) {
            remainder =  gallery_width - (new_left + rightEdgeOffset);
            step = step_size - remainder;
            new_left = left_int - step;
        }
    }
    
    image_slide.style.left = String(new_left) + "px";
};