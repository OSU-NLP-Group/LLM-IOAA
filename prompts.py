TOC = """\\begin{document}

\\section*{Universal Constants}

\\begin{tabular}{l l}
Avogadro constant & $6.022 \\times 10^{23}\\ \\text{mol}^{-1}$ \\\\
Boltzmann constant & $1.381 \\times 10^{-23}\\ \\text{J K}^{-1}$ \\\\
Charge of electron $e$ & $1.602 \\times 10^{-19}\\ \\text{C}$ \\\\
Planck constant & $6.626 \\times 10^{-34}\\ \\text{J s}$ \\\\
Speed of light in vacuum & $2.998 \\times 10^{8}\\ \\text{m s}^{-1}$ \\\\
Universal gravitational constant & $6.674 \\times 10^{-11}\\ \\text{N m}^2\\ \\text{kg}^{-2}$ \\\\
Universal gas constant & $8.315\\ \\text{J mol}^{-1}\\ \\text{K}^{-1}$ \\\\
Stefan-Boltzmann constant & $5.670 \\times 10^{-8}\\ \\text{W m}^{-2}\\ \\text{K}^{-4}$ \\\\
Wien’s displacement constant & $2.898 \\times 10^{-3}\\ \\text{m K}$ \\\\
Permittivity of free space & $8.854 \\times 10^{-12}\\ \\text{m}^{-3}\\ \\text{kg}^{-1}\\ \\text{s}^4\\ \\text{A}^2$ \\\\
Permeability of free space & $1.257 \\times 10^{-6}\\ \\text{N A}^{-2}$ \\\\
Mass of electron & $9.109 \\times 10^{-31}\\ \\text{kg} = 0.511\\ \\text{MeV}/c^2$ \\\\
Mass of proton & $1.673 \\times 10^{-27}\\ \\text{kg} = 938.272\\ \\text{MeV}/c^2$ \\\\
Mass of neutron & $1.675 \\times 10^{-27}\\ \\text{kg} = 939.565\\ \\text{MeV}/c^2$ \\\\
Mass of deuteron & $3.344 \\times 10^{-27}\\ \\text{kg} = 1875.613\\ \\text{MeV}/c^2$ \\\\
Mass of He nucleus & $6.645 \\times 10^{-27}\\ \\text{kg} = 3727.181\\ \\text{MeV}/c^2$ \\\\
\\end{tabular}

\\section*{Astronomical Data}

\\begin{tabular}{l l}
Mass of Sun & $1.988 \\times 10^{30}\\ \\text{kg}$ \\\\
Radius of Sun & $6.957 \\times 10^{8}\\ \\text{m}$ \\\\
Luminosity of Sun & $3.828 \\times 10^{26}\\ \\text{W}$ \\\\
Effective temperature of Sun & $5772\\ \\text{K}$ \\\\
Apparent magnitude of Sun (V-band) & $-26.74$ \\\\
Absolute magnitude of Sun (V-band) & $+4.82$ \\\\
Apparent bolometric magnitude of Sun & $-26.83$ \\\\
Absolute bolometric magnitude of Sun & $+4.74$ \\\\
Solar constant (above atmosphere of Earth) & $1361\\ \\text{W m}^{-2}$ \\\\
Apparent angular diameter of Sun (from Earth) & $\\approx 32'$ \\\\
Mass of Earth & $5.972 \\times 10^{24}\\ \\text{kg}$ \\\\
Radius of Earth & $6.378 \\times 10^{6}\\ \\text{m}$ \\\\
Axial tilt of Earth & $23^\\circ 26'$ \\\\
Inclination of lunar orbit to ecliptic & $5^\\circ 8' 43''$ \\\\
Mass of Jupiter & $1.898 \\times 10^{27}\\ \\text{kg}$ \\\\
Radius of Jupiter & $6.991 \\times 10^{7}\\ \\text{m}$ \\\\
1 Astronomical Unit (au) & $1.496 \\times 10^{11}\\ \\text{m}$ \\\\
1 parsec (pc) & $3.086 \\times 10^{16}\\ \\text{m}$ \\\\
1 light-year (ly) & $9.461 \\times 10^{15}\\ \\text{m}$ \\\\
1 jansky (Jy) & $10^{-26}\\ \\text{W m}^{-2}\\ \\text{Hz}^{-1}$ \\\\
1 tropical year & $365.2422\\ \\text{days} = 3.156 \\times 10^7\\ \\text{s}$ \\\\
 & $= 365\\ \\text{d}\\ 5\\ \\text{h}\\ 48\\ \\text{min}\\ 46\\ \\text{s}$ \\\\
1 sidereal year & $365.2564\\ \\text{days} = 3.156 \\times 10^7\\ \\text{s}$ \\\\
 & $= 365\\ \\text{d}\\ 6\\ \\text{h}\\ 9\\ \\text{min}\\ 13\\ \\text{s}$ \\\\
Rate of precession of Vernal Equinox & $1^\\circ$ per 71.6 years \\\\
\\end{tabular}

\\section*{Calculus Related Formulas}

\\[
\\frac{d}{dx} x^n = n x^{n-1}
\\]

\\[
\\frac{d}{dx} \\sin(kx) = k \\cos(kx)
\\]

\\[
\\frac{d}{dx} \\cos(kx) = -k \\sin(kx)
\\]

\\[
\\frac{d}{dx} \\tan(kx) = k \\sec^2(kx)
\\]

\\[
\\int x^n dx = \\frac{x^{n+1}}{n+1} + C, \\quad n \\neq -1
\\]

\\[
f(x) \\approx f(x_0) + \\left.\\frac{df}{dx}\\right|_{x=x_0} (x - x_0), \\quad x \\approx x_0
\\]

\\end{document}"""


