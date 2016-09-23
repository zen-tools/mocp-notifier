mocp-notifier
=====

mocp-notifier is a simple python scripts that shows popup with current track for mocp player.

![screenshot](http://pix.academ.info/images/img/2016/04/23/a82ac81d53eb32b8b977d35d8c6f66bc.gif "mocp-notifier")

Requirements:
```
sudo apt-get install python3-notify2 moc
```

How-to use:

# Download and save notifier.py script under ~/.moc directory. Like this:
~/.moc/notifier.py
# Open ~/.moc/config file and replace next line:
```
# OnSongChange = "/home/jack/.moc/myscript %a %r"
```
with this one:
```
OnSongChange = "/home/zen/.moc/notifier.py -a %a -s %t -r %r -f %f"
```
