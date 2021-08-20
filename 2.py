from moviepy  import editor 
video=editor.VideoFileClip('mirize.mp4')
video.audio.write_audiofile('mirize.mp3')