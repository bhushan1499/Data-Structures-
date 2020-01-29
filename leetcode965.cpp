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
    set<int >s;
    bool isUnivalTree(TreeNode* root) {
        
        if(root){
        s.insert(root->val);
        isUnivalTree(root->left);
        isUnivalTree(root->right);
        }
        if(s.size()>1)
            return false;
        return true;
    }
};
