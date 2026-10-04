---
title: Convert Object to BigDecimal
nav: Convert Object to BigDecimal
description: throw new ClassCastException("Not possible to coerce ["+value+"] from class "+value.getClass()+" into a BigDecimal.");
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20111105111550/http://java2s.com/Tutorial/Java/0040__Data-Type/ConvertObjecttoBigDecimal.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
/**
 * Utility methods for math classes
 *
 * @author etirelli
 */
public class MathUtils {
    public static BigDecimal getBigDecimal( Object value ) {
        BigDecimal ret = null;
        if( value != null ) {
            if( value instanceof BigDecimal ) {
                ret = (BigDecimal) value;
            } else if( value instanceof String ) {
                ret = new BigDecimal( (String) value );
            } else if( value instanceof BigInteger ) {
                ret = new BigDecimal( (BigInteger) value );
            } else if( value instanceof Number ) {
                ret = new BigDecimal( ((Number)value).doubleValue() );
            } else {
                throw new ClassCastException("Not possible to coerce ["+value+"] from class "+value.getClass()+" into a BigDecimal.");
            }
        }
        return ret;
    }
}
```
