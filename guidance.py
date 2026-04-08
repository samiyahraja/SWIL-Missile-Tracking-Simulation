import numpy as np

def compute_guidance(missile_pos, missile_vel, target_pos):
    # Simple proportional navigation
    gain = 0.5
    direction = target_pos - missile_pos
    desired_velocity = direction / (np.linalg.norm(direction) + 1e-6)
    accel = gain * (desired_velocity - missile_vel)
    return accel
