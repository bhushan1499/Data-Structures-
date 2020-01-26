/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode*first = head;
        ListNode*second = head;
        while(second!=NULL&&second->next!=NULL){
            
            second = second->next->next;
            first = first->next;
        }
        return first;
    }
};
