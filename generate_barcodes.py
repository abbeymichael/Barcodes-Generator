import barcode
from barcode.writer import ImageWriter

start_value = 1234567
num_barcodes = 3000

# Set the width and height of the barcode image
barcode_width = 60
barcode_height = 30

for i in range(start_value, start_value + num_barcodes):
    code = barcode.get('code128', '{:07d}'.format(i), writer=ImageWriter())
    
    # Set the options for the barcode image
    options = {'module_width': 0.3, 'module_height': 5.0, 'quiet_zone': 10.0}
    options['write_text'] = True  # Remove the text below the barcode
    options['font_size'] = 10  # Set the font size of the text above the barcode
    
    # Set the size of the barcode image
    options['width'] = barcode_width
    options['height'] = barcode_height
    
    code.save(f"{i:07d}", options=options)
