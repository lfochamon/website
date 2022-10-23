title: Test post 1
date: 2011-12-03 10:20
tags: pelican, publishing
status: draft

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed luctus, justo sed rhoncus mattis, lorem erat ornare sem, sit amet egestas magna leo ut nibh. Integer eu condimentum orci. Aenean quis convallis quam. In magna est, maximus in libero ornare, molestie maximus leo. Aliquam porttitor, nisi tincidunt rutrum lobortis, ligula tellus tincidunt lectus, a tempor lacus tellus sed quam. Aliquam a imperdiet nibh. Nunc pharetra dui sit amet ex tristique eleifend. Integer at tempus felis. Nunc metus orci, ultrices ut viverra nec, ultrices vitae lectus. Nunc lobortis mauris tempus, euismod sem a, bibendum lectus. Mauris ornare non tortor sit amet molestie.

$$x^2$$

Integer $\log(x)$ quis quam vitae est semper fermentum sed et tellus. Aenean eget tempor leo. Nam pharetra ullamcorper convallis. Fusce luctus, ante ac vestibulum congue, ex est lobortis massa, quis vehicula massa urna vel erat. Maecenas ac accumsan risus. Ut molestie ante nec quam maximus, id condimentum metus varius. Vestibulum est nisi, porttitor non mi faucibus, fringilla vestibulum diam.

$$
  x^3
$$

\begin{equation}\label{E:test}
  \sin(x)^3
\end{equation}

\begin{align}
  y &= \sin(x)^3
  \\
  z &= \cos(x)^{10}
\end{align}

$\eqref{E:test}$ Proin bibendum urna vitae purus bibendum hendrerit. Sed faucibus sit amet ex in eleifend. Duis pellentesque suscipit metus faucibus scelerisque. Vivamus consequat turpis at eros consequat, maximus dapibus enim accumsan. Donec quis justo quis lacus pretium iaculis ut vitae nibh. Pellentesque tempus est sed nisl ultricies varius. Ut sed fermentum magna. Suspendisse purus sapien, sollicitudin sed `code` maximus sed, feugiat sed orci. Sed sit amet nibh sollicitudin, venenatis justo ut, efficitur felis. Phasellus dignissim ligula in mi gravida condimentum.

    :::python hl_lines="4 7"
    from typing import Iterator

    # This is an example
    class Math:
        @staticmethod
        def fib(n: int) -> Iterator[int]:
            """ Fibonacci series up to n """
            a, b = 0, 1
            while a < n:
                yield a
                a, b = b, a + b

    result = sum(Math.fib(42))
    print("The answer is {}".format(result))
