---
title: Coding & Output Puzzles - Interview Bank
nav: Interview - Coding
description: 20 classic Java coding questions and output puzzles with worked answers - string/array problems, tricky snippets, complexity notes.
section: Interview & Certification
order: 90
---

## Coding & Puzzles - topic bank

Topic bank #8 of the [Interview Prep hub](interview.html). These are the "write it on the board" and "what does this print" classics. Try each before expanding.

<details class="iq"><summary>1. Print this pattern / FizzBuzz - what are they screening?</summary>
<p>FizzBuzz (multiples of 3 → Fizz, 5 → Buzz, both → FizzBuzz): tests loop + modulo + ordering of conditions. Board answer: one loop 1..n, check <code>i % 15 == 0</code> first, then 3, then 5. Say the complexity (O(n)) and the modulo order trap (15 must be first) - that's the actual signal.</p>
</details>

<details class="iq"><summary>2. Reverse a String without library reverse?</summary>
<p><code>char[] a = s.toCharArray(); for (int i=0,j=a.length-1; i&lt;j; i++,j--) { char t=a[i]; a[i]=a[j]; a[j]=t; } new String(a);</code> Mention: O(n) time, O(n) space (or two-index over StringBuilder). Bonus: surrogate pairs mean char-level reversal can corrupt emoji - raise it, then proceed with the simple version for ASCII unless told otherwise.</p>
</details>

<details class="iq"><summary>3. Is it a palindrome (ignoring case/punctuation)?</summary>
<p>Two indices from both ends, skipping non-alphanumerics, <code>Character.toLowerCase</code> compare; O(n)/O(1). Or normalize + compare with StringBuilder.reverse. Edge cases interviewers check: empty string (true), single char, digits only, unicode - state your assumptions out loud.</p>
</details>

<details class="iq"><summary>4. Find the first non-repeated character?</summary>
<p>Two passes with a LinkedHashMap<Character,Integer> counts (insertion order preserved): count, then first entry with count 1 - O(n). If the alphabet is small, int[128]/int[256] array is faster and allocation-free. Follow-up: first repeated character - flip the check on the second pass.</p>
</details>

<details class="iq"><summary>5. Check two strings are anagrams?</summary>
<p>Lengths differ → false; int[26]/int[256] counts (increment one, decrement other, all zero) - O(n) time, O(1) alphabet space. Or sort both and compare - O(n log n). Discuss unicode/case: normalize with toLowerCase(Locale.ROOT) and state it. Classic follow-up: one is a permutation of a substring of the other (sliding window counts).</p>
</details>

<details class="iq"><summary>6. Fibonacci - three ways?</summary>
<p>Naive recursion O(2^n) (never write this); iterative two-variable O(n)/O(1) (the right answer); memoized or matrix exponentiation for very large n (and mention long overflow → BigInteger). Nail the base cases fib(0)=0, fib(1)=1 out loud.</p>
</details>

<details class="iq"><summary>7. Factorial and string permutation of huge numbers?</summary>
<p>factorial(50) overflows long fast - use BigInteger for exactness. Permutations recursively with swap + backtrack, or iterative Heap's algorithm; count = n!. For "print all permutations of a string with duplicates", the follow-up is dedup (sort + skip adjacent equal at each level) - say it before they ask.</p>
</details>

<details class="iq"><summary>8. Two sum - array, find pair adding to target?</summary>
<p>HashMap<value, index> single pass: for each x check target-x seen - O(n) time, O(n) space. Sorted variant: two pointers O(n)/O(1). State the trade-off; if asked "all pairs", switch to counts and handle duplicates carefully (the duplicate-pair bug is the trap).</p>
</details>

<details class="iq"><summary>9. Find duplicates / remove duplicates from an array?</summary>
<p>Find: HashSet add() return value, first false wins - O(n). Remove (sorted array): read/write pointers O(n)/O(1). Remove (unsorted, preserve order): LinkedHashSet or new array with seen set. Interview point: clarify "duplicates of what - all values or adjacent, one copy or all" before coding.</p>
</details>

<details class="iq"><summary>10. Array rotation by k?</summary>
<p>Reversal trick: reverse whole, reverse first k, reverse rest - O(n)/O(1) (modulo k first: k %= n). Or juggling algorithm. Or copy-based O(n)/O(k). Say the modulo on k &gt; n upfront - that's the missing edge case everyone probes.</p>
</details>

