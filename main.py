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
player1_win_counter = 0
player2_win_counter = 0
tie_counter = 0

#define color variables
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

def main():
    global winner
    global draw_counter
    global game_over 
    global pos
    global board 
    global players_list 
    global player1_win_counter
    global player2_win_counter
    global tie_counter

    clock = pygame.time.Clock()
    run = True
    clicked = False
    next_round = False
    while run:  
        if next_round == False:
            clock.tick(FPS)
            draw_window()
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
            draw_board()
            if game_over == True:
                if winner == 1:
                    player1_win_counter += 1
                else:
                    player2_win_counter += 1
                while next_round == False:
                    display_winner(winner)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                            clicked = True
                        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                            clicked = False
                            next_round = True
                    pygame.display.update()

            elif draw_counter == 9:
                tie_counter += 1
                while next_round == False:
                    display_draw()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                            clicked = True
                        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                            clicked = False
                            next_round = True
                    pygame.display.update()
        else:
            winner = 0 
            draw_counter = 0
            game_over = False
            pos = []
            board = [[0,0,0],[0,0,0],[0,0,0]]
            players_list = [1,2]

            next_round = False
            WIN.fill(WHITE)
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
    if winner == 1:
        sym = "X" 
    else:
        sym = "O"
    text = f"Player{winner}({sym}) wins!"
    display_score(text, GREEN)

#draw-outcome condition
def display_draw():
    text = f"It's a draw!"
    display_score(text, WHITE)

def display_score(txt, color):
    global player1_win_counter
    global player2_win_counter 
    global tie_counter

    WIN.fill(BLACK)
    text = font.render(txt, True, color)
    text_rect = text.get_rect(center=(WIDTH/2, 100))
    WIN.blit(text, text_rect)
    WIN.blit(font.render("Score:", True, WHITE), text.get_rect(center=(WIDTH/2,150)))
    WIN.blit(font.render(f"Player1(X): {player1_win_counter}", True, WHITE), text.get_rect(center=(WIDTH/2,170)))
    WIN.blit(font.render(f"Player2(O): {player2_win_counter}", True, WHITE), text.get_rect(center=(WIDTH/2,190)))
    WIN.blit(font.render(f"Draw: {tie_counter}", True, WHITE), text.get_rect(center=(WIDTH/2, 210)))
    WIN.blit(font.render(f"Click to continue...", True, WHITE), text.get_rect(center=(WIDTH/2, 230)))

if __name__ == "__main__":
    main()
