Title: Research
Date: 1001-01-02


{% macro collapsible_pubs(key_list) -%}
<div class="collapsible">
<button type="button">Selected publications</button>
<div class="collapsible-content">

<ul class="pubs_list">
    {% for publication in publications | sort(True, attribute='year') | selectattr('key', 'in', key_list) %}
      <li>
        {{ publication.text }}
        {% if publication.award %}
          <strong>({{ publication.award }})</strong>
        {% endif %}
      <br />
      {% for label, target in [('PDF', publication.pdf), ('arXiv', publication.arxiv), ('YouTube', publication.video), ('Slides', publication.slides), ('Poster', publication.poster), ('Link', publication.url)] %}
        {{ "[&nbsp;<a href=\"%s\">%s</a>&nbsp;]" % (target, label) if target }}
      {% endfor %}
      </li>
    {% endfor %}
</ul>

</div>
</div>
{%- endmacro %}



<style>
  .pics {
    display: block;
  }
  .pics div {
    display:block;
    margin-right:0;
    max-width:100%;
  }

@media (min-width: 38em) {
  .pics {
    display: flex;
    flex-flow: row;
  }
  .pics div {
    display:block;
    margin-right:1rem;
    max-width:49%;
  }
}

/* Style the button that is used to open and close the collapsible content */
.collapsible button {
  background-color: #555;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.collapsible p {
  margin: 0;
}

/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
.active button, .collapsible:hover button {
  background-color: #0a3050;
}

/* Style the collapsible content. Note: hidden by default */
.collapsible-content {
  padding-right: 1rem;
  padding-top: 1rem;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}

.pubs_list{
  padding: 0 30px;
  font-size: 16px;
  list-style-type: none;
}

.pubs_list li{
  margin: 0 0 15px 0;
}
</style>


# Research

### Current projects

