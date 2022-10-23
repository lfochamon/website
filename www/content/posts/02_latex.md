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

Still, there are a few rules and habits that can make your easier both in
making your Latex source more readable, but also avoiding formatting pitfalls
and bad design practices. Here is a compilation of my rules. If you have any
other interesting tip or habit, send me an [email](mailto:{{EMAIL}}). I'm always
looking to add new tricks to my workflow. And in the spirit of good scholarship,
you'll get a citation for that rule.

  1. Use `~` (unbreakable space) between words and inline equations, reference
    numbers, citations, and essentially any Latex command (as in the example above).
    You never want a dangling reference or math symbol starting a line.

``` { .latex cssstyles="background:#FFCECC;" }
For all $x < \tau$, the \eqref{E:upper_bound} holds trivially \cite{LastNameYYp}.
```

``` { .latex cssstyles="background:#B8E6C8;"}
For all~$x < \tau$, the~\eqref{E:upper_bound} holds trivially~\cite{LastNameYYp}.
```

  2. Separate your displayed math environments from text using `%` (as in the
    example above). Latex takes blank lines to mean it should start a new paragraph.
    Often, that is *not* what you want. Still, you always want to separate the
    Latex environments from the text to improve your source readability.

  3. Use `-`, `--`, and `---` appropriately. A *dash* (`-`) is to be used when forming composed
    nouns or adjectives (as in `state-of-the-art performance` or `a complicated trade-off`).
    An *endash* (`--`) is to be used to indicate ranges (as in `pages 2--3` or `Figures 1--4`).
    Note that there is no space around the endash. An *emdash* (`---`) is to be
    used similarly to parentheses`---as is the case with this example`.
    Do not leave space`---and I mean, no space whatsoever---`before of after emdashes.

  4. Always use an endash (`--`) when indicating page ranges in bibtex files.

  5. Never write "according to equation (X)." Simply use "according to (X)."
  An exception is typically made in the beginning of sentences. Equation (X),
  in this case, is usually acceptable. Still don't do it. Just reword your
  sentence as "In this case, (X) is acceptable."

  **Note**: in certain fields, you are required to write "equation (X)," but I
  do not typically work in those field.

  6. Never start sentences or lines with math symbols, equation numbers, or references.
    If you follow Rule`~`1, then this will never happen without your consent.

  7. If you use a point to indicate an abbreviation and it is not the end of a sentence,
    then follow it by a `\ ` (as in `Dept.\ of Electrical Engineering`). Latex adds
    a bit more space after points because it assumes it is a always period. Doing this
    will avoid some awkward extra space in the middle of your sentence.

  8. Use the `\cite[]{}` to refer to specific sections/theorems, especially when referring
    to specific results from a paper or when citing from books. It is a favor for the reader
    that wants to check the result and good scholarship: unless the statement you just
    made relies on all the results in a paper/book, you should refer only to what is
    directly relevant.

  - Indent!
  - Use `E:`, `T:`, `F:`, `S:`, `X:`, `P:`, `L:`
  - If you are working with me, use my macros!
  - Place environments `begin` and `end` on lines by themselves
  - Leave space before and after binary operations
  - Indent the contents of environments
  - Keep a formula on a single line. If it's too long, break in logical parts and indent
  - Use `\text` in math environments
  - Take advantage of the various math environments: `equation`, `align`, `aligned`, `gather`, `gathered`, `multline`, and starred version
  - Use `\dot`, `\dots`, `\cdot`, `\cdots` accordingly
  - I like `\big`, `\Big`, `\bigg` better than iterated `\left`, `\right`: gives you more control
  - Also, `\bigm` is useful (delimiter with binary spacing)
  - Use `\DeclareMathOperator` rather than `\newcommand` for math
  - Leverage `\quad` and `\qquad`
  - Use the `bm` packed for bold symbols: it looks better
  - Choose a notation and stick with it! (but make sure to review it: sometimes, our convention choices turn out to be less than ideal)
  - For me: fraktur for distributions and measures, caligraphic for sets and spaces, bold lowercase for vectors, bold uppercase for matrices
  - Do `{}+{}` or `{}={}` for binaries on multiline environments
