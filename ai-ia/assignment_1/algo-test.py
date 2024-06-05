import gymnasium as gym
from copy import deepcopy
import numpy as np
from collections import deque
import heapq

class algo_test:
    
    def __init__(self, env="Taxi-v3", render_mode="ansi", action=[0,1,2,3,4,5]):
        self.env = None
        try: 
            self.env = gym.make(env, render_mode=render_mode)
            # self.env.reset(seed=10)
            self.env.reset()
        except Exception as e: 
            raise f"Unknown error or render mode {e}"

        self.actions = np.array(action)

    def display(self, path=[], reward=0, algo_type="undefined", line_break=False):
        print(f"{algo_type} algorithm:")
        print("Goal reached!!")
        print(f"Path taken: {path}")
        print(f"Reward: {reward}")
        if line_break:
            print("\n")

    


    def bfs(self):
        copy_env = deepcopy(self.env)
        initial_state, _ = copy_env.reset()
        queue = deque([(initial_state, [])])
        visited = set()

        visited.add(initial_state)
        total_reward = 0
        while queue:
            state, path = queue.popleft()

            for action in range(copy_env.unwrapped.action_space.n):
                copy_env.unwrapped.s = state
                new_state, reward, done, _, _ = copy_env.step(action)


                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path+[action]))
                    total_reward += reward

                if done:
                    self.display(path=path+[action], reward=total_reward, algo_type="BFS", line_break=True)
                    return

        print("No solution found")
                

    def heuristic(self, done):
        if done: 
            return 0
        return 1

    def afs(self):
        copy_env = deepcopy(self.env)
        
        initial_state, _ = copy_env.reset()
        queue = [(0, initial_state, [])]
        visited = set()

        visited.add(initial_state)
        cost = {initial_state: 0}
        total_reward = 0
        while queue:
            _, state, path = heapq.heappop(queue)

            done = False
            for action in range(copy_env.unwrapped.action_space.n):
                copy_env.unwrapped.s = state
                new_state, reward, done, _, _ = copy_env.step(action)
                new_cost = cost[state] + 1
                if new_state not in visited or cost.get(new_state, float('inf')) > new_cost:
                    cost[new_state] = new_cost
                    visited.add(new_state)
                    priority = new_cost + self.heuristic(done)
                    heapq.heappush(queue, (priority, new_state, path+[action]))
                    total_reward += reward
                
                if done:
                    self.display(path=path+[action], reward=-total_reward, algo_type="A*", line_break=True)
                    return
        print("No solution found")

    def ucs(self):
        pass
    
    def test(self):
        copy_env = deepcopy(self.env)
        actions = np.array([0,1,2,3,4,5])
        state, reward, done, move, info = copy_env.step(0)
        filtered_action = actions[info['action_mask'] == 1]
        print(info)
        print(filtered_action)
        # print(copy_env.unwrapped.P[state])


if __name__ == "__main__":
    a = algo_test()
    a.bfs()
    a.afs()
    # a.bfs2()
    # a.test()