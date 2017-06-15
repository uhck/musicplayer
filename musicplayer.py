from user import User
from song import Song
import random
import os

class MusicPlayer():

	def __init__(self,songs_file):
		f = open(songs_file, 'r')
		lines = f.readlines()
		self._library = []
		[self._library.append(Song(line.split()[0])) for line in lines]
		self._user = User(raw_input('Username: '))
		self._currently_playing = None
		self._active_playlist = []
		#self.run_state_machine()

	def run_state_machine(self):
		print 'Hello', self._user.get_username()
		menu = [MusicPlayer.open_library, MusicPlayer.open_playlists, \
				MusicPlayer.open_search, MusicPlayer.exit]
		exit = False
		while not exit:
			exit = self.process_action(menu,self.open_main_menu())

	def process_action(self,menu,action):
		if action == len(menu):
			return True
		return menu[action](self)

	def open_main_menu(self):
		os.system('clear')
		print_menu_index = [0,1,2,3]
		self.display_menu('MAIN MENU', print_menu_index)
		return self.get_answer('Enter Menu Selection:',1,4)

	def open_playlists(self):
		os.system('clear')
		menu = [MusicPlayer.add_playlist, MusicPlayer.delete_playlist, \
				MusicPlayer.listen_to_playlist, MusicPlayer.add_song_to_playlist, \
				MusicPlayer.remove_song_from_playlist, MusicPlayer.exit]
		print_menu_index = [4,5,6,7,8,9]
		go_back = False
		while not go_back:
			playlists = self._user.get_playlists_list()
			size = len(playlists)
			print '-'*27,'PLAYLISTS','-'*27
			if len(playlists) == 0:
				print "You have no playlists."
				return
			for i in range(0,len(playlists)):
				print str(i+1)+") Open", playlists[i]
			self.display_menu('PLAYLISTS MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,6)
			go_back = self.process_action(menu,ans)
		return False
		
	def open_playlist(self,title,song_list):
		os.system('clear')
		menu = [MusicPlayer.open_song, MusicPlayer.listen_to_playlist, \
				MusicPlayer.delete_playlist, MusicPlayer.exit]
		print_menu_index = [10,6,5,9]
		go_back = False
		while not go_back:
			self.display_songlist(title,song_list)
			self.display_menu('PLAYLIST MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,3)
			go_back = self.process_action(menu,ans)
		return False

	def open_song(self):
		os.system('clear')
		menu = [MusicPlayer.play_song, MusicPlayer.skip_song, MusicPlayer.stop_song, \
				MusicPlayer.like_song, MusicPlayer.dislike_song, \
				MusicPlayer.add_song_to_playlist, MusicPlayer.remove_song_from_playlist, \
				MusicPlayer.exit]
		print_menu_index = [11,12,19,13,14,7,8,9]
		if self._currently_playing == None:
			print "Select a song to open."
			self._currently_playing = self.get_answer('Enter Song Selection:',1,len(self._library))
		go_back = False
		while not go_back:
			self._library[self._currently_playing].display_song_info()
			self.display_menu('SONG MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,8)
			go_back = self.process_action(menu,ans)
		return False	

	def open_library(self):
		os.system('clear')
		menu = [MusicPlayer.open_song, MusicPlayer.listen_to_library, \
				MusicPlayer.exit]
		print_menu_index = [10,15,9]
		go_back = False
		while not go_back:
			self.display_songlist('LIBRARY',range(0,len(self._library)))
			self.display_menu('LIBRARY MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,3)
			go_back = self.process_action(menu,ans)
		return False

	def open_search(self):
		os.system('clear')
		menu = [MusicPlayer.search_by_title, MusicPlayer.search_by_artist, \
				MusicPlayer.search_by_album, MusicPlayer.exit]
		print_menu_index = [16,17,18,9]
		go_back = False
		while not go_back:
			self.display_menu('SEARCH MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,4)
			go_back = self.process_action(menu,ans)
		return False

	def search_by_title(self):
		menu = [MusicPlayer.open_song, MusicPlayer.exit]
		print_menu_index = [10,9]
		title = raw_input('Search song title: ')
		go_back = False
		while not go_back:
			results = [i for i in range(0,len(self._library)) \
					   if self._library[i].get_title().find(title) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			self.display_menu('SEARCH MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,2)
			go_back = self.process_action(menu,ans)
		return False

	def search_by_artist(self):
		menu = [MusicPlayer.open_song, MusicPlayer.exit]
		print_menu_index = [10,9]
		artist = raw_input('Search artist: ')
		go_back = False
		while not go_back:
			results = [i for i in range(0,len(self._library)) \
					   if self._library[i].get_artist().find(artist) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			self.display_menu('SEARCH MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,2)
			go_back = self.process_action(menu,ans)
		return False

	def search_by_album(self):
		menu = [MusicPlayer.open_song, MusicPlayer.exit]
		print_menu_index = [10,9]
		album = raw_input('Search album: ')
		go_back = False
		while not go_back:
			results = [i for i in range(0,len(self._library)) 
					   if self._library[i].get_album().find(album) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			self.display_menu('SEARCH MENU', print_menu_index)
			ans = self.get_answer('Enter Menu Selection:',1,2)
			go_back = self.process_action(menu,ans)
		return False

	def listen_to_library(self):
		os.system('clear')
		self.display_songlist('LIBRARY',range(len(self._library)))
		self._active_playlist = random.sample(range(len(self._library)),len(self._library))
		for song_index in self._active_playlist:
			self._currently_playing = song_index
			self.play_song()
			self.open_song()
			if self._currently_playing == None:
				break
		return False

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

	def play_song(self):
		self._library[self._currently_playing].play()

	def skip_song(self):
		if self._currently_playing != None and len(self._active_playlist) > 0:
			self._library[self._currently_playing].stop()
		return True

	def stop_song(self):
		self._library[self._currently_playing].stop()

	def like_song(self):
		if self._currently_playing != None:
			self._user.add_like_song(self._currently_playing)
			print 'You liked', '"', self._library[self._currently_playing].get_title(), 'by', \
				  self._library[self._currently_playing].get_artist(), '"'

	def dislike_song(self):
		if self._currently_playing != None:
			self._user.add_dislike_song(self._currently_playing)
			print 'You disliked', '"', self._library[self._currently_playing].get_title(), 'by', \
				  self._library[self._currently_playing].get_artist(), '"'

	def get_answer(self,message,min_i,max_i):
		ans = raw_input(message+' ')
		while (not ans.isdigit()) or int(ans) < min_i or int(ans) > max_i:
			ans = raw_input(message+' ')
		return int(ans)-1

	def display_menu(self,title,opts):
		# 0 1 2 3 \ 4 5 6 \ 7 8 \ 9 10 11 12 \ 13 14 15 16 \ 17 18 19
		opts_list = ['Open Library', 'Open Playlists', 'Search', 'Exit', \
					 'Create New Playlist', 'Delete Playlist', 'Listen To Playlist', \
			 		 'Add Song To Playlist', 'Remove Song From Playlist', \
					 'Return To Main Menu', 'Open Song', 'Play Song', 'Skip Song', \
					 'Like Song', 'Dislike Song', 'Listen To Library','By Song Title', \
					 'By Artist','By Album', 'Stop Song']
		print ''
		print '-'*27,title,'-'*27
		for i in range(0,len(opts)):
			print str(i+1)+')', opts_list[opts[i]]
		print ''

	def display_songlist(self,title,songs):
		print '\n','-'*27,title,'-'*27
		if len(songs) <= 0:
			print 'No songs found.'
			return
		for i in range(0,len(songs)):
			print (str(i+1)+')').ljust(4), self._library[songs[i]].get_title().ljust(25), \
				  self._library[songs[i]].get_artist().ljust(25), \
				  self._library[songs[i]].get_album().ljust(25)
		print ''

	def exit(self):
		self.stop_song()
		self._currently_playing = None
		self._active_playlist = []
		return True
