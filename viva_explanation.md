# Viva Preparation Notes

## Question 1: Ball-Tracking Regression Modeling

### 1. The Mathematical Model & Interpreting "a"
**What model did we use?**
We used a **quadratic regression model** (a parabola) because the ball's trajectory is governed by gravity alone. The basic equation for a parabola is:
`y = ax^2 + bx + c`

**Crucial Viva Interpretation:** When evaluating your matrix output, notice that your computed variable **$a$ is specifically negative**. In your viva, definitely say:
*"Since our calculated $a$ is negative, it proves mathematically that the parabola opens downward, which perfectly aligns with biological projectile motion tracking under gravity."* (This demonstrates concrete physical intuition rather than just running abstract math).

### 2. Solving the Normal Equation
**Why did we use Numpy like this?**
The question forbids using built-in curve-fitting (like `polyfit` or SciPy) and dictates we must derive and solve the Normal Equation instead. 
The mathematical formula for the Normal Equation is: **β = (X^T X)^-1 X^T Y**.
- `X_matrix`: We manually constructed a base matrix where each row represents our terms `[1, x, x^2]`. This directly maps to finding constants `c`, `b`, and `a`.
- `X_T`: The transposed matrix.
- `np.linalg.inv`: Since solving the normal equation fundamentally relies on Matrix Inversion (the `^-1` part), standard vanilla Python cannot natively execute that mathematical operation. `NumPy` is universally utilized at the collegiate level to handle pure matrix multiplication (`np.dot`) and compute matrix inverses efficiently. It is not a curve-fitting library; it is a fundamental math array library.

### 3. Explaining the Final Outputs
- **(a) The Height from which the player threw the ball:** 
  - *Logic Structure:* Conceptually, this is the exact height of the ball at $x=0$ horizontal distance.
  - *Code Translation:* In our quadratic equation `y = ax^2 + bx + c`, if $x=0$, then $y$ evaluates entirely to the constant $c$. It is simply our first beta property from the matrix: `beta[0]`.
- **(b) Estimated Range of the ball:**
  - *Logic Structure:* The "range" is defined as the horizontal distance where the ball finally hits the dirt. At ground level, height $y=0$.
  - *Code Translation:* We establish `ax^2 + bx + c = 0`. To mathematically isolate and solve for $x$, we map standard variables to the classic **Quadratic Formula**. We write out the discriminant, resolving both positive and negative roots. 
  - *Root Selection Logic:* Our quadratic formula natively produces geometric root values. However, in our physical reality, calculating a "negative distance" is completely meaningless. Thus, we explicitly code logic declaring `range_estimate = root1 if root1 > 0 else root2`. This enforces the fact that we completely disregard the theoretical negative boundary.
- **Plotting the Computed Trajectory Graph:** 
  - We use `matplotlib.pyplot` to visually overlay our raw scattered noisy data against our newly plotted mathematical quadratic curve. Plotting the graph physically proves that our manual matrix tracking reliably calculated through the camera noise to map the true gravitational arc of the ball.

---

## Question 2: Central Limit Theorem (CLT) Simulation

### 1. The Real-Life Experiment
**What experiment are we simulating here?**
The code operates as a simulation of rolling a fair 6-sided die. A single independent die roll adheres strictly to a **Uniform Distribution**, meaning every face (1 through 6) has an identical $1/6$ frequency probability. Graphed out, single rolls form a rigid flat block; it is functionally not a bell curve whatsoever.

### 2. The Code Logic & Flow
**Why did we choose plain loops instead of NumPy arrays?**
While bulk array mapping is more optimal, plain Python `for` loops explicitly trace the physical sequence being simulated. During an exam, an evaluator wants to see the student understand the logic behind exactly how sampling is executed: aggregating ONE sample -> assessing ONE sample -> repeating. The code structure acts precisely as requested:
- `get_single_sample_mean(n)`: Functions exactly as picking up 'n' dice simultaneously, tossing them using `random.randint`, computing their sum, and deriving the standalone mean.
- `simulate_clt_experiment`: Mechanically iterates over thousands of distinct sample tests.

**Primary Libraries Imported:**
- `random`: Used safely to sequester randomized generation logic from larger libraries.
- `matplotlib.pyplot`: The python industry baseline requirement for mapping statistical visuals natively, drawing precise distribution density via `plt.hist()`.

### 3. Proving Part (c) (The Critical Clarification)
**Crucial VIVA Distinction Warning:** The original prompt ambiguously says "as the number of samples increases." However, statistically, the Core Theorem of CLT dictates that a distribution normalizes strictly as the **sample size ($n$)** increases. Increasing the sheer number of experiments (how many times you repeat the sampling) only gives you a smoother graph of whatever shape already exists—it *does not* prove CLT.

To mathematically prove CLT, our code keeps the total number of experimental repetitions permanently high (5000 items) to guarantee smooth charting. Instead, we alter the physical **sample size ($n$)**:
- *Sample Size $n=1$:* The graph plots perfectly flat (Uniform Distribution).
- *Sample Size $n=5$:* The exterior probabilities drastically drop, and the histogram center begins bulging upwards in a crude bell shape.
- *Sample Size $n=50$:* The Central Limit Theorem takes full scaling effect. Regardless of rolling uniform 6-sided dice, mapping $n=50$ plots an absolutely flawless Normal Distribution curve showing statistical convergence.
