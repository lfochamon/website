title: Latex rules
date: 2022-02-14
summary: For me and mine, they're rules. But for all others, they're just tips.
status: draft

Latex is how the vast majority of scientific texts get written. It handles math well,
does a good job at bibliography management (using *bibtex*), and compiles straight to
the cross-platform `pdf` format. On top of all that, most scientific publications
provide you with Latex templates. That means you don't need to worry with margins,
spacing, font sizes, paragraph indentations... Essentially, Latex separates content
from form: you write your content in a way that can then be compiled to fit virtually
any journal or conference (with minor modifications, of course). It's the same idea
behind modern web design: HTML for content, CSS for style.

Because of that, it is useful to think of Latex in two ways. On the one hand,
writing in Latex is like *coding* a text. The source file contains the content that will
be given form during compilation. As such, all good coding rules apply: indent,
space out, use different file for different modules (text parts)... When at all
possible, you should strive to make your Latex sources as readable to a human as the
compiled `pdf` version. Imagine coming back to edit this

``` { .latex cssstyles="background:#FFCECC;" }
When $x^2<c_t\tau$, we obtain that\[z(t)\leq\Vert z-z^\star\Vert_\infty,\] which
concludes the proof.
```

compared to

``` { .latex cssstyles="background:#B8E6C8;"}
When~$x^2 < c_t \tau$, we obtain that
%
\begin{equation*}
  z(t) \leq \Vert z-z^\star \Vert_\infty
    \text{,}
\end{equation*}
%
which concludes the proof.
```

And that's not even the worst I've seen.

On the other hand, it's important to remember the goal is to write, not code.
Too much focus on source formatting can easily get in the way of putting words
on a page, which is what gets papers written.

Still, there are a few rules and habits that can make your life easier by both
making your Latex source more readable and avoiding formatting pitfalls
and bad design practices. Below is a compilation of mine. If you have any
other interesting tip or habit, send me an [email](mailto:{{EMAIL}}). I'm always
looking to add new tricks to my workflow. And in the spirit of good scholarship,
you'll get a citation for that rule.



## The rules

*Caveat: some examples below only make sense on screens that display this sentence on a single line.
That is particularly the case for those examples that have to do with spacing rules (e.g., Rule 8).*


#### 1. Use `~`

Use `~` (unbreakable space) between words and inline equations, reference numbers,
citations, and essentially any Latex command. You never want a dangling reference
or math symbol starting a line.

``` { .latex cssstyles="background:#FFCECC;" }
For all $x < \tau$, the \eqref{E:upper_bound} holds trivially \cite{LastNameYYp}.
```

``` { .latex cssstyles="background:#B8E6C8;"}
For all~$x < \tau$, the~\eqref{E:upper_bound} holds trivially~\cite{LastNameYYp}.
```


#### 2. Space out environments
Separate your displayed math environments from text using `%` (as in the
example above). Latex takes blank lines to mean it should start a new paragraph.
Often, that is *not* what you want. Still, you always want to separate the
Latex environments from the text to improve your source readability.

``` { .latex cssstyles="background:#FFCECC;" }
It therefore holds that\[z(t)\leq\Vert z-z^\star\Vert_\infty,\] which concludes the proof.
```

``` { .latex cssstyles="background:#B8E6C8;"}
It therefore holds that
%
\begin{equation*}
  z(t) \leq \Vert z - z^\star \Vert_\infty
    \text{,}
\end{equation*}
%
which concludes the proof.
```


#### 3. Use `-`, `--`, and `---` appropriately
A *dash* (`-`) is to be used when forming composed
nouns or adjectives (as in `state-of-the-art performance` or `a complicated trade-off`).
An *endash* (`--`) is to be used to indicate ranges (as in `pages 2--3` or `Figures 1--4`).
Note that there is no space around the endash. An *emdash* (`---`) is to be
used similarly to parentheses`---as is the case with this example`.
Do not leave space`---and I mean, no space whatsoever---`before or after emdashes.

Always use an endash (`--`) when indicating page ranges in bibtex files.



