Title: Research
Date: 1001-01-02


{% from 'fragments/functions.html' import cite with context %}
{% from 'fragments/functions.html' import collapsible_pubs with context %}


<style>
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

.research-icon {
  margin-top: 2rem;
  margin-bottom: 2rem;
}

@media (min-width: 1400px) {
  .research-item {
    display: flex;
    align-items: center;
  }
  .research-icon {
    flex-shrink: 0;
    order: 2;
    margin-left: 2rem;
  }
}
</style>


# Research

My group develops tools that enable intelligent systems to

  * <b>extract</b>,
    <span style="color:#999;font-size:90%;">e.g.,
      sampling {{- cite('Chamon18g')}},
      sensor selection {{- cite('Chamon21a')}},
      experimental design {{- cite('Chamon17a')}}
    </span>
  * <b>process</b>,
    <span style="color:#999;font-size:90%;">e.g.,
      constrained learning {{- cite('Chamon20p', 'Robey21a', 'Robey22p', 'Chamon23c')}},
      network data processing {{- cite('Ruiz20g', 'Ruiz21g')}},
      estimation/inference {{- cite('Chamon20f', 'Peifer20s', 'Kalogerias20b', 'Arzani180')}}
    </span>
  * <b>act</b>,
    <span style="color:#999;font-size:90%;">e.g.,
      resource allocation {{- cite('Eisen19l')}},
      scheduling {{- cite('Chamon22a')}},
      resilient control {{- cite('Chamon20r', 'Chamon20c')}},
      (safe) reinforcement learning {{- cite('Paternain19c', 'Paternain23s')}}</span>

on information.

