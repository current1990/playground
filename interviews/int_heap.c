#include <stdio.h>
#include <unistd.h>

static int heap_size = 0;

int get_root(int idx) {
    return (idx - 1) / 2;
}

int get_left(int idx) {
    return 2 * idx + 1;
}

int get_right(int idx) {
    return 2 * idx + 2;
}

void swap(int* table, int idx1, int idx2) {
    int tmp = table[idx1];
    table[idx1] = table[idx2];
    table[idx2] = tmp;
}

void adjust(int* table, int idx, int max) {
    printf("adjust %d\n", idx);
    sleep(1);
    int left = get_left(idx);
    int right = get_right(idx);
    if(left >= max) {
        return;
    }
    int min_idx = idx;

    if(table[left] < table[idx]) {
        swap(table, idx, left);
        min_idx = left;
    }
    if(right < max && table[right] < table[idx]) {
        swap(table, idx, right);
        min_idx = right;
    }

    for(int i = 0; i < heap_size; i++) {
        if(i == idx || i == min_idx) {
            printf("\033[31m%d\033[0m,", table[i]);
        } else if(i == left || i == right) {
            printf("\033[33m%d\033[0m,", table[i]);
        } else {
            printf("%d,", table[i]);
        }
    }
    printf("\n");
    if(min_idx != idx) {
        adjust(table, min_idx, max);
    }
}

void build_heap(int* data, int len) {
    int last_root = get_root(len);
    while(last_root >= 0) {
        adjust(data, last_root, len);
        last_root --;
    }
}

void heap_insert(int* heap, int data) {
    heap[heap_size] = data;
    heap_size++;
    int last_root = get_root(heap_size - 1);
    while(last_root >= 0) {
        adjust(heap, last_root, heap_size);
        if(last_root == 0) {
            break;
        }
        last_root = get_root(last_root);
    }
}

int heap_delete(int* heap) {
    int ret = heap[0];
    swap(heap, 0, heap_size - 1);
    heap_size--;
    adjust(heap, 0, heap_size);
    return ret;
}

void print_heap(int* heap) {
    for(int i = 0; i < heap_size; i++) {
        printf("%d,", heap[i]);
    }
    printf("\n");
}

int main() {
    int a[100];
    heap_size = 10;
    for(int i = 0; i < heap_size; i++) {
        a[i] = heap_size - i + 1;
    }

    build_heap(a, heap_size);
    print_heap(a);

    heap_insert(a, 1);
    print_heap(a);

    int t = heap_delete(a);
    printf("Got %d\n", t);
    print_heap(a);

    t = heap_delete(a);
    printf("Got %d\n", t);
    print_heap(a);

    t = heap_delete(a);
    printf("Got %d\n", t);
    print_heap(a);

    return 0;
}
