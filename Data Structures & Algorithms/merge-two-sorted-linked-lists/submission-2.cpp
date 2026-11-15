/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) {
            return list2;
        }
        if (!list2) {
            return list1;
        }

        ListNode *dummy = new ListNode();
        ListNode *result = new ListNode();
        dummy->next = result;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                result->next = list1;
                list1 = list1->next;
            }
            else {
                result->next = list2;
                list2 = list2->next;
            }

            result = result->next;
        }

        if (!list1) {
            result->next = list2;
        }
        else{
            result->next = list1;
        }

        return dummy->next->next;
        
    }
};
