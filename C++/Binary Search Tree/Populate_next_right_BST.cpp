// Populate next right pointer in Binary Search Tree 
// Author: Pavan Kumar Paluri
// Leetcode Question: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

// Time Complexity: O(N) since each node is being visited once 
// Space Complexity: O(N) since we are maintaining a que of atmost N nodes of BST

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if(root == nullptr)
            return root;
        queue<Node*> q;
        // push the root node
        q.push(root);
        while(!q.empty())
        {
            int len = q.size();
            for(int i=0; i<len; i++)
            {
                Node* current = q.front();
                q.pop();
                // To check if the top most element of que is not None:
                if(i < len-1)
                    current->next = q.front();
                if(current->left != NULL)
                    q.push(current->left);
                if(current->right!= NULL)
                    q.push(current->right);
            }
        }
        return root;
    }
};
