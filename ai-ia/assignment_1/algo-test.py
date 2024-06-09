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

    # def afs(self):
    #     copy_env = deepcopy(self.env)
        
    #     initial_state, _ = copy_env.reset()
    #     queue = [(0, initial_state, [])]
    #     visited = set()

    #     visited.add(initial_state)
    #     cost = {initial_state: 0}
    #     total_reward = 0
    #     while queue:
    #         _, state, path = heapq.heappop(queue)

    #         done = False
    #         for action in range(copy_env.unwrapped.action_space.n):
    #             copy_env.unwrapped.s = state
    #             new_state, reward, done, _, _ = copy_env.step(action)
    #             new_cost = cost[state] + 1
    #             if new_state not in visited or cost.get(new_state, float('inf')) > new_cost:
    #                 cost[new_state] = new_cost
    #                 visited.add(new_state)
    #                 priority = new_cost + self.heuristic(done)
    #                 heapq.heappush(queue, (priority, new_state, path+[action]))
    #                 total_reward += reward
                
    #             if done:
    #                 self.display(path=path+[action], reward=-total_reward, algo_type="A*", line_break=True)
    #                 return
    #     print("No solution found")

    def ucs(self):
        copy_env = deepcopy(self.env)

        initial_state, _ = copy_env.reset()
        queue = [(0, initial_state, [])]
        visited = set()
        
        visited.add(initial_state)
        cost = {initial_state: 0}
        total_reward = 0

        while queue: 
            current_cost, state, path = heapq.heappop(queue)
            
            done = False
            for action in range(copy_env.unwrapped.action_space.n):
                copy_env.unwrapped.s = state
                new_state, reward, done, _, _ = copy_env.step(action)
                new_cost = current_cost + 1
                if new_state not in visited or cost.get(new_state, float('inf')) > new_cost:
                    cost[new_state] = new_cost
                    visited.add(new_state)
                    heapq.heappush(queue, (new_cost, new_state, path + [action]))
                    total_reward += reward

                if done: 
                    self.display(path=path + [action], reward=-total_reward, algo_type="UCS", line_break=True)
                    return
        print("No solution found")
    
    # def bds(self):
    #     copy_env = deepcopy(self.env)

    #     initial_state, _ = copy_env.reset()
    #     forward_queue = [(0, initial_state, [])]
    #     forward_visited = {initial_state}
    #     forward_cost = {initial_state: 0}

    #     # Initialize backward search with an arbitrary state (goal not known)
    #     backward_queue = []
    #     for action in range(copy_env.unwrapped.action_space.n):
    #         copy_env.unwrapped.s = initial_state
    #         new_state, _, done, _, _ = copy_env.step(action)
    #         if done:
    #             backward_queue.append((0, new_state, []))
    #             backward_visited = {new_state}
    #             backward_cost = {new_state: 0}
    #             break

    #     total_reward_forward = 0
    #     total_reward_backward = 0

    #     while forward_queue and backward_queue:
    #         # Expand forward search
    #         current_cost, state, path = heapq.heappop(forward_queue)
    #         for action in range(copy_env.unwrapped.action_space.n):
    #             copy_env.unwrapped.s = state
    #             new_state, reward, done, _, _ = copy_env.step(action)
    #             new_cost = current_cost + 1
    #             if new_state not in forward_visited or forward_cost.get(new_state, float('inf')) > new_cost:
    #                 forward_cost[new_state] = new_cost
    #                 forward_visited.add(new_state)
    #                 heapq.heappush(forward_queue, (new_cost, new_state, path + [action]))
    #                 total_reward_forward += reward

    #         # Expand backward search
    #         current_cost, state, path = heapq.heappop(backward_queue)
    #         for action in range(copy_env.unwrapped.action_space.n):
    #             copy_env.unwrapped.s = state
    #             new_state, reward, done, _, _ = copy_env.step(action)
    #             new_cost = current_cost + 1
    #             if new_state not in backward_visited or backward_cost.get(new_state, float('inf')) > new_cost:
    #                 backward_cost[new_state] = new_cost
    #                 backward_visited.add(new_state)
    #                 heapq.heappush(backward_queue, (new_cost, new_state, path + [action]))
    #                 total_reward_backward += reward

    #         # Check for meeting point
    #         intersection = forward_visited.intersection(backward_visited)
    #         if intersection:
    #             meeting_point = next(iter(intersection))
    #             forward_path = self.reconstruct_path(forward_cost, initial_state, meeting_point)
    #             backward_path = self.reconstruct_path(backward_cost, meeting_point, state, reverse=True)
    #             path = forward_path + backward_path
    #             self.display(path=path, reward=total_reward_forward + total_reward_backward, algo_type="BDS", line_break=True)
    #             return

    #     print("No solution found")

    # def reconstruct_path(self, cost, start, end, reverse=False):
    #     path = []
    #     state = end
    #     while state != start:
    #         for action in range(self.env.unwrapped.action_space.n):
    #             self.env.unwrapped.s = state
    #             new_state, _, _, _, _ = self.env.step(action)
    #             if cost.get(new_state, float('inf')) + 1 == cost[state]:
    #                 path.append(action)
    #                 state = new_state
    #                 break
    #     if reverse:
    #         path.reverse()
    #     return path
    
    def bds(self):
        copy_env = deepcopy(self.env)

        initial_state, _ = copy_env.reset()
        forward_queue = [(0, initial_state, [])]
        forward_visited = {initial_state: (0, [])}  # (cost, path)

        # Initialize backward search
        backward_queue = []
        backward_visited = {}
        for action in range(copy_env.unwrapped.action_space.n):
            copy_env.unwrapped.s = initial_state
            new_state, _, done, _, _ = copy_env.step(action)
            if done:
                backward_queue.append((0, new_state, []))
                backward_visited[new_state] = (0, [])
                break
        
        print(backward_queue)

        while forward_queue and backward_queue:
            # Expand forward search
            forward_cost, forward_state, forward_path = heapq.heappop(forward_queue)
            for action in range(copy_env.unwrapped.action_space.n):
                copy_env.unwrapped.s = forward_state
                new_state, reward, done, _, _ = copy_env.step(action)
                new_cost = forward_cost + 1
                if new_state not in forward_visited or forward_visited[new_state][0] > new_cost:
                    forward_visited[new_state] = (new_cost, forward_path + [action])
                    heapq.heappush(forward_queue, (new_cost, new_state, forward_path + [action]))

            # Expand backward search
            backward_cost, backward_state, backward_path = heapq.heappop(backward_queue)
            for action in range(copy_env.unwrapped.action_space.n):
                copy_env.unwrapped.s = backward_state
                new_state, reward, done, _, _ = copy_env.step(action)
                new_cost = backward_cost + 1
                if new_state not in backward_visited or backward_visited[new_state][0] > new_cost:
                    backward_visited[new_state] = (new_cost, backward_path + [action])
                    heapq.heappush(backward_queue, (new_cost, new_state, backward_path + [action]))

            # Check for meeting point
            intersection = set(forward_visited.keys()).intersection(set(backward_visited.keys()))
            if intersection:
                meeting_point = next(iter(intersection))
                forward_path = forward_visited[meeting_point][1]
                backward_path = backward_visited[meeting_point][1]
                total_path = forward_path + backward_path[::-1]  # Reversing the backward path
                total_reward = -forward_visited[meeting_point][0] - backward_visited[meeting_point][0]
                self.display(path=total_path, reward=total_reward, algo_type="BDS", line_break=True)
                return

        print("No solution found")

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
    a.ucs()
    a.bds()
    