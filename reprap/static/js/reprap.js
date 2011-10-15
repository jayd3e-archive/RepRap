slide = function(node, direction) {
    parent = node.parentNode;
    gallery_children = parent.children;
    image_slide = undefined;
    $.each(parent.children, function(id, childNode) {
        if(childNode.className == "image_slide") {
            image_slide = childNode;   
        }
    });
    left = image_slide.style.left == "" ? "0px" : image_slide.style.left;
    left_int = parseInt(left);
    
    if(direction == "left") {
        step = -20;   
    }
    else {
        step = 20;   
    }
    
    image_slide.style.left = String(left_int + step) + "px";
};