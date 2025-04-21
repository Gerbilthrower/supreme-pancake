# Chess Game with a Smaller Board

import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 10  # Adjusted for a smaller board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

class ChessPiece():
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE))
        self.has_moved = False

board = [[None for _ in range(10)] for _ in range(10)]  # Adjusted for a smaller board

current_player = 'white'
selected_piece = None
selected_pos = None

def init_board():
    for col in range(12):
        board[1][col] = ChessPiece('black', 'pawn', './images/black_pawn.png')
        board[8][col] = ChessPiece('white', 'pawn', './images/white_pawn.png')
    board[0][0] = board[0][9] = ChessPiece('black', 'rook', './images/black_rook.png')
    board[9][0] = board[9][9] = ChessPiece('white', 'rook', './images/white_rook.png')
    board[0][1] = board[0][8] = ChessPiece('black', 'knight', './images/black_knight.webp')
    board[9][1] = board[9][8] = ChessPiece('white', 'knight', './images/white_knight.jpeg')
    board[0][2] = board[0][7] = ChessPiece('black', 'bishop', './images/black_bishop.png')
    board[9][2] = board[9][7] = ChessPiece('white', 'bishop', './images/white_bishop.png')
    board[0][3] = ChessPiece('black', 'queen', './images/black_queen.png')
    board[9][3] = ChessPiece('white', 'queen', './images/white_queen.jpeg')
    board[0][4] = ChessPiece('black', 'king', './images/black_king.webp')
    board[9][4] = ChessPiece('white', 'king', './images/white_king.png')

def draw_board():
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    if selected_pos:
        pygame.draw.rect(screen, YELLOW, (selected_pos[1] * SQUARE_SIZE, selected_pos[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_piece():
    for row in range(10):
        for col in range(10):
            piece = board[row][col]
            if piece:
                screen.blit(piece.image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_valid_moves(piece, row, col):
    moves = []
    if piece.type == 'pawn':
        direction = -1 if piece.color == 'white' else 1
        if 0 <= row + direction < 10 and board[row + direction][col] is None:
            moves.append((row + direction, col))
            if (piece.color == 'white' and row == 8) or (piece.color == 'black' and row == 1):
                if board[row + 2 * direction][col] is None:
                    moves.append((row + 2 * direction, col))
        for dc in [-1, 1]:
            if 0 <= row + direction < 10 and 0 <= col + dc < 10:
                if board[row + direction][col + dc] and board[row + direction][col + dc].color != piece.color:
                    moves.append((row + direction, col + dc))

    # Additional movement logic for other pieces (rook, knight, bishop, queen, king) would go here...

    return moves

def is_check(color):
    # Check logic for king's safety would go here...
    return False

def is_game_over():
    # Game over logic would go here...
    return False

def handle_click(pos):
    global selected_piece, selected_pos, current_player
    col = pos[0] // SQUARE_SIZE
    row = pos[1] // SQUARE_SIZE

    if selected_piece is None:
        piece = board[row][col]
        if piece and piece.color == current_player:
            selected_piece = piece
            selected_pos = (row, col)
    else:
        if (row, col) in get_valid_moves(selected_piece, selected_pos[0], selected_pos[1]):
            board[row][col] = selected_piece
            board[selected_pos[0]][selected_pos[1]] = None
            selected_piece.has_moved = True
            current_player = 'black' if current_player == 'white' else 'white'

        selected_piece = None
        selected_pos = None

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
