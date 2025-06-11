import pygame

# --- Your Sudoku Solver Code ---
# (The isSafe, solveSudokuRec, and solveSudoku functions from your question)
def isSafe(mat, row, col, num):
    for x in range(9):
        if mat[row][x] == num:
            return False
    for x in range(9):
        if mat[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if mat[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudokuRec(mat, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if mat[row][col] != 0:
        return solveSudokuRec(mat, row, col + 1)
    for num in range(1, 10):
        if isSafe(mat, row, col, num):
            mat[row][col] = num
            if solveSudokuRec(mat, row, col + 1):
                return True
            mat[row][col] = 0
    return False

def solveSudoku(mat):
    return solveSudokuRec(mat, 0, 0)

# --- Pygame GUI Code ---
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("comicsans", 40)

# Grid properties
CELL_SIZE = WIDTH // 9

def draw_grid(board, original_board):
    screen.fill(WHITE)
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                color = BLACK if original_board[i][j] != 0 else BLUE
                text = font.render(str(board[i][j]), True, color)
                screen.blit(text, (j * CELL_SIZE + (CELL_SIZE // 2 - text.get_width() // 2), i * CELL_SIZE + (CELL_SIZE // 2 - text.get_height() // 2)))

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    original_board = [row[:] for row in board]
    selected = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = (pos[1] // CELL_SIZE, pos[0] // CELL_SIZE)
            if event.type == pygame.KEYDOWN:
                if selected and event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                    row, col = selected
                    board[row][col] = int(event.unicode)
                    original_board[row][col] = int(event.unicode)
                if selected and (event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE):
                    row, col = selected
                    board[row][col] = 0
                    original_board[row][col] = 0
                if event.key == pygame.K_RETURN:
                    if solveSudoku(board):
                         print("Sudoku solved!")
                    else:
                        print("No solution exists for this Sudoku.")

        draw_grid(board, original_board)
        if selected:
            pygame.draw.rect(screen, RED, (selected[1] * CELL_SIZE, selected[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()