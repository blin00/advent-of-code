#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
template<typename C,typename T=typename enable_if<!is_same<C,string>::value,typename C::value_type>::type>
ostream& operator<<(ostream&os,const C&v){os<<"[";bool f=1;for(const T&x:v){if(!f)os<<", ";os<<x;f=0;}return os<<"]";}
template<typename T1,typename T2>
ostream& operator<<(ostream&os,const pair<T1,T2>&p){return os<<"("<<p.first<<", "<<p.second<<")";}
#define nl '\n'
#ifndef DEBUG_393939
#define cerr while (0) cerr
static const int __39 = [](){ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);return 39;}();
#endif
template<class Fun>
class y_combinator_result {
    Fun fun_;
public:
    template<class T>
    explicit y_combinator_result(T&& fun): fun_(std::forward<T>(fun)) {}
    template<class ...Args>
    decltype(auto) operator()(Args&& ...args) {
        return fun_(std::ref(*this), std::forward<Args>(args)...);
    }
};
template<class Fun>
decltype(auto) y_combinator(Fun &&fun) {
    return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun));
}
template<class T> T& setmin(T& tgt, const T& src) { return (tgt = min(tgt, src)); }
template<class T> T& setmax(T& tgt, const T& src) { return (tgt = max(tgt, src)); }
const uint64_t RANDOM = chrono::high_resolution_clock::now().time_since_epoch().count();
constexpr uint64_t HASH_C = 0x57325bbf44649447; // large odd number for C; ll(4e18 * acos(0)) | 71
struct chash {
    ll operator()(ll x) const { return __builtin_bswap64((x ^ RANDOM) * HASH_C); }
    ll operator()(pii x) const { return operator()((ll(x.first) << 32) | x.second); }
};


const int dx[4]{-1,0,1,0};
const int dy[4]{0,1,0,-1};

const int inf = 2e9;

int main() {
    vector<string> grid;
    int R, C;
    string s;
    while (cin >> s) {
        grid.push_back(s);
    }
    R = sz(grid);
    C = sz(grid[0]);
    int R2 = R * 5, C2 = C * 5;
    vector<vi> grid2(R2, vi(C2));
    rep(ii, 0, 5) {
        rep(jj, 0, 5) {
            rep(i, 0, R) {
                rep(j, 0, C) {
                    int orig = grid[i][j] - '0';
                    int extra = ii + jj;
                    int nv = orig + extra;
                    while (nv > 9) {
                        nv -= 9;
                    }
                    grid2[ii * R + i][jj * C + j] = nv;
                }
            }
        }
    }
    priority_queue<array<int, 3>, vector<array<int, 3>>, greater<array<int, 3>>> pq;
    vector<vi> dist(R2, vi(C2, inf));
    dist[0][0] = 0;
    pq.push({0, 0, 0});
    while (!pq.empty()) {
        auto [d, i, j] = pq.top(); pq.pop();
        if (i == R2 - 1 && j == C2 - 1) {
            cout << d << nl;
            return 0;
        }
        if (d > dist[i][j]) {
            continue;
        }
        rep(k, 0, 4) {
            int ni = i + dx[k];
            int nj = j + dy[k];
            if (ni < 0 || ni >= R2 || nj < 0 || nj >= C2) continue;
            int nd = dist[i][j] + grid2[ni][nj];
            if (nd < dist[ni][nj]) {
                dist[ni][nj] = nd;
                pq.push({nd, ni, nj});
            }
        }
    }
    return 0;
}
