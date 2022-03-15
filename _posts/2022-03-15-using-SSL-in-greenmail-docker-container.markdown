---
layout: post
title:  "Using SSL/TLS in a Greenmail Docker Container"
---

## Complaining

I'm making this post because I literally spent at least 8 hour of my life over the past three days trying to figure this out. For someone who knows crypto stuff, that's probably going to seem ridiculous, but I do not know crypto stuff, and my eyes immediately glaze over when I see an `openssl` command.

So here's the deal: I'm working on a simple mail client, written in Rust, and I wanted to do some integration testing. I'm using [rust-imap](https://github.com/jonhoo/rust-imap), and that project has integration tests that use a tool called [Greenmail](https://greenmail-mail-test.github.io/greenmail/). Greenmail is a mail server built for doing integration; in other words, exactly what I need. 

So I downloaded the docker container and quickly got it up and running, using the `rust-imap` tests as a starting point. However, when I say "up and running" I just mean that the server was running and listening for connections, but my client wasn't able to connect due to an SSL issue: the server's certificate was untrusted.

What came next was a lot of reading and a lot of barking up wrong trees. For example, since Greenmail doesn't really have documentation, I was looking at the code to figure out how to configure certificates, but it was at least an hour before I realized that the configuration code had been added in the last couple weeks and they hadn't pushed a new docker image for it.

So I tried to build the project from source, ran into issues there, yadda yadda, lots of frustration. Here's the steps I went through to solve this, hopefully it'll help someone out there.

## The Solution

Note: this is for Greenmail 1.6.7. Later version will hopefully make using a custom keystore easier, and so steps 4 and 5 will be different, and you may be able to use a different password for the keystore.

**1: Create a certificate and key:**

```
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
 -keyout greenmail.key -out greenmail.crt -subj "/CN=localhost" \
 -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
 ```
 
 The `subjectAltName` is the critical bit; a lot of places on the internet imply that it'll work as long as the CN is set to `localhost`. However, support for that has been apparently deprecated for almost two decades.  Had to learn that from a random post on the [python bug tracker](https://bugs.python.org/issue34440#msg323786). 🙄 
 
**2: Generate the `.p12` keystore:**
 
 ```
 openssl pkcs12 -export -out greenmail.p12 -inkey greenmail.key -in greenmail.crt
```

When it asks to set a password, use `changeit`. The password is hardcoded in Greenmail.

**3: Add certificate as a Trusted Root Certificate Authority**

In Linux:

```
sudo cp greenmail.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

In Windows, use the graphical Certificate Manager (just search "certificate" and it should come up).

**4: Add the keystore to the JAR**

Get the `greenmail-standalone.jar` file for the version of the docker image you're using. You can find all the JARs at [on maven](https://mvnrepository.com/artifact/com.icegreen/greenmail-standalone).

Add the keystore: `jar uvf greenmail-standalone.jar greenmail.p12` (or just open the JAR in 7zip or whatever).

**5: Bind mount the JAR when running docker:**

```
docker run -v <full path to greenmail-standalone.jar>:/home/greenmail/greenmail-standalone.jar -t -i -e GREENMAIL_OPTS='-Dgreenmail.setup.test.all -Dgreenmail.hostname=0.0.0.0 -Dgreenmail.auth.disabled -D-Dgreenmail.verbose' -p 3025:3025 -p 3110:3110 -p 3143:3143 -p 3465:3465 -p 3993:3993 -p 3995:3995 greenmail/standalone:1.6.7
```

Note that I had to use the *full* path, not relative, of the local JAR file to get it working.

---------------------

After all that, I can successfully establish a secure connection with the Greenmail server. Now I can actually write some tests. 😤  