#### 4. Never write "equation X"
Never write "according to equation X" or "according to equation (X)."
Write "according to (X)" as in
`according to~\eqref{E:equationName}`{: style="background:#B8E6C8;"}
and not `according to (\ref{E:equationName})`{: style="background:#FFCECC;"}
or `according to (X)`{: style="background:#FFCECC;"}.
An exception is typically made in the beginning of sentences. Equation (X),
in this case, is acceptable. Still, don't do it. Just reword the sentence
as "In this case, (X) is acceptable."

**Note**: in certain fields, writing "equation (X)" is the norm, but I do not typically
work in those field.



#### 5. Only words begin
Never start sentences or lines with math symbols, equation numbers, or references.
If you follow Rule`~`1, then this will never happen without your consent.



#### 6. Use `.\_` when a point is not a period
If you use a point to indicate an abbreviation *and* it is not the end of a sentence,
then follow it by a `\_` (as in `Dept.\ of Electrical Engineering`{: style="background:#B8E6C8;"}
or `L.\ F.\ O.\ Chamon`{: style="background:#B8E6C8;"}). Latex adds extra space after every point
because it always assumes it is a period. Doing this will avoid some awkward extra spacing in the
middle of your sentence.



#### 7. Consider `\cite[]{}`
Use the `\cite[]{}` to refer to specific sections/theorems, especially when you refer to
a specific result in a paper (e.g., `\cite[Thm.~3]{LastNameYYp}`{: style="background:#B8E6C8;"}).
When citing from books this is mandatory (e.g., `\cite[Section~3.2]{LastNameYYp}`{: style="background:#B8E6C8;"}).
It is a favor for the reader that wants to check the result and good scholarship: unless the
statement you just made relies on all the results in a paper/book, you should refer only to what is
directly relevant.



#### 8. Keep math in line (or break it on purpose)
Keep all math expressions on a single source code line.

``` { .latex cssstyles="background:#FFCECC;"}
So if you find that your inline math expression won't fit in the same line~$z(t) \leq \Vert z-z^\star \Vert_\infty$.
```

``` { .latex cssstyles="background:#B8E6C8;"}
So if you find that your inline math expression won't fit in the same
line~$z(t) \leq \Vert z-z^\star \Vert_\infty$, just put it in the next one.
```
If the expression is too long, break it down in logical parts and use indentation as if you were coding Python!

``` { .latex cssstyles="background:#FFCECC;" }
\begin{equation*}
z(t) \leq \Vert z-z^\star \Vert_\infty \text{,}
\end{equation*}

\begin{equation}
\sum_{i = 1}^m \mu_i \Big( \E_{(\bx,y) \sim \fkD_i}
\Big[ \ell_i\big( f(\bx),y \big) \Big] \Big) \text{,}
\end{equation}

\begin{align}
\hat{L}(\btheta, \bmu) &= \frac{1}{N_0}
\sum_{n_0 = 1}^{N_0} \ell_0\big( f(\bx_{n_0}), y_{n_0} \big)\\
{}&+ \sum_{i = 1}^m \mu_i \left[ \frac{1}{N_i} \sum_{n_i = 1}^{N_i}
\ell_i\big( f(\bx_{n_i}), y_{n_i} \big) \right] \text{,}
\end{align}
```

``` { .latex cssstyles="background:#B8E6C8;"}
\begin{equation*}
  z(t) \leq \Vert z-z^\star \Vert_\infty
    \text{,}  % Separate and indent punctuation and text
\end{equation*}

\begin{equation}
  \sum_{i = 1}^m \mu_i \Big(    % Break when opening brackets...
    \E_{(\bx,y) \sim \fkD_i} \Big[ \ell_i\big( f(\bx),y \big) \Big]
  \Big)   % ...then close it on a separate line
    \text{,}
\end{equation}

\begin{align}
  L(\btheta, \bmu) &=   % Break at binary operators
    \frac{1}{N_0} \sum_{n_0 = 1}^{N_0} \ell_0\big( f(\bx_{n_0}), y_{n_0} \big)
  \\  % Clearly separate equations groups
  {}&+ \sum_{i = 1}^m \mu_i \left[
    \frac{1}{N_i} \sum_{n_i = 1}^{N_i}
      \ell_i\big( f(\bx_{n_i}), y_{n_i} \big)   % Indent to show continuation
  \right]
    \text{,}
\end{align}
```


