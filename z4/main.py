from pydub import AudioSegment
from pydub.effects import speedup

sound = AudioSegment.from_file("mus.wav", format="wav")
playback_speed = int(input('Введите желаемую скорость (1=изначальная) '))
new_sound = speedup(sound, playback_speed, chunk_size=150, crossfade=30)
new_filename = "changed_mus.wav"
new_sound.export(new_filename, format="wav")