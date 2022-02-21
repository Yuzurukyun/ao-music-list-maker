# Attorney Online Music List YAML Creator

An Attorney Online Music List YAML Creator, mostly for Danganronpa Online usage. Created in Python with PyQt5 along with QtDesigner.  

Creates a Music List on the reference of Danganronpa Online Roleplay Custom Content.

## Notes

When running the program, you will see a small window pop up. This is the program's interface.

- Menu: Github Page
  - This will redirect you to this Github Page.

- Menu: Tutorial Document
  - This button contains a link where you will be redirected to a [Google Doc](https://docs.google.com/document/d/11gmWUdRREEEPuU4NsORP6iznFtJgbPJbQCuPdhve19c/edit?usp=sharing) document on which it will explain how to use the program.
  
- Load Directory
  - This will load the directory of where you placed your music. This is an important step and it is mandatory for you to read the Google Document given above.
  
- Multi-Directory
  - This will read the entire list of folders within the directory you have loaded and it will use this to look for music instead.

- AO2.8+
  - This will give the audio values of -1 for all the music. Please read the Limitations section of this wiki.

- Prefix
  - This Prefix will act as your subfolder where you place all of the following music in. Please refer to the Google Document given above.

- Format Extensions
  - This will change the suffix/extension of your music in the yaml to a certain extension. Choosing "Original Format" will not change anything inside the yaml.

- Execute
  - Once you've loaded your image files into the program, this button will become available and start the batch automation process.

### Limitations

- Due to Mutagen's behaviour, you can only use MP3 to obtain the audio length. This is not a problem for Attorney Online Users as they do not need an audio length to loop itself. If you are using AO2.8+, please tick "AO2.8+".
- You can't customize Prefixes at this time. A future update may be held to reflect this.

## License

This program is licensed under the AGPLv3 license. 
In short, if you use a modified version of this program, you *must* distribute its source licensed under the AGPLv3 as well, and notify your users where the modified source may be found.

See the [LICENSE](LICENSE.md) file for more information.

