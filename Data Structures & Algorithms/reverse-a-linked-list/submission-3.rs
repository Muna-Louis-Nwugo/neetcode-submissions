// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head == None {
            return None;       
        }
        let mut old_head = head.unwrap();
        let mut new_head = old_head.next.take();

        old_head.next = None;
         
        while let Some(_) = new_head {
            let mut new_head_local = new_head.clone().unwrap();
            
            let next_item = new_head_local.next.take();

            new_head_local.next = Some(old_head); 

            old_head = new_head_local;
            new_head = next_item;
        }

        Some(old_head)

    }
}