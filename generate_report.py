from fpdf import FPDF

class ReportPDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 9)
        w = self.w - 2 * self.l_margin
        start_x = self.l_margin
        
        self.set_x(start_x)
        self.cell(w / 3, 5, 'SOCSE', align='L', border=0)
        self.cell(w / 3, 5, '2025-2026', align='C', border=0)
        self.cell(w / 3, 5, str(self.page_no()), align='R', border=0, new_x="LMARGIN", new_y="NEXT")
        
        line_y = self.get_y() + 1
        self.line(start_x, line_y, self.w - self.r_margin, line_y)
        self.ln(4)

    def footer(self):
        pass

    def heading(self, title):
        self.set_font('Times', 'B', 14)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def para(self, text):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 7, text)
        self.ln(2)

    def bold(self, text):
        self.set_font('Times', 'B', 12)
        self.multi_cell(0, 7, text)
        self.ln(1)

    def bullet(self, text):
        self.set_font('Times', '', 12)
        self.set_x(self.l_margin + 10)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 10, 7, '- ' + text)
        self.set_x(self.l_margin)

    def subbullet(self, text):
        self.set_font('Times', '', 12)
        self.set_x(self.l_margin + 20)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 20, 7, 'o ' + text)
        self.set_x(self.l_margin)

pdf = ReportPDF()
pdf.set_auto_page_break(auto=True, margin=20)

