
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
WALLS = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
RED = (230, 0, 0)
BLUE = (0, 0, 255)

# Create the screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game with Walls") 

# Defines the chess piece and puts them in a group
class ChessPiece():
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.has_moved = False

# Board initialization
board = [[None for _ in range(8)] for _ in range(8)]
walls = []  # List to store wall positions

current_player = 'white'
selected_piece = None
selected_pos = None

def init_board():
    for col in range(8):
        board[1][col] = ChessPiece('black', 'pawn', './images/black_pawn.png')
        board[6][col] = ChessPiece('white', 'pawn', './images/white_pawn.png')
    board[0][0] = board[0][7] = ChessPiece('black', 'rook', './images/black_rook.png')
    board[7][0] = board[7][7] = ChessPiece('white', 'rook', './images/white_rook.png')
    board[0][1] = board[0][6] = ChessPiece('black', 'knight', './images/black_knight.webp')
    board[7][1] = board[7][6] = ChessPiece('white', 'knight', './images/white_knight.jpeg')
    board[0][2] = board[0][5] = ChessPiece('black', 'bishop', './images/black_bishop.png')
    board[7][2] = board[7][5] = ChessPiece('white', 'bishop', './images/white_bishop.png')
    board[0][3] = ChessPiece('black', 'queen', './images/black_queen.png')
    board[7][3] = ChessPiece('white', 'queen', './images/white_queen.jpeg')
    board[0][4] = ChessPiece('black', 'king', './images/black_king.webp')
    board[7][4] = ChessPiece('white', 'king', './images/white_king.png')

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    for wall in walls:
        pygame.draw.rect(screen, BLUE, (wall[1] * SQUARE_SIZE, wall[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    if selected_pos:
        pygame.draw.rect(screen, RED, (selected_pos[1] * SQUARE_SIZE, selected_pos[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_piece():
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                screen.blit(piece.image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def handle_click(pos):
    global selected_piece, selected_pos, current_player
    col = pos[0] // SQUARE_SIZE
    row = pos[1] // SQUARE_SIZE

    if selected_piece is None:
        piece = board[row][col]
        if piece and piece.color == current_player:
            selected_piece = piece
            selected_pos = (row, col)
        elif (row, col) not in walls and len(walls) < WALLS:
            walls.append((row, col))  # Place a wall
    else:
        if (row, col) in get_valids_moves(selected_piece, selected_pos[0], selected_pos[1]):
            board[row][col] = selected_piece
            board[selected_pos[0]][selected_pos[1]] = None
            selected_piece.has_moved = True
            current_player = 'black' if current_player == 'white' else 'white'
        selected_piece = None
        selected_pos = None

# Main game loop
def main():
    init_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())
        draw_board()
        draw_piece()
        pygame.display.flip()

if __name__ == "__main__":
    main()
