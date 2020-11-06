# Artisitic-Style-Transfer-for-Videos
Artisitic Style Transfer for Videos

The Neural Style algorithm synthesizes a pastiche by separating and combining the content of one image with the style of another image using convolutional neural networks (CNN). Below is an example of transferring the artistic style of The Starry Night onto an video:

![Style Transfer on Video](https://github.com/Gauravsinghal09/Artisitic-Style-Transfer-for-Videos/blob/master/Sample%20Videos/video_gif.gif)
### Usage
1. Copy video frames to the default video content directory `./video_input`  
2. Copy style images to the default style directory `./styles`  
3. Run the command with specific arguments:
```
python neural_style.py --video \
                       --video_input_dir ./video_input/my_video_frames \
                       --style_imgs starry-night.jpg \
                       --content_weight 5 \
                       --style_weight 1000 \
                       --temporal_weight 1000 \
                       --start_frame 1 \
                       --end_frame 50 \
                       --max_size 1024 \
                       --first_frame_iterations 3000 \
                       --verbose;
```
#### Arguments
* `--video`: Boolean flag indicating if the user is creating a video.
* `--start_frame`: First frame number. *Default*: `1`
* `--end_frame`: Last frame number. *Default*: `1` 
* `--video_input_dir`: Relative or absolute directory path to input frames. *Default*: `./video_input`
* `--video_output_dir`: Relative or absolute directory path to write output frames to. *Default*: `./video_output`
* `--first_frame_iterations`: Maximum number of optimizer iterations of the first frame. *Default*: `2000`
* `--frame_iterations`: Maximum number of optimizer iterations for each frame after the first frame. *Default*: `800`
* `--learning_rate`: Learning-rate parameter for the Adam optimizer. *Default*: `1e0` 
* `--content_img`: Filename of the content image. *Example*: `lion.jpg`
* `--content_img_dir`: Relative or absolute directory path to the content image. *Default*: `./image_input`
* `--style_imgs`: Filenames of the style images. To use multiple style images, pass a *space-separated* list.  *Example*: `--style_imgs starry-night.jpg`
* `--style_imgs_weights`: The blending weights for each style image.  *Default*: `1.0` (assumes only 1 style image)
* `--style_imgs_dir`: Relative or absolute directory path to the style images. *Default*: `./styles`
* `--init_img_type`: Image used to initialize the network. *Choices*: `content`, `random`, `style`. *Default*: `content`
* `--max_size`: Maximum width or height of the input images. *Default*: `512`
* `--content_weight`: Weight for the content loss function. *Default*: `5e0`
* `--style_weight`: Weight for the style loss function. *Default*: `1e4`
* `--model_weights`: Weights and biases of the VGG-19 network.  Download [here](http://www.vlfeat.org/matconvnet/pretrained/). *Default*:`imagenet-vgg-verydeep-19.mat`