#### 9. Indent!
Aside from math expressions, also indent text environments such as lists and tables for clarity.

``` { .latex cssstyles="background:#FFCECC;" }
\begin{itemize}
\item the function~$\ell_i$ is convex
\item $\calY$ is finite, the conditional random variables~$\bx \vert y$ is non-atomic,
and~$\calH$ is decomposable
\end{itemize}
```

``` { .latex cssstyles="background:#B8E6C8;"}
\begin{itemize}
  \item the function~$\ell_i$ is convex
  \item $\calY$ is finite, the conditional random variables~$\bx \vert y$ is non-atomic,
        and~$\calH$ is decomposable
\end{itemize}
```


#### 10. `begin` and `end` on separate lines
Latex environments must always `begin` and `end` on separate lines.

``` { .latex cssstyles="background:#FFCECC;" }
\begin{equation*} z(t) \leq \Vert z-z^\star \Vert_\infty \end{equation*}
```

``` { .latex cssstyles="background:#B8E6C8;"}
\begin{equation*}
  z(t) \leq \Vert z-z^\star \Vert_\infty
\end{equation*}
```


#### 11. Give binary operators their space
Always place spaces before and after binary operators. You should be writing

``` { .latex cssstyles="background:#B8E6C8;"}
$x = y$, $x \leq y$, $x - y$, and $x \cdot y$
```

and not

``` { .latex cssstyles="background:#FFCECC;" }
$x=y$, $x\leq y$, $x-y$, and $x\cdot y$
```

#### 12. Break-up `frac`
Unless both numerator and denominator are short, e.g., `\frac{x^2}{2y}`{: style="background:#B8E6C8;"},
always place them in separate (indented) lines as in

``` { .latex cssstyles="background:#B8E6C8;"}
\frac{
  \abs{\calK}^2
}{
  \trace \left[ \bLambda^{-1} \right] +
  \trace \left[ \left( \sum_{i \in \calS} \lambda_{w,i}^{-1} \bv_i \bv_i^{H} \right) \right]
}
```

instead of

``` { .latex cssstyles="background:#FFCECC;" }
\frac{\abs{\calK}^2}{\trace \left[ (\bW \bLambda)^{-1} \right]+\trace \left[ \bW^{-1} \left( \sum_{i \in \calS} \lambda_{w,i}^{-1} \bv_i \bv_i^{H} \right) \right]}
```


#### 13. Use `\text` in math environments
Whenever you have text in a math environment, place it in a `\text` tag. That includes names, i.e.,
`$\text{OPT} \leq 0.1$`{: style="background:#B8E6C8;"} and not `$OPT \leq 0.1$`{: style="background:#FFCECC;"};
sub/superscripts that are not variables, i.e.,
`$J_\text{max}$`{: style="background:#B8E6C8;"} and not `$J_{max}$`{: style="background:#FFCECC;"}
(or worse, `$J_{\max}$`{: style="background:#FFCECC;"}!);
and punctuation, i.e.,

``` { .latex cssstyles="background:#B8E6C8;"}
\begin{equation*}
  z(t) \leq \Vert z-z^\star \Vert_\infty
    \text{.}
\end{equation*}
```

and not

``` { .latex cssstyles="background:#FFCECC;" }
\begin{equation*}
  z(t) \leq \Vert z-z^\star \Vert_\infty.
\end{equation*}
```

If you are writing in the context of a definition or theorem environment, which are sometimes typeset in italic, you should use the `\textup` tag.



