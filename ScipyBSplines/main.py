import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
import io
import markdown as md
import base64
import imageio
import time


class HTMLDoc:
    def __init__(self):
        self.markdown = ''
        self.html = None

    def add_text(self, text):
        self.markdown += text
        self.markdown += '\n'

    def add_bytestring_image(self, bytestring, alt_text = 'alt_text'):
        image_string = '![' + alt_text + '](data:image/png;base64,' + bytestring + ')'
        self.markdown += image_string
        self.markdown += '\n'

    def add_image(self, image, alt_text = 'alt_text'):
        image_string = '![' + alt_text + '](' + image + ')'
        self.markdown += image_string
        self.markdown += '\n'

    def add_css(self, css_file):
        css_string = '<html>\n<head>\n<link rel=\"stylesheet\" href=\"' + css_file + '\">\n</head>'
        self.html = css_string + self.html
        self.html += '</html>'

    def to_html(self):
        self.html = md.markdown(self.markdown)

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def compute_deriv(image = None):

    if image is None:
        image = misc.face(gray=True).astype(np.float32)
    else:
        image = rgb2gray(image)
    print(image.shape)
    derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
    ck = signal.cspline2d(image, 8.0)
    deriv = (signal.sepfir2d(ck, derfilt, [1]) +
             signal.sepfir2d(ck, [1], derfilt))

    return image, deriv

def plot_images(image, deriv):

    s = io.BytesIO()
    plt.figure()
    plt.imshow(image)
    plt.gray()
    plt.title('Original image (Grayscale)')

    plt.savefig(s, format='png', bbox_inches="tight", transparent=True)
    plt.close()
    s1 = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")
    del s

    s = io.BytesIO()
    plt.figure()
    plt.imshow(deriv)
    plt.gray()
    plt.title('Output of spline edge filter')

    plt.savefig(s, format='png', bbox_inches="tight", transparent=True)
    plt.close()
    s2 = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")

    return s1, s2

def prepare_html_output(s1, s2):
    text = '''# Signal Processing (scipy.signal) - B splines
            The following code and figure use spline-filtering to compute an edge-image (the second derivative of a smoothed spline).
            
            The command sepfir2d was used to apply a separable 2-D FIR filter with mirror-symmetric boundary conditions
            to the spline coefficients.
            This function is ideally-suited for reconstructing samples from spline coefficients
            and is faster than convolve2d, which convolves arbitrary 2-D filters and allows for
            choosing mirror-symmetric boundary conditions.
        '''

    style = '''<html><head>
            <style>
                * {
                font-family: 'Roboto', sans-serif;
                }
                h1 {
                text-align: center;
                }
                p {
                text-align: left;
                }
            </style>
            </head>
            '''

    doc = HTMLDoc()
    doc.add_text(text)
    doc.add_bytestring_image(s1)
    doc.add_bytestring_image(s2)
    doc.to_html()
    doc.html = style + doc.html
    doc.html += '</html'
    # doc.add_css("styling.css")

    return doc.html

def run():
    # start = time.time()
    image = None
    
    image, deriv = compute_deriv(None)
    # s1, s2 = plot_images(image, deriv)

    # print("Execution time : ", time.time() - start)

    # html_out = prepare_html_output(s1, s2)

    return image

