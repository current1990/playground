int get_root(int idx, int max) {
    return (idx + 1) / 2;
}

int get_left(int idx, int max) {
    int p = 2 * idx + 1;
    return p <= max ? p : -1;
}

int get_right(int idx, int max) {
    int p = 2 * idx + 2;
    return p <= max ? p : -1;
}

int has_child(int idx, int max) {
    return get_left(idx, max) > 0 || get_right(idx, max) > 0
}

void adjust(int* table, int idx, void (*judge)(int, int, int)) {
    if(!has_child()) {
        return;
    }

    if(judge())
}

int max_three(int a, int b, int c) {
    if(a >= b && a >= c) {
        return a;
    }
    if(b >= a && b >= c) {
        return b;
    }
    if(c >= b && c >= a) {
        return c;
    }
}

int min_three(int a, int b, int c) {
    if(a  <= b && a  <= c) {
        return a;
    }
    if(b  <= a && b <= c) {
        return b;
    }
    if(c  <= b && c  <= a) {
        return c;
    }
}


void build_heap(int* data, int len) {

}
