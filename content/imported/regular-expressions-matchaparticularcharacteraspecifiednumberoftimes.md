---
title: Match a particular character a specified number of times.
nav: Match a particular charact...
description: One class of operators is greedy, that is, they match as much as they can, until the end.
section: Imported - java2s Archive
order: 2221
source: https://web.archive.org/web/20140829090951/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Matchaparticularcharacteraspecifiednumberoftimes.htm
---
There are two general ways the repetition operators work.
One class of operators is greedy, that is, they match as much as they can, until the end.
The other class is reluctant (or lazy), and matches only to the first chance they can terminate.
For example, the regular expression .*; matches any number of characters up to the last semicolon it finds.
To only match up to the first semicolon, the reluctant version .*?; must be used.
Greedy Operator Description X? Matches X zero or one time X* Matches X zero or more times X+ Matches X one or more times X{n} Matches X exactly n times, where n is any number X{n,} Matches X at least n times X{n,m} Matches X at least n, but no more than m times
Reluctant (Lazy) Operator Description X?? Matches X zero or one time X*? Matches X zero or more times X+? Matches X one or more times X{n}? Matches X exactly n times, where n is any number X{n,}? Matches X at least n times X{n,m}? Matches X at least n, but no more than m times
