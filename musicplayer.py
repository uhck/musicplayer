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
		self._active_play_list = []
		#self.run_state_machine()

	def run_state_machine(self):
		exit = False
		while not exit:
			exit = self.process_action(main_menu,self.open_main_menu())
			
	def get_answer(self,min_i,max_i):
		ans = int(raw_input('Enter: '))
		while ans < min_i or ans > max_i:
			ans = int(raw_input('Enter: '))
		return ans-1

	def process_action(self,menu,action):
		if action == len(menu):
			return True
		return menu[action](self)

	def open_main_menu(self):
		main_menu = [MusicPlayer.open_library, MusicPlayer.open_playlists, MusicPlayer.open_search, MusicPlayer.exit]
		print '\n','-'*27,'MAIN MENU','-'*27
		print "1) Open Library"
		print "2) Open Playlists"
		print "3) Search"
		print "4) Exit\n"
		return self.get_answer(1,4)

	def open_playlists(self):
		playlists_menu = [MusicPlayer.add_playlist, MusicPlayer.delete_playlist, MusicPlayer.listen_to_playlist, MusicPlayer.add_song_to_playlist, MusicPlayer.remove_song_from_playlist, MusicPlayer.exit]
		go_back = False
		while not go_back:
			playlists = self._user.get_playlists_list()
			size = len(playlists)
			print '-'*27,'PLAYLISTS','-'*27
			if len(playlists) == 0:
				print "No playlist to display."
				return
			for i in range(0,len(playlists)):
				print str(i+1)+") Open", playlists[i]
			print '\n','-'*27,'PLAYLISTS MENU:','-'*27
			print '1) Create New Playlist'
			print '2) Delete Playlist'
			print '3) Listen To Playlist'
			print '4) Add Song To Playlist'
			print '5) Delete Song From Playlist'
			print '6) Return To Main Menu\n'
			ans = self.get_answer(1,6)
			go_back = self.process_action(playlists_menu,ans)
		return False
		
	def open_playlist(self,title,song_list):
		playlist_menu = [MusicPlayer.open_song, MusicPlayer.listen_to_playlist, MusicPlayer.exit]
		go_back = False
		while not go_back:
			display_songlist(title,song_list)
			print '\n','-'*27,'PLAYLIST MENU:','-'*27
			print '1) Open Song'
			print '2) Listen to Playlist'
			print '3) Return To Main Menu\n'
			ans = self.get_answer(1,3)
			go_back = self.process_action(playlist_menu,ans)
		return False

	def open_song(self,i):
		song_menu = [MusicPlayer.play_song, MusicPlayer.skip_song, MusicPlayer.like_song, MusicPlayer.dislike_song, MusicPlayer.add_song_to_playlist, MusicPlayer.remove_song_from_playlist, MusicPlayer.exit]
		go_back = False
		while not go_back:
			self._library[i].display_song_info()
			print '\n','-'*27,'SONG MENU','-'*27
			print '1) Play Song'
			print '2) Skip Song'
			print '3) Like Song'
			print '4) Dislike Song'
			print '5) Add Song To Playlist'
			print '6) Remove Song From Playlist'
			print '7) Return To Main Menu\n'
			ans = self.get_answer(1,7)
			go_back = self.process_action(song_menu,ans)
		return False	

	def open_library(self):
		library_menu = [MusicPlayer.open_song, MusicPlayer.listen_to_library, MusicPlayer.exit]
		go_back = False
		while not go_back:
			self.display_songlist('LIBRARY',range(0,len(self._library)))
			print '\n','-'*27,'LIBRARY MENU','-'*27
			print '1) Open Song'
			print '2) Listen To Library'
			print '3) Back to Main Menu\n'
			ans = self.get_answer(1,3)
			go_back = self.process_action(library_menu,ans)
		return False

	def open_search(self):
		search_type_menu = [MusicPlayer.search_by_title, MusicPlayer.search_by_artist, MusicPlayer.search_by_album, MusicPlayer.exit]
		go_back = False
		while not go_back:
			print '-'*27,'SEARCH','-'*27
			print '1) By Song Title'
			print '2) By Artist'
			print '3) By Album'
			print '4) Back to Main Menu\n'
			ans = self.get_answer(1,4)
			go_back = self.process_action(search_type_menu,ans)
		return False

	def search_by_title(self):
		search_menu = [MusicPlayer.open_song, MusicPlayer.exit]
		title = raw_input('Search song title: ')
		go_back = False
		while not go_back:
			results = [i for i in range(0,len(self._library)) if self._library[i].get_title().find(title) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			print '\n','-'*27,'SEARCH MENU','-'*27
			print '1) Open Song'
			print '2) Back to Main Menu\n'
			ans = self.get_answer(1,2)
			go_back = self.process_action(search_menu,ans)
		return False

	def search_by_artist(self):
		search_menu = [MusicPlayer.open_song, MusicPlayer.exit]
		artist = raw_input('Search artist: ')
		go_back = False
		while not go_back:
			results = [i for i in range(0,len(self._library)) if self._library[i].get_artist().find(artist) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			print '\n','-'*27,'SEARCH MENU','-'*27
			print '1) Open Song'
			print '2) Back to Main Menu\n'
			ans = self.get_answer(1,2)
			go_back = self.process_action(search_menu,ans)
		return False

	def search_by_album(self):
		search_menu = [MusicPlayer.open_song, MusicPlayer.exit]
		album = raw_input('Search album: ')
		go_back = False
		while not go_back:
			results = [i for i in range(0,len(self._library)) if self._library[i].get_album().find(album) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			print '\n','-'*27,'SEARCH MENU','-'*27
			print '1) Open Song'
			print '2) Back to Main Menu\n'
			ans = self.get_answer(1,2)
			go_back = self.process_action(search_menu,ans)
		return False

	def listen_to_library(self):
		pass

	def listen_to_playlist(self):
		pass

	def add_playlist(self):
		pass

	def delete_playlist(self):
		pass

	def add_song_to_playlist(self,song):
		pass

	def remove_song_from_playlist(self,song):
		pass

	def play_song(self,song):
		self._library[song].play()

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



	def display_songlist(self,title,songs):
		print '-'*27,title,'-'*27
		for i in range(0,len(songs)):
			print (str(i+1)+')').ljust(4), self._library[songs[i]].get_title().ljust(25), self._library[songs[i]].get_artist().ljust(25), self._library[songs[i]].get_album().ljust(25)

	def exit(self):
		return True
