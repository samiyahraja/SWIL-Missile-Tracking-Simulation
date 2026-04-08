import numpy as np
import matplotlib.pyplot as plt
from dynamics import update_position
from guidance import compute_guidance
from sensor import get_noisy_measurement

dt = 0.1
steps = 200

# Initial states
target_pos = np.array([0.0, 0.0])
target_vel = np.array([1.0, 0.5])

missile_pos = np.array([-10.0, -5.0])
missile_vel = np.array([0.0, 0.0])

target_path = []
missile_path = []

for _ in range(steps):
    # Target moves
    target_pos = update_position(target_pos, target_vel, dt)

    # Sensor reads noisy target position
    measured_target = get_noisy_measurement(target_pos)

    # Guidance computes acceleration
    accel = compute_guidance(missile_pos, missile_vel, measured_target)

    # Update missile motion
    missile_vel += accel * dt
    missile_pos = update_position(missile_pos, missile_vel, dt)

    target_path.append(target_pos.copy())
    missile_path.append(missile_pos.copy())

# Convert to arrays
target_path = np.array(target_path)
missile_path = np.array(missile_path)

# Plot
plt.plot(target_path[:,0], target_path[:,1], label="Target")
plt.plot(missile_path[:,0], missile_path[:,1], label="Missile")
plt.legend()
plt.title("SWIL Missile Tracking Simulation")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
