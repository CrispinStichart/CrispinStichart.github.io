---
layout: post
title:  "Backing Up My Notes To GitHub"
---

Somewhat recently I started using [Obsidian][obsidian] as my note-taking app, and -- simultaneously -- taking way more notes. Before, I was just using Google Keep, which works well enough for short things. I don't know how I heard about it, but at some point Obsidian came to my attention, and I remember thinking that the graph view, that shows you the web of interconnections of related notes, was super neat. So I downloaded it, fiddled around, and never actually used it.

Fast forward a year and, as I started working on a bunch of different coding projects, I realized that I needed to start writing things down about what I was doing, so when I dropped a project for a few weeks, I could actually come back to it and quickly get back up to speed.

This was a roaring success, and I started taking way more notes, on way more things. I now have a note that consolidates all the information on my car, including maintenance notes like when I changed the oil, and what tools I own. Obsidian is a fully-featured Markdown editor, so it's easy to write notes that are organized and very clear.

Honestly, I'm kind of amazed that it took me this long to figure out that "writing stuff down is good, actually." I mean, I'd had some notes for things scattered across various platforms -- Google Sheets/Docs, and Keep, mainly -- but having them organized and more readable is a major improvement, and lowers the friction creating and editing them to almost nothing.

## Backups

The best thing about Keep was that I knew I'd never lose them (well, as long as Google never nuked my account). I don't have a general backup solution in place on my computer, just because most things are already in the cloud somewhere.

For a bunch of markdown documents, GitHub seemed like a logical choice. Even free accounts get unlimited private repositories, so I created one and pushed my notes to it. Step 1, complete. Step 2, automate it. But how?

My first thought was a cronjob, and my second thought was that maybe systemd has something similar. Which it does -- [timers][timers]. I like living in the future, so I spent at least an hour trying to get timers to work, but couldn't get past a permissions issue. So I gave up on that and a few minutes later had a cronjob working.

Here's backup script:

```sh
#!/bin/bash
set -euo pipefail

cd "$(dirname -- "$(readlink -f "${BASH_SOURCE}")")"

git add -A
git commit -m "Automatic Backup"
git push
```

Adding a cronjob was surprisingly easy. I'd actually never used cron before, and I thought I'd be editing a file, but actually you don't touch the files yourself, you run `crontab -e` which opens a file in your default editor. Mine looks like:

```
0 14 * * * /home/critter/Documents/Notes/auto_commit.sh >> ~/crontab.log
```

This will run the backup script every day at 2PM. I chose 2PM because my computer is almost always on at that time. Note that when you save this file, the default save location is a random file in `/tmp` -- this is normal, and the save location doesn't actually matter, because as soon as it's saved to wherever, cron will copy it to `/var/spool/cron/<username>`.

And that's it! It just works!

I found out later that I could use anacron to ensure that the script would run daily even if I missed the 2PM window, but for this task, cron is good enough.

[obsidian]: https://obsidian.md/
[timers]: https://wiki.archlinux.org/title/Systemd/Timers