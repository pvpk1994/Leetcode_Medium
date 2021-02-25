// Finding the Kth largest value in a Binary Search tree
// Using Reverse-Inorder Traversal => (right, root, left)
// Time Complexity: O(H+K), H:height of BST
// Space Complexity: O(H) 
// Author: Pavan Kumar Paluri
// AlgoExpert Question: https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST

using namespace std;

// This is an input class. Do not edit.
class BST {
public:
  int value;
  BST *left = nullptr;
  BST *right = nullptr;

  BST(int value) { this->value = value; }
};

struct Tree_Info {
	int num_nodes;
	int last_visited_node;
};

void reverse_inorder(BST* root, int k, Tree_Info &tf) // pass by ref for tf
{
	if(root == nullptr || tf.num_nodes==k)
		return;
	reverse_inorder(root->right, k, tf);
	if(tf.num_nodes < k)
	{
		tf.num_nodes += 1;
		tf.last_visited_node = root->value;
	}
	reverse_inorder(root->left, k, tf);
}

int findKthLargestValueInBst(BST *tree, int k) {
  // Write your code here.
	BST *root = tree;
	auto tf = Tree_Info{0, -1}; // passing default values to an instance of struct tf
	reverse_inorder(root, k, tf);
  return tf.last_visited_node;
}

