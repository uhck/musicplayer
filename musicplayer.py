from user import User
from song import Song

class MusicPlayer():

	def __init__(self,songs_file):
		f = open(songs_file, 'r')
		lines = f.readlines()
		self._library = []
		[self._library.append(Song(line)) for line in lines]
		self.users = {}
		self.currently_playing = None

	def display_action_menu(self):
		print "MENU"
		print "1) Display library"
		print "2) Search for song"
		print "3) Search for artist"
		print "4) Search for album"
		print "5) Search for users"
		print "6) "
		pass

	def display_search_menu(self):
		pass

	def process_action(self):
		pass

	def search_by_title(self,title):
		pass

	def search_by_artist(self,artist):
		pass

	def search_by_album(self,album):
		pass

	def search_for_user(self,user):
		pass

	def add_song(self,song):
		pass

	def delete_song(self,song):
		pass

	def play_song(self,song):
		pass

	def skip_song(self,song):
		pass

	def like_song(self,song):
		pass

	def dislike_song(self,song):
		pass

