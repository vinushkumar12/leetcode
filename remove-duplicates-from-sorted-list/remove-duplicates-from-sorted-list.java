/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.LinkedHashSet;
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        LinkedHashSet<Integer> uniqueIntegers = new LinkedHashSet<>();
        ListNode answer = new ListNode();
        while(head != null) {
            uniqueIntegers.add(head.val);
            head = head.next;
        }
        ListNode answer_1 = answer;
        for (int tempo: uniqueIntegers) {
            System.out.println(tempo);
            ListNode temp = new ListNode(tempo);
            answer.next = temp;
            answer = answer.next;
        }
        return answer_1.next;
    }
}