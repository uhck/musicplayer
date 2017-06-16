from user import User
from song import Song
import random
import os

class MusicPlayer():

	#---------------------------------------------------------------- Initializes class variables
	def __init__(self,songs_file):
		os.system('clear')
		#------------------------------------- Library fills up from text file listing song paths
		f = open(songs_file, 'r')
		lines = f.readlines()
		self._library = []
		[self._library.append(Song(line.split()[0])) for line in lines]
		#----------------------------------------------------------- User inputs desired username
		self._user = User(raw_input('USERNAME: '))
		#------------------------------------------------ Initialize active variables for library
		self._active_song = None
		self._active_playlist = range(0,len(self._library))
		self._active_playlist_name = 'LIBRARY'
		self.run_state_machine()

	#----------------------------- Runs the music player's state machine - uses main menu as home
	def run_state_machine(self):
		print 'Hello', self._user.get_username()
		menu = [MusicPlayer.open_library, MusicPlayer.open_playlists, \
				MusicPlayer.open_search, MusicPlayer.exit]
		exit = False
		#------------------------------------------- While exit is false, continue to run program
		while not exit:
			exit = self.process_action(menu,self.open_main_menu())

	#----------------------------------- Calls functions stored in menu lists based on user input
	def process_action(self,menu,action):
		if action >= len(menu):
			return True
		return menu[action](self)

	#--------------------------------------------------- Prints the main menu and gets user input
	def open_main_menu(self):
		os.system('clear')
		print_menu_index = [0,1,2,3]
		self.display_menu('MAIN MENU', print_menu_index)
		return self.get_answer('Enter Menu Selection:',1,4)

	#----------------------------------------- Prints user's playlists and responds to user input
	def open_playlists(self):
		os.system('clear')
		menu = [MusicPlayer.add_playlist, MusicPlayer.delete_playlist, MusicPlayer.open_playlist, \
				MusicPlayer.exit]
		print_menu_index = [4,5,20,9]
		#----------------------------------- While go_back is false, let user work with playlists
		go_back = False
		while not go_back:
			playlists = self._user.get_playlists_list()
			#------------------------------------------------- Prints list of playlists plus menu
			print '-'*27,'PLAYLISTS','-'*27
			if len(playlists) == 0:
				print "You have no playlists."
			for i in range(0,len(playlists)):
				print str(i+1)+")", playlists[i]
			self.display_menu('PLAYLISTS MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False
		
	#--------------------------------- Prints songs in user's playlist and responds to user input
	def open_playlist(self):
		menu = [MusicPlayer.open_song, MusicPlayer.listen_to_playlist, \
				MusicPlayer.delete_playlist, MusicPlayer.add_song_to_playlist, \
				MusicPlayer.remove_song_from_playlist, MusicPlayer.exit]
		print_menu_index = [10,6,5,7,8,9]
		#---------------------------------------------------------- Gets name of playlist to view
		ans = ''
		while (ans not in self._user.get_playlists_list()) or (ans == ''):
			ans = raw_input('Enter Name of Playlist To Open (Cancel to cancel): ')
			if ans == 'Cancel':
				return False
		#------------------------------------------------------- Set up active playlist variables
		self._active_playlist = self._user.get_playlist(ans)
		self._active_playlist_name = ans
		go_back = False
		#------------------------------------ While go_back is false, let user work with playlist
		while not go_back:
			self.display_songlist(self._active_playlist_name,self._active_playlist)
			self.display_menu('PLAYLIST MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False

	#---------------------------------- Prints active song information and responds to user input
	def open_song(self):
		menu = [MusicPlayer.play_song, MusicPlayer.skip_song, MusicPlayer.stop_song, \
				MusicPlayer.like_song, MusicPlayer.dislike_song, \
				MusicPlayer.add_song_to_playlist, MusicPlayer.remove_song_from_playlist, \
				MusicPlayer.exit]
		print_menu_index = [11,12,19,13,14,7,8,9]
		#------------------------ Display active song info and validates active song and playlist
		if self._active_playlist == []:
			return False
		self.display_songlist(self._active_playlist_name,self._active_playlist)
		if self._active_song == None:
			print "Select a song to open."
			self._active_song = self.get_answer('Enter Song Selection:',1,len(self._active_playlist))
		go_back = False
		#---------------------------------------- While go_back is false, let user work with song
		while not go_back:
			os.system('clear')
			print 'Currently playing index:', self._active_song
			self._library[self._active_song].display_song_info()
			self.display_menu('SONG MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return True	

	#----------------------------------- Prints library songs and menu and responds to user input
	def open_library(self):
		os.system('clear')
		menu = [MusicPlayer.open_song, MusicPlayer.listen_to_library, \
				MusicPlayer.exit]
		print_menu_index = [10,15,9]
		go_back = False
		#------------------------------------- While go_back is false, let user work with library
		while not go_back:
			self.display_songlist('LIBRARY',range(0,len(self._library)))
			self.display_menu('LIBRARY MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False

	#------------------------------------------- Prints search options and responds to user input
	def open_search(self):
		os.system('clear')
		menu = [MusicPlayer.search_by_title, MusicPlayer.search_by_artist, \
				MusicPlayer.search_by_album, MusicPlayer.exit]
		print_menu_index = [16,17,18,9]
		go_back = False
		#-------------------------------------- While go_back is false, let user work with search
		while not go_back:
			self.display_menu('SEARCH MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False

	#---------------------------------------------------------------- Searches for songs by title
	def search_by_title(self):
		menu = [MusicPlayer.open_song, MusicPlayer.exit]
		print_menu_index = [10,9]
		title = raw_input('Search song title: ')
		go_back = False
		#------------------------------------ While go_back is false, let user search for results
		while not go_back:
			results = [i for i in range(0,len(self._library)) \
					   if self._library[i].get_title().find(title) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			self.display_menu('SEARCH MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False

	#--------------------------------------------------------------- Searches for songs by artist
	def search_by_artist(self):
		menu = [MusicPlayer.open_song, MusicPlayer.exit]
		print_menu_index = [10,9]
		artist = raw_input('Search artist: ')
		go_back = False
		#------------------------------------ While go_back is false, let user search for results
		while not go_back:
			results = [i for i in range(0,len(self._library)) \
					   if self._library[i].get_artist().find(artist) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			self.display_menu('SEARCH MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False

	#---------------------------------------------------------------- Searches for songs by album
	def search_by_album(self):
		menu = [MusicPlayer.open_song, MusicPlayer.exit]
		print_menu_index = [10,9]
		album = raw_input('Search album: ')
		go_back = False
		#------------------------------------ While go_back is false, let user search for results
		while not go_back:
			results = [i for i in range(0,len(self._library)) 
					   if self._library[i].get_album().find(album) >= 0]
			self.display_songlist('SEARCH RESULTS',results)
			self.display_menu('SEARCH MENU', print_menu_index)
			#------------------------------------------------------------------ Gets user's input
			ans = self.get_answer('Enter Menu Selection:',1,len(menu))
			go_back = self.process_action(menu,ans)
		return False

	#-------------------------------------- Shuffles library songs into a playlist and plays them
	def listen_to_library(self):
		os.system('clear')
		self._active_playlist_name = 'LIBRARY'
		#----------------------------- Sets active playlist to library and shuffles library songs
		self._active_playlist = random.sample(range(len(self._library)),len(self._library))
		self.display_songlist('LIBRARY',self._active_playlist)
		#------------------------------------------------------------ For loop runs through songs
		for song_index in self._active_playlist:
			self._active_song = song_index
			self.play_song()
			stop = self.open_song()
			if stop:
				break
		return False

	#----------------------------------------------------- Shuffles playlist songs and plays them
	def listen_to_playlist(self):
		os.system('clear')
		#---------------------------------------------------- Ensures there are songs in playlist
		if len(self._active_playlist) == 0:
			print "No songs in playlist."
			return False
		#------------------------------------------------------------ For loop runs through songs
		for song_index in self._active_playlist:
			self._active_song = song_index
			self.play_song()
			stop = self.open_song()
			if stop:
				break
		return False

	#---------------------------------------------------- Adds a new playlist to user's playlists
	def add_playlist(self):
		name = ''
		while name == '':
			name = raw_input('New Playlist Name (Cancel to cancel): ')
			if name == 'Cancel':
				return False
		self._user.add_playlist(name)
		return False

	#--------------------------------------------------- Deletes a playlist from user's playlists
	def delete_playlist(self):
		if self._user.get_playlists_list() == []:
			print 'You have no playlists.'
			return False
		name = ''
		while name == '':
			name = raw_input('Name Of Playlist To Remove (Cancel to cancel): ')
			if name == 'Cancel':
				return False
		self._user.delete_playlist(name)
		return False

	#------------------------------------------------ Adds a specified song to specified playlist
	def add_song_to_playlist(self):
		#------------------------------------------------------ Gets user input if no active song
		if self._active_song == None:
			self.display_songlist('LIBRARY',range(len(self._library)))
			self._active_song = self.get_answer('Enter Song Selection:',1,len(self._library))
		#-------------------------------------------------- Gets user input if no active playlist
		while self._active_playlist_name not in self._user.get_playlists_list():
			self._active_playlist_name = raw_input('Enter Playlist Selection (Cancel to cancel): ')
			if self._active_playlist_name == 'Cancel':
				return False
		#------------------------------------------------------------------------------ Adds song
		self._active_playlist = self._user.add_song_to_playlist(self._active_playlist_name, \
																self._active_song)
		self._active_song = None
		return False

	#------------------------------------------- Removes a specified song from specified playlist
	def remove_song_from_playlist(self):
		#-------------------------------------------------- Gets user input if no active playlist
		if self._active_playlist_name == '' or self._active_playlist_name == 'LIBRARY':
			while self._active_playlist_name not in self._user.get_playlists_list():
				self._active_playlist_name = raw_input('Enter Playlist Selection (Cancel to \
														cancel): ')
		self._active_playlist = self._user.get_playlist(self._active_playlist_name)
		self.display_songlist(self._active_playlist_name,self._active_playlist)
		#------------------------------------------------------ Gets user input if no active song
		if self._active_song == None or self._active_song not in self._active_playlist:
			self._active_song = self.get_answer('Enter Song Selection (Cancel to cancel):', \
													   1,len(self._library))
		self._active_playlist = self._user.remove_song_from_playlist(self._active_playlist_name, \
													self._active_playlist[self._active_song])
		self._active_song = None
		return False

	#----------------------------------------------------------------------- Plays specified song
	def play_song(self):
		self._library[self._active_song].play()
		return False

	#------------------------------------ Skips specified song if playing from an active playlist
	def skip_song(self):
		if self._active_song != None and len(self._active_playlist) > 0:
			self._library[self._active_song].stop()
		return True

	#--------------------------------------------------------------- Stops playing specified song
	def stop_song(self):
		self._library[self._active_song].stop()
		return False

	#---------------------------------------------------------------------- Add song to like list
	def like_song(self):
		if self._active_song != None:
			self._user.add_like_song(self._active_song)
			print 'You liked', '"', self._library[self._active_song].get_title(), 'by', \
				  self._library[self._active_song].get_artist(), '"'

	#------------------------------------------------------------------- Add song to dislike list
	def dislike_song(self):
		if self._active_song != None:
			self._user.add_dislike_song(self._active_song)
			print 'You disliked', '"', self._library[self._active_song].get_title(), 'by', \
				  self._library[self._active_song].get_artist(), '"'

	#------------------------------------------ Gets integer answer between specified min and max
	def get_answer(self,message,min_i,max_i):
		ans = raw_input(message+' ')
		while (not ans.isdigit()) or int(ans) < min_i or int(ans) > max_i:
			ans = raw_input(message+' ')
		return int(ans)-1

	#---------------------------------------------- Displays menu options based on given scenario
	def display_menu(self,title,opts):
		# 0 1 2 3 \ 4 5 6 \ 7 8 \ 9 10 11 12 \ 13 14 15 16 \ 17 18 19 20
		opts_list = ['Open Library', 'Open Playlists', 'Search', 'Exit', \
					 'Create New Playlist', 'Delete Playlist', 'Listen To Playlist', \
			 		 'Add Song To Playlist', 'Remove Song From Playlist', \
					 'Go Back', 'Open Song', 'Play Song', 'Skip Song', \
					 'Like Song', 'Dislike Song', 'Listen To Library','By Song Title', \
					 'By Artist','By Album', 'Stop Song', 'Open Playlist']
		print ''
		print '-'*27,title,'-'*27
		for i in range(0,len(opts)):
			print str(i+1)+')', opts_list[opts[i]]
		print ''

	#--------------------------------------------- Prints song title, artist, and album in a list
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

	#---------------------------------------------------------------------- Returns true to  exit
	def exit(self):
		self.stop_song()
		return True

#-------------------------------------------------------------------------------------- MAIN MENU
MusicPlayer('songs.txt')
