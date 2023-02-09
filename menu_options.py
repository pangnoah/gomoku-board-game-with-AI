import pygame, sys
from game_functions import *
from button import Button
from minimax import minimax
import time

def main_menu():
    pygame.init()
    pygame.display.set_caption('Menu')
    play_button = Button(ORANGE, 210, 225, 300, 100, 'Play')
    controls_button = Button(ORANGE, 210, 450, 300, 100, 'Controls')

    while True:
        SCREEN.fill(LIGHT_BLUE)
        font = pygame.font.SysFont('timesnewroman', 60)
        game_name = font.render('Gomoku', True, BLUE, LIGHT_BLUE)
        SCREEN.blit(game_name, (255, 51))
        play_button.draw_button(SCREEN, (0,0,0))
        controls_button.draw_button(SCREEN, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.on_button(pos):
                    players()
                elif controls_button.on_button(pos):
                    controls()

            if event.type == pygame.MOUSEMOTION:
                if play_button.on_button(pos):
                    play_button.color = GREEN
                elif controls_button.on_button(pos):
                    controls_button.color = GREEN
                else:
                    play_button.color = ORANGE
                    controls_button.color = ORANGE

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def controls():
    pygame.init()
    pygame.display.set_caption('Controls')
    back_button = Button(ORANGE, 210, 535, 300, 100, 'Back')

    while True:
        SCREEN.fill(LIGHT_BLUE)
        title_font = pygame.font.SysFont('timesnewroman', 60)
        font = pygame.font.SysFont('timesnewroman', 40)
        controls = title_font.render('Controls', True, BLUE, LIGHT_BLUE)
        left_click = font.render('Left Click  =  Place Piece', True, BLUE, LIGHT_BLUE)
        undo = font.render('Backspace  =  Undo Move', True, BLUE, LIGHT_BLUE)
        restart = font.render('R  =  Restart Game', True, BLUE, LIGHT_BLUE)
        escape = font.render('Escape  =  Exit Game', True, BLUE, LIGHT_BLUE)
        back_button.draw_button(SCREEN, (0,0,0))
        SCREEN.blit(controls, (257, 20))
        SCREEN.blit(left_click, (146, 135))
        SCREEN.blit(undo, (146, 235))
        SCREEN.blit(restart, (146, 335))
        SCREEN.blit(escape, (146, 435))
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.on_button(pos):
                    main_menu()

            if event.type == pygame.MOUSEMOTION:
                if back_button.on_button(pos):
                    back_button.color = GREEN
                else:
                    back_button.color = ORANGE
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    pygame.init()
    player = 1
    game_over = False
    saved_rows = []
    saved_cols = []
    game_font = pygame.font.SysFont('timesnewroman', 40)
    player_1 = game_font.render('Black Wins', True, WHITE, BLACK)
    player_2 = game_font.render('White Wins', True, WHITE, BLACK)
    pygame.display.set_caption('Gomoku')
    SCREEN.fill(BROWN)
    draw_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_col = int(mouseX // BLOCK_SIZE)
                clicked_row = int(mouseY // BLOCK_SIZE)
            
                if available_square(clicked_row, clicked_col):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        draw_figures()
                        saved_rows.append(clicked_row)
                        saved_cols.append(clicked_col)
                        if check_win(player, board):
                            game_over = True
                            SCREEN.blit(player_1, (267, 5))
                        player = 2

                    elif player == 2:
                        mark_square(clicked_row, clicked_col, 2)
                        draw_figures()
                        saved_rows.append(clicked_row)
                        saved_cols.append(clicked_col)
                        if check_win(player, board):
                            game_over = True
                            SCREEN.blit(player_2, (265, 5))
                        player = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(saved_rows) != 0:
                        player = player % 2 + 1
                        undo_row = saved_rows[len(saved_rows) - 1]
                        undo_col = saved_cols[len(saved_cols) - 1]
                        saved_rows.pop()
                        saved_cols.pop()
                        unmark_square(undo_row, undo_col)
                        SCREEN.fill(BROWN)
                        draw_grid()
                        draw_figures()
                        game_over = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def players():
    pygame.init()
    pygame.display.set_caption('Players')
    ai_button = Button(ORANGE, 210, 225, 300, 100, 'Player vs AI')
    player_button = Button(ORANGE, 210, 450, 300, 100, 'Player vs Player')

    while True:
        SCREEN.fill(LIGHT_BLUE)
        font = pygame.font.SysFont('timesnewroman', 60)
        game_name = font.render('Gomoku', True, BLUE, LIGHT_BLUE)
        SCREEN.blit(game_name, (255, 51))
        ai_button.draw_button(SCREEN, (0,0,0))
        player_button.draw_button(SCREEN, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ai_button.on_button(pos):
                    play_ai()
                elif player_button.on_button(pos):
                    play()

            if event.type == pygame.MOUSEMOTION:
                if ai_button.on_button(pos):
                    ai_button.color = GREEN
                elif player_button.on_button(pos):
                    player_button.color = GREEN
                else:
                    ai_button.color = ORANGE
                    player_button.color = ORANGE

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play_ai():
    pygame.init()
    player = 1
    game_over = False
    saved_rows = []
    saved_cols = []
    previous = []
    game_font = pygame.font.SysFont('timesnewroman', 40)
    player_1 = game_font.render('Black Wins', True, WHITE, BLACK)
    player_2 = game_font.render('White Wins', True, WHITE, BLACK)
    pygame.display.set_caption('Gomoku')
    SCREEN.fill(BROWN)
    draw_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_col = int(mouseX // BLOCK_SIZE)
                clicked_row = int(mouseY // BLOCK_SIZE)
            
                if available_square(clicked_row, clicked_col):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        draw_figures()
                        pygame.display.update()
                        saved_rows.append(clicked_row)
                        saved_cols.append(clicked_col)
                        if check_win(player, board):
                            game_over = True
                            SCREEN.blit(player_1, (267, 5))
                            break
                        player = 2
                        time.sleep(0.1)
                        run1 = minimax(board, 1, 2, -1000000000, 1000000000)
                        run2 = minimax(board, 2, 2, -1000000000, 1000000000)
                        difference = run1[0] - run2[0]
                        previous.append(run1[0])
                        if run1[0] - previous[(len(previous) - 2)] > 4000:
                            result = run1[1]
                        elif difference > 500:
                            result = run2[1]
                        elif run2[0] < 0:
                            result = run2[1]
                        else:
                            result = run1[1]
                        mark_square(result[0], result[1], 2)
                        draw_figures()
                        saved_rows.append(result[0])
                        saved_cols.append(result[1])
                        if check_win(player, board):
                            game_over = True
                            SCREEN.blit(player_2, (265, 5))
                        player = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(saved_rows) != 0 and len(saved_rows) != 1:
                        player = player
                        undo_row = saved_rows[len(saved_rows) - 1]
                        undo_col = saved_cols[len(saved_cols) - 1]
                        saved_rows.pop()
                        saved_cols.pop()
                        unmark_square(undo_row, undo_col)
                        undo_row = saved_rows[len(saved_rows) - 1]
                        undo_col = saved_cols[len(saved_cols) - 1]
                        saved_rows.pop()
                        saved_cols.pop()
                        unmark_square(undo_row, undo_col)
                        SCREEN.fill(BROWN)
                        draw_grid()
                        draw_figures()
                        game_over = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()