#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <numeric>
#include <cmath>
#include <queue>
#include <algorithm>
#include <cmath>
#include <fstream>
using namespace std;

struct xorshift128{
    const unsigned int ini_x = 123456789, ini_y = 362436069, ini_z = 521288629, ini_w = 88675123;
    unsigned int x, y, z, w;
    
    xorshift128() {}

    // シードによってx,y,z,wを初期化 ... initialize x,y,z,w by seed
    void set_seed(unsigned int seed){
        x = ini_x, y = ini_y, z = ini_z, w = ini_w ^ seed;
    }

    unsigned int randint(){
        unsigned int t = x ^ (x << 11);
        x = y;
        y = z;
        z = w;
        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    }

    // [0,r)の範囲の整数で乱数発生 ... generate random integer in [0,r)
    unsigned int randint(unsigned int r){
        assert(r != 0);
        return randint() % r;
    }

    // [l,r)の範囲の整数で乱数発生 ... generate random integer in [l,r)
    unsigned int randint(unsigned int l, unsigned int r){
        assert(r > l);
        return l + randint(r-l);
    }

    // 長さnの順列をランダムに生成し、その前k個分を出力する ... generate a random permutation of size n, and return the first k
    vector<int> randperm(int n, int k){
        assert(k >= 0 && k <= n);
        vector<int> ret(n);
        for(int i = 0; i < n; i++){
            ret[i] = i;
        }
        for(int i = 0; i < k; i++){
            swap(ret[i], ret[randint(i, n)]);
        }
        return vector<int>(ret.begin(), ret.begin() + k);
    }

    // [0,1]の範囲の実数で乱数発生 ... generate random real number in [0,1]
    double uniform(){
        return double(randint()) * 2.3283064370807974e-10;
    }

    // [0,r]の範囲の実数で乱数発生 ... generate random real number in [0,r]
    double uniform(double r){
        assert(r >= 0.0);
        return uniform() * r;
    }

    // [l,r]の範囲の実数で乱数発生 ... generate random real number in [l,r]
    double uniform(double l, double r){
        assert(r >= l);
        return l + uniform(r - l);
    }
};

xorshift128 Random;

int int_pow(int x, int n){
    int ret = 1;
    while(n--) ret *= x;
    return ret;
}

// 文字列をスペース区切りで分割 ... seperate string with a whitespace character 
vector<string> split(string S){
    vector<string> ret;
    string temp;
    for(char c: S){
        if(c == ' '){
            if (!temp.empty()) ret.push_back(temp);
            temp.clear();
        }
        else{
            temp += c;
        }
    }
    ret.push_back(temp);
    return ret;
}

bool eq(double a, double b){
    return abs(a-b) < 1e-6;
}

vector<pair<int, int>> list_ranges(int l, int r){
    if(r - l == 1){
        return {make_pair(l, r)};
    }
    else{
        int m = (l + r) / 2;
        assert(l < m && m < r);
        vector<pair<int, int>> L = list_ranges(l, m), R = list_ranges(m, r);
        L.insert(L.end(), R.begin(), R.end());
        L.insert(L.end(), make_pair(l, r));
        return L;
    }
}

vector<vector<int>> list_attrib_combs(int &A, int &max_attrib_count, vector<int> &attrib_roots, int i, vector<int> cur, set<int> used){
    if(i == A || cur.size() == max_attrib_count){
        return {cur};
    }
    vector<vector<int>> temp = list_attrib_combs(A, max_attrib_count, attrib_roots, i+1, cur, used);
    if(!used.count(attrib_roots[i])){
        cur.push_back(i);
        used.insert(attrib_roots[i]);
        vector<vector<int>> add = list_attrib_combs(A, max_attrib_count, attrib_roots, i+1, cur, used);
        temp.insert(temp.end(), add.begin(), add.end());
        used.erase(attrib_roots[i]);
        cur.pop_back();
    }
    return temp;
}

void assign_work_time(vector<vector<int>> &item_station_work_time, int i, int l, int r, int t){
    while(t--){
        item_station_work_time[i][Random.randint(l, r)]++;
    }
}

