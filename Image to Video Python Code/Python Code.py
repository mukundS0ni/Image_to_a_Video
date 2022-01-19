import cv2
import numpy as np
import glob
import ffmpeg
import random
img_array = []
for filename in glob.glob('NO_COPY/*.jpg'):
    img = cv2.imread(filename)
    img_array.append(img)

out = cv2.VideoWriter('Video_No_Audio.mp4',cv2.VideoWriter_fourcc(*'XVID'),1,(2560,1440))
#55 photes in folder = 55 sec
each_image_duration =int(input("Enter the Seconds in video: "))
for _ in range(each_image_duration):
    out.write(img_array[0])
cv2.destroyAllWindows()
out.release()
def combine_audio(vidname, audname, outname, fps=1):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)
combine_audio("Video_No_Audio.mp4", "Audio.aac", "Output_Final_Video.mp4")