class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // [index][number_seen] -> 9 rows/cols/boxes, numbers 1-9
        bool rows[9][10] = {false};
        bool cols[9][10] = {false};
        bool boxes[9][10] = {false};
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;
                
                int num = board[r][c] - '0';
                
                // Map the 2D grid of boxes into a single 1D index from 0 to 8
                int box_idx = (r / 3) * 3 + (c / 3);
                
                // If we've seen this number in the current row, col, or box, it's invalid
                if (rows[r][num] || cols[c][num] || boxes[box_idx][num]) {
                    return false;
                }
                
                // Mark it as seen
                rows[r][num] = true;
                cols[c][num] = true;
                boxes[box_idx][num] = true;
            }
        }
        
        return true;
    }
};