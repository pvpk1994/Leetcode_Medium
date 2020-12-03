// Increasing Binary Search Tree using Morris Inorder Traversal 
// Author: Pavan Kumar Paluri
// Leetcode Question: https://leetcode.com/problems/increasing-order-search-tree/
// Time Complexity: O(N) and Space Complexity: O(1)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* current = root;
        TreeNode* dummy = new TreeNode();
        TreeNode* r = dummy;
        // Morris Inorder traversal 
        while(current!=nullptr)
        {
            if(current->left != nullptr)
            {
                TreeNode* new_node = current->left;
                while(new_node->right != nullptr)
                    // keep moving right 
                    new_node = new_node->right;
                // if here: new_node->right is null
                new_node->right = current;
                //break the link between current and new_node 
                TreeNode* left = current->left;
                current->left = NULL;
                current = left;
                // current = current->left;
                // current->left = NULL;
            }
            else
            {   r->right = current;
                r = r->right;
                // current->left is NULL
                current = current->right;
            }
        }
        return dummy->right;
    }
};
