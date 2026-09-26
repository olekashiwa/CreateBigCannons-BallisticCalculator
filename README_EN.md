# 🎯 Mirage-Geo: Ballistic Calculator for Create: Big Cannons

**[Launch Web App](https://olekashiwa.github.io/CreateBigCannons-BallisticCalculator/)** | [Русская версия](README.md)

This tool instantly calculates the exact Yaw and Pitch angles required to hit your target in the *Create: Big Cannons* mod, accounting for gravity, air resistance, barrel length, and projectile type. Stop guessing and start hitting!

---

## 🎒 In-Game Preparation
The Debug Screen (**F3**) is your best friend. Note the following before calculating:
1. **Mount Coordinates:** The block where the cannon is anchored (X, Y, Z).
2. **Target Coordinates:** The exact block you want to hit (X, Y, Z).
3. **Barrel Length:** Total number of blocks from the mount to the very tip of the muzzle (inclusive).
4. **Powder Charges:** Number of charges loaded into the breech.
5. **Facing Direction:** The cardinal direction (North, South, East, West) the cannon points to when unmounted.

---

## ⚙️ How to Use
1. Enter the cannon and target coordinates.
2. Input barrel length and powder charges.
3. Select the facing direction and **Projectile Type** (including *CBC: Advanced Technologies* shells).
4. Click **Calculate**.

---

## 📊 Understanding the Results
The calculator provides two firing solutions:
*   🚀 **Trajectory 1 (Low / Direct):** Faster time of flight, harder to intercept, requires line of sight.
*   🌙 **Trajectory 2 (High / Indirect):** Perfect for firing over walls, hills, or fortifications.

| Metric | Description |
|--------|-------------|
| **Yaw** | Horizontal rotation angle (in degrees). |
| **Pitch** | Vertical elevation angle. *(Over 60 / Under -30 means this angle is physically unreachable with current power).* |
| **Airtime** | Total flight time in ticks and seconds. |
| **Fuze Time** | **Crucial for HE shells!** Set your shell's fuze to this exact tick value to detonate on or above the target. |
| **Precision** | Estimated accuracy. If < 90%, a spotting round is recommended. |

---

## 💣 Projectile & Addon Specifics
The calculator includes physics profiles for various shells (different drag and velocity):
*   **AP / Solid Shot:** High velocity, low drag. Best for direct fire.
*   **Grapeshot:** Rapidly loses velocity and drops quickly. Effective only at close range. Displays cone of fire estimation.
*   **Smoke:** Long hang time. Use high trajectory for smoke screens.
*   **CBC: Advanced Technologies:** Adv. HE and Custom AP shells have adjusted physical constants for better accuracy.
> ⚠️ **Golden Rule:** For custom modded shells, the calculator provides a highly accurate baseline. Always fire 1–2 spotting rounds before a full combat volley.

---

## 💡 Calculation Examples
**Example 1: Direct Strike.** Mount at 100, 64, 100, target at 150, 64, 100 (East, 50 blocks). Barrel: 5 blocks, 3 charges. Result: Yaw 90°, Pitch ~15°.

**Example 2: Indirect Fire.** Target is behind a wall and higher than you. The calculator will recommend Trajectory 2 with a high Pitch and an exact Fuze Time to clear the obstacle and detonate on impact.

---

## 🚀 App Features
- 📱 **PWA:** Installable on mobile/desktop, works offline.
- 🌐 **3D Visualization:** Interactive projectile flight scene (Three.js).
- 📊 **Comparison:** Overlay trajectories of up to 4 different projectiles on one graph.
- 💾 **Scenarios:** Save and load firing configurations as JSON files.
- 🎓 **Anki Integration:** Instantly create flashcards for ballistics memorization (requires AnkiConnect).

*Based on the original calculator by [Malex21](https://github.com/Malex21/CreateBigCannons-BallisticCalculator). License: MIT.*
