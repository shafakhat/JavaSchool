---
title: Wrapper for arrays of ordered strings. This verifies the arrays and supports efficient lookups.
nav: Wrapper for arrays of orde...
description: * Wrapper for arrays of ordered strings. This verifies the arrays and supports
section: Imported - java2s Archive
order: 2384
source: https://web.archive.org/web/20140404052531/http://www.java2s.com/Tutorial/Java/0140__Collections/WrapperforarraysoforderedstringsThisverifiesthearraysandsupportsefficientlookups.htm
---
```java title=Example.java
/**
 * Wrapper for arrays of ordered strings. This verifies the arrays and supports
 * efficient lookups.
 *
 * @author Dennis M. Sosnoski
 */
public class StringArray
{
    /** Ordered array of strings. */
    private final String[] m_list;
    /**
     * Constructor from array of values. This checks the array values to make
     * sure they're ordered and unique, and if they're not throws an exception.
     * Once the array has been passed to this constructor it must not be
     * modified by outside code.
     *
     * @param list array of values
     */
    public StringArray(String[] list) {
        validateArray(list);
        m_list = list;
    }
    /**
     * Constructor from array of values to be added to base instance. This
     * merges the array values, making sure they're ordered and unique, and if
     * they're not throws an exception.
     *
     * @param list array of values
     * @param base base instance
     */
    public StringArray(String[] list, StringArray base) {
        validateArray(list);
        m_list = mergeArrays(list, base.m_list);
    }
    /**
     * Constructor from pair of base instances. This merges the values, making
     * sure they're unique, and if they're not throws an exception.
     *
     * @param array1 first base array
     * @param array2 second base array
     */
    public StringArray(StringArray array1, StringArray array2) {
        m_list = mergeArrays(array1.m_list, array2.m_list);
    }
    /**
     * Constructor from array of values to be added to pair of base instances.
     * This merges the array values, making sure they're ordered and unique, and
     * if they're not throws an exception.
     *
     * @param list array of values
     * @param array1 first base array
     * @param array2 second base array
     */
    public StringArray(String[] list, StringArray array1, StringArray array2) {
        validateArray(list);
        m_list = mergeArrays(list, mergeArrays(array1.m_list, array2.m_list));
    }
    /**
     * Constructor from array of values to be added to three base instances.
     * This merges the array values, making sure they're ordered and unique, and
     * if they're not throws an exception.
     *
     * @param list array of values
     * @param array1 first base array
     * @param array2 second base array
     * @param array3 third base array
     */
    public StringArray(String[] list, StringArray array1, StringArray array2,
        StringArray array3) {
        validateArray(list);
        m_list = mergeArrays(list, mergeArrays(array1.m_list,
            mergeArrays(array2.m_list, array3.m_list)));
    }
    /**
     * Constructor from array of values to be added to four base instances.
     * This merges the array values, making sure they're ordered and unique, and
     * if they're not throws an exception.
     *
     * @param list array of values
     * @param array1 first base array
     * @param array2 second base array
     * @param array3 third base array
     * @param array4 fourth base array
     */
    public StringArray(String[] list, StringArray array1, StringArray array2,
        StringArray array3, StringArray array4) {
        validateArray(list);
        m_list = mergeArrays(list, mergeArrays(array1.m_list,
            mergeArrays(array2.m_list,
            mergeArrays(array3.m_list, array4.m_list))));
    }
    /**
     * Merge a pair of ordered arrays into a single array. The two source arrays
     * must not contain any values in common.
     *
     * @param list1 first ordered array
     * @param list2 second ordered array
     * @return merged array
     */
    private String[] mergeArrays(String[] list1, String[] list2) {
        String[] merge = new String[list1.length + list2.length];
        int fill = 0;
        int i = 0;
        int j = 0;
        while (i < list1.length && j < list2.length) {
            int diff = list2[j].compareTo(list1[i]);
            if (diff > 0) {
                merge[fill++] = list1[i++];
            } else if (diff < 0) {
                merge[fill++] = list2[j++];
            } else {
                throw new IllegalArgumentException
                    ("Repeated value not allowed: \"" + list1[i] + '"');
            }
        }
        if (i < list1.length) {
            System.arraycopy(list1, i, merge, fill, list1.length-i);
        }
        if (j < list2.length) {
            System.arraycopy(list2, j, merge, fill, list2.length-j);
        }
        return merge;
    }
    /**
     * Make sure passed-in array contains values that are in order and without
     * duplicate values.
     *
     * @param list
     */
    private void validateArray(String[] list) {
        if (list.length > 0) {
            String last = list[0];
            int index = 0;
            while (++index < list.length) {
                String comp = list[index];
                int diff = last.compareTo(comp);
                if (diff > 0) {
                    throw new IllegalArgumentException
                        ("Array values are not ordered");
                } else if (diff < 0) {
                    last = comp;
                } else {
                    throw new IllegalArgumentException
                        ("Duplicate values in array");
                }
            }
        }
    }
    /**
     * Get string at a particular index in the list.
     *
     * @param index list index to be returned
     * @return string at that index position
     */
    public String get(int index) {
        return m_list[index];
    }
    /**
     * Find index of a particular string in the array. This does
     * a binary search through the array values, using a pair of
     * index bounds to track the subarray of possible matches at
     * each iteration.
     *
     * @param value string to be found in list
     * @return index of string in array, or <code>-1</code> if
     * not present
     */
    public int indexOf(String value) {
        int base = 0;
        int limit = m_list.length - 1;
        while (base <= limit) {
            int cur = (base + limit) >> 1;
            int diff = value.compareTo(m_list[cur]);
            if (diff < 0) {
                limit = cur - 1;
            } else if (diff > 0) {
                base = cur + 1;
            } else {
                return cur;
            }
        }
        return -1;
    }
    /**
     * Get number of values in array
     *
     * @return number of values in array
     */
    public int size() {
        return m_list.length;
    }
}
```

