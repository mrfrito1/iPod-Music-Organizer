# iPod Music Organizer
=====================

This Python script helps to organize and preserve the original metadata of music files from an iPod using a Tkinter progress bar. It renames files using the song title and reorganizes them into subfolders based on the artist and album.

## Problem Statement
-------------------

When transferring music files from an iPod to a computer, the original metadata (such as song title, artist, and album) is often lost. This script helps to preserve this metadata and organize the files in a logical structure.

## Features
------------

* Renames .m4a files using the song title extracted from the metadata
* Reorganizes files into subfolders based on the artist and album
* Moves files without metadata to an "Unknown" folder
* Preserves the original metadata of the music files
* Displays a Tkinter progress bar for the reorganization process

## How to Use
--------------

1. Clone this repository and navigate to the directory in your terminal/command prompt.
2. Install the required dependencies by running `pip install mutagen`.
3. Run the script by executing `python main.py`.
4. The script will display a Tkinter window with a progress bar. The progress bar will update as the files are renamed and reorganized.

## Why This Script Matters
-------------------------

This script is particularly useful for those who have a large collection of music files from an iPod and want to preserve the original metadata. By reorganizing the files into a logical structure, it makes it easier to find and play specific songs or albums.

## Contributing
------------

If you'd like to contribute to this project, please fork this repository and submit a pull request with your changes. You can also report any issues or suggest new features by creating an issue.
