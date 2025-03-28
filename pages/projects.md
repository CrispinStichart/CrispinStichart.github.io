---
layout: default
permalink: projects
---

# Projects

Here are a few personal projects I've worked on. You'll note a lot of unfinished projects on here. What happens is that I get really excited about solving a problem, and then after I've done a large chunk of the work one of the following happens:

* it works well enough for my needs, and I never spend the time to polish it and release it for wider use
* while developing it, I come across existing software that does exactly what I want
* I lose interest in the original goal
* some combination of the above.

But trust me, as long as you're paying me, I won't lose interest and abandon you. I promise!

## Games (Godot, GDScript) 

[My itch.io page](https://crispinstichart.itch.io/)

I've been getting into making games with the Godot game engine. It's been really fun, and I've been able to learn about and use some CS techniques that I never had to before, like state machines and event buses.

You can click the link above to check out an up-to-date list, but so far it's just three:

1. [Diablo 69](https://crispinstichart.itch.io/diablo69), my first game and therefore worst. Elevated by my blatant copyright infringement of Diablo 2 music and sound effects.
2.  [Snerk](https://crispinstichart.itch.io/snerk), which I made in a week to see if I could actually go from start to finish in that time frame.
3. [Markerio](https://crispinstichart.itch.io/markerio-1-1) is the first level of the original Mario game, but drawn and played on a whiteboard. I made all the art and sound effects. Music is from a friend.
4. [Untitled Platformer](https://crispinstichart.itch.io/metroidvania-movement-test): the first game I made that I think is actually kinda fun. If you like challenging platforming games, anyway. I'm currently expanding this codebase to add combat mechanics, but I think I'll upload that version as a different project.

## Tutor.com Schedule to Google Calendar (Python)

[Github](https://github.com/ExtremeDramaLlama/ScheduleToCalendar)

I currently (as of February 2024) contract as a computer science tutor for a company called Tutor.com. Their online shift schedular doesn't offer any Calendar integrations, so I made one myself.  

This project gave me some exposure to working with a complex large API like google's, and it allowed me to write, and then fix, my very first daylight-savings-time-related bug.

As a side note, you may notice that the repository is under the name "ExtremeDramaLlama". This alt account was to shield myself from reprisal from Tutor.com if they decided to take umbrage to a project like this, which no doubt violates their terms of use. However, I no longer care, and if I get fired from that dumpster fire of a company, I won't even be mad. 

## Kobo Backup and Analytics (Rust, SQL)

[Github](https://github.com/CrispinStichart/Kobo-Backup), [Blog Post](../backing-up-and-parsing-kobo-database)

I have a Kobo E-Reader and I spent some time working on a solution to performing automatic backups of the database and doing analysis on the data. Although I didn't get too far into it, some things I discovered might help out anyone who wants to do anything similar.

## Wordle Results Editor (JavaScript/React)

[GitHub](https://github.com/CrispinStichart/wordle-result-editor) \| [Try it out](https://crispinstichart.github.io/wordle-result-editor/)

I'm guessing you're familiar with the cultural phenomenon known as Wordle, as well as how it copies your spoiler-free results into your clipboard as a grid of colored square emojis. My friends and I got into the habit of sharing our results in our Discord server, except replacing the default emojis with some of our custom discord emotes.

I grew tired of having to spend fifteen seconds every day manually replacing the emojis, so naturally, I learned JavaScript and React and spent a week making a web app to do it for me.

Time well spent.

## Special Purpose Mail Client (Rust, work-in-progress)

[GitHub](https://github.com/CrispinStichart/email-liberator)

This project started when I wanted to automatically filter Gmail messages based on regex. Although Gmail does offer custom filtering, it's based around their limited search operators, with no regex support. I thought, "how hard can it be to write a simple mail client myself?"

The answer was "trickier than expected," especially as the scope of the project expanded. I even switched languages partway through. After writing 90% of it in Python, I grew so annoyed by the state of the Python packaging ecosystem that I rewrote it in Rust.

## Jekyll Plugin to Auto Archive Links (Ruby, work-in-progress)

[GitHub](https://github.com/CrispinStichart/jekyll-automatic-link-archiver)

[Link rot][linkrot] is the name for the fact that over time, links break. Read any blog from fifteen years ago, and chances are good that any links provided are either non-functional or point to something completely different.

The Internet Archive really helps, but they can't spider everything. And furthermore, relying on them puts the burden on your future readers. What if instead, *you* archived everything you linked to?

That's what this tool aims to do. Right now it's a Jekyll plugin that will scan your blog posts for links and use `wget` to download the entire page, if it's not already downloaded.

It's very early in the prototyping stage and I still have a lot of work to do, but I think it could really be useful for a lot of people.

[linkrot]: https://en.wikipedia.org/wiki/Link_rot

## Zillow Internet Availability Integration (JavaScript, work-in-progress)

At least in the United States, Zillow is the main website to look for a house or apartment. Despite containing all the other information you would want about a property, it doesn't answer the most important question: what kind of internet can I get here?

This project is a browser extension that will inject, on the Zillow page, information about the internet availability at whatever property you're looking at.

It's in the prototyping stages now, but I've tested out individual pieces of the project, and it's working as expected.

The biggest issue I've run into so far is that the Google Fiber website (and, I'm guessing most other ISP websites) are not easy to scrape. They're all dynamically generated on the client side with JavaScript. As such, I'm currently using Puppeteer to fetch the site contents, and exposing it to the plugin via a server running on localhost.


## Blog Via SSH (Go)

[GitHub](https://github.com/CrispinStichart/website-via-ssh)

This project was an excuse to learn Go and play around with Charm, which is a collection of libraries to assist with easily building nice-looking Terminal User Interfaces (TUIs, AKA command-line applications).

There's not a whole lot of custom code here. I mainly just glued a lot of Charm stuff together to end up with an application that displays my blog posts.

Speaking of blog posts, I wrote [a blog post][blog] about my experience working with Charm.

[blog]: ../learning-go-and-charm/

## Text Shaper (JavaScript)

[GitHub](https://github.com/CrispinStichart/text-shaper) \| [Try it out](https://crispinstichart.github.io/text-shaper/)

This is a web app that lets you format any text you provide into whatever shape you want, using a transparent `.png` as the mask.  I wrote this back in 2017 while I was still in college, but recently dusted it off and gave it a new coat of paint, and I plan on adding a few features.

At least when I wrote this, I couldn't find anything else on the web that could do this, so it *could* be one of a kind. I wrote it because my school's ACM chapter was having a t-shirt design contest, and I thought it'd be cool to have the schools's mascot, but made up of code.

My design did not win.

## Random Dinosaur Comics Second Panel (Python/Flask/Heroku)

[Click here][random] for a random second panel from Dinosaur Comics. This is an oddball one, so I wrote a whole [post][dino] about it.

[random]: https://dino-comics-second-panel.herokuapp.com/random
[dino]: ../dino-comics

## CHIP-8 Emulator (Rust)

[GitHub](https://github.com/kingcritter/chip8_interpreter)

There are many CHIP-8 emulators, but this one is mine.

I wrote it a few years ago, during my first attempt at learning Rust. It's simple and far from original, but I'm including it on this list because I look at it and think: *dude, I wrote an emulator, how cool is that?*
