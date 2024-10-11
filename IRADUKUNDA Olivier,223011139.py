from collections import deque

class MusicPlaylistManager:
    def __init__(self):
        self.playlist = []  
        self.undo_stack = []  
        self.song_requests = deque() 
    
    def add_song_to_playlist(self, song):
        self._save_state()  
        self.playlist.append(song)
        print(f'Song "{song}" added to playlist.')
    
    
    def remove_song_from_playlist(self, song):
        if song in self.playlist:
            self._save_state()  
            self.playlist.remove(song)
            print(f'Song "{song}" removed from playlist.')
        else:
            print(f'Song "{song}" not found in the playlist.')
    
    
    def get_current_playlist(self):
        return self.playlist
    
    
    def add_song_request(self, song):
        self.song_requests.append(song)
        print(f'Song request "{song}" added to the queue.')
    
    
    def play_next_request(self):
        if self.song_requests:
            next_song = self.song_requests.popleft()
            print(f'Now playing requested song: "{next_song}".')
            return next_song
        else:
            print("No song requests in the queue.")
            return None
    
    def undo_last_change(self):
        if self.undo_stack:
            self.playlist = self.undo_stack.pop()
            print("Last change undone.")
        else:
            print("No changes to undo.")
    
    
    def _save_state(self):
        self.undo_stack.append(self.playlist.copy())  # Save a copy of the current playlist

if __name__ == "__main__":
    manager = MusicPlaylistManager()


    manager.add_song_to_playlist("Song A")
    manager.add_song_to_playlist("Song B")
    print("Current Playlist:", manager.get_current_playlist())

    
    manager.remove_song_from_playlist("Song A")
    print("Current Playlist:", manager.get_current_playlist())

    manager.undo_last_change()
    print("Current Playlist after undo:", manager.get_current_playlist())


    manager.add_song_request("Song X")
    manager.add_song_request("Song Y")

    
    manager.play_next_request()
    manager.play_next_request()
    manager.play_next_request()  