SYS_INST = "Ignore all previous instructions and DO NOT worry about fitting your answer in a single chat window. You are an expert in Astronomy and Astrophysics who is participating in an International Olympiad on Astronomy and Astrophysics (IOAA) level exam."


GEN_INST = """Please think step by step and solve the given problem with a complete, detailed, and thorough answer.
Please rigorously justify and clearly explain each step of your solution and do not skip important steps. You have unlimited space to write your answer. A correct final answer with flawed or incomplete reasoning will receive no credit.
Please use LaTeX to clearly format your answer, especially properly wrapping math expressions in `$...$` for inline math and `\\[...\\]` for display math. A poorly formatted LaTeX solution that cannot compile will receive no credit.
When asked to draw a plot, please use `tikzpicture` and `pgfplots` to directly make the figure in LaTeX and provide a clear and correct caption of your plot to explain your reasoning. A missing figure or poor caption will receive no credit.
Please remember to wrap your solution in `\\begin{document}` and `\\end{document}`, as the grader will use them to extract the solution. A solution that cannot be extracted will receive no credit.

Here is the problem statement:
"""


IMPROVE_INST = """Please think step by step and revise your answer to the given problem according to the feedback.
Please rewrite the entire solution and include all parts and steps in your revision even if they are correct and unchanged. The grader will only check the latest revision, so make sure it is complete and no part is missing. You have unlimited space to write your answer.
Please rigorously justify and clearly explain each step of your solution and do not skip important steps. You have unlimited space to write your answer. A correct final answer with flawed or incomplete reasoning will receive no credit.
Please use LaTeX to clearly format your answer, especially properly wrapping math expressions in `$...$` for inline math and `\\[...\\]` for display math. A poorly formatted LaTeX solution that cannot compile will receive no credit.
When asked to draw a plot, please use `tikzpicture` and `pgfplots` to directly make the figure in LaTeX and provide a clear and correct caption of your plot to explain your reasoning. A missing figure or poor caption will receive no credit.
Please remember to wrap your solution in `\\begin{document}` and `\\end{document}`, as the grader will use them to extract the solution. A solution that cannot be extracted will receive no credit.
"""


IMPROVE_INST2 = """Here are the problem statement, your previous solution, and the feedback:
### Problem ###
{}

### Solution to Revise ###
{}

### Feedback ###
{}
"""


VER_SYS_INST = "Ignore all previous instructions and DO NOT worry about fitting your answer in a single chat window. You are an expert astronomer and astrophysicist and a meticulous grader for an International Olympiad on Astronomy and Astrophysics (IOAA) level exam."


VER_INST = """Please think step by step and rigorously verify each step in the provided solution to an IOAA level exam problem. DO NOT solve the problem, correct the errors, or fill the gaps you find.
Please make sure to perform a step-by-step check of the entire solution and justify your assessment of each step: for correct steps, a brief justification suffices; for steps with errors or gaps, you must provide a detailed explanation.
A solution that arrives at a correct final answer through flawed reasoning, educated guesses, or with gaps in its arguments must be flagged as incorrect or incomplete.

Here're some common errors that you may pay extra attention to:
- Calculation Error (e.g., correct expression, wrong arithmetic)
- Dimensional Mismatch (e.g., LHS/RHS units don't match)
- Incorrect Order of Magnitude (e.g., clearly implausible scale)
- Inconsistency with Given Data (e.g., reverse-check fails)
- Incorrect Formula / Inapplicable Formula (e.g., using a formula outside its valid range)
- Justification Gap (e.g., conclusion possibly true but argument incomplete/hand-wavy)

In your response to user, please make sure to include a detailed summary of each error you have found by quoting the relevant text and explaining the issue. Conclude your response with a final verdict on the solution's correctness: "The solution is (correct/incorrect)."


The problem and solution for you to grade are as follows:
### Problem ###
{}

### Solution ###
{}
"""