import pygame

#initialize pygame imported modules
pygame.init()

#define window variables
WIDTH, HEIGHT = 300, 300
FPS = 60
line_width = 4
font = pygame.font.SysFont(None, 27)

#define game logic variables
winner = 0 
draw_counter = 0
game_over = False
pos = []
board = [[0,0,0],[0,0,0],[0,0,0]]
players_list = [1,2]

#define color variables
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

def main():
    clock = pygame.time.Clock()
    run = True
    clicked = False
    while run:  
        clock.tick(FPS)
        draw_window()
        draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if game_over == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                    clicked = False
                    pos = pygame.mouse.get_pos()
                    cell_x = pos[0]
                    cell_y = pos[1]
                    if board[cell_x // 100][cell_y // 100] == 0:
                        current_player = players_list[0]
                        players_list.append(players_list.pop(0))
                        board[cell_x // 100][cell_y // 100] = current_player
                        check_winner(current_player)
        if game_over == True:
            display_winner(winner)
        if draw_counter == 9:
            display_draw()
        pygame.display.update()
    pygame.quit()

def draw_window():
    WIN.fill(BLACK) 
    for x in range(1,3):
        pygame.draw.line(WIN, WHITE, (0, x * 100), (WIDTH, x * 100), line_width)
        pygame.draw.line(WIN, WHITE, (x * 100, 0), (x * 100, HEIGHT), line_width)

def draw_board():
    x_pos = 0
    for x in board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(WIN, WHITE, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(WIN, WHITE, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == 2:
                pygame.draw.circle(WIN, WHITE, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1 

def check_winner(current_player):
    global draw_counter 
    global winner
    global game_over
    asc_diagonal_cond = True
    dsc_diagonal_cond = True
    #horizontal win 
    for i in range(3):
        if board[i].count(current_player) == 3:
            winner = current_player
            game_over = True
    #vertical win
    for i in range(3):
        vertical_counter = 0
        for x in range(3):
            if board[x][i] == current_player:
                vertical_counter += 1 
            if vertical_counter == 3:
                winner = current_player
                game_over = True
    #diagonal win
    for i in range(3):
        if board[i][i] != current_player:
            dsc_diagonal_cond = False
        if board[i][len(board) - 1 - i] != current_player:
            asc_diagonal_cond = False
    if asc_diagonal_cond == True or dsc_diagonal_cond == True:
        winner = current_player
        game_over = True
    draw_counter += 1

def display_winner(winner):
    win_text = f"Player{winner} is the winner!"
    win_img = font.render(win_text, True, BLUE)
    pygame.draw.rect(WIN, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 - 60, 200 ,50))
    WIN.blit(win_img, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

#draw-outcome condition
def display_draw():
    draw_text = f"It's a draw!"
    draw_img = font.render(draw_text, True, BLUE)
    pygame.draw.rect(WIN, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 - 60, 200 ,50))
    WIN.blit(draw_img, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

if __name__ == "__main__":
    main()
