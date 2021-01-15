from PySide6.QtCore import QRect
from PySide6.QtGui import QImage, QWindow, QPixmap, Qt, QBrush, QPainter


# function to alter image
def mask_image(imgdata, imgtype ='png', size = 64): 
  
    # Load image 
    image = QImage.fromData(imgdata, imgtype) 
  
    # convert image to 32-bit ARGB (adds an alpha 
    # channel ie transparency factor): 
    image.convertToFormat(QImage.Format_ARGB32) 
  
    # Crop image to a square: 
    imgsize = min(image.width(), image.height()) 
    rect = QRect( 
        int((image.width() - imgsize) / 2),
        int((image.height() - imgsize) / 2),
        imgsize, 
        imgsize, 
     ) 
       
    image = image.copy(rect) 
  
    # Create the output image with the same dimensions  
    # and an alpha channel and make it completely transparent: 
    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32) 
    out_img.fill(Qt.transparent) 
  
    # Create a texture brush and paint a circle  
    # with the original image onto the output image: 
    brush = QBrush(image) 
  
    # Paint the output image 
    painter = QPainter(out_img) 
    painter.setBrush(brush) 
  
    # Don't draw an outline 
    painter.setPen(Qt.NoPen) 
  
    # drawing circle 
    painter.drawEllipse(0, 0, imgsize, imgsize) 
  
    # closing painter event 
    painter.end() 
  
    # Convert the image to a pixmap and rescale it.  
    pr = QWindow().devicePixelRatio() 
    pm = QPixmap.fromImage(out_img) 
    pm.setDevicePixelRatio(pr) 
    size *= pr 
    pm = pm.scaled(size, size, Qt.KeepAspectRatio,  
                               Qt.SmoothTransformation) 
  
    # return back the pixmap data 
    return pm 