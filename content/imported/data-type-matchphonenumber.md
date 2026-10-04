---
title: Match Phone Number
nav: Match Phone Number
description: String phoneNumberPattern = "(\\d-)?(\\d{3}-)?\\d{3}-\\d{4}";
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/MatchPhoneNumber.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    String phone = "(111)-111-1111";
    String phoneNumberPattern = "(\\d-)?(\\d{3}-)?\\d{3}-\\d{4}";
    System.out.println(phone.matches(phoneNumberPattern));
  }
}
```
