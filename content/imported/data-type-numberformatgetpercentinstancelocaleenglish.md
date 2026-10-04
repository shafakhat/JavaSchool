---
title: NumberFormat.getPercentInstance(Locale.ENGLISH)
nav: NumberFormat.getPercentIns...
description: NumberFormat percentFormat = NumberFormat.getPercentInstance(Locale.ENGLISH);
section: Imported - java2s Archive
order: 1242
source: https://web.archive.org/web/20140829090326/http://www.java2s.com/Tutorial/Java/0040__Data-Type/NumberFormatgetPercentInstanceLocaleENGLISH.htm
---
```java title=Example.java
import java.text.NumberFormat;
import java.util.Locale;
public class MainClass {
  public static void main(String[] args) {
    NumberFormat percentFormat = NumberFormat.getPercentInstance(Locale.ENGLISH);
    for (double d = 0.0; d <= 1.0; d += 0.005) {
      System.out.println(percentFormat.format(d));
    }
  }
}
java title=Example.java
0%
0%
1%
2%
2%
2%
3%
4%
4%
4%
5%
5%
6%
6%
7%
8%
8%
8%
9%
10%
10%
11%
11%
12%
12%
13%
13%
14%
14%
15%
15%
16%
16%
17%
17%
18%
18%
19%
19%
20%
20%
21%
21%
22%
22%
23%
23%
24%
24%
25%
25%
26%
26%
27%
27%
28%
28%
29%
29%
30%
30%
31%
31%
32%
32%
33%
33%
34%
34%
35%
35%
36%
36%
37%
37%
38%
38%
39%
39%
40%
40%
41%
41%
42%
42%
43%
43%
44%
44%
45%
45%
46%
46%
47%
47%
48%
48%
49%
49%
50%
50%
51%
51%
52%
52%
53%
53%
54%
54%
55%
55%
56%
56%
57%
57%
58%
58%
59%
59%
60%
60%
61%
61%
62%
62%
63%
63%
64%
64%
65%
65%
66%
66%
67%
67%
68%
68%
69%
69%
70%
70%
71%
71%
72%
72%
73%
73%
74%
74%
75%
75%
76%
76%
77%
77%
78%
78%
79%
79%
80%
80%
81%
81%
82%
82%
83%
83%
84%
84%
85%
85%
86%
86%
87%
87%
88%
88%
89%
89%
90%
90%
91%
91%
92%
92%
93%
93%
94%
94%
95%
95%
96%
96%
97%
97%
98%
98%
99%
99%
100%
```

| 2.14.1. | Number formatting helps make your numbers more readable. |
|---|---|
| 2.14.2. | Specifying Precision |
| 2.14.3. | Applied to strings, the precision specifier specifies the maximum field length |
| 2.14.4. | Illustrating the precision specifier |
| 2.14.5. | Add leading zeros to a number |
| 2.14.6. | NumberFormat.getInstance() |
| 2.14.7. | NumberFormat.getCurrencyInstance(Locale.ENGLISH) |
| 2.14.8. | NumberFormat: Minimum Integer Digits, Maximum/Minimum Fraction Digits |
| 2.14.9. | Number format with FieldPosition |
| 2.14.10. | NumberFormat.getPercentInstance(Locale.ENGLISH) |
| 2.14.11. | A number formatter for logarithmic values. This formatter does not support parsing. |
| 2.14.12. | Format a percentage for presentation to the user |
| 2.14.13. | Get Percent Value |
| 2.14.14. | Helper class for format number and currency |
