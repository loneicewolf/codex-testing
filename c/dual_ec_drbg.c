#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define P_FIELD 233
#define A_COEFF 1

typedef struct {
    int64_t x;
    int64_t y;
    int inf;
} Point;

static int64_t mod_inv(int64_t a, int64_t p) {
    int64_t t = 0, newt = 1;
    int64_t r = p, newr = a % p;
    while (newr != 0) {
        int64_t q = r / newr;
        int64_t tmp = newt;
        newt = t - q * newt;
        t = tmp;
        tmp = newr;
        newr = r - q * newr;
        r = tmp;
    }
    if (r > 1) return -1;
    if (t < 0) t += p;
    return t;
}

static Point point_add(Point P, Point Q) {
    if (P.inf) return Q;
    if (Q.inf) return P;
    if (P.x == Q.x && (P.y + Q.y) % P_FIELD == 0) {
        Point R = {0,0,1};
        return R;
    }
    int64_t m;
    if (P.x != Q.x || P.y != Q.y) {
        int64_t denom = (Q.x - P.x) % P_FIELD;
        if (denom < 0) denom += P_FIELD;
        m = ((Q.y - P.y) * mod_inv(denom, P_FIELD)) % P_FIELD;
    } else {
        int64_t denom = (2 * P.y) % P_FIELD;
        m = ((3 * P.x * P.x + A_COEFF) * mod_inv(denom, P_FIELD)) % P_FIELD;
    }
    if (m < 0) m += P_FIELD;
    int64_t x3 = (m * m - P.x - Q.x) % P_FIELD;
    if (x3 < 0) x3 += P_FIELD;
    int64_t y3 = (m * (P.x - x3) - P.y) % P_FIELD;
    if (y3 < 0) y3 += P_FIELD;
    Point R = {x3, y3, 0};
    return R;
}

static Point point_mul(int64_t k, Point P) {
    Point R = {0,0,1};
    while (k > 0) {
        if (k & 1) R = point_add(R, P);
        P = point_add(P, P);
        k >>= 1;
    }
    return R;
}

void dual_ec_drbg(int64_t seed, int blocks) {
    Point G = {3, 65, 0};
    Point Q = {83, 97, 0};
    int64_t s = seed;
    for (int i = 0; i < blocks; i++) {
        Point sP = point_mul(s, G);
        s = sP.x % P_FIELD;
        Point rP = point_mul(s, Q);
        printf("%ld\n", rP.x % P_FIELD);
    }
}

#ifndef NO_MAIN
int main(int argc, char **argv) {
    int64_t seed = 7;
    int blocks = 5;
    if (argc > 1) seed = atoll(argv[1]);
    if (argc > 2) blocks = atoi(argv[2]);
    dual_ec_drbg(seed, blocks);
    return 0;
}
#endif