void generate_testcase(int t, string INPUT, string outputfile_name){
    int N = 1000;                               // 車の台数 ... number of cars
    int T = 60;                                 // 車の間隔 ... length of interval
    int sz = 4;                                 // s (3 or 4)
    int M = 5 * int_pow(2, sz-1);               // 車の種類数 ... number of types of cars
    int A = int_pow(2, sz);                     // 属性の個数 ... number of attributes
    int SP = 5;                                 // 1工程に割り当てる作業ステーション数の平均 ... average number of work stations per process
    int NP = int_pow(2, sz);                    // 工程の個数 ... number of processes
    int S = SP * NP;                            // 作業ステーションの数 ... number of work stations
    int L;                                      // 最大作業時間 ... limit of work time
    double tmargin_lb = 0.7;                    // a (0.5, 0.6, 0.7 or 0.8)
    double tmargin_ub = 1.0;                    // b (1.0)
    double xmargin = 1.1;                       // c (1.0 or 1.1)
    double tl_max_dev = 0.1;                    // d (0.1)
    bool proto_flag = true;                     // f (true or false)
    unsigned long long sd = 0;                  // seed
    int max_attrib_depth = 3;                   // 属性の親子関係(森)の根からの深さの上限 ... max depth of attribute
    int max_attrib_count = 5;                   // 車種のもつ属性の個数の上限 ... max attribribute of each car type
    double load_min = 1.0;                      // 属性の負荷の下限 ... lower bound of attribute loads
    double load_max = 3.0;                      // 属性の負荷の上限 ... upper bound of attribute loads
    vector<int> attrib_parent;                  // 各属性の親 ... parent of each attribute
    vector<int> attrib_depth;                   // 各属性の親子関係の根からの深さ ... depth of each attribute
    vector<int> attrib_roots;                   // 各属性を含む木の根 ... root of each attribute
    vector<pair<int, int>> attrib_ranges;       // 各属性が影響を与える工程の範囲 ... range of each attribute
    vector<double> attrib_loads;                // 各属性の負荷 ... loads of each attribute
    vector<vector<int>> item_attribs;           // 各車種の属性の集合 ... attribute set of each car type
    vector<vector<double>> item_loads;          // 各車種の各工程への(全ての属性の)負荷の大きさの総和 ... load on each process for each car type
    vector<double> item_sum_loads;              // 各車種の(全ての工程への)負荷の大きさの総和の-1.5乗 ... load for each car type to the power of -1.5
    vector<double> item_weights;                // 各車種の生産比率 ... production ratio of each car type
    vector<double> proc_avg_loads;              // 各工程に割り当てるステーションの数の比率 ... proportion of the number of stations assigned to each process
    vector<int> proc_station_counts;            // 各工程に割り当てるステーションの数 ... number of stations assigned to each process
    vector<vector<int>> item_proc_time;         // 各車種を作るのに各工程でかかる時間 ... total working time of each car type and process
    vector<vector<int>> item_station_work_time; // 各車種を作るのに各ステーションでかかる時間 ... working time of each car type and station
    vector<int> x;                              // 各ステーションの座標 ... coorinate of each station
    vector<int> num_cars;                       // 各車種の生産台数 ... number of each car type

    // 入力によるパラメータ変更 ... process input parameter
    vector<string> argv = split(INPUT);
    int argc = argv.size();

    for(int i = 0; i < argc-1; i += 2){
        string temp = argv[i];
        if(temp == "-sz"){
            sz = stoi(argv[i+1]);
            M = 5 * int_pow(2, sz-1);
            A = int_pow(2, sz);
            NP = int_pow(2, sz);
            S = SP * NP;
        }
        else if(temp == "-a"){
            tmargin_lb = stof(argv[i+1]);
        }
        else if(temp == "-c"){
            xmargin = stof(argv[i+1]);
        }
        else if(temp == "-f"){
            proto_flag = (stoi(argv[i+1]) == 1);
        }
        else if(temp == "-seed"){
            sd = stoull(argv[i+1]);
        }
        else if(temp == "-N"){
            N = stoi(argv[i+1]);
        }
        else{
            cerr << "unknown option: " << argv[i] << '\n';
            exit(0);
        }
    }

    assert(sz == 3 || sz == 4);
    assert(eq(tmargin_lb, 0.5) || eq(tmargin_lb, 0.6) || eq(tmargin_lb, 0.7) || eq(tmargin_lb, 0.8));
    assert(eq(xmargin, 1.0) || eq(xmargin, 1.1));

    if(N < M) N = M;
    Random.set_seed(sd);

    // 属性の親子関係を決定 ... determine attribute tree (forest)
    attrib_parent.assign(A, -1);
    attrib_depth.assign(A, 0);
    attrib_roots.resize(A);
    for(int a = A/2; a < A; a++){
        if(Random.randint(2) == 0){
            int p = Random.randint(a);
            if(attrib_depth[p] < max_attrib_depth){
                attrib_parent[a] = p;
                attrib_depth[a] = attrib_depth[p] + 1;
            }
        }
    }
    for(int i = 0; i < A; i++){
        if(attrib_parent[i] != -1){
            int j = attrib_parent[i];
            assert(j < i);
            attrib_roots[i] = attrib_roots[j];
        }
        else{
            attrib_roots[i] = i;
        }
    }
    
    // 各属性の影響を与える工程の範囲と負荷を決定 ... determine range and loads of each attribute
    vector<pair<int, int>> procs = list_ranges(0, NP);
    assert(procs.size() >= A);
    for(int e: Random.randperm(procs.size(), A)){
        attrib_ranges.push_back(procs[e]);
    }
    for(int i = 0; i < A; i++){
        attrib_loads.push_back(Random.uniform(load_min, load_max));
    }

    // 各車種の持つ属性を決定 ... determine attribute set of each item
    vector<vector<int>> attrib_sets = list_attrib_combs(A, max_attrib_count, attrib_roots, 0, {}, set<int>());
    assert(attrib_sets.size() >= M);
    for(int e: Random.randperm(attrib_sets.size(), M)){
        item_attribs.push_back(attrib_sets[e]);
    }
    
    // 各車種の生産比率を計算 ... calculate proportion of each type
    item_loads.assign(M, vector<double>(NP, 1.0));
    for(int i = 0; i < M; i++){
        for(int a: item_attribs[i]){
            int b = a;
            // 各属性の祖先の負荷も合算する ... consider ancestors of each attribute
            while(b != -1){
                int l = attrib_ranges[b].first, r = attrib_ranges[b].second;
                for(int j = l; j < r; j++){
                    item_loads[i][j] += attrib_loads[b];
                }
                b = attrib_parent[b];
            }
        }
    }
    for(int i = 0; i < M; i++){
        item_sum_loads.push_back(accumulate(item_loads[i].begin(), item_loads[i].end(), 0.0));
        item_weights.push_back(pow(item_sum_loads[i], -1.5));
    }
    double all_item_weights = accumulate(item_weights.begin(), item_weights.end(), 0.0);
    for(int i = 0; i < M; i++){
        item_weights[i] /= all_item_weights;
    }
    
    // 各工程に割り当てる作業ステーションの個数の比率を計算 ... calculate proportion of the number of stations assigned to each process
    for(int j = 0; j < NP; j++){
        proc_avg_loads.push_back(0.0);
        for(int i = 0; i < M; i++){
            proc_avg_loads[j] += item_loads[i][j] * item_weights[i];
        }
    }
    
    // 比率とだいたい一致するように個数を決定 ... calculate number of stations assigned to each process according to proportion
    proc_station_counts.assign(NP, 0);
    priority_queue<pair<double, int>> que;
    for(int i = 0; i < NP; i++){
        que.emplace(proc_avg_loads[i], i);
    }
    for(int t = 0; t < S; t++){
        int i = que.top().second;
        que.pop();
        proc_station_counts[i]++;
        que.emplace(proc_avg_loads[i] / (proc_station_counts[i] + 1.0), i);
    }
    
    // 各車種を作るのに各ステーションでかかる時間を決定 ... calculate working time
    double T_0 = 0.0;
    for(int j = 0; j < NP; j++){
        if(proc_station_counts[j] == 0) continue;
        double temp = 0.0;
        for(int i = 0; i < M; i++){
            temp += item_loads[i][j] * item_weights[i];
        }
        T_0 += temp / proc_station_counts[j];
    }
    T_0 = (NP * T) / T_0;
    item_proc_time.assign(M, vector<int>(NP));
    for(int i = 0; i < M; i++){
        for(int j = 0; j < NP; j++){
            item_proc_time[i][j] = round(T_0 * item_loads[i][j] * Random.uniform(tmargin_lb, tmargin_ub));
            item_proc_time[i][j] = max(item_proc_time[i][j], proc_station_counts[j]);
        }
    }
    item_station_work_time.assign(M, vector<int>(S, 1));
    for(int i = 0; i < M; i++){
        int l = 0;
        for(int j = 0; j < NP; j++){
            int r = l + proc_station_counts[j];
            assign_work_time(item_station_work_time, i, l, r, item_proc_time[i][j] - proc_station_counts[j]);
            l = r;
        }
    }
    
    // 各ステーションの長さを決定 ... calculate length of each station
    x.push_back(0);
    for(int j = 0; j < S; j++){
        int base_len = 0;
        for(int i = 0; i < M; i++){
            base_len = max(base_len, item_station_work_time[i][j]);
        }
        base_len = max(T, int(round(base_len * xmargin)));
        x.push_back(x.back() + 1 + base_len);
    }
    
    // 最後の車種が試作品である場合、所要時間を変更 ... if type M is a prototype, change its working time
    if(proto_flag){
        for(int j = 0; j < S; j++){
            item_station_work_time[M-1][j] = Random.randint(item_station_work_time[M-1][j], x[j+1] - x[j]);
        }
        item_weights[M-1] = 0.0;
    }

    // 制限時間を決定 ... calculate time limit
    L = round(Random.uniform(1 - tl_max_dev, 1 + tl_max_dev) * (T * N + x.back()));
    
    // 各車種の生産台数を決定 ... calculate demand of each car type
    num_cars.assign(M, 1);
    vector<double> cum_weights(M+1, 0.0);
    for(int i = 0; i < M; i++){
        cum_weights[i+1] = cum_weights[i] + item_weights[i];
    }
    for(int t = 0; t < N-M; t++){
        double temp = Random.uniform(cum_weights.back());
        int i = lower_bound(cum_weights.begin(), cum_weights.end(), temp) - cum_weights.begin() - 1;
        if(i < 0) i = 0;
        if(i >= M) i = M-1;
        num_cars[i]++;
    }
    
    // テストケースを出力 ... output testcase
    string OUTPUT = to_string(t);
    while(OUTPUT.size() < 4) OUTPUT = '0'+OUTPUT;
    OUTPUT = outputfile_name + OUTPUT;
    OUTPUT += ".txt";
    ofstream outputfile(OUTPUT);
    
    outputfile << M << ' ' << S << ' ' << T << ' ' << L << '\n';
    for(int i = 0; i < M; i++){
        for(int j = 0; j < S; j++){
            outputfile << item_station_work_time[i][j] << (j == S-1? '\n' : ' ');
        }
    }
    for(int j = 1; j <= S; j++){
        outputfile << x[j] << (j == S? '\n' : ' ');
    }
    for(int i = 0; i < M; i++){
        outputfile << num_cars[i] << (i == M-1? '\n' : ' ');
    }
    outputfile.close();
}

int main(int argc, char *argv[]){
    string outputfile_name = "input";
    if(argc >= 2) outputfile_name = argv[1];
    string INPUT;

    for(int t = 1; getline(cin, INPUT); t++){
        generate_testcase(t, INPUT, outputfile_name);
    }
}
