package code01;

import java.util.HashSet;
import java.util.Set;

/**
 * 面试题 01.01. 判定字符是否唯一
 * 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
 *
 * 示例 1：
 *
 * 输入: s = "leetcode"
 * 输出: false
 * 示例 2：
 *
 * 输入: s = "abc"
 * 输出: true
 * 限制：
 *
 * 0 <= len(s) <= 100
 * 如果你不使用额外的数据结构，会很加分。
 */
public class C0101_IsUnique {

    /**
     * indexOf
     * @param astr
     * @return
     */
    public boolean isUnique5(String astr) {
        for (int i = 0; i < astr.length(); i++) {
            char c = astr.charAt(i);
            //查看后面是否有当前字符
            if (astr.indexOf(c, i + 1) != -1)
                return false;
        }
        return true;
    }

    /**
     * Using Set
     * @param astr
     * @return
     */
    public boolean isUnique4(String astr) {
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < astr.length(); i++) {
            set.add(astr.charAt(i));
        }
        return set.size() == astr.length();
    }

    /**
     * Bits
     * @param astr
     * @return
     */
    public boolean isUnique3(String astr) {
        long bits = 0;
        int size = astr.length();
        for (int i = 0; i < size; i++) {
            int move = astr.charAt(i) - 'A';
            if ((bits & (1L << move)) != 0) {
                //有重复的，直接返回false
                return false;
            } else {
                //标记当前位置有这个字符
                bits |= (1L << move);
            }
        }
        return true;
    }

    /**
     * unicode
     * @param astr
     * @return
     */
    public boolean isUnique2(String astr) {
        int[] arr = new int[128];
        for (int i = 0; i < astr.length(); i++) {
            //把字符和数组关联
            if (arr[astr.charAt(i)] != 0)
                return false;
            arr[astr.charAt(i)]++;
        }
        return true;
    }

    /**
     * Bubble
     * @param astr
     * @return
     */
    public boolean isUnique(String astr) {
        if(astr == null || astr.length() <=1) {
            return true;
        }
        for(int i = 0; i <= astr.length() - 1; i++) {
            for(int j = i + 1; j <= astr.length() - 1; j++) {
                if(astr.charAt(i) == astr.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(new C0101_IsUnique().isUnique("aa"));
    }

}
