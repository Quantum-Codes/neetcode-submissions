class Solution {
private:
    bool check_square(pair<int, int> topleft, vector<int>& freq, vector<vector<char>>& board) {
        // topleft = topleft of the square. we check topleft,.., topleft+2 inclusive rows x cols
        fill(freq.begin(), freq.end(), 0);
        for (int i = topleft.first; i < topleft.first + 3; i++) {
            for (int j = topleft.second; j < topleft.second + 3; j++) {
                char c = board[i][j];
                int idx = (c == '.') ? 0 : c - '0';
                freq[idx]++;
                if (freq[idx] > 1 && idx > 0) {
                    return false;
                }
            }
        }
        return true;
    }
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // rows check
        vector<int> freq;
        freq.resize(10);
        for (vector<char>& row : board) {
            fill(freq.begin(), freq.end(), 0);
            for (char& c : row) {
                int idx = (c == '.') ? 0 : c - '0';
                freq[idx]++;
                if (freq[idx] > 1 && idx > 0) {
                    return false;
                }
            }
        }

        // cols check
        for (int col = 0; col < 9; col++) {
            fill(freq.begin(), freq.end(), 0);
            for (int row = 0; row < 9; row++) {
                char c = board[row][col];
                int idx = (c == '.') ? 0 : c - '0';
                freq[idx]++;
                if (freq[idx] > 1 && idx > 0) {
                    return false;
                }
            }
        }

        // square check
        for (int i = 0; i < 9; i = i+3) {
            for (int j = 0; j < 9; j = j+3) {
                if (!check_square({i, j}, freq, board)) {
                    return false;
                }
            }
        }
        return true;
    }
};
