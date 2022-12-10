sample = "sample_input.txt"
real = "real_input.txt"

class CheckForest(object):
    def __init__(self, filename):
        self.forest = []
        with open(filename, 'r') as forest_file:
            for trees in forest_file:
                self.forest.append(trees.rstrip())

        self.rows = len(self.forest)
        self.cols = len(self.forest[0])


    def get_visible_trees(self):
        max_scenic_score = 0


        for row in range(1, self.rows-1):
            for col in range(1, self.cols-1):
                current_scenic_score = self.check_visibility(row, col)
                max_scenic_score = max(max_scenic_score, current_scenic_score)

        return max_scenic_score


    def check_visibility(self, current_row, current_col):
            current_hight = self.forest[current_row][current_col]
            left, right, top, bottom = 0, 0, 0, 0 # scenic scores

            #check left
            i = current_col - 1
            while i >= 0:
                left += 1
                if current_hight <= self.forest[current_row][i]:
                    break
                i -= 1

            #check right
            i = current_col + 1
            while i <= self.cols-1:
                right += 1
                if current_hight <= self.forest[current_row][i]:
                    break
                i += 1

            #check top
            j = current_row - 1
            while j >= 0:
                top += 1
                if current_hight <= self.forest[j][current_col]:
                    break
                j -= 1

            #check bottom
            j = current_row + 1
            while j <= self.rows-1:
                bottom += 1
                if current_hight <= self.forest[j][current_col]:
                    break
                j += 1

            return left * right * top * bottom


c = CheckForest(real)
print(c.get_visible_trees())