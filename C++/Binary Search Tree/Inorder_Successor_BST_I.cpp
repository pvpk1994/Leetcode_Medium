// Inorder Successor Binary-Search Tree
// Using Iteration + Inorder Traversal + Node Stack
// Author: Pavan Kumar Paluri

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* right_successor(TreeNode* node)
    {
        // To find the immediate right successor, go one node to root and then left
        node = node->right;
        while(node->left != nullptr)
        {
            node = node->left;
        }
        // if here: node is the leftmost-leaf node
        return node;
    }
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        // if p has right node:
        if(p->right != nullptr)
            return right_successor(p);
        // if p does not have right node:
        vector<TreeNode*> node_stack;
        // begin from root node
        if(root == nullptr)
            return nullptr;
        int prev_node_val = INT_MIN;
        // Go to the leftmost node
        while(node_stack.size()>0 || root != nullptr)
        {
            while(root!=nullptr)
            {
                node_stack.push_back(root);
                root = root->left;
            }
            // last-leaf leftmost node: root
            root = node_stack[node_stack.size()-1];
            node_stack.pop_back();
            if(prev_node_val == p->val)
            {
                return root;
            }
            prev_node_val = root->val;
            root = root->right;
            
        }
        return nullptr;
        }
};
