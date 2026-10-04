---
title: Format minutes in mm format like 01, 02 etc.
nav: Format minutes in mm forma...
description: System.out.println("minutes in mm format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1559
source: https://web.archive.org/web/20140427053410/http://www.java2s.com/Tutorial/Java/0120__Development/Formatminutesinmmformatlike0102etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("mm");
    System.out.println("minutes in mm format : " + sdf.format(date));
  }
}
// minutes in m format : 35
```

| 6.12.1. | Get Today's Date |
|---|---|
| 6.12.2. | new SimpleDateFormat('hh') |
| 6.12.3. | new SimpleDateFormat('H') // The hour (0-23) |
| 6.12.4. | new SimpleDateFormat('m'): The minutes |
| 6.12.5. | new SimpleDateFormat('mm') |
| 6.12.6. | new SimpleDateFormat('s'): The seconds |
| 6.12.7. | new SimpleDateFormat('ss') |
| 6.12.8. | new SimpleDateFormat('a'): The am/pm marker |
| 6.12.9. | new SimpleDateFormat('z'): The time zone |
| 6.12.10. | new SimpleDateFormat('zzzz') |
| 6.12.11. | new SimpleDateFormat('Z') |
| 6.12.12. | new SimpleDateFormat('hh:mm:ss a') |
| 6.12.13. | new SimpleDateFormat('HH.mm.ss') |
| 6.12.14. | new SimpleDateFormat('HH:mm:ss Z') |
| 6.12.15. | The day number: SimpleDateFormat('d') |
| 6.12.16. | Two digits day number: SimpleDateFormat('dd') |
| 6.12.17. | The day in week: SimpleDateFormat('E') |
| 6.12.18. | Full day name: SimpleDateFormat('EEEE') |
| 6.12.19. | SimpleDateFormat('MM'): number based month value |
| 6.12.20. | SimpleDateFormat('MM/dd/yy') |
| 6.12.21. | SimpleDateFormat('dd-MMM-yy') |
| 6.12.22. | The month: SimpleDateFormat('M') |
| 6.12.23. | SimpleDateFormat('E, dd MMM yyyy HH:mm:ss Z') |
| 6.12.24. | SimpleDateFormat('yyyy') |
| 6.12.25. | Three letter-month value: SimpleDateFormat('MMM') |
| 6.12.26. | Full length of month name: SimpleDateFormat('MMMM') |
| 6.12.27. | Formatting a Date Using a Custom Format |
| 6.12.28. | Formatting date with full day and month name and show time up to milliseconds with AM/PM |
| 6.12.29. | Format date in dd/mm/yyyy format |
| 6.12.30. | Format date in mm-dd-yyyy hh:mm:ss format |
| 6.12.31. | Formatting day of week using SimpleDateFormat |
| 6.12.32. | Formatting day of week in EEEE format like Sunday, Monday etc. |
| 6.12.33. | Formatting day in d format like 1,2 etc |
| 6.12.34. | Formatting day in dd format like 01, 02 etc. |
| 6.12.35. | Format hour in h (1-12 in AM/PM) format like 1, 2..12. |
| 6.12.36. | Format hour in hh (01-12 in AM/PM) format like 01, 02..12. |
| 6.12.37. | Format hour in H (0-23) format like 0, 1...23. |
| 6.12.38. | Format hour in HH (00-23) format like 00, 01..23. |
| 6.12.39. | Format hour in k (1-24) format like 1, 2..24. |
| 6.12.40. | Format hour in kk (01-24) format like 01, 02..24. |
| 6.12.41. | Format hour in K (0-11 in AM/PM) format like 0, 1..11. |
| 6.12.42. | Format hour in KK (00-11) format like 00, 01,..11. |
| 6.12.43. | Formatting minute in m format like 1,2 etc. |
| 6.12.44. | Format minutes in mm format like 01, 02 etc. |
| 6.12.45. | Format month in M format like 1,2 etc |
| 6.12.46. | Format Month in MM format like 01, 02 etc. |
| 6.12.47. | Format Month in MMM format like Jan, Feb etc. |
| 6.12.48. | Format Month in MMMM format like January, February etc. |
| 6.12.49. | Format seconds in s format like 1,2 etc. |
| 6.12.50. | Format seconds in ss format like 01, 02 etc. |
| 6.12.51. | Format TimeZone in z (General time zone) format like EST. |
| 6.12.52. | Format TimeZone in zzzz format Eastern Standard Time. |
| 6.12.53. | Format TimeZone in Z (RFC 822) format like -8000. |
| 6.12.54. | Format year in yy format like 07, 08 etc |
| 6.12.55. | Format year in yyyy format like 2007, 2008 etc. |
| 6.12.56. | Parsing custom formatted date string into Date object using SimpleDateFormat |
| 6.12.57. | Date Formatting and Localization |
| 6.12.58. | Add AM PM to time using SimpleDateFormat |
| 6.12.59. | Check if a String is a valid date |
