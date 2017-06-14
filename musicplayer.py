from user import User
from song import Song

class MusicPlayer():

	def __init__(self,songs_file):
		f = open(songs_file, 'r')
		lines = f.readlines()
		self._library = []
		[self._library.append(Song(line.split()[0])) for line in lines]
		self._user = User(raw_input('Username: '))
		self._currently_playing = None

		self.run_state_machine()

	def run_state_machine(self):
		#main_menu = [MusicPlayer.open_library(),
		self.display_main_menu()
			

	def display_main_menu(self):
		print '-'*20,'MAIN MENU','-'*20
		print "1)  Open Library"
		print "2)  Open Playlists"
		print "3)  Search"
		print "4)  Shuffle Play"

	def display_playlists(self):
		playlists = self._user.get_playlists_list()
		size = len(playlists)
		print '-'*27,'PLAYLISTS','-'*27
		if len(playlists) == 0:
			print "No playlist to display."
			return False
		for i in range(0,len(playlists)):
			print str(i+1)+") Open", playlists[i]
		print ''
		print str(size)+')', 'Create New Playlist'
		print str(size+1)+')', 'Delete Playlist'
		print str(size+2)+')', 'Listen To Playlist'
		print str(size+3)+')', 'Add Song'
		print str(size+4)+')', 'Delete Song'
		
	def display_songs(self,title,list_of_songs):
		print '-'*27,title,'-'*27
		for i in list_of_songs:
			print (str(i)+')').ljust(4),self._library[i].get_title().ljust(18),self._library[i].get_artist().ljust(18),self._library[i].get_album().ljust(18)

	def display_song_menu(self,i):
		print '-'*27,'SONG','-'*27
		print self._library[i].get_title()
		print self._library[i].get_artist()
		print self._library[i].get_album(), '\n'
		print '1) Play Song'
		print '2) Stop Song'
		print '3) Like Song'
		print '4) Dislike Song'
		print '5) Add Song To Playlist'
		print '6) Remove Song From Playlist'

	def process_action(self,fptrs):
		pass

	def open_library(self):
		pass

	def search_by_title(self,title):
		pass

	def search_by_artist(self,artist):
		pass

	def search_by_album(self,album):
		pass

	def search_for_user(self,user):
		pass

	def add_song_to_playlist(self,song):
		pass

	def delete_song_from_playlist(self,song):
		pass

	def play_song(self,song):
		pass

	def skip_song(self,song):
		pass

	def like_song(self,song_index):
		self._user.add_like_song(song_index)

	def dislike_song(self,song_index):
		self._user.add_dislike_song(song_index)

	def unlike_song(self,song):
		self._user.remove_like_song(song_index)

	def undislike_song(self,song_index):
		self._user.remove_dislike_song(song_index)



