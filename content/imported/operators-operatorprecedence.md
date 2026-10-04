---
title: Operator Precedence
nav: Operator Precedence
description: Operators with a higher precedence are executed before those of a lower precedence.
section: Imported - java2s Archive
order: 1121
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/OperatorPrecedence.htm
---
Operators with a higher precedence are executed before those of a lower precedence.

Operators on the same line have the same precedence:

Operator Precedence Group  Associativity  Operator Precedence
(), [], postfix ++, postfix --  left  Highest
unary +, unary -, prefix ++, prefix --, ~, !  right
(type), new  left
*, /, %  left
+, -  left
< < , >>, >>>  left
< , < = , >, >=, instanceof
==, !=
&  left
^  left
left
&&  left
left
?:  left
=, +=, -=, *=, /=, %=, < < =, >>=, >>>=, &=,  =, ^=  right  lowest
