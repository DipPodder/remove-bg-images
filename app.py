from rembg import remove
import easygui
from PIL import Image

inputpath = easygui.fileopenbox(title='Select the image')
outputpath = easygui.filesavebox(title='Save file to..')

input = Image.open(inputpath)
output = remove(input)
output.save(outputpath)