#include <stdio.h>
#include <stdlib.h>

typedef struct Note{
  int value;
  struct Note *right;
  struct Note *left;
}Tree;

Tree *create(int data){
  Tree *new = (Tree*)malloc(sizeof(Tree));
  new->value = data;
  new->right = NULL;
  new->left = NULL;
  return new;
}

Tree *add(Tree *root, int data){
  Tree *cur = root, *pred = root, *new = (Tree*)malloc(sizeof(Tree));
  new->value = data;
  new->right = NULL;
  new->left = NULL;
  while(1){
    if(data < pred->value){
      cur = cur->left;
      if(cur == NULL){
        pred->left = new;
        break;
      }
      pred = cur;
    } else if(data > pred->value){
      cur = cur->right;
      if(cur == NULL){
        pred->right = new;
        break;
      }
      pred = cur;
    } else{
      break;
    }
  }
  return root;
}

void pryamoi(Tree* root) {
    if (root) {
        printf("%d ", root->value);
        pryamoi(root->left);
        pryamoi(root->right);
    }
}

void obrat(Tree* root) {
    if (root){
        obrat(root->left);
        obrat(root->right);
        printf("%d ", root->value);
    }
}
int ma(int a, int b){
  if(a > b){
    return a;
  }
  return b;
}

int visot(Tree* root){
  if(root == NULL){
    return 0;
  }
  return (ma(visot(root->left), visot(root->right)) + 1);
}

int leaf(Tree *root){ 
  if(root == NULL){
    return 0;
  }
  if(root->left == NULL && root->right == NULL){
    return 1;
  }
  return leaf(root->left) + leaf(root->right);
}

int lev(Tree *root, int level){
  if(root == NULL){
    return 0;
  }
  if(level == 0){
    return 1;
  }
  return lev(root->left, level - 1) + lev(root->right, level - 1);
}
int main(void) {
  Tree * q, *q1;
  FILE *in;
  int a, l;
  in = fopen("input.txt", "r");
  fscanf(in, "%d", &l);
  fscanf(in, "%d", &a);
  q = create(a);
  while(fscanf(in, "%d", &a) != EOF){
    q = add(q, a);
  }
  q1 = q;
  printf("%d", lev(q1, l));
  return 0;
}
