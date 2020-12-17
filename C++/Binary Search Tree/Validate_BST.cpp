// Validate a Binary Search Tree
// Author: Pavan Kumar Paluri
// Time Complexity: O(N) and Space Complexity: O(N)
// Leetcode Question: https://leetcode.com/problems/validate-binary-search-tree/

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
    bool valid_bst(TreeNode* current, long low, long high)
    {
        if(current==nullptr)
            return true;
        if(current->val <= low||current->val >= high)
            return false;
        return valid_bst(current->left, low, current->val) && valid_bst(current->right, current->val, high);
    }
    bool isValidBST(TreeNode* root) {
        return valid_bst(root, LONG_MIN, LONG_MAX);
    }
};
