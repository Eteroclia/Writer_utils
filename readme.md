# W(riter)ut(ilities)

Wut is a simple tool to help webnovels writers manage the creation and numbering of their story chapters'.

## Utilization

The script will check what is written in the *master_doc.md* file. It will then split the chapters using a special balise.

**Exemple:**
> this is a chapter[space][space]
> EOC[space][space]
> this is another chapter

The balise EOC (end of chapter) is what allows the program to do its job, and must be placed after every (finished) chapter for it to work.

If you launch the script with the master doc looking like the exemple, you will obtain a numbered chapter in the split_chapters directory and the line "*this is another chapter*" will be left in the master doc.

### Linux
Open a terminal, then make the *linux_launch.sh* executable using `chmod u+x linux_launch.sh` then launch it using `./linux_launch.sh`.

***or***

Open a terminal, then directly launch it using `/bin/bash ./linux_launch.sh`.

You can directly open the terminal in the right place by navigating into the folder using the files manager, clicking the navigation bar and typing `cmd`.

### Windows

Simply launch *windows_launch.bat* by double clicking it.

***or***

Open a terminal, then write `windows_launch.bat`. Your terminal need to be in the folder for the command to work. You can directly open the terminal in the right place by navigating into the folder using the files manager, clicking the navigation bar (middle top) and typing `cmd`.

## The markdown (md) format

Markdown is a powerfull format used instead of simple .txt (text). It allows text to contain title, bold, tables and more, and can be easily converted to HTML for webpages.

Contrary to word or other well known text editor, markdown is not tied to any system, and can thus be used across a wide range of platforms, hence the reason for it's utilization in Wut.
