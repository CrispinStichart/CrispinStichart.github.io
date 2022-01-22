---
layout: post
title:  "ROT13ing your Clipboard"
---

(Spoiler alert: I made [a program](https://github.com/CrispinStichart/rot13_clipboard) that ROT13s the contents of your clipboard. This post talks about technical details behind that.)

I was reading the [Wikipedia article on spoilers][spoiler] (as in, the concept of spoiling the ending of a piece of media) and read that, back in the day, Usenet users would sometimes obscure spoilers through the use of [ROT13][rot13_wiki]. 

[spoiler]: https://en.wikipedia.org/wiki/Spoiler_(media)
[rot13_wiki]: https://en.wikipedia.org/wiki/ROT13

ROT13 is a simple "substitution cipher". If you imagine the alphabet printed on a bracelet, for every letter in the text you're trying to encrypt, you find the letter on the bracelet, rotate the bracelet by thirteen characters, and substitute that letter. Since there are 26 letters in the alphabet, running the encrypted text back through the same ROT13 cipher will unencrypt the text. 

As an example, the sentence "Snape kills Dumbledore" is, when ROT13'd, "Fancr xvyyf Qhzoyrqber." It's not what you want to use to encrypt the nuclear launch codes, but it works great to obscure text that you want people to be able to read if they put in a bit of effort. Basically it's the digital equivalent of writing something upside down. I think I may have seen ROT13 used for hiding spoilers here and there, but it's not common. Reddit and Discord are two notable platforms that have spoiler functionality built in -- with both, the text is blacked out until you mouse over it.

But in this year of our Lord 2021, how do you go about ROT13ing a spoiler? Well, I've always used one of the many online tools. Googling `rot13` brings up many hits, with the first one being [rot13.com][rot13], which is exactly what you'd expect. But what if you're lazy? What if your internet isn't working, but you still want to compose a Usenet post that reveals the ending of the new Spiderman film?

[rot13]: https://rot13.com/

Introducing: ROT13 Clipboard, a program that ROT13s the contents of your clipboard! (Only on Windows for now.)

It was easier than expected. I decided to use Python, and some quick googling about accessing the clipboard brought me to [`pywin32`][pywin] which as the name suggests is a python wrapper for the win32 API. I was only interested in the Clipboard functionality, which is a small module with only a [handful of functions][pywin_clip_docs].  I was worried at first, reading the docs. Most of the functions accepted or returned an integer ID of a window, and there's something called a clipboard chain, and I wasn't sure what a "clipboard viewer" was in this context... so I just tossed some things into a python file, ignored the window ID stuff, and lo and behold, it actually worked. 

[pywin]:  https://pypi.org/project/pywin32/
[pywin_clip_docs]: https://mhammond.github.io/pywin32/win32clipboard.html

Here's the relevant code (note that I imported `win32clipboard` as `clip`):

```python
clip.OpenClipboard()
s = clip.GetClipboardData(clip.CF_UNICODETEXT)
s = rot13(s)
clip.EmptyClipboard()
clip.SetClipboardText(s, clip.CF_UNICODETEXT)
clip.CloseClipboard()
```

At this point, I wasn't really sure *how* it was working, but since it *was* working, I moved onto triggering the script via a hotkey. 

It turns out that Windows does have built in support for this, via an unlikely path: the humble shortcut. If you create a shortcut, right-click and open the properties window. There will be a "Shortcut key" text box, and you simply need to click the box and then type a key. To actually get it to work, you have to put it on the desktop or in the startup directory[^1]. You're also restricted to only using ctrl-alt-whatever shortcuts. The worst thing, however, is the multi-second lag between activating the shortcut and the script actually running. The [official explanation][shortcut_lag] for this is that the Explorer process that handles shortcut keys has to iterate through all open applications to see if one of them is already using the shortcut. If any of them are slow to respond, this will cause the noticeable lag.

[^1]: You can find the startup directory by opening the run dialog with Win+R and typing `shell:startup`.

[shortcut_lag]: https://devblogs.microsoft.com/oldnewthing/20120502-00/?p=7723


The work-around is to use [AutoHotKey][autohotkey]. It has a very powerful scripting language for the creation of macros, but I just needed this (half of which is the default boilerplate):

[autohotkey]: https://www.autohotkey.com/


```
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; ctrl-alt-P -- you can change this to whatever.
^!p::
    ; Note the use of pythonw to prevent a console window from appearing.
    Run, .\venv\Scripts\pythonw.exe rot13.py
    return
```

And that was that -- I had my working ROT13 script triggered by a hotkey. 

That's what I love about programming in the modern day: so much work has already been done for you, all you have to do is plug things together in the right order. No reinventing the wheel, just pure problem solving. However, this was intended as a learning exercise, so I decided to figure out the mysteries of the clipboard API, like what the window IDs were for and what the clipboard chain was. The `pywin32` docs are slim, but that's okay because we can go straight to the [Microsoft documentation for the API][clipboard_api_docs].

[clipboard_api_docs]: https://docs.microsoft.com/en-us/windows/win32/dataxchg/clipboard

The clipboard chain turns out to be a linked list of clipboard viewers, which in turn are windows that receive messages whenever the contents of the clipboard change. ("Windows" is the keyword, more on that in a moment.)  Strangely enough, it's the application's duty to manage the chain and keep it properly linked. And when it gets a message that the clipboard changed (specifically the `WM_DRAWCLIPBOARD` message) it needs to pass this message on to the next window in the chain. 

So, wait, messages? How do I receive messages? I went down a rabbit hole looking into [COM][COM_docs], which seems... complicated, to say the least. And the [tutorial][tutorial_archive] linked from the `pywin32` documentation is long gone, and requires the Wayback Machine to read it. Luckily, the messages the clipboard documentation is talking about are actually tied to the GUI API and have nothing to do with COM. 

I found a very helpful [example program][python_clipboard] that fully implements a simple clipboard viewer. It uses wxWidgets to create a window. I tried it out, and it works perfectly even after deleting `frame.Show()`, which is what actually makes the window appear. I'm sure it's possible to initialize a window object without resorting to an entire toolkit, but I do not know how. 

[python_clipboard]: https://code.activestate.com/recipes/355593-windows-clipboard-viewer/
[tutorial_archive]: https://web.archive.org/web/20090130004155/http://thor.prohosting.com/~pboddie/Python/COM.html
[COM_docs]: https://docs.microsoft.com/en-us/windows/win32/com/com-objects-and-interfaces


This was a fun little project. I'm not sure if I'll ever use this knowledge for anything truly useful, but I might! This same basic idea of editing your clipboard could be handy for certain macros... perhaps that will be a future blog post. We'll see!

**Github Repo:** [https://github.com/CrispinStichart/rot13_clipboard](https://github.com/CrispinStichart/rot13_clipboard)