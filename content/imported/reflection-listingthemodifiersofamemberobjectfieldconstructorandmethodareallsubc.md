---
title: Listing the Modifiers of a Member Object
nav: Listing the Modifiers of a...
description: int mods = String.class.getDeclaredMethods()[0].getModifiers();
section: Imported - java2s Archive
order: 2187
source: https://web.archive.org/web/20140829092742/http://www.java2s.com/Tutorial/Java/0125__Reflection/ListingtheModifiersofaMemberObjectFieldConstructorandMethodareallsubclassesofMember.htm
---
```java title=Example.java
import java.lang.reflect.Modifier;
public class Main {
  public static void main(String[] argv) throws Exception {
    int mods = String.class.getDeclaredMethods()[0].getModifiers();
    if (Modifier.isPublic(mods)) {
      System.out.println("member is public");
    }
  }
}
```

| 7.12.1. | Return true if the integer argument includes the public modifier, false otherwise |
|---|---|
| 7.12.2. | Return true if the integer argument includes the private modifier, false otherwise. |
| 7.12.3. | Return true if the integer argument includes the protected modifier,false otherwise. |
| 7.12.4. | Return true if the integer argument includes the static modifier, false otherwise. |
| 7.12.5. | Return true if the integer argument includes the final modifier, false otherwise. |
| 7.12.6. | Return true if the integer argument includes the abstract modifier, false otherwise. |
| 7.12.7. | Get all object accessible public fields |
| 7.12.8. | Overriding Default Access |
| 7.12.9. | Listing the Modifiers of a Class Object |
| 7.12.10. | Listing the Modifiers of a Member Object: Field, Constructor, and Method are all subclasses of Member. |
| 7.12.11. | Set Accessibility |
| 7.12.12. | Make AccessibleObject Accessible |
| 7.12.13. | Make field accessible, explicitly setting it accessible |
| 7.12.14. | whether given field is a "public static final" constant |
| 7.12.15. | Gets a method and forces it to be accessible, even if it is not. |
| 7.12.16. | AccessController.doPrivileged(new PrivilegedAction() ) |