# ===================== PAGE 1: TITLE =====================
pdf.add_page()
pdf.ln(25)
pdf.set_font('Times', 'B', 16)
pdf.cell(0, 10, 'SCHOOL OF COMPUTER SCIENCE AND ENGINEERING', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)
pdf.set_font('Times', 'B', 14)
pdf.cell(0, 10, 'CIE-3 Activity', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, 'Probability and Statistics', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Times', '', 13)
pdf.cell(0, 10, '(CS2800) 2025-2026', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(15)
pdf.set_font('Times', 'B', 13)
pdf.cell(0, 8, 'Submitted by', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
members = [
    ('Name 1: Priya N Bhat',          'USN: 1RUA24CSE0335'),
    ('Name 2: Rohit Ajit Bharadwaj',   'USN: 1RUA24CSE0375'),
    ('Name 3: Rohith P Hegde',         'USN: 1RUA24CSE0376'),
    ('Name 4: S Sachithananthan',      'USN: 1RUA24CSE0384'),
    ('Name 5: Saket M',               'USN: 1RUA24CSE0395'),
]
for name, usn in members:
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 7, name, align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, usn, align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
pdf.ln(10)
pdf.set_font('Times', 'B', 13)
pdf.cell(0, 8, 'Under the guidance of', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Times', '', 13)
pdf.cell(0, 8, 'Prof. Amruthesh Bhat', align='C', new_x="LMARGIN", new_y="NEXT")

# ===================== PAGE 2: CERTIFICATE =====================
pdf.add_page()
pdf.set_font('Times', '', 11)
pdf.cell(0, 6, 'School of Computer Science and Engineering', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, 'RV University-560059', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_font('Times', 'B', 14)
pdf.cell(0, 10, 'RV UNIVERSITY, BENGALURU-59', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.cell(0, 10, 'SCHOOL OF COMPUTER SCIENCE AND ENGINEERING', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(15)
pdf.set_font('Times', 'B', 16)
pdf.cell(0, 10, 'CERTIFICATE', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)
pdf.set_font('Times', '', 12)
pdf.multi_cell(0, 7,
    'Certified that the project work titled CIE3 - Activity is carried out by '
    'Priya N Bhat (335), Rohit Ajit Bharadwaj (375), Rohith P Hegde (376), '
    'S Sachithananthan (384), Saket M (395) '
    'in partial fulfilment of the completion of the course Probability and Statistics with course code CS2800 '
    'of the IV Semester Computer Science Engineering programme, during the academic year 2025-2026. '
    'It is certified that all corrections/suggestions indicated for the Internal Assessment have been '
    'incorporated in the project report and duly approved by the faculty.')
pdf.ln(20)
pdf.set_font('Times', '', 12)
pdf.cell(90, 7, 'Signature of Faculty', align='L')
pdf.cell(0, 7, 'Signature of Head of the Department', align='R', new_x="LMARGIN", new_y="NEXT")

# ===================== PAGE 3: TABLE OF CONTENTS =====================
pdf.add_page()
pdf.heading('Table of Contents')
pdf.ln(5)
toc = [('Abstract','4'), ('Introduction','5'), ('Objectives','6'), ('Methodology','7'),
       ('Implementation','10'), ('Result','12'), ('Conclusion','18'), ('References','19')]
for t, p in toc:
    pdf.set_font('Times', '', 12)
    pdf.cell(160, 8, t)
    pdf.cell(0, 8, p, align='R', new_x="LMARGIN", new_y="NEXT")

# ===================== PAGE 4:ABSTRACT =====================
pdf.add_page()
pdf.heading('ABSTRACT')
pdf.para(
    'This report presents two fundamental applications of probability and statistics: '
    'parabolic regression using the Normal Equation (solved via Gaussian Elimination) and '
    'verification of the Central Limit Theorem (CLT) through simulation.')
pdf.para(
    'In the first problem, data obtained from a ball-tracking system is used to estimate the '
    'trajectory of a ball. Since projectile motion follows a parabolic path, a quadratic regression '
    'model is fitted. The Normal Equation is first derived from first principles, then the resulting '
    '3x3 linear system is solved using Gaussian Elimination with partial pivoting. From this model, '
    'the launch height and the range of the ball are estimated. The negative value of the leading '
    'coefficient confirms the downward-opening parabola consistent with gravitational motion. Analytical '
    'verification of the provided dataset shows it forms a perfect mathematical parabola with zero variance.')
pdf.para(
    'In the second problem, a simulation-based experiment is designed to demonstrate the Central '
    'Limit Theorem using a die-rolling experiment. The sample size (n) is varied while keeping '
    'the number of experiments constant and high (5000). It is observed that as the sample size increases, '
    'the sampling distribution of the mean transitions from a uniform shape to a normal distribution.')
pdf.para(
    'The implementation is carried out using Python with NumPy, Matplotlib, and the random module, '
    'without using built-in regression or curve-fitting libraries, ensuring a clear understanding of '
    'the mathematical foundations.')

# ===================== PAGE 5: INTRODUCTION =====================
pdf.add_page()
pdf.heading('1. Introduction')
pdf.para(
    'In modern engineering and scientific applications, data collected from sensors and real-world '
    'systems is often affected by noise and uncertainty. Extracting meaningful information from '
    'such data requires the use of statistical tools and mathematical modeling techniques.')
pdf.para(
    'One of the most widely used techniques for modeling relationships between variables '
    'is regression analysis. In physical systems such as projectile motion, the relationship between '
    'horizontal distance and vertical height follows a quadratic pattern due to the influence of '
    'gravity. However, real-world data rarely fits perfectly due to measurement errors. Therefore, '
    'regression methods are used to approximate the underlying trend.')
pdf.para(
    'In this report, the first problem focuses on modeling the trajectory of a ball using quadratic '
    'regression. The Normal Equation is derived from first principles and the resulting linear system '
    'is solved using Gaussian Elimination. This approach avoids reliance on high-level curve-fitting '
    'libraries and strengthens the understanding of both linear algebra and numerical methods.')
pdf.para(
    'The second part of the report focuses on the Central Limit Theorem (CLT), which is one of '
    'the most important results in probability theory. The CLT explains why many natural '
    "phenomena follow a normal distribution. It states that the distribution of the sample mean "
    "approaches a normal distribution as the sample size increases, regardless of the population's "
    'original distribution.')
pdf.para('Understanding CLT is essential for: Statistical inference, Hypothesis testing, and Data analysis in machine learning.')
pdf.para(
    'This report combines theoretical understanding with practical simulation to provide a '
    'comprehensive view of both regression and probabilistic behavior.')

# ===================== PAGE 6: OBJECTIVES =====================
pdf.add_page()
pdf.heading('2. Objectives')
pdf.para('The objectives of this activity are designed to provide both theoretical understanding and practical implementation skills in probability and statistics.')
pdf.bold('Primary Objectives')
pdf.bullet('To understand the concept of regression analysis and its application in modeling real-world data')
pdf.bullet('To derive the Normal Equation from first principles (minimizing the sum of squared errors)')
pdf.bullet('To solve the resulting linear system using Gaussian Elimination')
pdf.bullet('To fit a quadratic model to trajectory data and analyze mathematical residuals')
pdf.bullet('To estimate important physical parameters such as:')
pdf.subbullet('Launch height of the ball')
pdf.subbullet('Horizontal range of the ball')
pdf.ln(3)
pdf.bold('Secondary Objectives')
pdf.bullet('To understand the concept of sampling distributions')
pdf.bullet('To experimentally verify the Central Limit Theorem by varying sample size')
pdf.bullet('To analyze how the distribution of sample means changes with increasing sample size (n)')
pdf.bullet('To compare empirical results with theoretical normal distribution')
pdf.ln(3)
pdf.bold('Technical Objectives')
pdf.bullet('To implement statistical models using Python')
pdf.bullet('To visualize results using graphs and plots')
pdf.bullet('To interpret statistical outputs in a meaningful way')
pdf.ln(3)
pdf.para('This activity aims to bridge the gap between theoretical concepts and practical implementation.')

# ===================== PAGE 7-9: METHODOLOGY =====================
pdf.add_page()
pdf.heading('3. Methodology')
pdf.bold('Problem 1: Ball Trajectory Modeling')
pdf.para(
    'The trajectory of a ball under gravity follows a parabolic path. Therefore, the relationship '
    'between horizontal distance x and vertical height y can be modeled as:')
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 7, '    y = ax^2 + bx + c', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.set_font('Times', '', 12)
pdf.para('Where a, b, and c are coefficients to be determined; c represents the initial height; and a must be negative (parabola opens downward under gravity).')

# ---- DERIVATION OF NORMAL EQUATION ----
pdf.bold('3.1 Derivation of the Normal Equation')
pdf.para(
    'The goal of regression is to find coefficients that minimize the Sum of Squared Errors (SSE). '
    'For a model Y = X * beta, the error vector is e = Y - X * beta, and the SSE is:')
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 7, '    SSE = e^T * e = (Y - X*beta)^T * (Y - X*beta)', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.para('Expanding this expression:')
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 7, '    SSE = Y^T*Y - 2*beta^T*X^T*Y + beta^T*X^T*X*beta', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.para(
    'To minimize SSE, we take the partial derivative with respect to beta and set it to zero:')
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 7, '    d(SSE)/d(beta) = -2*X^T*Y + 2*X^T*X*beta = 0', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.para('Rearranging gives us the Normal Equation:')
pdf.set_font('Times', 'B', 13)
pdf.cell(0, 10, '    X^T * X * beta = X^T * Y', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.para(
    'This is a system of linear equations. Instead of computing the matrix inverse (which is '
    'computationally expensive and numerically unstable), we solve this system directly using '
    'Gaussian Elimination.')

pdf.add_page()
pdf.bold('3.2 Solving Using Gaussian Elimination')
pdf.para(
    'Gaussian Elimination is a systematic method for solving systems of linear equations. '
    'It consists of two phases:')
pdf.bold('Phase 1: Forward Elimination')
pdf.para(
    'The augmented matrix [A | b] is transformed into upper triangular form by eliminating '
    'entries below the main diagonal. Partial pivoting (swapping rows to place the largest '
    'absolute value on the diagonal) is used to improve numerical stability.')
pdf.bold('Phase 2: Back Substitution')
pdf.para(
    'Starting from the last equation (which now has only one unknown), we solve for each '
    'variable by substituting already-known values back into the equations above.')
pdf.para(
    'For our quadratic model y = ax^2 + bx + c, the design matrix X has rows [1, x_i, x_i^2]. '
    'The product X^T * X produces a 3x3 matrix, and X^T * Y produces a 3x1 vector. '
    'Gaussian Elimination solves this 3x3 system to yield the coefficients c, b, and a.')

pdf.ln(3)
pdf.bold('3.3 Physical Interpretation')
pdf.bullet('Launch height = c (value of y when x = 0)')
pdf.bullet('Range = positive root of ax^2 + bx + c = 0, found via the Quadratic Formula')
pdf.bullet('The coefficient a must be negative, confirming a downward-opening parabola under gravity')

pdf.add_page()
pdf.bold('Problem 2: Central Limit Theorem Simulation')
pdf.ln(3)
pdf.bold('Steps Followed')
pdf.para('1. Define a population with a Uniform Distribution (rolling a fair 6-sided die)')
pdf.para('2. Keep the number of experiments fixed at a high value (5000) for smooth histograms')
pdf.para('3. Vary the sample size n across three values: n=1, n=5, n=50')
pdf.para('4. For each experiment, roll n dice, compute the sample mean')
pdf.para('5. Plot the histogram of sample means for each sample size')
pdf.ln(3)
pdf.bold('Key Idea')
pdf.para(
    'The CLT is correctly demonstrated by increasing the sample size (n), NOT by increasing the '
    'number of experiments. Increasing the number of experiments only makes the histogram smoother '
    'but does not change the shape of the distribution. Increasing n causes the distribution to '
    'transition from uniform to normal.')

# ===================== IMPLEMENTATION =====================
pdf.add_page()
pdf.heading('4. Implementation')
pdf.bold('Problem 1: Implementation Details')
pdf.para(
    'The implementation begins by importing NumPy (for matrix operations) and Matplotlib (for plotting). '
    'The dataset from the ball-tracking setup is stored as Python lists.')
pdf.para(
    'A design matrix is created by manually appending [1, x, x^2] rows in a loop. The Normal Equation '
    'system A*beta = b is formed by computing A = X^T*X and b = X^T*Y using np.dot() and np.transpose().')
pdf.para(
    'Instead of using np.linalg.inv() to compute the matrix inverse, we implement a custom '
    'gaussian_elimination() function that performs:')
pdf.bullet('Construction of the augmented matrix [A | b]')
pdf.bullet('Forward elimination with partial pivoting (row swapping for numerical stability)')
pdf.bullet('Back substitution to extract the solution vector beta')
pdf.para('After computing the coefficients:')
pdf.bullet('The fitted quadratic equation is printed')
pdf.bullet('Launch height is extracted as c = beta[0]')
pdf.bullet('The Quadratic Formula is used to compute roots, with explicit checking that the selected root is positive')
pdf.bullet('A smooth regression curve is generated using np.linspace and plotted alongside the original data')

pdf.ln(5)
pdf.bold('Problem 2: Implementation Details')
pdf.para(
    "A die-rolling simulator is built using Python's built-in random module with random.randint(1, 6). "
    'Plain for-loops are used instead of vectorized NumPy operations to maintain clarity and explain the '
    'sampling process step-by-step.')
pdf.para('For each configuration:')
pdf.bullet('get_single_sample_mean(n) rolls n dice, sums their values, and returns the mean')
pdf.bullet('The experiment is repeated 5000 times, storing each mean in a list')
pdf.bullet('Histograms are plotted with density=True to show probability density rather than raw counts')
pdf.ln(3)
pdf.para('Three subplots are generated for sample sizes n=1, n=5, and n=50 to visually demonstrate the CLT.')

# ===================== RESULTS =====================
pdf.add_page()
pdf.heading('5. Result')
pdf.bold('Activity 1: Ball Trajectory Regression (Gaussian Elimination)')
pdf.ln(3)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 7, 'Code:', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
with open('question1_ball_tracker.py', 'r') as f:
    q1_code = f.read()
pdf.set_font('Courier', '', 7)
for line in q1_code.split('\n'):
    pdf.cell(0, 4, '  ' + line, new_x="LMARGIN", new_y="NEXT")

pdf.add_page()
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 7, 'Console Output:', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_font('Courier', '', 10)
pdf.cell(0, 6, '  Parabolic Equation: y = -0.00726x^2 + 0.57735x + 1.60000', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, '', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, "  a) The height from which the ball left the player's hand: 1.60000 metres", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, '  b) Estimated range of the ball: 82.21388 metres', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 7, 'Graph Output & Important Analytical Observation:', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_font('Times', '', 11)
pdf.multi_cell(0, 6, "Observation on Data Noise: While the problem statement suggests that the camera data is 'imprecise and noisy', analytical inspection of the provided table reveals a perfect mathematical series. Computing the second differences (e.g., [y2 - y1] - [y1 - y0]) yields a constant value of roughly -0.05807 across all points. This mathematically proves that the tabulated data is an EXACT downward-opening parabola with zero variance or external noise added. Consequently, as seen in the graph below, our fitted regression curve correctly passes cleanly through the center of every single data point with near-zero residuals.")
pdf.ln(2)
pdf.image('q1_output.png', x=15, w=180)

# Q2 Results
pdf.add_page()
pdf.bold('Activity 2: Central Limit Theorem Simulation')
pdf.ln(3)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 7, 'Code:', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
with open('question2_clt_simulation.py', 'r') as f:
    q2_code = f.read()
pdf.set_font('Courier', '', 8)
for line in q2_code.split('\n'):
    pdf.cell(0, 4.5, '  ' + line, new_x="LMARGIN", new_y="NEXT")

pdf.add_page()
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 7, 'Graph Output:', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.image('q2_output.png', x=10, w=190)
pdf.ln(5)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 7, 'Observations:', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.bullet('n=1: The histogram is flat and uniform, reflecting the original die distribution')
pdf.bullet('n=5: The distribution begins to resemble a bell curve, with tails shrinking')
pdf.bullet('n=50: The histogram closely approximates a perfect Normal Distribution, confirming CLT')

# ===================== CONCLUSION =====================
pdf.add_page()
pdf.heading('6. Conclusion and Future Enhancement')
pdf.para(
    'The results validate both regression modelling and the Central Limit Theorem through '
    'practical implementation.')
pdf.para(
    'In the first problem, quadratic regression using the Normal Equation (derived from first principles '
    'and solved via Gaussian Elimination) provided an accurate model for the trajectory of a ball. '
    'Despite noise in the data, the regression model was able to estimate key parameters such as '
    'launch height (1.60 metres) and range (82.21 metres) effectively. The negative coefficient a '
    'confirmed the downward-opening parabolic trajectory consistent with gravitation. Using Gaussian '
    'Elimination instead of direct matrix inversion demonstrated a deeper understanding of numerical methods.')
pdf.para(
    'In the second problem, the Central Limit Theorem was validated through simulation. It was '
    'clearly observed that as the sample size (n) increases, the distribution of sample means '
    'transitions from uniform to normal. This correctly demonstrates the theoretical foundation '
    'of the CLT, which depends on sample size rather than the number of experimental repetitions.')
pdf.para('Overall, this activity enhanced understanding of:')
pdf.bullet('Derivation and application of the Normal Equation')
pdf.bullet('Gaussian Elimination for solving linear systems')
pdf.bullet('Matrix-based computation for analytical solutions')
pdf.bullet('Sampling distributions and the role of sample size')
pdf.bullet('Statistical simulation and visual verification')
pdf.ln(3)
pdf.para(
    'These concepts are fundamental in fields such as data science, machine learning, and '
    'engineering analysis.')

# ===================== REFERENCES =====================
pdf.add_page()
pdf.heading('References')
pdf.bullet('Sheldon Ross, Introduction to Probability and Statistics')
pdf.bullet('NumPy Official Documentation - https://numpy.org')
pdf.bullet('Matplotlib Documentation - https://matplotlib.org')
pdf.bullet('Python random module Documentation - https://docs.python.org/3/library/random.html')
pdf.bullet('Lecture Notes - Probability and Statistics Course')

pdf.output('PS_Report_CIE3.pdf')
print('Report saved to PS_Report_CIE3.pdf')
