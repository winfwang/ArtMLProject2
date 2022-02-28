from strotss_winfred import *
from helper import *

#@title Run STROTSS
#@markdown Put publicly accessible URLs to images for content_url and style_url
style_url = 'https://d3f1iyfxxz8i1e.cloudfront.net/courses/course_image/6649c6ee8999.jpg'  #@param {type:"string"}

#Using dataset of custom personally picked concert photo urls
file = open('strotss/dataset/contents.txt', 'r')
content = file.read().split('\n')
for i in range(10, len(content)):
    print("Applying nature style for img", i)

    content_url = content[i] #@param {type:"string"}
    print("url: ", content_url)

    content_pil = pil_loader_internet(content_url)
    style_pil = pil_loader_internet(style_url) 
    #plot_style_and_content(style_pil, content_pil)

    max_width = 512  #@param {type:"integer"}

    #@markdown How much weight to give to content. 
    # 0.85 for dark style img, 1.35 for nature style img
    content_weight = 1.35 #@param {type:"number"}
    content_weight *= 16.0 

    result = strotss(pil_resize_long_edge_to(content_pil, max_width), 
            pil_resize_long_edge_to(style_pil, max_width), 
            content_weight, device, "vgg")
    #print('Final Result')
    show_img(pil_to_np(result), i)