import gymnasium as gym

env=gym.make('CartPole-v1',render_mode='human')
env.reset()
env.render()
action = env.action_space.sample()
pole_e = [0]
cart_e = [0]
for i in range(1, 10000):
    observation, reward, terminated, truncated, info = env.step(action)
    cp, cv, pa, pv = observation
    pole_e.append(0 - pa)
    cart_e.append(0 - cp)
    p = (5 * pole_e[-1]) + (30 * (pole_e[-1] - pole_e[-2]))
    c = (1 * cart_e[-1]) + (20 * (cart_e[-1] - cart_e[-2]))

    action = 1 if p + c < 0 else 0