| 9.9.1. | How to sort an array |
|---|---|
| 9.9.2. | Sorting an Array in Descending (Reverse) Order |
| 9.9.3. | Shuffle elements of an array |
| 9.9.4. | Minimum and maximum number in array |
| 9.9.5. | Convert an Array to a List |
| 9.9.6. | Extend the size of an array |
| 9.9.7. | How to copy an array |
| 9.9.8. | Performing Binary Search on Java Array |
| 9.9.9. | Java Sort byte Array |
| 9.9.10. | Java Sort char Array |
| 9.9.11. | Java Sort double Array |
| 9.9.12. | Java Sort float Array |
| 9.9.13. | Sort an array: case-sensitive |
| 9.9.14. | Sort an array: case-insensitive |
| 9.9.15. | java.utils.Arrays provides ways to dump the content of an array. |
| 9.9.16. | Dump multi-dimensional arrays |
| 9.9.17. | Use java.util.Arrays.deepToString() to dump the multi-dimensional arrays |
| 9.9.18. | Shifting Elements in an Array: Shift all elements right by one |
| 9.9.19. | Shifting Elements in an Array: Shift all elements left by one |
| 9.9.20. | Compare two byte type arrays |
| 9.9.21. | Compare two char type arrays |
| 9.9.22. | Compare two short type arrays |
| 9.9.23. | Compare two int type arrays |
| 9.9.24. | Compare two long type arrays |
| 9.9.25. | Compare two float type arrays |
| 9.9.26. | Compare two double type arrays |
| 9.9.27. | Filling Elements in an Array |
| 9.9.28. | filling object arrays: |
| 9.9.29. | fill to a contiguous range of elements in an array |
| 9.9.30. | If the given objects are equal |
| 9.9.31. | Append the given Object to the given array |
| 9.9.32. | Array To String |
| 9.9.33. | Convert the given array (which may be a primitive array) to an object array |
| 9.9.34. | Gets the subarray from array that starts at offset. |
| 9.9.35. | Gets the subarray of length length from array that starts at offset. |
| 9.9.36. | Growable String array with type specific access methods. |
| 9.9.37. | Wrapper for arrays of ordered strings. This verifies the arrays and supports efficient lookups. |
| 9.9.38. | Reverses the order of the given object array. |
