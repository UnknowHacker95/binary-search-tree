#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Note{
  char value[101];
  struct Note *right;
  struct Note *left;
}Tree;

Tree *create(char* data){
  Tree *new = (Tree*)malloc(sizeof(Tree));
  strcpy(new->value, data);
  new->right = NULL;
  new->left = NULL;
  return new;
}

int compare(char str1[], char str2[]){
  int i = 0;
  while(str1[i] == str2[i]){
    if(str1[i] == '\0')
      return 0;
    i++;
  }
  return str1[i] - str2[i];
}

Tree *add(Tree *root, char* data){
  Tree *cur = root, *pred = root, *new = (Tree*)malloc(sizeof(Tree));
  strcpy(new->value, data);
  new->right = NULL;
  new->left = NULL;
  while(1){
    if(compare(data, pred->value) < 0){
      cur = cur->left;
      if(cur == NULL){
        pred->left = new;
        break;
      }
      pred = cur;
    } else if(compare(data, pred->value) > 0){
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
        printf("%s\n", root->value);
        pryamoi(root->left);
        pryamoi(root->right);
    }
}

void obrat(Tree* root) {
    if (root){
        obrat(root->left);
        obrat(root->right);
        printf("%s\n", root->value);
    }
}

void sim(Tree* root) {
  if (root) {
    sim(root->left);
    printf("%s\n", root->value);
    sim(root->right);
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
  char str[101];
  in = fopen("input.txt", "r");
  fscanf(in, "%d", &l);
  fscanf(in, "%s", str);
  q = create(str);
  str[0] = '\0';
  while(fscanf(in, "%s", str) != EOF){
    q = add(q, str);
    str[0] = '\0';
  }
  q1 = q;
  sim(q1);
  return 0;
}
