---
title: Default access level
nav: Default access level
description: When there is no access control modifier preceding a class declaration, the class has the default access level. Classes with the default access level can only be used by
section: Imported - java2s Archive
order: 1123
source: https://web.archive.org/web/20140216153715/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Defaultaccesslevel.htm
---
When there is no access control modifier preceding a class declaration, the class has the default access level. Classes with the default access level can only be used by other classes that belong to the same package.
The Chapter class with the default access level is defined as follows.

```java title=Example.java
class Chapter {
    String title;
    int numberOfPages;
    public void review() {
        Page page = new Page();
        int sentenceCount = page.numberOfSentences;
        int pageNumber = page.getPageNumber();
    }
}
```

| 5.25.1. | Access Control: four access control modifiers |
|---|---|
| 5.25.2. | Class Access Control Modifiers |
| 5.25.3. | Using Access Attributes |
| 5.25.4. | Class Member Access Matrix |
| 5.25.5. | Specifying Access Attributes |
| 5.25.6. | The public Book class |
| 5.25.7. | Default access level |
| 5.25.8. | Class Member Access Control Modifiers |
| 5.25.9. | Composition with public objects |
| 5.25.10. | The protected keyword |
| 5.25.11. | Private Override |
| 5.25.12. | Understand the effects of public and private access |
| 5.25.13. | In a class hierarchy, private members remain private to their class. |
| 5.25.14. | A Superclass Variable Can Reference a Subclass Object |
| 5.25.15. | Create a Singleton Object |
