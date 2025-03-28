---
layout: post
title:  "Remaking the Dinosaur Comics Random Second Panel Endpoint"
---

![gasp](/images/posts/2022-05-05-dino-comics/1.png)


## Background

There is a webcomic by the name of Dinosaur Comics. Naturally, its URL is [qwantz.com][qwantz] (although you can also access it via [chewbac.ca][chewbacca]).

It's what Wikipedia calls a "[constrained comic][wiki]" -- in this case the constraint is that in every comic, the art remains the same (with some minor exceptions).

You might think that the author, Ryan North, would run out of content, but after almost two decades and just under 4000 comics, he's still going strong.

## Get to the point please

Due to the nature of Ryan's writing style, the second panel of almost any of the comics can be taken out of context and remain funny (if your sense of humor is tuned correctly, I guess).

In the long-ago times (circa 2009) someone had written a randomizer that would do just that. There was a URL you could go to that would return a random second panel, and... that was it. That was all it needed to do.

Back then, I had a website on which I used this randomizer, and I loved it. I recently remembered it and decided I wanted the same thing my [current website][site], but sadly the old script URL is dead, and I couldn't find a new version.

So I made one!

## I had no idea making web apps was so easy

Seriously, last time I messed around with making server-side websites, there were no free offerings. If you wanted a server you could actually do something with, you had to pay for it.

And once you paid for it, you had to manage it. Take your eyes off it for a minute, and next thing you know it's part of a Russian botnet.

Today, in the span of an hour, I:

1. discovered that Heroku has a free tier
2. signed up
3. read enough of the docs to stumble my way to victory
4. pushed my git repo to their server

And... that's it. A free host for running a dynamic web application (albeit a very simple one, in this case) that integrates with git and manages everything I don't want to care about.

## Gimmie the URL!

Check this out:

[https://dino-comics-second-panel.herokuapp.com/random](https://dino-comics-second-panel.herokuapp.com/random
)

You can also request specific panels, like so:

* [https://dino-comics-second-panel.herokuapp.com/comic/1](https://dino-comics-second-panel.herokuapp.com/comic/1)
* [https://dino-comics-second-panel.herokuapp.com/comic/69](https://dino-comics-second-panel.herokuapp.com/comic/69)
* [https://dino-comics-second-panel.herokuapp.com/comic/420](https://dino-comics-second-panel.herokuapp.com/comic/420)

### Update

Not too long after posting this, Heroku got rid of their free tree. I'll probably eventually set it up with an alternate host.

## Do it yourself

If you like this but want to host it yourself, or use the panels for another purpose, I [uploaded everything to GitHub](https://github.com/CrispinStichart/dinosaur-comics-random-second-panel).


## Oh and one more thing

During the course of making this, I discovered that every Dinosaur Comics page includes this as an HTML comment at the bottom of the source:

```
                                          ,~~~~~~~~~~~~~~~~~~~~,
                                        ,'   Um what!  What    ',
                                        |    does that code      |
                                        ',   even MEAN??        ,'
                                          '~~~~~~.,   ,.~~~~~~~'
                                                  |  /
                                                  | /
                                                  |/
                                                  '
                                           .~-,
                                         .' `,>
                                      .-'   ,>  <7`,
                                    ,`     ,>  <7  }
                                   {   o   !> <7  /
                                   {       j_7`  !
                                   :            j'
                                    `,         ]
                                     F        }
                                    F       , {
                                   F         `.   rr
                                 .F          | `=-"
       _,-`                    .F            `,
     ,`;                     .F               j
    :  7                    F                 ;
    :  `^,                F`                 ,'
    `,    `^,          ,F`     .          ,  /
      `,     `^-^-^-^-`       ;           | ;
        `.                    :          .`/      ,-^,-
          `-.                 }         ,'' `,_.-^ /'
             `-,___           ;      .'` -_      ,7
                   ``=-....-={     ,/      `-','`Q
                              \     |                .-'-.]
                               `,   `.             .`  0  `.
                                `,   l_           `|  __   |`
                               .C.-,___`==,        |  ||   |

```

I feel ya, T-Rex.


[site]: https://crispinstichart.github.io/
[qwantz]: https://qwantz.com/
[chewbacca]: http://chewbac.ca/
[wiki]: https://en.wikipedia.org/wiki/Constrained_comics