import vlc
import time

player = vlc.MediaPlayer("Anderson Freire - Raridade (Ao Vivo).mp3")
player.play()

time.sleep(10)  # mantém o programa aberto