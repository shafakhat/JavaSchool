---
title: All static information about a character
nav: All static information abo...
description: public static void main(String[] args) throws java.io.IOException {
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20090124230322/http://www.java2s.com:80/Code/Java/Data-Type/Allstaticinformationaboutacharacter.htm
---
All static information about a character

```java title=Example.java
public class Classify {
  public static void main(String[] args) throws java.io.IOException {
    char c = '\u0beb'; // Tamil digit.
    System.out.println("Character = " + (int) c);
    System.out.println("Defined = " + Character.isDefined(c));
    System.out.println("Digit = " + Character.isDigit(c));
    System.out.println("Ignorable = " + Character.isIdentifierIgnorable(c));
    System.out.println("ISO control = " + Character.isISOControl(c));
    System.out.println("Java identifier part = " + Character.isJavaIdentifierPart(c));
    System.out.println("Java identifier start = " + Character.isJavaIdentifierStart(c));
    System.out.println("Letter = " + Character.isLetter(c));
    System.out.println("Letter or digit = " + Character.isLetterOrDigit(c));
    System.out.println("Lowercase = " + Character.isLowerCase(c));
    System.out.println("Space = " + Character.isSpaceChar(c));
    System.out.println("Titlecase = " + Character.isTitleCase(c));
    System.out.println("Unicode identifier part = " + Character.isUnicodeIdentifierPart(c));
    System.out.println("Unicode identifier start = " + Character.isUnicodeIdentifierStart(c));
    System.out.println("Uppercase = " + Character.isUpperCase(c));
    System.out.println("White space = " + Character.isWhitespace(c));
    byte[] types = { Character.COMBINING_SPACING_MARK, Character.CONNECTOR_PUNCTUATION,
        Character.CONTROL, Character.CURRENCY_SYMBOL, Character.DASH_PUNCTUATION,
        Character.DECIMAL_DIGIT_NUMBER, Character.ENCLOSING_MARK, Character.END_PUNCTUATION,
        Character.FORMAT, Character.LETTER_NUMBER, Character.LINE_SEPARATOR,
        Character.LOWERCASE_LETTER, Character.MATH_SYMBOL, Character.MODIFIER_SYMBOL,
        Character.NON_SPACING_MARK, Character.OTHER_LETTER, Character.OTHER_NUMBER,
        Character.OTHER_PUNCTUATION, Character.OTHER_SYMBOL, Character.PARAGRAPH_SEPARATOR,
        Character.PRIVATE_USE, Character.SPACE_SEPARATOR, Character.START_PUNCTUATION,
        Character.SURROGATE, Character.TITLECASE_LETTER, Character.UNASSIGNED,
        Character.UPPERCASE_LETTER };
    String[] typeNames = { "Combining spacing mark", "Connector punctuation", "Control",
        "Currency symbol", "Dash punctuation", "Decimal digit number", "Enclosing mark",
        "End punctuation", "Format", "Letter number", "Line separator", "Lowercase letter",
        "Math symbol", "Modifier symbol", "Non spacing mark", "Other letter", "Other number",
        "Other punctuation", "Other symbol", "Paragraph separator", "Private use",
        "Space separator", "Start punctuation", "Surrogate", "Titlecase letter", "Unassigned",
        "Uppercase letter" };
    int type = Character.getType(c);
    for (int i = 0; i < types.length; i++)
      if (type == types[i]) {
        System.out.println("Type name = " + typeNames[i]);
        break;
      }
    System.out.println("Unicode block = " + Character.UnicodeBlock.of(c));
  }
}
/*Character = 3051
Defined = true
Digit = true
Ignorable = false
ISO control = false
Java identifier part = true
Java identifier start = false
Letter = false
Letter or digit = true
Lowercase = false
Space = false
Titlecase = false
Unicode identifier part = true
Unicode identifier start = false
Uppercase = false
White space = false
Type name = Decimal digit number
Unicode block = TAMIL
*/
```

1.  Character class creates primitives that wrap themselves around data items of the char data type
---  ---
2.  Create Character objects and compare them
3.  Use Character.isLowerCase, Character.isUpperCase to check the letter case
4.  Use Character.isLetter to check if a char is a letter
5.  Use Character.isDigit to check the if a char is a digit
6.  switch with char value
7.  Char is Int
8.  Convert to hex
