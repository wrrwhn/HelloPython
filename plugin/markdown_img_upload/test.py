
# pics= grab.grabclipboard()
# pics.save('test.png', 'PNG')

import clipboard

im= clipboard.grabFileImage()
print im.format, im.size, im.mode
im.show()