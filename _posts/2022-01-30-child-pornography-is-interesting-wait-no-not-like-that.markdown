---
layout: post
title:  "Child Pornography Is Interesting – Wait No Not Like That, Come Back!"
---

Child pornography is, legally, very interesting. As far as I can tell, it's the only digital contraband under American law. By contraband, I mean something that is illegal to possess, for any reason, by anyone. In the physical realm, an example would be schedule one drugs, like heroin. 

There are of course many things, both physical and digital, that are illegal to possess under certain circumstances. For example, stolen property is illegal to possess, but of course it's not the property itself that is the problem, it's the ownership of it. Similarly, you can be prosecuted for possession of classified material -- in physical or digital form -- without the material itself being illegal.

Another interesting aspect of child pornography is how it's tied to cryptography, and the laws surrounding that. In the modern world, child pornography is entirely digital, and can thus be encrypted. Furthermore, prosecutors need to prove the existence of the material itself; there's not a lot of room for other circumstantial evidence. 

For example if, someone's being accused of selling government secrets to Russia, even if the solid evidence is locked away in a cryptographically protected hard drive, there's plenty of other evidence on which to build a case, like phone records, travel records, intercepted communication from the Russian embassy, and so on and so forth. For a digital crime like child pornography, the prosecution probably only has the fact that the defendant's IP address was logged visiting an [FBI honeypot][honeypot].

If you have an encrypted hard drive, can the court legally force you to hand over the password, and punish you if you don't comply? Does the fifth amendment protect you from self-incrimination in this case? Since cryptography is relatively new, there's not a lot of specific case law yet, so lawyers and judges have to extrapolate from related concepts, which vary based on the details of the case.

For example, when a [Pennsylvania man was arrested][foregone-conclusion] for possession of child pornography, he told the investigators: "It's 64 characters and why would I give that to you. We both know what's on there. It's only going to hurt me. No fucking way I'm going to give it to you." Because he said these things, the court argued that he had waived his fifth amendment rights.

Their argument was based on the legal doctrine of the "foregone conclusion exception", which says that courts can force the reveal of incriminating documents, *if* the court already knows exactly what they contain and where they are. In the end, the Pennsylvania Supreme Court overruled the lower court's decision, and declared that:

> Distilled to its essence, the revealing of a computer password is a verbal communication, not merely a physical act that would be nontestimonial in nature. . . one cannot reveal a passcode without revealing the contents of one’s mind.

Not all courts agree. In a [similar Philadelphia case][philly_case], the 3rd US Circuit Court of Appeals accepted the prosecutions use of the foregone conclusion exception. In this case, they had eye-witness testimony about the contents of the encrypted drive, as well as some forensic evidence. At the time of the ruling, the suspect was being held in jail on a contempt of court charge for refusing to hand over the password. 

The defendant in question was [eventually freed][four_years_prison] after spending four years in jail. His lawyers successfully argued that his detention violated a law that puts an 18-month limit on contempt of court for witnesses who won't testify. The prosecution's argument was that the law didn't apply since the defendant was a *suspect*, not a witness, and there was no limit for detaining suspects. The 3rd Circuit Court of Appeals disagreed. The lone dissenting judge brought up the All Writs Act, saying that it was what gave the court the power to hold the defendant in contempt, and it didn't have any time limits.

The [All Writs Act][all_writs] gives the courts broad powers to compel testimony, and has been used frequently in modern times to gain access to encrypted devices. The act was introduced in 1789, and was meant to be applied to paper documents; if you google it now, you just get a bunch of articles about encryption. The FBI used it against Apple in their quest to force them to help [break into a terrorist's iPhone][fbi_iphone].

Anyway, uh, I hope you learned something? Writing this post now gives me motivation to write a lot more posts, very quickly, so "CHILD PORN" is not the first thing someone sees when arriving at this site. 

[ars]: https://arstechnica.com/

[fbi_iphone]: https://www.smithsonianmag.com/smart-news/what-all-writs-act-1789-has-do-iphone-180958188/

[philly_case]: https://arstechnica.com/tech-policy/2016/05/feds-say-suspect-should-rot-in-prison-for-refusing-to-decrypt-drives/

[all_writs]: https://en.wikipedia.org/wiki/All_Writs_Act

[four_years_prison]: https://arstechnica.com/tech-policy/2020/02/man-who-refused-to-decrypt-hard-drives-is-free-after-four-years-in-jail/

[honeypot]: https://arstechnica.com/tech-policy/2016/01/after-fbi-briefly-ran-tor-hidden-child-porn-site-investigations-went-global/

[foregone-conclusion]: https://arstechnica.com/tech-policy/2019/11/police-cant-force-child-porn-suspect-to-reveal-his-password-court-rules/


