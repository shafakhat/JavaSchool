---
title: Regular expression languages also have character classes.
nav: Regular expression languag...
description: Character classes specify a list of possible characters that can match any single character in the string you want to match.
section: Imported - java2s Archive
order: 2236
source: https://web.archive.org/web/20140217200437/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Regularexpressionlanguagesalsohavecharacterclasses.htm
---
Character classes specify a list of possible characters that can match any single character in the string you want to match.
Using the expression [^012], any single digit except for 0, 1, and 2 is matched. You can specify character ranges using the dash. The character class [a–z] matches any single lowercase letter. [^a–z] matches any character except a lowercase letter. [0–9] to match a single digit. [0–3] to match a 0, 1, 2, or 3. [a–zA–Z] to match any single letter.
Character Class Meta-Character Matches . Any single character \d A digit [0–9] \D A nondigit [^0–9] \s A whitespace character [ \t\n\x0B\f\r] \S A nonwhitespace character [^\s] \w A word character [a–zA–Z_0–9] \W A nonword character [^\w]
