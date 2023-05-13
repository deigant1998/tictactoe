import numpy as np

class Agent():
    def __init__(self, playerId, state_vector_size, action_vector_size, alpha, gamma, eps):
        self.weights = np.random.rand(action_vector_size, state_vector_size + 1)
        self.alpha = alpha
        self.gamma = gamma
        self.eps = eps
        self.playerId = playerId
        
    def get_optimal_q_value(self, state, possible_action_indices):
        q_values = self.weights @ (np.concatenate(([1], state), axis = 0))
        
        max_value = q_values[0]
        max_action = 0;
        
        for i in possible_action_indices:
            if(q_values[i] >= max_value):
                max_value = q_values[i]
                max_action = i
                
        return max_value, max_action
    
    def calculate_q_value(self, state, action_index):
        q_value = self.weights[action_index] * (np.concatenate(([1], state), axis = 0))
        return q_value
    
    def get_possible_action_indices(self, state):
        possible_action_indices = []
        
        for i in range(len(state)):
            if(state[i] == 0):
                possible_action_indices.append(i)
                
        return np.array(possible_action_indices)
                
    def update_weights(self, previous_state, action, q_value, next_state, reward):
        possible_actions_next_state = self.get_possible_action_indices(next_state)
        max_q_value_next_state, _ = self.get_optimal_q_value(next_state, possible_actions_next_state)
        self.weights[action] = self.weights[action] - self.alpha * (q_value - (reward + self.gamma * max_q_value_next_state)) * (np.concatenate(([1], previous_state), axis = 0))
    
    def play_move_train(self, board):
        state = board.get_flattened_state()
        possible_action_indices = self.get_possible_action_indices(state)
        choice = np.random.choice([0, 1], size = 1, p = [self.eps, 1 - self.eps])
        
        chosen_action = 0
        chosen_q_value = 0
        if(choice == 0):
            chosen_action = np.random.choice(possible_action_indices, size = 1)[0]
            chosen_q_value = self.calculate_q_value(state, chosen_action)
        else:
            chosen_q_value, chosen_action = self.get_optimal_q_value(state, possible_action_indices)
        
        reward = board.apply_action(self.playerId, chosen_action)
        self.update_weights(state, chosen_action, chosen_q_value, board.get_flattened_state(), reward)
        return reward
    
    def play_move_test(self, board):
        state = board.get_flattened_state()
        possible_action_indices = self.get_possible_action_indices(state)
        choice = np.random.choice([0, 1], size = 1, p = [self.eps, 1 - self.eps])
        
        chosen_action = 0
        chosen_q_value = 0
        if(choice == 0):
            chosen_action = np.random.choice(possible_action_indices, size = 1)[0]
            chosen_q_value = self.calculate_q_value(state, chosen_action)
        else:
            chosen_q_value, chosen_action = self.get_optimal_q_value(state, possible_action_indices)
        
        reward = board.apply_action(self.playerId, chosen_action)
        self.update_weights(state, chosen_action, chosen_q_value, board.get_flattened_state(), reward)
        return reward
        
                        
        
        
        