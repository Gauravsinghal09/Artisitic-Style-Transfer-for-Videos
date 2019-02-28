import cv2
import numpy as np

img = []
for i in range(1, 51):
    if i < 10:
        img.append(cv2.imread('/home/gaurav/neural-style-tf/first_video_result/frame_000' + str(i) + '.ppm'))
        print('/home/gaurav/neural-style-tf/first_video_result/frame_000' + str(i) + '.ppm')
    else:
        img.append(cv2.imread('/home/gaurav/neural-style-tf/first_video_result/frame_00' + str(i) + '.ppm'))
        print('/home/gaurav/neural-style-tf/first_video_result/frame_00' + str(i) + '.ppm')

height, width, layers = img[1].shape

# fourcc = cv2.CASCADE_SCALE_IMAGE.CV_FOURCC(*'XVID')
video = cv2.VideoWriter('video2.avi', -1, 25, (width, height))

for j in range(0, 50):
    video.write(img[j])

cv2.destroyAllWindows()
video.release()
# import cv2
# import numpy as np
# import os

# from os.path import isfile, join


# def convert_frames_to_video(pathIn, pathOut, fps):
#     frame_array = []
#     files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

#     # for sorting the file names properly
#     files.sort(key=lambda x: int(x[5:-4]))

#     for i in range(len(files)):
#         filename = pathIn + files[i]
#         # reading each files
#         img = cv2.imread(filename)
#         height, width, layers = img.shape
#         size = (width, height)
#         print(filename)
#         # inserting the frames into an image array
#         frame_array.append(img)

#     out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

#     for i in range(len(frame_array)):
#         # writing to a image array
#         out.write(frame_array[i])
#     out.release()


# def main():
#     pathIn = '/home/gaurav/neural-style-tf/first_video_result'
#     pathOut = 'video.avi'
#     fps = 25.0
#     convert_frames_to_video(pathIn, pathOut, fps)


# if __name__ == "__main__":
#     main()
