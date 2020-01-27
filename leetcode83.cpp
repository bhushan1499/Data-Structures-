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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode*current = head;
        ListNode*Next;
        if(current==NULL)
            return NULL;
        while(current->next!=NULL){
            
            if(current->val==current->next->val)
            {
                Next = current->next->next;
                delete current->next;
                current->next = Next;
            }
            else{
                current = current->next;
            }
            
            
        }
        return head;
    }
};
