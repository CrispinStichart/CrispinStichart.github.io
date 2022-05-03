---
layout: post
title:  "My Experience with Go and the Charm TUI Toolkit"
---

I spent the last week learning [Go][go] and building a simple terminal-based application with various [Charm][charm] libraries. Charm is a startup that [according to linkedin][linkedin] raised $3 million in funding via Crunchbase. They build libraries for building Terminal User Interfaces (TUIs, AKA command-line applications). I have no idea how they make any money.

Their BubbleTea library is a TUI toolkit; think GTK or Qt, but for terminal based apps. BubbleTea itself is just the framework for building components, but they offer a lot of premade components via their Bubbles project.

If you haven't already done so, click the above link and check their website out. They have a *very* distinct, very playful aesthetic that permeates everything, from the look to the names to the documentation.

# Learning Go

I now have learned enough languages that I'm starting to see similarities between them, in terms of syntax, convention, and overall philosophy. It's pretty neat! Go does a few things I haven't seen before. For starters, declaring and assigning a variable is done with either `var foo = "bar"` or `foo := "bar"`. That `:=` syntax is really interesting, because it's the same as [assignment expressions][python] in Python. Assignment expressions let you do things like:

```python
while line := f.readline():
    print(line)
```

Since you can do the same kind of thing in Go, and with that syntax, it makes me think that Go was the inspiration.

In general, I like working with the language. It's statically typed but really doesn't feel like it; the type system is very unobtrusive and most types are inferred. It doesn't feel much different to using python with typehints.

I've barely scratched the surface of the language, and haven't touched it's main claim to fame, goroutines, but I like what I've seen so far.

# Charm: BubbleTea, Bubbles, Glamour, and Wish

For this project ([code is in GitHub](code)) I decided that I was going to just make a program to access my blog, render the markdown with Glamour, and make it usable over SSH with Wish. And so that's what I did! There's not a whole lot of custom code here, because I was mainly just gluing together premade components. Not unlike building a simple GUI application, I guess.

Using BubbleTea felt a bit verbose, and I want to say that it wasn't abstract enough, since a BubbleTea application involves passing a lot of strings around and joining them. I feel that maybe it should have tried harder to hide the fact that it was strings all the way down, and instead work more like a GUI toolkit.

On the other hand, TUIs are not GUIs, and perhaps hiding the raw text may have caused more problems than it solved. And whatever the case may be, BubbleTea is certainly lightyears ahead of anything I'd be able to code by myself.

I do wish there was an advanced tutorial; the one they have provides a nice introduction, but it glosses over some things, like when you're supposed to use the `Init` method and when exactly it's called. Luckily they have a ton of clearly written examples, so I can't be too mad.

I used Glamour to render the markdown. Nothing really to say about it: text goes in, pretty text comes out. Works as expected.

Wish is an interesting product: essentially, it lets you take any TUI application and easily make it accessible over SSH. I copy and pasted a tiny bit of code, changed a few lines, and *bam* it just worked, first time. Very cool!

# Verdict

I have no idea when or if I'll ever have a real reason to make another TUI application, but I can say for sure that if I do, I'll use Charm if I can. To do something comparable from scratch would have taken me far longer, and probably would have led to a lot of messy code with nasty edge cases. TUI toolkits are a niche market, but I'm glad someone stepped up to the plate.


[go]: https://go.dev/
[charm]: https://charm.sh/
[linkedin]: https://www.linkedin.com/company/charmbracelet/
[python]: https://peps.python.org/pep-0572/
[code]: https://github.com/CrispinStichart/website-via-ssh