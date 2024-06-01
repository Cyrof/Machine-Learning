# This python file is to play around with gym library to be used in the first assignment 

import gymnasium as gym
from collections import deque

env = gym.make("Taxi-v3", render_mode="ansi")
env.reset(seed=2)

def dfs(env):
    actions = [0, 1, 2, 3, 4, 5]  # Actions: South, North, East, West, Pickup, Dropoff
    stack = []
    visited = set()

    initial_state = env.reset()[0]
    stack.append((initial_state, [], 0, False))  # Add state, path, accumulated reward, and pickup status to the stack
    visited.add(initial_state)

    while stack:
        state, path, total_reward, picked_up = stack.pop()
        env.unwrapped.s = state
        print(env.render())

        for action in actions:
            env.unwrapped.s = state  # Reset to the current state
            next_state, reward, done, truncated, info = env.step(action)
            next_path = path + [action]
            next_total_reward = total_reward + reward

            if next_state not in visited:
                next_picked_up = picked_up
                taxi_row, taxi_col, passenger_loc, destination = tuple(env.unwrapped.decode(next_state))

                # Check if passenger is picked up and update status
                if action == 4 and passenger_loc != 4:  # Pickup action
                    if (taxi_row, taxi_col) == env.unwrapped.locs[passenger_loc]:
                        next_picked_up = True

                # Check if passenger is dropped off and update status
                if action == 5 and picked_up:  # Dropoff action
                    if (taxi_row, taxi_col) == env.unwrapped.locs[destination]:
                        next_picked_up = False  # Passenger dropped off
                        done = True  # Goal achieved

                visited.add(next_state)
                stack.append((next_state, next_path, next_total_reward, next_picked_up))

            if done:
                print("Goal reached!")
                print(env.render())
                print(f"Actions to reach goal: {next_path}")
                print(f"Total reward: {next_total_reward}")
                return

    print("All reachable states visited.")
    print(f"Visited states: {visited}")
            

if __name__ == "__main__":
    dfs(env)