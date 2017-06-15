import eyed3
from pygame import mixer

class Song():

	def __init__(self,location):
		mixer.init()
		self._location = location
		audiofile = eyed3.load(location)
		self._title = audiofile.tag.title
		self._artist = audiofile.tag.artist
		self._album = audiofile.tag.album

	def play(self):
		mixer.music.load(self._location)
		mixer.music.play()
		return True

	def pause(self):
		mixer.music.pause()
		return True

	def unpause(self):
		mixer.music.unpause()
		return True

	def stop(self):
		mixer.music.stop()
		return True

	def get_title(self):
		return self._title

	def get_artist(self):
		return self._artist

	def get_album(self):
		return self._album

	def display_song_info(self):
		print '\n','-'*27,'SONG','-'*27
		print self.get_title()
		print self.get_artist()
		print self.get_album(),'\n'