- [Constrained learning](#constrained-learning)
- [Non-convex functional optimization and sparsity](#non-convex-functional-optimization)
- [Graph(on) neural networks](#graphon-neural-networks)

### Past projects

- [Combinatorial optimization and approximate submodularity](#combinatorial-optimization-and-approximate-submodularity)
- [Combinations of adaptive filters](#combinations-of-adaptive-filters)
- [Real-sized aircraft cabin simulator](#aircraft-cabin-simulator)

&nbsp;

-----



# Current projects


## Constrained learning

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/csl_1.png)</div>
<div markdown="1">![Figure 2]({static}/images/research/csl_2.png)</div>
</div>

Learning has the power to automate the engineering of complex systems, allowing us to go from data to operation
with little to no human intervention. But learning today does not organically incorporate requirements,
despite their central role in engineering. This has led to data-driven solutions that are biased, prejudiced,
and prone to tampering and unsafe behaviors. Ultimately, this is due to our
inability to specify fairness, robustness, and safety requirements. I contend
that we can no longer expect learning to bring about *trustworthy systems* by improving
existing methods. We must *advance beyond the current paradigm of minimizing costs and develop learning methods capable of satisfying requirements*.
The goal of this research project is to realize this **autonomous system engineering vision
by developing the theory and practice of learning under requirements**.

My first step involved the development of a **formal theory of constrained learning**.
In doing so, I showed that, despite being strikingly different problems,
constrained learning is as hard as unconstrained learning in the sense that any
PAC learnable class is also PAC constrained learnable. In fact, under mild conditions,
constrained learning can be tackled using dual learning which involves solving only
unconstrained learning tasks
[[CPCR ICASSP'20]({filename}/pages/publications.md#Chamon20ta) (*best student paper award*);
[CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p);
[CPCR IEEE TIT'22]({filename}/pages/publications.md#Chamon22c)].
These results show that, unbeknown to us, our ability to solve unconstrained learning tasks
also allows us to solve constrained learning ones. They have enabled
model-free wireless resource allocation
[[EZCLR IEEE TSP'19]({filename}/pages/publications.md#Eisen19l)],
safe reinforcement learning
[[PCCR NeurIPS'19]({filename}/pages/publications.md#Paternain19c);
[PCCR IEEE TAC'23]({filename}/pages/publications.md#Paternain23s)],
fair classification
[[CPCR ICASSP'20]({filename}/pages/publications.md#Chamon20ta);
[CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p)],
and robust learning
[[CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p);
[RCPRH NeurIPS'21]({filename}/pages/publications.md#Robey21a)].


{{ collapsible_pubs(('Chamon22c', 'Robey21a', 'Chamon20ta', 'Chamon20p', 'Eisen19l', 'Paternain19c', 'Paternain23s')) }}

&nbsp;

&nbsp;





## Non-convex functional optimization

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/sfp_1.png)</div>
<div markdown="1">![Figure 2]({static}/images/research/sfp_2.png)</div>
</div>


Up until 60 years ago, the boundary between tractable and intractable in optimization
separated *linear* and *nonlinear* programs. Later, advances in convex analysis and barrier methods
would push this boundary to separate *convex* from *non-convex* programming. It is not uncommon
nowadays to hear the word *convex* used as a synonym for *tractable* and *non-convex*
as a synonym for *intractable*. Naturally, reality is more subtle than this black-and-white picture.
Many *non-convex programs* are tractable&mdash;e.g., low-rank approximation&mdash;while many *convex programs*
can be quite challenging&mdash;e.g., large-scale semi-definite programming. But the fact remains that, from a complexity
theory perspective, convex optimization is worst-case *easier* than non-convex optimization.

While studying continuous compressing sensing problems, I discovered what
is another fundamental tractability frontier: (uncountably) infinite dimensionality.
Indeed, **problems that are known to be intractable in finite dimensions often become tractable in infinite dimensions**.
Take sparse regression, for example. While it has been proven to be NP-hard in finite dimensions,
its functional counterpart can be tackled using duality. In fact, the same is true for nonlinear models.
This is due to the fact that, under mild conditions, non-convex functional optimization manifests
the same duality properties as convex optimization [[CER IEEE TSP'20]({filename}/pages/publications.md#Chamon20f)].
These advances imply that we need not resort to atomic norm relaxations
to tackle many *off-the-grid compressive sensing* problems
[[CER ICASSP'18]({filename}/pages/publications.md#Chamon18s);
[CER ICASSP'19]({filename}/pages/publications.md#Chamon19s);
[CER IEEE TSP'20]({filename}/pages/publications.md#Chamon20f)].
I have also used these results to develop multiresolution kernel methods
able to fit functions with heterogeneous degrees of smoothness
[[PCPR IEEE TSP'20]({filename}/pages/publications.md#Peifer20s)]
and learn hierarchical Gaussian Processes by replacing Bayes rule by empirical risk minimization
[[CPR Asilomar'19]({filename}/pages/publications.md#Chamon19l)].
I continue to explore the impact of these contributions on how we process and interact
with the continuous nature real world signals beyond classical sampling as well as
their impact in other areas, e.g., [learning](#constrained-learning).

{{ collapsible_pubs(('Chamon20f', 'Peifer20s', 'Chamon19l')) }}


&nbsp;

&nbsp;



## Graph(on) neural networks

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/graphon_1.png)</div>
<div markdown="1">![Figure 2]({static}/images/research/graphon_2.png)</div>
</div>

We live in an increasingly interconnected world where network data is becoming pervasive.
Social networks, power grids, Internet-of-Things, industry 4.0, all provide massive
amounts of data that only make sense in the context of the networks giving rise
to them. Graph signal processing (GSP) grew out of a need to extract information from these
network (graph) signals. Its techniques, however, do not scale well to graphs with a
large number of nodes, which also limits its use in the context of non-stationary, dynamic
networks. Even acquiring the full graph can be challenging in these situations.
However, it is reasonable to expect that if two graphs are similar, then their
graph Fourier transforms, graph filters, and graph neural networks would also be similar.
In particular, we are interested in questions such as

1. when are the graph Fourier transforms of graphs similar?
2. are the outputs of graph filters similar for graph from the same family?
3. does a graph neural network trained based on a small graph transfer to larger graphs?

[Luana Ruiz](https://www.seas.upenn.edu/~rubruiz/) and I provide answers to these
questions by developing the theory of **graphon signal processing**. *Graphons* are
limits of certain sequences of graphs. In many ways, they are *continuous* counterparts
of graphs. Graphons also define families of "similar" graphs, namely,
those graphs that converge to the same graphon. In that sense, graphons can be interpreted
as *continuous* stochastic block models. Therefore, by showing that **graph signal
processing converges to graphon signal processing** as the underlying graphs grow
[[RCR IEEE TSP'21]({filename}/pages/publications.md#Ruiz21g)],
we have developed a formal tool to analyze graph signals that relies on the
more amenable compact operator theory rather than matrix theory. In particular,
we have shown that

1. large graphs obtained from the same graphon have similar graph Fourier transforms
[[RCR IEEE TSP'21]({filename}/pages/publications.md#Ruiz21g)]
2. graph filters from large graphs of the same graphon family have similar outputs
[[RCR IEEE TSP'21]({filename}/pages/publications.md#Ruiz21g)]
3. graph neural network trained on a smaller graph transfer to larger ones
[[RCR NeurIPS'20]({filename}/pages/publications.md#Ruiz20g),
[RCR arXiv'21]({filename}/pages/publications.md#Ruiz21t)]


{{ collapsible_pubs(('Ruiz20g', 'Ruiz21g', 'Ruiz20t', 'Ruiz20ga', 'Ruiz21t')) }}



&nbsp;

-----


# Past projects

## Combinatorial optimization and approximate submodularity

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/alpha_1.png)</div>
<div markdown="1">![Figure 2]({static}/images/research/alpha_2.png)</div>
</div>

When the scale of underlying systems and/or technological constraints
such as computation, power, and communication, limit our capabilities, we are forced
to choose a subset of the available resources over which to operate. This leads to
questions such as

* which sensors should we use for state estimation (Kalman filtering)? (**estimation**)
* where and when should we actuate to regulate a dynamical system (LQG)? (**control**)
* which pixels do we really need to do face recognition (using, e.g., kernel PCA)? (**sampling**)
* which movie ratings should we obtain to start giving out good recommendations? (**experimental design**)

Due to budget or operational constraints, these selection problems are notoriously hard
(often NP-hard, in fact). So in most practical cases, the best we can do is find an
approximate solution. Greedy search is widely used in this context due to its simplicity
and iterative nature. What is more, if the objective we are optimizing
has a "diminishing returns" property known as *submodularity*, greedy search is near-optimal.
In fact, we cannot hope to do better. It should therefore be no surprise that greedy
algorithms often lead to good results in practice.

However, **none of the problems I mentioned above are *submodular*.** In fact,
quadratic costs in general only display "diminishing returns" under stringent
conditions. It is therefore not uncommon for submodular surrogates (e.g., logdet) and
convex relaxations to be used instead. Still, the **empirical effectiveness of greedy algorithms**
has been observed in these scenarios for decades. I resolved this paradox by showing
that while the MSE and the LQR objective are not submodular, they are not far from it.
In most cases of practical interest, they can in fact be treated as such. To do so,
I leveraged spectral matrix theory to bound the diminishing returns violations of these
functions and derived near-optimality certificates for their greedy optimization.
While notions of approximate submodularity had been investigated before, these were
the first computable, *a priori* guarantees for these problems. These results have
had implications for the sampling of graph signals
[[CR GlobaSiP'16]({filename}/pages/publications.md#Chamon16n);
[CR IEEE TSP'18]({filename}/pages/publications.md#Chamon18g)],
A- and E-optimal experimental design
[[CR NeurIPS'17]({filename}/pages/publications.md#Chamon17a)],
sensor selection for Kalman filtering
[[CPR IEEE TAC'21]({filename}/pages/publications.md#Chamon21a)],
and control scheduling (subject to matroid constraints)
[[CAR IEEE TAC'22]({filename}/pages/publications.md#Chamon22a)].


{{ collapsible_pubs(('Chamon22a', 'Chamon21a', 'Chamon19m', 'Chamon18g', 'Chamon17a', 'Chamon16n')) }}


&nbsp;

&nbsp;




## Combinations of adaptive filters

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/af_1.svg)</div>
<div markdown="1">![Figure 2]({static}/images/research/af_2.svg)</div>
</div>

Adaptive filters, as most stochastic optimization algorithms, suffer from trade-offs
that can hinder their use in practice. A classical example is convergence rate or
tracking performance vs.\ steady-state error: larger step sizes lead to faster
convergence and better tracking filters, but also to larger steady-state error
in stationary scenarios. Combinations of adaptive filters can addresses these issue
by mixing, for instance, the output of a fast filter with that of an accurate one.
A supervisor is then responsible for deciding which output to use depending on which filter
is doing better at each point in time.

Still, there are many different way in which the output of adaptive filters could be
mixed. So this project set out to answer the basic question of
**what is the best way to combine adaptive filters?** Before this, adaptive filters
were combined *in parallel* by running the filters independently then mixing their
outputs. This, however, leads the output error to plateau while the slow filter
catches up to the fast one. Only then does the error start to decrease again.
My work proposed a myriad of new combination topologies that can
be used to address this and other issues, including cyclic coefficients feedback
[[CLL ICASSP'12]({filename}/pages/publications.md#Chamon12c);
[CL arXiv'16]({filename}/pages/publications.md#Chamon16c)],
incremental combinations
[[CL EUSIPCO'13]({filename}/pages/publications.md#Chamon13t)].
data-reusing combinations
[[CFL Asilomar'12]({filename}/pages/publications.md#Chamon12a)],
and their composition
[[CL SBrT'13]({filename}/pages/publications.md#Chamon13o);
[CL ICASSP'14]({filename}/pages/publications.md#Chamon14t)].
In doing so, I also created an algebra for describing combinations of adaptive filters,
reducing them to message passing graphs such as those in the first figure above.

An unexpected consequence of these new topologies is the ability to use combinations
to **reduce the complexity of adaptive algorithms**. Consider the APA, for example.
This filer is commonly used to deal with the fact that correlated inputs considerably
slow down adaptive algorithms such as the LMS filter. But if you look at the bubble
in the lower corner first figure (the area is proportional to the complexity), you will see that
you can easily fit two dozens LMS filters in each APA iteration. You'll also notice
a bubble for a combination of sign-error LMS filters that has essentially the same complexity of
an LMS filter, but the performance of the APA [[CL ICASSP'14]({filename}/pages/publications.md#Chamon14t)].
Using a properly designed topology, **we can therefore go from an adaptive filter that involves
a matrix inversion to one based essentially on bit shifts with no performance loss.**


{{ collapsible_pubs(('Chamon16c', 'Chamon14t', 'Chamon13t', 'Chamon12a', 'Chamon12c')) }}


&nbsp;

&nbsp;




## Aircraft cabin simulator

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/sarava_luz.jpg)</div>
<div markdown="1">![Figure 2]({static}/images/research/sarava_mics.png)</div>
</div>

The drop in airfares has made air passenger traffic grow fast in the last few decades. This
increase in competition has made aircraft carriers and manufacturers aware of the need to
find new ways to attract customers, inevitably turning to the comfort factor. Although
studies on automotive comfort are abundant, those on aircraft environments are still scarce,
partly due to the difficulties in running experiments (costs, risks...). In order to address these issues,
a real-sized aircraft cabin simulator capable of controlling variables such as sound, vibration,
temperature, air flow, pressure, and lighting, was built at the University of São Paulo
in collaboration with EMBRAER.

I co-designed and built the vibro-acoustic reproduction system, composed of more
than 20&nbsp;loudspeakers and 30&nbsp;shakers. Using new MIMO equalization methods I developed
[[CQBN ICSV'18]({filename}/pages/publications.md#Chamon11a)],
we were able to precisely simulate the noise patterns of dozens of aircrafts, including
take-off and landing. From the control room, we could monitor the environment inside
the simulator using microphones and accelerometers installed on each seat. After half a decade
of work, the project culminated in more than 60&nbsp;simulated flights with over 1000&nbsp;people.
I was also responsible for the statistical analysis of the results to understand the interplay
between variables and passenger comfort. The simulator is still used in collaborations
between the University of São Paulo and aeronautic industries.


{{ collapsible_pubs(('Bittencourt12p', 'Chamon11a', 'Chamon10t')) }}


&nbsp;

<div class="pics" markdown="1">
<div markdown="1">![Figure 1]({static}/images/research/sarava_speaker.jpg)</div>
<div markdown="1">![Figure 2]({static}/images/research/sarava_plots.svg)</div>
</div>



<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.getElementsByClassName("collapsible-content")[0];
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>