#### 14. Know your math environments
Choose the right math environments for the job. If you do this right, you should have little to no need to manually mess with spacing or labels.
Here are the main suspects you should know how to use, in order of importance:

  - `equation`/`equation*`: typical, single-line equation. The starred version omits the equation label.
  - `align`/`align*`: math environment spanning multiple lines aligned at a specific symbol or operator. Every line receives a different label,
    so this environment is better-suited to present a set of multiple equations in parallel. The starred version omits all labels, which also
    makes it suited for a single equation that spans multiple lines (although you are better off using `aligned` for this).
  - `aligned`: use this environment inside an `equation` environment to get a set of multiple aligned equations with a single centered label.
    You should never use `align` together with `\notag` to achieve this result.
  - `multline`/`multline*`: a single equation spanning multiple lines without alignment. The first line is flushed left while the last line is
    flushed right, giving a sense of flow to the equation. I prefer multiline equations to be aligned, but `multiline` occasionally looks better.
  - `gather`/`gather*`: math environment spanning multiple lines in which the equations are centered. Every line receives a different label,
    so this environment should be used similarly to `align`. The starred version omits all labels.
  - `gathered`: similarly to `aligned`, you can use this inside an `equation` environment to get a set of multiple, centered equations with a
    single label. You should never use `gather` together with `\notag` to achieve this result.
  - `alignat`: a more flexible version of `align`. This is very niche and you should not have to use it.

Two other "math environments" worth knowing (and using) involve matrices (`pmatrix` for parenthesis and `bmatrix` for brackets) and equation with
cases as in

``` { .latex cssstyles="background:#B8E6C8;"}
\begin{equation*}
  \phi_{\epsilon}(\bx) =
    \begin{cases}
      \phi(\bx) \text{,}
        &\text{for } \bx \in \calT
      \\
      \phi^\prime(\bx) \text{,}
        &\text{for } \bx \in \calT^c
    \end{cases}
\end{equation*}
```

Never use some weird combination of `\left{` and `\right.` to do this.




  - Where to break long equations
    - at a relation operators (equality, inequality): keep on the previous line
    - at a binary operator (preferably, an addition... if you must break at a multiplication using `\times` to make it extra explicit): place on the next line (except for multiplication)
  - Do `{}+{}` or `{}={}` for binaries on multiline environments
  - Only label equations you will reference later
  - Use `E:`, `T:`, `F:`, `S:`, `X:`, `P:`, `L:`
  - Use `\dot`, `\dots`, `\cdot`, `\cdots` accordingly
  - I like `\big`, `\Big`, `\bigg` better than iterated `\left`, `\right`: gives you more control
    - Also, `\bigm` is useful (delimiter with binary spacing)
  - Use `\DeclareMathOperator` rather than `\newcommand` for math
  - Leverage `\quad` and `\qquad`
  - Use the `bm` packed for bold symbols: it looks better

  - Choose a notation and stick with it! (but make sure to review it: sometimes, our convention choices turn out to be less than ideal)
  - If you are working with me, use my macros!
  - For me:
    - vectors are columns and boldface lowercase
    - matrices are boldface uppercase
    - sets are caligraphic (except for number sets, e.g., real, rational, integer, natural, which are blackboard)
    - measures are Fraktur
    - use eta for step sizes
    - use lambda for eigenvalues
    - use sigma for variance
    - use lambda (inequalities) and mu (equalities) for dual variable (if eigenvalues are not very important, you may replace lambda with sigma... otherwise, use nu)
    - Lagrangian are capital L and the dual function is d (even if g is arguably more common)
    - use gamma for regularizing parameters
    - use theta for "solution parametrization" (unless you have a linear model, in which case use w)
    - use phi for generic functions and f_\theta for their parametrization
    - use x for the input, y for the desired output, (x,y) for samples, \hat{y} for the predicted output
    - use \hat for predictions
    - constraints are always lower than for minimization and larger than for maximization
    - optimization problems are tagged (PXX), where XX is a roman number. Named optimization problems (good practice, but easily abused!) are tagged (P-NAME).
      Their dual problems are tagged (DXX) and (D-NAME), respectively.
