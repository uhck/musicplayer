class User():

	def __init__(self,user):
		self._username = user
		self._playlists = {}
		self._likes = []
		self._dislikes = []

	def get_username(self):
		return self._username

	def get_playlists_list(self):
		return self._playlists.keys()

	def get_playlist(self,key):
		return self._playlists[key]

	def add_song_to_playlist(self,playlist,song_index):
		self._playlists[playlist].append(song_index)
		return self._playlists[playlist]

	def remove_song_from_playlist(self,playlist,song_index):
		del self._playlists[playlist][self._playlists[playlist].index(song_index)]
		return self._playlists[playlist]

	def add_playlist(self,playlist):
		self._playlists[playlist] = []
		return self.get_playlists_list()

	def delete_playlist(self,playlist):
		del self._playlists[playlist]
		return self.get_playlists_list()

	def add_like_song(self,song_index):
		if song_index not in self._likes:
			self._likes.append(song_index)
			return True
		return False

	def remove_like_song(self,song_index):
		if song_index in self._likes:
			del self._likes[self._likes.index(song_index)]
			return True
		return False

	def add_dislike_song(self,song_index):
		if song_index not in self._dislikes:
			self._dislikes.append(song_index)
			return True
		return False

	def remove_dislike_song(self,song_index):
		if song_index in self._dislikes:
			del self._dislikes[self._dislikes.index(song_index)]
			return True
		return False
