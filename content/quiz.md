---
title: Java Quiz
nav: Java Quiz
description: Test your Java knowledge with instant-feedback multiple choice questions covering the whole tutorial.
section: Reference
order: 40
---

## Java quiz

10 questions covering syntax, OOP, collections and core APIs. Pick an answer for every question, then hit **Submit** - you'll get instant scoring with explanations.

```raw
<div id="quiz-root"></div>
```

```raw
<script type="application/json" id="quiz-data">
[
  {
    "q": "Which of these is required for a runnable Java program?",
    "o": ["A class with a main method", "A package declaration", "An interface", "A build tool"],
    "a": 0,
    "e": "The JVM looks for public static void main(String[] args) - usually in a class whose name matches the file."
  },
  {
    "q": "What does the following print?  System.out.println(7 / 2);",
    "o": ["3.5", "3", "4", "Compilation error"],
    "a": 1,
    "e": "Both operands are int, so Java performs integer division and truncates the fraction. Use 7.0 / 2 for 3.5."
  },
  {
    "q": "Which String comparison is always correct for checking text content?",
    "o": ["s1 == s2", "s1.equals(s2)", "s1.compareTo(s2) == 1", "s1.equals(s2, s2)"],
    "a": 1,
    "e": "== compares references, not content. equals() compares character by character."
  },
  {
    "q": "What is the default value of an instance int field (never assigned)?",
    "o": ["null", "Garbage value", "0", "Compilation error"],
    "a": 2,
    "e": "Instance fields get defaults: 0 for numbers, false for boolean, null for references. Local variables have no default."
  },
  {
    "q": "Which access modifier means 'visible inside the package only'?",
    "o": ["public", "protected", "private", "no modifier (package-private)"],
    "a": 3,
    "e": "A member with no access modifier is package-private: accessible to classes in the same package."
  },
  {
    "q": "A class implements an interface. What must it provide?",
    "o": ["A constructor matching the interface", "Implementations of all abstract methods", "A main method", "A copy constructor"],
    "a": 1,
    "e": "Concrete classes must implement every abstract interface method - unless they are themselves abstract."
  },
  {
    "q": "Which collection keeps UNIQUE elements and offers average O(1) lookups?",
    "o": ["ArrayList", "LinkedList", "HashSet", "TreeMap"],
    "a": 2,
    "e": "HashSet is backed by hashing: uniqueness by definition, contains() in average O(1)."
  },
  {
    "q": "HashMap.get(key) returns null when the key is missing. What is the safe way to read an int count?",
    "o": ["map.get(key)", "(int) map.get(key)", "map.getOrDefault(key, 0)", "map.count(key)"],
    "a": 2,
    "e": "getOrDefault returns 0 instead of null, avoiding the NullPointerException during unboxing."
  },
  {
    "q": "What does the 'finally' block do?",
    "o": ["Runs only if an exception occurs", "Runs whether an exception occurs or not", "Replaces the catch block", "Runs once at program exit only"],
    "a": 1,
    "e": "finally always executes - return, exception, or normal flow. Modern code often uses try-with-resources instead."
  },
  {
    "q": "Which statement about lambda expressions is TRUE?",
    "o": ["They can implement any abstract class", "They must be one line", "They can implement a functional interface (one abstract method)", "They create a new thread automatically"],
    "a": 2,
    "e": "A lambda is assignable to a functional interface - Predicate, Function, Runnable, or your own single-method interface."
  }
]
</script>
```

## How did you do?

| Score | Suggested next step |
|---|---|
| 9-10 | Excellent - explore [Streams](streams.html) and [Threads](threads.html) |
| 7-8 | Good - revisit [Collections](collections.html) and [Exceptions](exceptions.html) |
| 4-6 | Re-read [OOP basics](classes-objects.html) and [Variables](variables.html) |
| 0-3 | Start from the [Introduction](intro.html) and work through the sidebar in order |

Retake the quiz as often as you like - answers and explanations reset each time.
