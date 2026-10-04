---
title: Validate email address
nav: Validate email address
description: System.out.println("isValid = " + isValidEmailAddress("user@domain.com"));
section: Imported - java2s Archive
order: 2266
source: https://web.archive.org/web/20140606205005/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Validateemailaddress.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.println("isValid = " + isValidEmailAddress("user@domain.com"));
  }
  static boolean isValidEmailAddress(String email) {
    String EMAIL_REGEX = "^[\\w-_\\.+]*[\\w-_\\.]\\@([\\w]+\\.)+[\\w]+[\\w]$";
    return email.matches(EMAIL_REGEX);
  }
}
```

| 8.6.1. | Pattern.matches method |
|---|---|
| 8.6.2. | Find the end point of the second 'B(ond)' |
| 8.6.3. | Match Duplicate Words |
| 8.6.4. | Validate email address |
| 8.6.5. | Matching Line Boundaries in a Regular Expression |
| 8.6.6. | Regex for IP v4 Address |
| 8.6.7. | Regex for IP v6 Address |
