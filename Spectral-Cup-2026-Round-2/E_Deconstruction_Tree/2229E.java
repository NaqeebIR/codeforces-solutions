import java.io.*;
import java.util.*;

public class Main {
    static final long AkASH_MOD = 998244353L;

    static class NaqeebIr {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c, val = 0;
            do c = read(); while (c <= ' ');
            while (c > ' ') {
                val = val * 10 + c - '0';
                c = read();
            }
            return val;
        }
    }

    static class IrtazaTree {
        int limit;
        long[] bit;

        IrtazaTree(int n) {
            limit = n;
            bit = new long[n + 5];
        }

        void touch(int idx, long val) {
            val %= AkASH_MOD;
            if (val < 0) val += AkASH_MOD;

            while (idx <= limit) {
                bit[idx] = (bit[idx] + val) % AkASH_MOD;
                idx += idx & -idx;
            }
        }

        void cover(int l, int r, long val) {
            if (l > r) return;
            touch(l, val);
            touch(r + 1, -val);
        }

        long ask(int idx) {
            long res = 0;
            while (idx > 0) {
                res = (res + bit[idx]) % AkASH_MOD;
                idx -= idx & -idx;
            }
            return res;
        }
    }

    public static void main(String[] args) throws Exception {
        NaqeebIr input = new NaqeebIr();
        StringBuilder Naqeeb_Irtaza_AkASH = new StringBuilder();

        int test = input.nextInt();

        while (test-- > 0) {
            int n = input.nextInt();

            ArrayList<Integer>[] road = new ArrayList[n + 1];
            ArrayList<Integer>[] son = new ArrayList[n + 1];

            for (int i = 1; i <= n; i++) {
                road[i] = new ArrayList<>();
                son[i] = new ArrayList<>();
            }

            for (int i = 0; i < n - 1; i++) {
                int u = input.nextInt();
                int v = input.nextInt();

                road[u].add(v);
                road[v].add(u);
            }

            int[] father = new int[n + 1];
            int[] branch = new int[n + 1];
            int[] line = new int[n];

            int len = 0;
            father[n] = -1;
            line[len++] = n;

            for (int p = 0; p < len; p++) {
                int now = line[p];

                for (int nxt : road[now]) {
                    if (nxt == father[now]) continue;

                    father[nxt] = now;
                    son[now].add(nxt);

                    branch[nxt] = (now == n) ? nxt : branch[now];
                    line[len++] = nxt;
                }
            }

            if (son[n].size() <= 1) {
                Naqeeb_Irtaza_AkASH.append(1).append('\n');
                continue;
            }

            int[] inTime = new int[n + 1];
            int[] outTime = new int[n + 1];
            int[] pointer = new int[n + 1];
            int[] box = new int[n + 2];

            int timer = 1, top = 0;
            inTime[n] = timer;
            box[top++] = n;

            while (top > 0) {
                int now = box[top - 1];

                if (pointer[now] < son[now].size()) {
                    int nxt = son[now].get(pointer[now]++);
                    inTime[nxt] = ++timer;
                    box[top++] = nxt;
                } else {
                    outTime[now] = timer;
                    top--;
                }
            }

            int[] downBest = new int[n + 1];

            for (int i = len - 1; i >= 0; i--) {
                int now = line[i];

                for (int nxt : son[now]) {
                    downBest[now] = Math.max(downBest[now], nxt);
                    downBest[now] = Math.max(downBest[now], downBest[nxt]);
                }
            }

            int lastLeaf = 0;
            for (int i = 1; i <= n; i++) {
                if (son[i].isEmpty()) {
                    lastLeaf = Math.max(lastLeaf, i);
                }
            }

            int firstValue = -1, firstBranch = -1;
            int secondValue = -1;

            for (int start : son[n]) {
                int value = Math.max(start, downBest[start]);

                if (value > firstValue) {
                    secondValue = firstValue;
                    firstValue = value;
                    firstBranch = start;
                } else if (value > secondValue) {
                    secondValue = value;
                }
            }

            int[] outside = new int[n + 1];

            for (int i = 1; i < n; i++) {
                outside[i] = (branch[i] == firstBranch) ? secondValue : firstValue;
            }

            ArrayList<Integer>[] enter = new ArrayList[n + 1];
            ArrayList<Integer>[] leave = new ArrayList[n + 1];

            for (int i = 1; i <= n; i++) {
                enter[i] = new ArrayList<>();
                leave[i] = new ArrayList<>();
            }

            for (int node = 1; node < n; node++) {
                int left = downBest[node] + 1;
                int right = node - 1;

                if (left <= right) {
                    enter[right].add(node);
                    leave[left].add(node);
                }
            }

            long[] dp = new long[n + 1];
            dp[n] = 1;

            IrtazaTree fenwick = new IrtazaTree(n + 2);
            long active = 0;

            for (int current = n - 1; current >= 1; current--) {
                for (int node : enter[current]) {
                    active = (active + dp[node]) % AkASH_MOD;
                    fenwick.cover(inTime[node], outTime[node], dp[node]);
                }

                long blocked = fenwick.ask(inTime[current]);
                dp[current] = (active - blocked + AkASH_MOD) % AkASH_MOD;

                if (outside[current] < current) {
                    dp[current] = (dp[current] + 1) % AkASH_MOD;
                }

                for (int node : leave[current]) {
                    active = (active - dp[node] + AkASH_MOD) % AkASH_MOD;
                    fenwick.cover(inTime[node], outTime[node], -dp[node]);
                }
            }

            Naqeeb_Irtaza_AkASH.append(dp[lastLeaf] % AkASH_MOD).append('\n');
        }

        System.out.print(Naqeeb_Irtaza_AkASH);
    }
}