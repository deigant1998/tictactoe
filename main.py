
import sys
import numpy as np
from environment.TicTacToeEnvironment import Board
from agent.Agent import Agent

if __name__ == "__main__":
    episodes = int(sys.argv[1])
    alpha = float(sys.argv[2])
    gamma = float(sys.argv[3])
    epsilon = float(sys.argv[4])
    
    board = Board(3,3,1,-1)
    agent1 = Agent(1, 3*3, 3*3, alpha, gamma, epsilon)
    agent2 = Agent(-1, 3*3, 3*3, alpha, gamma, epsilon)
    
    player1_reward = []
    player2_reward = []
    for i in range(episodes):
        current_player = -1
        board.reset_board()
        total_player_1_reward = 0;
        total_player_2_reward = 0;
        for j in range(9):
            if(current_player == 1):
                r = agent1.play_move_train(board)
                total_player_1_reward += r
                current_player = -1
            else:
                r = agent2.play_move_train(board)
                total_player_2_reward += r
                current_player = 1
            if(r == 1):
                #board.show_board()
                break;
        player1_reward.append(total_player_1_reward)
        player2_reward.append(total_player_2_reward)
        
    #print(player1_reward)
    #print(player2_reward)
    
    print("Starting Human Game")
    board.reset_board()
    
    for i in range(9):
        