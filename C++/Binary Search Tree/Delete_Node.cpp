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
    // inorder traversal - has all sorted in ascending order
    int left_pred(TreeNode* root)
    {
        // take one right and proceed until last left node
        root = root->left;
        while(root->right != nullptr)
        {
            // proceed until last left node
            root = root->right;
        }
        // if here: the node is the leftmost node
        return root->val;
    }
    
    int right_succ(TreeNode* root)
    {
        root = root->right;
        while(root->left != nullptr)
        {
            root = root->left;
        }
        return root->val;
    }
    
    TreeNode* deleteNode(TreeNode* root, int key) {
        // if root is Null: return None
        if(root == nullptr)
            return nullptr;
        // if given key is greater than root node in a BST
        if(key > root->val)
        {
            // explore right subtree 
            root->right = deleteNode(root->right, key);
        }
        else if(key < root->val)
        {
            // explore left subtree
            root->left = deleteNode(root->left, key);
        }
        else{
            // if here: key == root->val and is a leaf node 
            if(key == root->val && root->left == nullptr && root->right == nullptr) // this is the desired node to be deleted
                root = nullptr;
            // if there exists a right subtree: explore that
            else if(root->right != nullptr)
            {
                root->val = right_succ(root);
                // delete that node after making current node the val
                root->right = deleteNode(root->right, root->val);
            }
            else {
                root->val = left_pred(root);
                root->left = deleteNode(root->left, root->val);
            }
        }
        return root;
    }
};
