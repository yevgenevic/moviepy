import moviepy.editor

video = moviepy.editor.VideoFileClip('my.mp4')
audio = video.audio
audio.write_audiofile('my_audio.mp3')
