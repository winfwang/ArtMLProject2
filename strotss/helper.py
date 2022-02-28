#@title Helper Functions
import torch
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else 'cpu'
if not torch.cuda.is_available():
    print('YOU ARE NOT USING A GPU.  IT\'S GONNA BE REAAALLLLY SLOW')
    print('Go to the top of the page.  Click Runtime -> Change Runtime Type -> Hardware accelerator')
    print('From the dropdown, select GPU and rerun all this stuff')

def pil_loader_internet(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img.convert('RGB')

def show_img(img, count):
    # Code for displaying at actual resolution from:
    # https://stackoverflow.com/questions/28816046/displaying-different-images-with-actual-size-in-matplotlib-subplot
    dpi = 80
    height, width, depth = img.shape
    figsize = width / float(dpi), height / float(dpi)
    plt.figure(figsize=figsize)

    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('strotss/results/final_nature/%d.jpg' % (count))
    # disabled for when applying all images from custom dataset
    #plt.show()


def plot_style_and_content(style, content):
    fig, ax = plt.subplots(1,2, figsize=(10,5))
    ax[0].imshow(content)
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    ax[0].set_title('Content')
    ax[1].imshow(style)
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    ax[1].set_title('Style')
    plt.show()