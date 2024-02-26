---
layout: post
title:  "Backing up the Kobo Clara Database"
---

I have a Kobo Clara HD e-reader. It's great, and the whole concept of e-readers is great. 

A neat thing about the Kobo is that it logs everything you do with it and stores that into an SQLite database. Literally everything -- it's not just tracking what books you've read, but it tracks how many seconds per reading session and how many pages you covered. A session is defined, as best I can tell, from the time you enter a book (either turning it on, or navigating to a new book from the menu) to the time you leave a book.

My plan was to automatically back up this database every time I connected the e-reader to my computer, and automatically do some data analysis (like getting the last 10 books I read, or what I'm currently reading) and post it on my website, or put it in my discord status or whatever. 

I accomplished the back-up part, and played around with some SQL queries for doing analysis, but never ended up wiring that up to any platforms. 

I'm sharing some information I discovered in the course of this project, in the hopes that it helps out anyone else attempting a similar task.

## The Database

The data is stored in `.kobo/KoboReader.sqlite`. There are a number of tables, but two are notable: `AnalyticsEvents`, and `content`.

### `AnalyticsEvents`
`AnalyticsEvents` is the one that stores all the things that have ever happened. The `Type` column holds the type of event, and there are, in my database, 50 different entries (there may be more that I just haven't encountered). Examples include `OpenContent`, `LeaveContent`, `StartReadingBook`, `MarkAsFinished`, `PluggedIn`, and so on. 

There's also a `Timestamp` column, but the really interesting data is stored as JSON in either `Attributes` or `Metrics`

To give you an example, here's a `LeaveContent`'s `Attributes` entry:


```json
{
  "ContentFormat": "application/epub+zip",
  "ContentType": "application/epub+zip",
  "Monetization": "Sideloaded",
  "Origin": "Sideloaded",
  "ViewType": null,
  "author": "Indra Das",
  "isbn": "9781101967522",
  "progress": "2",
  "title": "The Devourers"
}
```

And then the matching `Metrics`:

```json
{
  "IdleTime": 91,
  "PagesTurned": 0,
  "SecondsRead": 91
}
```

(Side note: *The Devourers* is a fantastic book.)

Not all events have both, or even either. For example, `AppStart` just has `{}` for both columns, while `OpenContent` only includes the attributes, and `PluggedIn` only has `Metrics`.

### `content`

The `content` table (note the lowercase c -- there doesn't seem to be a pattern for when table names use CamelCase or snake_case) stores information about books currently on the device. Of interest are columns like `FirstTimeReading`, `DateLastRead`, `ReadStatus`, CurrentChapterProgres` and (I'm just noticing this now) `IsInternetArchive`.

However, most of these columns aren't used, or the values are confusing -- `FirstTimeReading` doesn't seem to actually track what the name would suggest. Your milage may vary.

## The SQL

ChatGPT was a big help -- I don't write SQL often enough to remember it all on my own, but I know enough to wrangle GPT to do it for me.

### Last 10 Books Read

```sql
SELECT Title, Attribution, DateLastRead as DateFinished
FROM content
WHERE ReadStatus=2
ORDER BY DateLastRead DESC
LIMIT 10;
```

### Currently Reading

```sql
SELECT Title, Attribution
FROM content
WHERE ReadStatus=1
ORDER BY DateLastRead DESC
LIMIT 1;
```

### More Advanced Statistics
 
As mentioned, `content` only contains data for books that are still on the device. To include books that I read and then deleted, I would have to use `AnalyticsEvents`. In addition, anything more sophisticated, like finding out which books I reread (and how many times), or the total time spent on a book, would require using `AnalyticsEvents`. Another issue with `content` is that if I accidentally open a finished book and set it to finished again, then that becomes the new finished time. In order to weed out these sorts of things, I'd have to use some heuristics and look at a few different events. 

With the help of GPT I produced this monstrosity, that finds all books with a progress of above 90%, which is a starting point for finding the "real" finished date.

```sql
WITH BookProgress90 AS (
  SELECT 
    Timestamp,
    json_extract(Attributes, '$.progress') AS Progress,
	Attributes
  FROM 
    AnalyticsEvents
  WHERE 
    Type = 'BookProgress' 
    AND json_extract(Attributes, '$.progress') = '90'
)

SELECT 
  BP.Timestamp AS ProgressTimestamp,
  BP.Progress,
  (
    SELECT 
      AE.Timestamp
    FROM 
      AnalyticsEvents AE
    WHERE 
      AE.Type = 'OpenContent' 
      AND AE.Timestamp < BP.Timestamp
    ORDER BY 
      AE.Timestamp DESC
    LIMIT 1
  ) AS LastOpenContentTimestamp,
  (
    SELECT 
      json_extract(AE.Attributes, '$.title')
    FROM 
      AnalyticsEvents AE
    WHERE 
      AE.Type = 'OpenContent' 
      AND AE.Timestamp < BP.Timestamp
    ORDER BY 
      AE.Timestamp DESC
    LIMIT 1
  ) AS LastOpenContentTitle,
  json_extract(BP.Attributes, '$.volumeid')
FROM 
  BookProgress90 BP
```

Honestly, I'm not sure if SQL is the right tool for the job -- it may be simpler to use a state machine(s) to parse the data. 

## Automatic Backups (on Windows)

There are two parts to this: a Rust program that does the copying, and the scheduled task that runs the program when the Kobo is plugged in.

### The Rust Program

[Here's the Github repo.](https://github.com/CrispinStichart/Kobo-Backup)

I was a bit rusty (haha) when I wrote this program, so don't judge too harshly. The program exits silently if the hardcoded path of `F:\.kobo\KoboReader.sqlite` isn't found. As you'll see in a moment, this program is going to be automatically run when *any* USB device is plugged in. Then it checks the sizes, and copies it only if the one on the reader is bigger. Which (I just realized as I wrote this) is going to be always, because the kobo logs when it's plugged in. Oh well.

Note the flags in `cargo.toml`:

```
rustflags = ["-C", "link-args=/SUBSYSTEM:WINDOWS", "-C", "link-args=/ENTRY:mainCRTStartup"]
```

This transforms it from a console app to a Windows app, meaning there won't be the flicker of the command prompt popping up when the program runs in the background. It was the desire to eliminate that command prompt that's the reason this simple program is a compiled program in the first place and not just a powershell script.


### The Task

First, you need to open the Event Viewer. Then drill down to `Applications and Services Logs/Microsoft/Windows/DriverFrameworks-UserMode/Operational`, then right click the log and enable it.

Now plug in your Kobo, and you should see a bunch of new events. Pay attention to the event ID -- there should be one event that has a unique ID. For me, it's ID 2006, and it's the last "Loading Drivers ..." event. When we make the task in the next step, it's just going to be watching this log for that event ID -- as far as I can tell, the other information can't be used to affect whether a task runs or not.

Right click the event, and select "Attach Task to Event". Follow the wizard, and point it at your EXE that you want to run. Once complete, it will create the task and you'll be able to find and modify/delete it in the Task Scheduler, under `Task Scheduler Library/Event Viewer Tasks`.

## The End

That's all, folks! Hope this helped someone out there.