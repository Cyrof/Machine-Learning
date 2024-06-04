import gymnasium as gym
from copy import deepcopy
import numpy as np
from collections import deque
import sys

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

    def bfs(self):
        copy_env = deepcopy(self.env)
        queue = []
        visited = [False for _ in range(copy_env.unwrapped.observation_space.n)]

        initial_state = copy_env.reset()[0]
        queue.append((initial_state, [], 0))
        visited[initial_state] = True

        picked_up = False
        while queue:
            state, path, reward = queue.pop(0)
            copy_env.unwrapped.s = state
            print(copy_env.render())
            
            for action in range(copy_env.unwrapped.action_space.n):
                next_state, reward, done, move, info = copy_env.step(action)

                filtered_action = self.actions[info['action_mask']==1]


                if next_state != state:
                    if not visited[next_state]:
                        print("This is working")
                        trow, tcol, ploc, dest = copy_env.unwrapped.decode(next_state)
                        if ploc == 4: 
                            print("Picked up passenger")
                            visited = [False for _ in range(copy_env.unwrapped.observation_space.n)]
                            picked_up == True
                            sys.exit()
            print("this is not working")


    def bfs2(self):
        copy_env = deepcopy(self.env)
        visited = [False for _ in range(copy_env.unwrapped.observation_space.n)]

        initial_state = copy_env.reset()[0]
        queue = deque([(initial_state, [])])
        visited[initial_state] = True
        total_reward = 0

        picked_up = False


        while queue:
            current_state, path = queue.popleft()
            copy_env.unwrapped.s = current_state
            copy_env.reset()
            print(copy_env.render())

            for action in range(copy_env.unwrapped.action_space.n):
                # copy_env.unwrapped.s = current_state
                next_state, reward, done, move, info = copy_env.step(action)
                copy_env.reset(seed=None)

                if next_state != current_state:
                    if next_state not in visited:
                        if action == 4 and not picked_up:
                            visited = [False for _ in range(copy_env.unwrapped.observation_space.n)]
                            picked_up = True
                            print("Picked up passenger")
                            sys.exit()


                        visited[next_state] = True
                        new_path = path + [action]
                        total_reward += reward
                        if done: 
                            print(f"The path is: {new_path}")
                            print(f"The reward is: {total_reward}")
                        queue.append((next_state, new_path))
                
        print("No solution found")


    def afs(self):
        pass

    def ucs(self):
        pass
    
    def test(self):
        copy_env = deepcopy(self.env)
        actions = np.array([0,1,2,3,4,5])
        state, reward, done, move, info = copy_env.step(0)
        # filtered_action = actions[info['action_mask'] == 1]
        # print(info)
        # print(filtered_action)
        # print(copy_env.unwrapped.P[state])
        print(state)
        print(copy_env.unwrapped.P[state][4][0][2])


if __name__ == "__main__":
    a = algo_test()
    a.bfs()
    # a.bfs2()
    # a.test()