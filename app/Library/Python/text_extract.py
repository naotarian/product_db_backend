import glob
import pyocr.builders
from PIL import Image

class OCRs:
    def __init__(self):
        self.tools = pyocr.get_available_tools()
        self.tool = self.tools[0]
        self.langs = self.tool.get_available_languages()
        self.lang = 'jpn'
        print(self.lang)
        self.res = False
        print(self.tools)
        if len(self.tools) != 0:
            self.res = True
    def read(self, file_name):
        if not self.res:
            return 'error'
        else:
            txt = self.tool.image_to_string(
                Image.open(file_name),
                lang=self.lang,
                builder=pyocr.builders.TextBuilder()
            )
            return txt
            
if __name__ == '__main__':
    cl = OCRs()
    cl.__init__()
    file_names = glob.glob('/app/product_db/app/Library/Python/img/*')
    print(file_names)
    for file_name in file_names:
        print(file_name)
        if cl.read(file_name) == 'error':
            print('OCRソフトが見つかりませんでした。')
            break
        else:
            print(cl.read(file_name))    