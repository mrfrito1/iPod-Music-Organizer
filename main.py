import os
from mutagen.mp4 import MP4
import tkinter as tk
from tkinter import ttk
from threading import Thread

def update_progress(progress, value):
    progress['value'] = value
    progress.update_idletasks()

def rename_files(folder, progress):
    """
    Renames .m4a files in a specific folder using the song title extracted from the metadata contained in those files.
    
    Args:
        folder (str): Path of the folder containing the .m4a files
        progress (ttk.Progressbar): Progress bar to update
    """
    total_files = sum([len(files) for r, d, files in os.walk(folder) if any(file.endswith('.m4a') for file in files)])
    processed_files = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.m4a'):
                file_path = os.path.join(root, file)
                try:
                    audio = MP4(file_path)
                    title = audio.tags['\xa9nam'][0]
                    title = title.replace('/', '_').replace('\\', '_').replace(':', '_')
                    new_name = f"{title}.m4a"
                    try:
                        os.rename(file_path, os.path.join(root, new_name))
                        print(f"File {file} renamed to {new_name}")
                    except Exception as e:
                        print(f"Error renaming file {file}: {e}")
                except Exception as e:
                    unknown_folder = os.path.join(folder, 'Unknown')
                    if not os.path.exists(unknown_folder):
                        os.makedirs(unknown_folder)
                    try:
                        os.rename(file_path, os.path.join(unknown_folder, file))
                        print(f"File {file} moved to {unknown_folder}")
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")
                
                processed_files += 1
                update_progress(progress, (processed_files / total_files) * 100)

def reorganize_files(folder, progress):
    """
    Reorganizes .m4a files in a specific folder into subfolders based on the artist and then by album.
    
    Args:
        folder (str): Path of the folder containing the .m4a files
        progress (ttk.Progressbar): Progress bar to update
    """
    total_files = sum([len(files) for r, d, files in os.walk(folder) if any(file.endswith('.m4a') for file in files)])
    processed_files = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.m4a'):
                file_path = os.path.join(root, file)
                try:
                    audio = MP4(file_path)
                    artist = audio.tags['\xa9ART'][0].replace('/', '_').replace('\\', '_').replace(':', '_')
                    album = audio.tags['\xa9alb'][0].replace('/', '_').replace('\\', '_').replace(':', '_')
                    
                    artist_folder = os.path.join(folder, artist)
                    if not os.path.exists(artist_folder):
                        os.makedirs(artist_folder)
                    
                    album_folder = os.path.join(artist_folder, album)
                    if not os.path.exists(album_folder):
                        os.makedirs(album_folder)
                    
                    try:
                        os.rename(file_path, os.path.join(album_folder, file))
                        print(f"File {file} moved to {album_folder}")
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")
                except Exception as e:
                    unknown_folder = os.path.join(folder, 'Unknown')
                    if not os.path.exists(unknown_folder):
                        os.makedirs(unknown_folder)
                    try:
                        os.rename(file_path, os.path.join(unknown_folder, file))
                        print(f"File {file} moved to {unknown_folder}")
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")

                processed_files += 1
                update_progress(progress, (processed_files / total_files) * 100)

def run_tasks():
    folder = 'Folder'

    # Create a Tkinter window
    root = tk.Tk()
    root.title("File Renaming and Organizing")

    # Create a progress bar
    progress = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
    progress.pack(padx=10, pady=10)

    # Run renaming and reorganizing tasks in separate threads
    rename_thread = Thread(target=rename_files, args=(folder, progress))
    rename_thread.start()
    rename_thread.join()  # Wait for the renaming task to complete

    reorganize_thread = Thread(target=reorganize_files, args=(folder, progress))
    reorganize_thread.start()

    # Start the Tkinter event loop
    root.mainloop()

# Run the Tkinter application
run_tasks()
