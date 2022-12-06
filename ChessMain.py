import pygame, sys
from data.constants import *
import engine, AI
import Menu
IMAGES={}
def loadImages():
    pie=['bR','bN','bB','bQ','bK','bp','wp','wK','wQ','wB','wN','wR']
    for item in pie:
        IMAGES[item] = pygame.transform.scale(pygame.image.load('data/images/'+ item +'.png'), (PIE_SIZE,PIE_SIZE))

def drawGameState(screen, gsta,validMoves, sqSelected, color1, color2):
    drawBoard(screen, color1, color2)
    hightlightSq(screen, gsta, validMoves, sqSelected)
    drawPiece(screen,gsta.board)
    
def drawBoard(screen, color1, color2):
    colors = [pygame.Color(color1), pygame.Color(color2)]
    for row in range(DIMENSIONS):
        for col in range(DIMENSIONS):
            color = colors[( (row+col) % 2 )]
            pygame.draw.rect(screen, color, pygame.Rect(col * PIE_SIZE, row * PIE_SIZE, PIE_SIZE, PIE_SIZE))
            
def drawPiece(screen,board):
    for row in range(DIMENSIONS):
        for col in range(DIMENSIONS):
            piece = board[row][col]
            if piece != '--':
                screen.blit(IMAGES[piece], pygame.Rect( col * PIE_SIZE, row * PIE_SIZE, PIE_SIZE, PIE_SIZE))

    # Do the job here !
    pass

def hightlightSq(screen, gsta, validMoves, sqSelected):
    if sqSelected != ():
        row, col = sqSelected
        if gsta.board[row][col][0] ==  ('w' if gsta.whiteMove else 'b'):
            #highlight ô đang chọn
            s = pygame.Surface((PIE_SIZE, PIE_SIZE))
            s.set_alpha(100)
            s.fill(pygame.Color('blue'))
            screen.blit(s, (col * PIE_SIZE, row * PIE_SIZE))
            #highlight những ô đi được
            s.fill(pygame.Color('yellow'))
            for move in validMoves:
                if move.startRow == row and move.startCol == col:
                    screen.blit(s, (move.endCol* PIE_SIZE, move.endRow * PIE_SIZE))

def soundMove(Capture):
    if not Capture:
        pygame.mixer.music.load('data/sound/Move.WAV')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('data/sound/Capture.WAV')
        pygame.mixer.music.play()
   
def soundGameOver():
    pygame.mixer.music.load('data\sound\GameOver.wav')
    pygame.mixer.music.play()

def drawText(screen, text, ms_rs = False):
    font = pygame.font.SysFont('tahoma', 30, True, False)
    message = font.render(text, 0, pygame.Color(D_RED))
    messageLocation = pygame.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - message.get_width()/2, HEIGHT/2 - message.get_height()/2)
    screen.blit(message, messageLocation)
    if ms_rs:
        msReset = font.render('Nhấn r để reset lại trò chơi!',0, pygame.Color(D_RED))
        msResetLocation = pygame.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - msReset.get_width()/2, HEIGHT/2 + msReset.get_height()/2)
        screen.blit(msReset, msResetLocation)

def GameStart(screen, gamemode, depth, GSTATE, color1, color2):
    run = True
    clock = pygame.time.Clock()
    

    loadImages()

    pieSelected = ()
    playerClick = []
    moveMade = False
    gameOver = False
    captureMove = False

    if GSTATE == None:
        gsta = engine.GameState()
    else:
        gsta = GSTATE

    validMoves = gsta.getValidMove()

    while run:
        playerTurn = gsta.whiteMove
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # xử lí nhấp chuột
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver and playerTurn:
                    location = pygame.mouse.get_pos()
                    col = location[0]//PIE_SIZE
                    row = location[1]//PIE_SIZE
                    
                    # hủy khi double click tại 1 ô
                    if pieSelected == (row,col):
                        pieSelected = ()
                        playerClick = []
                    else:
                        pieSelected = (row,col)
                        playerClick.append(pieSelected)
                    if len(playerClick) == 2:
                        move = engine.Move(playerClick[0], playerClick[1],gsta.board)
                        for i in range(len(validMoves)):                   
                            if move == validMoves[i]:
                                gsta.makeMove(validMoves[i])
                                moveMade = True
                                if validMoves[i].pieCaptured != '--':
                                    captureMove = True
                                pieSelected = ()
                                playerClick = []
                        if not moveMade:
                            playerClick = [pieSelected]

            # xữ lí nhập từ phím
            elif event.type == pygame.KEYDOWN:
                # undo move (phím : Z )
                if event.key == pygame.K_z:
                    if playerTurn:                 
                        gsta.undoMove()
                        gsta.undoMove()
                        moveMade = True

                if event.key == pygame.K_r:
                    gsta = engine.GameState()
                    pieSelected = ()
                    playerClick = []
                    validMoves = gsta.getValidMove()
                    moveMade = False
                    gameOver = False
                if event.key == pygame.K_ESCAPE:
                    Menu.main_menu(gsta)
        if not gameOver:
            if gamemode == 2 or (gamemode == 1 and not playerTurn):
                if playerTurn and gamemode == 2:
                    depth = 4
                elif gamemode == 2:
                    depth = 2
                BotMove, count = AI.findMovesNegaMax(gsta, validMoves, depth) 
                if BotMove != None:
                    gsta.makeMove(BotMove)
                    print('count: ',count)
                    moveMade = True

        if moveMade:
            validMoves = gsta.getValidMove()
            soundMove(captureMove)
            if gsta.checkmate or gsta.stalemate:
                soundGameOver()
            captureMove = False
            moveMade = False

        drawGameState(screen,gsta, validMoves, pieSelected, color1, color2)

        if gsta.checkmate:
            gameOver = True
            if gsta.whiteMove:
                drawText(screen, 'Trắng bị chiếu chết !',gameOver)
            else:
                drawText(screen, 'Đen bị chiếu chết !',gameOver)
        elif gsta.stalemate:
            if gsta.whiteMove:
                drawText(screen, 'Trắng hết nước đi !',gameOver)
            else:
                drawText(screen, 'Đen hết nước đi !',gameOver)          
        elif gsta.inCheck():
            if gsta.whiteMove:
                drawText(screen, 'Trắng đang bị chiếu !!!')
            else:
                drawText(screen, 'Đen đang bị chiếu !!!')

        clock.tick(FPS)
        pygame.display.flip()

