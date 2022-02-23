#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
using namespace std;

const int inf = 1e9 + 7;

struct Station
{
    int right,left;
};


int main(int argc, char* argv[]){
    try{
        ifstream inp(argv[1]);
        ifstream out(argv[2]);
        //input
        //入力
        int M, S, T, L;
        inp >> M >> S >> T >> L;
        //cin>>M>>S>>T>>L;
        vector<vector<int> > t(M, vector<int>(S));
        for(int i = 0; i < M; i++){
            for(int j = 0; j < S; j++){
                inp >> t[i][j];
                //cin>>t[i][j];
            }
        }
        int tmp = 0;
        vector<Station> station(S);
        for(int i = 0; i < S; i++){
            int x;
            inp >> x;
            //cin>>x;
            station[i].left = tmp + 1;
            station[i].right = x;
            tmp = x;
        }

        int N = 0;
        vector<int>num(M);
        for(int i = 0; i < M; i++){
            inp >> num[i];
            //cin>>num[i];
            N += num[i];
        }

        //output & validation
        //出力とその整合性を確認

        int K;
        vector<int> p;
        {
            int j = 0;
            string line;
            while(getline(out, line)){
                if(j > 1)throw logic_error("output contains too many lines");
                if(j == 0){
                    int now = 0;
                    int cnt = 0;
                    for(int i = 0; i < line.size(); i++){
                        if(cnt == 2)throw logic_error("invalid output format in line 1");
                        if(isspace(line[i])){
                            K = now;
                            cnt++;
                        }else if(line[i] - '0' < 0 || line[i] - '0' >= 10){
                            throw logic_error("invalid character in line 1");
                        }else{
                            if(cnt == 0)cnt = 1;
                            now *= 10;
                            now += line[i] - '0';
                            if(now > N){
                                throw logic_error("K is out of range");
                            }
                        }
                    }
                    if(cnt == 0)throw logic_error("invalid output format in line 1");
                    if(cnt == 1)K = now;
                    p.resize(K);
                }
                if(j == 1){
                    int now = 0;
                    int k = 0;
                    for(int i = 0; i < line.size(); i++){
                        if(k == K){
                            throw logic_error("invalid output format in line 2");
                        }
                        if(isspace(line[i])){
                            p[k] = now;
                            now = 0;
                            k++;
                        }else if(line[i] - '0' < 0 || line[i] - '0' >= 10){
                            throw logic_error("invalid character in line 2");
                        }else{
                            now *= 10;
                            now += line[i] - '0';
                            if(now > M){
                                string s  = "p[";
                                s += to_string(k+1);
                                s += "] is out of range";
                                throw logic_error(s);
                            }
                        }
                    }
                    if(k == K-1){
                        if(!isspace(line[line.size()-1])){
                            p[k] = now;
                            k++;
                        }
                    }
                    if(k <= K-1){ 
                        throw logic_error("Less than K elements in p");
                    }
                }
                j++;
            }
        }

        {
            vector<int>cnt(M);
            for(int i = 0; i < K; i++){
                p[i]--;
                if(p[i] < 0 || p[i] >= M){
                    string s  = "p[";
                    s += to_string(i+1);
                    s += "] is out of range";
                    throw logic_error(s);
                }
                cnt[p[i]]++;
            }
            for(int i = 0; i < M; i++){
                if(cnt[i] > num[i]){
                    string s="Too many cars of type " + to_string(i+1);
                    throw logic_error(s);
                }
            }
        }

        //シミュレーション
        //Simulation

        int Time = 0;
        int stop_Time = 0;

        //index of the next task for each station(0~K-1)
        //各ステーションに対し、次に処理すべきタスクの番号(0~K-1)
        vector<int>head(S);

        //progress of for each pair of car and station
        //タスクとステーションのペアに関する進捗
        vector<vector<int> >progress(K, vector<int>(S));

        //number of completed cars of each type
        //各種類のタスクについて完了した個数
        vector<int>m(M);

        while(head[S - 1] < K){
            //compute the minimum of these three kinds of time
            //the time when any incomplete task reaches at the end of the station
            //the time when any task reaches the beginning of the next station
            //the time when any task is completed

            //以下の中の最短時間を求める
            //未完了のタスクが未完了のままステーションの終点につく時間
            //あるタスクについて次のステーションに到着する時間
            //タスク完了する時間
            int t_min = inf;

            for(int j = 0; j < S; j++){
                int k = head[j];
                if(k == K)continue;
                int x = Time - stop_Time - k * T;
                if(x < station[j].left){
                    t_min = min(t_min, station[j].left - x);
                }else{
                    t_min = min(t_min, min(station[j].right - x,t[p[k]][j] - progress[k][j]) );
                }
            }
            //If the time of next event is over L, then finish
            //次のイベントが L を超えているなら終了
            if(t_min + Time > L){
                Time = L + 1;
                break;
            }
            //else process next event and time
            //そうでない時、次のイベントを処理して時間計算
            if(t_min > 0){
                for(int j = 0; j < S; j++){
                    int k = head[j];
                    if(k == K)continue;
                    int x = Time - stop_Time - k * T;
                    if(x < station[j].left)continue;
                    if(x >= station[j].left)progress[k][j] += t_min;
                }
                Time += t_min;
            }else{
                int res_min = inf;
                for(int j = 0; j < S; j++){
                    int k = head[j];
                    if(k == K)continue;
                    int x = Time - stop_Time - k * T;
                    if(x < station[j].left)continue;
                    res_min = min(res_min, t[p[k]][j] - progress[k][j]);
                }

                if(res_min + Time > L){
                    Time = L + 1;
                    break;
                }
                stop_Time += res_min;
                Time += res_min;
                for(int j = 0; j < S; j++){
                    int k = head[j];
                    if(k == K)continue;
                    int x = Time - stop_Time - k * T;
                    if(x < station[j].left)continue;
                    progress[k][j] += res_min;
                    if(progress[k][j] == t[p[k]][j]){
                        head[j]++;
                        if(j == S - 1){
                            m[p[k]]++;
                        }
                    }
                }
            }
        }
        //compute score
        //スコア計算
        int score = 0;
        if(Time == L + 1 || K < N){
            double sc = 0;
            for(int i = 0; i < M; i++){
                sc += sqrt( (double)m[i] / (double)num[i] );
            }
            sc *= 1000000.0;
            sc /= M;
            score = round(sc);
        }else{
            double sc = 1000000.0 * (2.0 - (double)Time / (double)L );
            score = round(sc);
        }

        printf("IMOJUDGE<<<%d>>>\n", score);
        return 0;
    }
    catch(logic_error e) {
        cerr << e.what() << endl;
        return 1;
    }
    catch(char* str){
        cerr << "error: " << str << endl;
        return 1;
    }
    return 1;
}