Currently, the main drive of my research is developing the theory, algorithms, and applications of
[**constrained learning**](#constrained-learning),
a tool that enables the data-driven design of systems that satisfy requirements
such as robustness {{- cite('Chamon20p', 'Robey21a','Robey22p', 'Chamon23c') }},
fairness {{- cite('Chamon20p', 'Chamon23c') }},
safety {{- cite('Paternain19c', 'Paternain23s', 'Calvo-Fullana21s') }},
smoothness {{- cite('Cervino22l') }},
and invariance {{- cite('Hounie22a') }}.
On the one hand, I investigate fundamental questions such as

- when is it possible to learning under requirements? 
  <span style="color:#999;">(whenever&nbsp;you&nbsp;can&nbsp;learn&nbsp;at&nbsp;all)</span> {{- cite('Chamon20p', 'Chamon23c') }}
- how much harder is it than vanilla learning? 
  <span style="color:#999;">(essentially&nbsp;the&nbsp;same&nbsp;difficulty)</span> {{- cite('Chamon20p', 'Chamon23c') }}
- are there problems that only constrained learning can tackle? 
  <span style="color:#999;">(in&nbsp;short,&nbsp;yes)</span> {{- cite('Calvo-Fullana21s') }}

On the other hand, I am interested in the impact constrained learning can have on traditional
learning tasks, such as
image classification {{- cite('Chamon20p', 'Robey21a','Robey22p', 'Chamon23c', 'Hounie22a') }},
semi-supervised learning {{- cite('Cervino22l') }},
and data-driven control {{- cite('Paternain19c', 'Paternain23s', 'Calvo-Fullana21s') }}.
Most importantly, I think of constrained learning as **a new mindset for the design data-driven solutions**
shifting away from the current objective-centric paradigm towards a constraint-driven one.

You can read more about this as well as other current and past projects below. If anything piques your interest,
reach out to me by [email]({filename}/pages/contact.md) or check out the [prospective members]({filename}/pages/prospective.md) page.


### Current projects

- [Constrained learning theory](#constrained-learning-theory)
- [Semi-infinite constrained learning](#semi-infinite-constrained-learning)
- [Non-convex functional optimization and sparsity](#non-convex-functional-optimization)
- [Graph(on) neural networks](#graphon-neural-networks)

### Past projects

- [Combinatorial optimization and approximate submodularity](#combinatorial-optimization-and-approximate-submodularity)
- [Combinations of adaptive filters](#combinations-of-adaptive-filters)
- [Real-sized aircraft cabin simulator](#aircraft-cabin-simulator)

&nbsp;

-----



# Current projects


## Constrained learning theory

<div markdown=1 class="research-item">

![Constrained learning theory icon]({static}/images/research/clt.png)
{: .research-icon}

Constrained learning uses the language of constrained optimization to tackle learning tasks
that involve statistical requirements. Its strength lies in combining the data-driven, model-free nature
of learning with the expressiveness of constrained programming. Doing so, however, also combines the statistical
challenges of the former with the computational complexity of the latter. Hence, it is natural
to wonder if constrained learning is feasible? If solving multiple learning problems simultaneously
does not compound their complexity? These are the type of questions that concern **constrained learning theory**.
We now know that constrained learning can solve problems that unconstrained learning cannot while often being
essentially as hard. In fact, it is usually possible to learn under constraints by solving only of unconstrained
problems. These results have already enabled many applications and opened up new theoretical questions on
the limits of this new learning task.

</div>

<!-- So far, we know that, in typical cases, constrained learning is possible whenever unconstrained
learning is possible&nbsp;(*uniform convergence implies both PAC learnability and PAC constrained learnability*)
and that they have essentially the same sample complexity&nbsp;(*up to a log factor*)
{{- cite('Chamon20p', 'Chamon23c') }}. In fact, constrained learning tasks can be tackled by
solving only unconstrained learning problems&nbsp;(*using classical dual ascent techniques*).
What is more, we know that constrained learning is strictly more expressive than its unconstrained
counterpart, since there exists reinforcement learning tasks that can only be solved using constrained
reinforcement learning (*no fixed reward can lead to the desired behavior*) {{- cite('Calvo-Fullana21s') }}.

These results have enabled
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
[RCPRH NeurIPS'21]({filename}/pages/publications.md#Robey21a)]. -->


{{ collapsible_pubs(('Chamon23c', 'Robey21a', 'Chamon20ta', 'Chamon20p', 'Eisen19l', 'Paternain19c', 'Paternain23s', 'Robey22p')) }}

&nbsp;

&nbsp;



## Semi-infinite constrained learning

<div markdown=1 class="research-item">

![Semi-infinite constrained learning icon]({static}/images/research/sicl.png)
{: .research-icon}

Statistical requirements lie in a spectrum between *in&nbsp;expectation* and *almost&nbsp;surely*.
On the former end, learning is performed using empirical averages over the available data.
This is the case, for example, in wireless resource allocation, safe reinforcement learning,
and certain definitions of fairness. **Semi-infinite constrained learning** is primarily concerned
with problems on the other end of the spectrum, e.g., those involving min-max properties such as
robustness and invariance. For these almost sure requirements to hold, however, an infinite number
of constraints must be satisfied for each data point. Combining duality and hybrid
stochastic&nbsp;optimization&ndash;MCMC&nbsp;sampling algorithms yield a new approach to tackle to
these seemingly intractable problems. These developments have lead to new theoretical questions and
applications, such as smooth learning and probabilistic robustness, a property that lies strictly in the
interior of the expectation&ndash;almost&nbsp;sure spectrum.

</div>

<!-- model-free wireless resource allocation
[[EZCLR IEEE TSP'19]({filename}/pages/publications.md#Eisen19l)],
safe reinforcement learning
[[PCCR NeurIPS'19]({filename}/pages/publications.md#Paternain19c);
[PCCR IEEE TAC'23]({filename}/pages/publications.md#Paternain23s)],
fair classification
[[CPCR ICASSP'20]({filename}/pages/publications.md#Chamon20ta);
[CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p)],
and robust learning
[[CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p);
[RCPRH NeurIPS'21]({filename}/pages/publications.md#Robey21a)]. -->


{{ collapsible_pubs(('Robey21a', 'Robey22p', 'Chamon20ta')) }}

&nbsp;

&nbsp;



## Non-convex functional optimization

<div markdown=1 class="research-item">

![Non-convex functional optimization icon]({static}/images/research/ncfo.png)
{: .research-icon}

Until 60 years ago, the tractability boundary in optimization separated *linear* from *nonlinear* programs.
Advances in convex analysis and barrier methods have since made it common place to hear *convex* used
as a synonym for *tractable* and *non-convex* as a synonym for *intractable*. Reality is naturally more subtle.
In fact, there are both computationally challenging *convex* programs&mdash;e.g., large-scale semi-definite
programming&mdash;and tractable *non-convex* ones&mdash;e.g., low-rank approximation. I am particularly
interested in a case of the latter that arises from the observation that
**problems known to be intractable in finite dimensions often become tractable in infinite dimensions**.
This means, for instance, that sparse regression is NP-hard in finite dimensions whereas its functional form is tractable.
This observation precludes the use of convex relaxations to tackle *off-the-grid compressive sensing* problems
and makes it possible to fit complex nonlinear models&nbsp;(from multi-resolution kernels to GPs), giving rise to new
statistical questions. It is also instrumental in the development of [constrained learning](#constrained-learning-theory).

</div>


<!-- This is due to the fact that, under mild conditions, non-convex functional optimization manifests
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
their impact in other areas, e.g., [learning](#constrained-learning). -->

{{ collapsible_pubs(('Chamon20f', 'Peifer20s', 'Chamon19l')) }}


&nbsp;

&nbsp;



## Graph(on) neural networks

<div markdown=1 class="research-item">

![Graph/Graphon neural networks icon]({static}/images/research/gnn.png)
{: .research-icon}

Massive amounts of data in our increasingly interconnected world only make sense in
the context of the networks from which they arise, be them social networks, power grids,
IoT devices, or industry&nbsp;4.0. Graph signal processing&nbsp;(GSP) and graph neural networks&nbsp;(GNNs)
grew out of the need to extract information from those network&nbsp;(graph) signals. These techniques,
however, are difficult to scale, hindering their use for large networks that can only be partially
observed or in non-stationary, dynamic settings. Yet, it seems reasonable that if two graphs are
"similar", then their graph Fourier transforms, graph filters, and GNNs should also be similar.
Formalizing this intuition is one of the motivations for developing the theory of
**graphon signal processing**. In fact, it has been used to show that GNNs are transferable
between graphs, i.e., that they can be trained on subgraphs to then be deployed on the full
network. These results raise fundamental questions on the limits of this transferability
as well as to what is the right graph similarity metric to characterize it.

</div>

<!-- Therefore, by showing that **graph signal
processing converges to graphon signal processing** as the underlying graphs grow
[[RCR IEEE TSP'21]({filename}/pages/publications.md#Ruiz21g)],
we have developed a formal tool to analyze graph signals that relies on the
more amenable compact operator theory rather than matrix theory. 

1. large graphs obtained from the same graphon have similar graph Fourier transforms
[[RCR IEEE TSP'21]({filename}/pages/publications.md#Ruiz21g)]
2. graph filters from large graphs of the same graphon family have similar outputs
[[RCR IEEE TSP'21]({filename}/pages/publications.md#Ruiz21g)]
3. graph neural network trained on a smaller graph transfer to larger ones
[[RCR NeurIPS'20]({filename}/pages/publications.md#Ruiz20g),
[RCR arXiv'21]({filename}/pages/publications.md#Ruiz21t)] -->


{{ collapsible_pubs(('Ruiz20g', 'Ruiz21g', 'Ruiz20t', 'Ruiz20ga', 'Ruiz21t')) }}



&nbsp;

-----


# Past projects

## Combinatorial optimization and approximate submodularity

<div markdown=1 class="research-item">

![Combinatorial optimization and approximate submodularity icon]({static}/images/research/coaas.png)
{: .research-icon}

When the scale of the underlying system and/or technological constraints such as computation,
power, and communication, limit our capabilities, we are forced to choose a subset of the
available resources to use. These might be sensors for state estimation,
actuators for control, pixels for face recognition, or movie ratings to kick-start a
recommender systems. These selection problems are notoriously hard&nbsp;(often NP-hard in fact),
so that the best we can expect is to find an approximate solution. Greedy search is widely used in
this context due to its simplicity, iterative nature, and the fact that it is near-optimal
when the objective has a "diminishing&nbsp;returns" property known as *submodularity*. Yet, despite 
the empirical evidence for its effectiveness in the above problems, **none of them are *submodular*.**
In fact, quadratic costs generally only display "diminishing returns" under stringent conditions.
What this research has shown is that while the MSE and the LQR objective are not submodular,
they are not far from it, enjoying similar near-optimal properties. While many notions of
approximate submodularity had been investigated before, these were the first computable,
*a priori* guarantees for these problems, precluding the use of submodular surrogates&nbsp;(e.g., logdet) or
convex relaxations.

</div>


<!-- These results have
had implications for the sampling of graph signals
[[CR GlobaSiP'16]({filename}/pages/publications.md#Chamon16n);
[CR IEEE TSP'18]({filename}/pages/publications.md#Chamon18g)],
A- and E-optimal experimental design
[[CR NeurIPS'17]({filename}/pages/publications.md#Chamon17a)],
sensor selection for Kalman filtering
[[CPR IEEE TAC'21]({filename}/pages/publications.md#Chamon21a)],
and control scheduling (subject to matroid constraints)
[[CAR IEEE TAC'22]({filename}/pages/publications.md#Chamon22a)]. -->


{{ collapsible_pubs(('Chamon22a', 'Chamon21a', 'Chamon19m', 'Chamon18g', 'Chamon17a', 'Chamon16n')) }}


&nbsp;

&nbsp;




## Combinations of adaptive filters

<div markdown=1 class="research-item">

![Combinations of adaptive filters icon]({static}/images/research/caf.png)
{: .research-icon}

As most stochastic optimization algorithms, adaptive filters suffer from trade-offs
that can hinder their use in practice. Larger step sizes, for example, lead to faster
convergence and better tracking, but also worse steady-state errors. Combinations of
adaptive filters were proposed to address such compromises by mixing the output of a
fast filter with that of an accurate one and adjusting that mixture depending on which
filter is performing best. How these outputs are combined has a large influence in the
resulting performance, so this research program set out to determine
**what is the best way to combine adaptive filters.** To do so, it developed an
algebra to describe combinations of adaptive filters using message passing graphs
and used it to design and analyze a myriad of combination topologies tackling a
diversity of new applications. In one instance, a combination of simple adaptive
filters was used to **reduce the complexity of adaptive algorithms** by
outperforming complex, Newton-type adaptive methods at roughly 30 times
lower computational complexity.

<!-- My work proposed a myriad of new combination topologies that can
be used to address this and other issues, including cyclic coefficients feedback
[[CLL ICASSP'12]({filename}/pages/publications.md#Chamon12c);
[CL arXiv'16]({filename}/pages/publications.md#Chamon16c)],
incremental combinations
[[CL EUSIPCO'13]({filename}/pages/publications.md#Chamon13t)].
data-reusing combinations
[[CFL Asilomar'12]({filename}/pages/publications.md#Chamon12a)],
and their composition
[[CL SBrT'13]({filename}/pages/publications.md#Chamon13o);
[CL ICASSP'14]({filename}/pages/publications.md#Chamon14t)]. -->

</div>


{{ collapsible_pubs(('Chamon16c', 'Chamon14t', 'Chamon13t', 'Chamon12a', 'Chamon12c')) }}


&nbsp;

&nbsp;




## Aircraft cabin simulator

![Figure 1]({static}/images/research/sarava_luz.jpg)

Air passenger traffic has grown enormously in the last few decades. This increase in competition
has made aircraft carriers and manufacturers aware of the need to find new ways to attract
customers, inevitably turning to the comfort factor. Although studies on automotive comfort are
abundant, those on aircraft environments are scarce, partly due to the difficulties in running
experiments (costs, risks...). In order to address these issues, a real-sized aircraft cabin
simulator capable of controlling variables such as sound, vibration, temperature, air flow,
pressure, and lighting, was built at the University of São Paulo in collaboration with EMBRAER.

I co-designed and built the vibro-acoustic reproduction system, composed of more than
20&nbsp;loudspeakers and 30&nbsp;shakers. Using new MIMO equalization methods {{- cite('Chamon11a') }},
we were able to precisely simulate the noise patterns of dozens of aircraft, including take-off
and landing. From the control room, it is possible to monitor the environment inside the simulator
using microphones and accelerometers installed on each seat. After half a decade of work,
this project culminated in more than 60&nbsp;simulated flights involved over 1000&nbsp;people.
I was responsible for the statistical analysis of the results to understand the interplay
between variables and passenger comfort. This simulator is still being used in collaborations
between the University of São&nbsp;Paulo and aeronautic industries.


{{ collapsible_pubs(('Bittencourt12p', 'Chamon11a', 'Chamon10t')) }}


&nbsp;

![Figure 2]({static}/images/research/sarava_mics.png)



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