<details class="iq"><summary>11. Merge two sorted arrays/lists?</summary>
<p>Two pointers, write the smaller, advance; O(n+m). Merging into the first array in place with space (LeetCode-style) works from the back to avoid overwriting. For linked lists, dummy-head node pattern. State complexity and what happens with duplicates (stable: take from left first).</p>
</details>

<details class="iq"><summary>12. Missing number in 1..n?</summary>
<p>Sum formula n(n+1)/2 minus array sum - O(n), watch overflow (use long). XOR trick avoids overflow: xor all indices and values. Sorting is O(n log n) - acceptable to mention, then improve. Follow-up: two missing numbers → XOR partition or sum-of-squares.</p>
</details>

<details class="iq"><summary>13. Count words / frequency map from a sentence?</summary>
<p>split(&quot;\\s+&quot;) then map.merge(w, 1, Integer::sum) - then the follow-ups: top K (PriorityQueue size K or sort entries), case normalization, punctuation stripping, streaming for huge inputs (better: split incrementally with a Reader). Interviewers love the top-K follow-up.</p>
</details>

<details class="iq"><summary>14. Largest/smallest in array, second largest?</summary>
<p>Single pass for min/max - O(n), initialize from the first element (not 0 - negative arrays!). Second largest: track best and runner-up in one pass, handle duplicates/len&lt;2 explicitly. Don't sort unless asked - O(n) is the pass.</p>
</details>

<details class="iq"><summary>15. Reverse a linked list (iterative + recursive)?</summary>
<p>Iterative: prev/curr/next three-pointer walk - O(n)/O(1). Recursive: reverse rest, fix two pointers - O(n) stack (mention for long lists). Also know: detect a cycle (Floyd slow/fast), find middle (slow/fast), merge sorted lists (dummy head) - the linked-list starter pack.</p>
</details>

<details class="iq"><summary>16. What does this print? <code>System.out.println(0.1 + 0.2 == 0.3);</code></summary>
<p><code>false</code> - binary floating point can't represent 0.1/0.2 exactly; the sum is 0.30000000000000004. Compare with epsilon or BigDecimal. Same family: <code>0.1f + 0.2f == 0.3f</code> is true (float rounding happens to land equal) - print both and explain.</p>
</details>

<details class="iq"><summary>17. What does this print? <code>Integer a = 127, b = 127; a == b;</code> and with 128?</summary>
<p>127 → true (cached box), 128 → false (new objects). Same as <code>Integer.valueOf</code> caching -128..127. Bonus probes: <code>new Integer(5) == new Integer(5)</code> false; <code>Long 127L</code> same; Float/Double have NO cache (always false).</p>
</details>

<details class="iq"><summary>18. What does this print? <code>String s = null; System.out.println(s + &quot;!&quot;);</code></summary>
<p>Prints <code>null!</code> - string concatenation with a null reference yields the literal "null" (String.valueOf semantics), no NPE. But <code>s.concat(&quot;!&quot;)</code> or <code>s.length()</code> throws NPE. Same trick: <code>System.out.println(1 + 2 + &quot;x&quot; + 1 + 2)</code> → <code>3x12</code> (left-to-right: numeric add then concat).</p>
</details>

<details class="iq"><summary>19. What does this print? try/catch/finally returns?</summary>
<p><code>try { return 1; } finally { return 2; }</code> → 2 (finally overrides). <code>try { throw e; } finally { return 2; }</code> → 2, exception swallowed. <code>try { return x++; } finally { x++; }</code> → returns old x (value computed before finally). Rule: never return/throw from finally; System.exit(0) is the only thing that skips finally.</p>
</details>

<details class="iq"><summary>20. What does this print? static initialization order puzzle?</summary>
<p>Given <code>class A { static int x = init(); static int init(){ return B.y + 1; } }</code> and B circling back - text-order initialization with defaults visible → prints surprising zeros. Golden rule for the board: fields/static blocks run in textual order at first use; referencing another class mid-init sees its default values. Recommend the speaker-class/holder idiom to dodge it.</p>
</details>

---

Hub: [Interview Prep home](interview.html) · Master list: [115 questions](interview-master.html) · Tests: [1](ocjp-practice.html) · [2](ocjp-practice-2.html) · [3](ocjp-practice-3.html)
