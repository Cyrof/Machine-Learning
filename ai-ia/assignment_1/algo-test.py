import gymnasium as gym
from copy import deepcopy

class algo_test:
    
    def __init__(self, env="Taxi-v3", render_mode="ansi", action=[0,1,2,3,4,5]):
        self.env = None
        try: 
            self.env = gym.make(env, render_mode=render_mode)
            # self.env.reset(seed=10)
            self.env.reset()
        except Exception as e: 
            raise f"Unknown error or render mode {e}"

        self.actions = action

    def bfs(self):
        copy_env = deepcopy(self.env)
        queue = []
        visited = [False for _ in range(copy_env.unwrapped.observation_space.n)]


        initial_state = copy_env.reset()[0]
        queue.append((initial_state, [], 0, False))
        visited[initial_state] = True

        while queue:
            state, path, total_reward, picked_up = queue.pop(0)
            copy_env.unwrapped.s = state
            print(copy_env.render())

            for action in self.actions:
                copy_env.unwrapped.s = state
                next_state, reward, done, move, info = copy_env.step(action)
                next_path = path + [action]
                new_total_reward = total_reward + reward

                if not visited[next_state]:
                    new_picked_up = picked_up 
                    trow, tcol, ploc, dest = tuple(copy_env.unwrapped.decode(next_state))

                    if action == 4 and ploc != 4:
                        if (trow, tcol) == env.unwrapped.locs[ploc]:
                            new_picked_up = True
                    
                    if action == 5 and picked_up:
                        if (trow, tcol) == env.unwrapped.locs[dest]:
                            new_picked_up = False
                            done = True

                    visited[next_state] = True
                    queue.append((next_state, next_path, new_total_reward, new_picked_up))
            
                if done: 
                    print("Goal reached!")
                    print(copy_env.render())
                    print(f"Actions to reach goal: {next_path}")
                    print(f"Total reward: {total_reward}")
                    return 
        print("All reachable states visited")
        print(f"Visited states: {visited}")


    def get_env(self):
        return self.env.unwrapped.s


if __name__ == "__main__":
    a = algo_test()
    a.bfs()