Title: About
Date: 1001-01-01

<style>
/* Tooltip container */
.tooltip {
  position: relative;
  display: inline-block;
}

/* Tooltip text */
.tooltip .tooltiptext {
  visibility: hidden;
  width: 500px;
  background-color: #fff;
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 90%;
  border: solid 1px #ccc;
  /* box-shadow: 1px 1px 2px #0a5daaaa; */
  box-shadow: 0 30px 90px -20px #0a5daa4b;
 
  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 100;
  bottom: 100%;
  left: 50%;
  margin-left: -50px;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>

{% set ns = namespace(refs={}) %}

{% macro cite() -%}
<sup style="font-size: 80%;">[
{%- for tag in varargs %}
  {% if tag not in ns.refs.keys() %}
    {% set _ = ns.refs.update({tag: ns.refs|length + 1}) %}
  {% endif -%}

  <span class="tooltip">
    <a href="{{SITEURL}}/pages/publications.html#{{ tag }}">{{ ns.refs[tag] }}</a>
    {% for publication in publications | selectattr('key', 'eq', tag) %}
      <span class="tooltiptext">{{ publication.text | replace('*','\*') }}</span>
    {% endfor %}
  </span>

  {%- if loop.revindex != 1%},{% endif %}
{% endfor -%}
]</sup>
{%- endmacro %}


{# Click here to skip the boring academic stuff to my boring personal interests #}

# About ([formal bio]({filename}/pages/bio.md))

I am a joint [ELLIS](https://ellis.eu/)&ndash;[SimTech](https://simtech.uni-stuttgart.de/)
independent research group leader at the [University of Stuttgart](https://www.uni-stuttgart.de/), Germany,
broadly interested in optimization, machine learning, signal processing, and control,
and in particular, in the intersections of these fields.

Currently, the main drive of my research is developing the theory, algorithms, and applications of
[**constrained learning**]({filename}/pages/research.md#constrained-learning),
a tool that enables the data-driven design of systems that satisfy requirements
such as robustness {{- cite('Chamon20p', 'Robey21a','Robey22p', 'Chamon22c') }},
fairness {{- cite('Chamon20p', 'Chamon22c') }},
safety {{- cite('Paternain19c', 'Paternain23s', 'Calvo-Fullana21s') }},
smoothness {{- cite('Cervino22l') }},
and invariance {{- cite('Hounie22a') }}.
On the one hand, I investigate fundamental questions such as

- when is it possible to learning under requirements? 
  <span style="color:#999;">(whenever&nbsp;you&nbsp;can&nbsp;learn&nbsp;at&nbsp;all)</span> {{- cite('Chamon20p', 'Chamon22c') }}
- how much harder is it than vanilla learning? 
  <span style="color:#999;">(essentially&nbsp;the&nbsp;same&nbsp;difficulty)</span> {{- cite('Chamon20p', 'Chamon22c') }}
- are there problems that only constrained learning can tackle? 
  <span style="color:#999;">(in&nbsp;short,&nbsp;yes)</span> {{- cite('Calvo-Fullana21s') }}

On the other hand, I am interested in the impact constrained learning can have on traditional
learning tasks, such as
image classification {{- cite('Chamon20p', 'Robey21a','Robey22p', 'Chamon22c', 'Hounie22a') }},
semi-supervised learning {{- cite('Cervino22l') }},
and data-driven control {{- cite('Paternain19c', 'Paternain23s', 'Calvo-Fullana21s') }}.

Most importantly, I think of constrained learning as **a new mindset for the design data-driven solutions**
shifting away from the current objective-centric paradigm towards a constraint-driven one. Part of this work received the
[*best student paper award*](https://2020.ieeeicassp.org/general/icassp-best-paper-awards/)
at ICASSP 2020 ([paper](https://arxiv.org/abs/2002.05183), [video](https://youtu.be/0cl35wNAfiA)).


### My background

I did my Ph.D. at the [University of Pennsylvania](https://www.seas.upenn.edu/)
advised by [Alejandro Ribeiro](https://alelab.seas.upenn.edu/), immediately followed by a postdoc at the
[Simons Institute](https://simons.berkeley.edu/) of the [University of California, Berkeley](https://www.berkeley.edu/).
During this time, I developed

- [**near-optimal selection methods**]({filename}/pages/research.md#combinatorial-optimization-and-approximate-submodularity)
  for experimental design {{- cite('Chamon17a') }}, actuator scheduling {{- cite('Chamon22a') }}, and sampling {{- cite('Chamon18g', 'Chamon21a') }};
- the theoretical and algorithmic foundations of
  [**sparse functional programs**]({filename}/pages/research.md#non-convex-functional-optimization), showing that sparsity
  is tractable on the continuum {{- cite('Chamon20f') }} and can be used for
  nonlinear line spectral estimation {{- cite('Chamon20f') }},
  fitting multiresolution kernel models {{- cite('Peifer20s') }},
  and learn Gaussian Processes from data {{- cite('Chamon19l') }};
- a [**graphon signal processing**]({filename}/pages/research.md#non-convex-functional-optimization) framework
  (in collaboration with [Luana Ruiz](https://sites.google.com/seas.upenn.edu/luanaruiz))
  {{- cite('Ruiz21g') }}
  that we used to demonstrate the transferability of **graph neural networks** {{- cite('Ruiz20g', 'Ruiz21t') }};
- a new [**risk-aware estimator**]({filename}/pages/publications.md#Kalogerias20b)
  (together with [Dionysios Kalogerias](https://www.dkalogerias.org/))
  that received the [*best paper award*](https://2020.ieeeicassp.org/general/icassp-best-paper-awards/) at ICASSP 2020.

Prior to moving to the US, I received my bachelor and master degrees in electrical
engineering from the [University of São Paulo](https://www.poli.usp.br), Brazil,
where I am originally from. My masters thesis was on
[**combinations of adaptive filters**]({filename}/pages/research.md#combinations-of-adaptive-filters),
but I also worked on innovative digital design projects (with [David Lamb](https://www.linkedin.com/in/davidlamb99/)),
one of which was [**patented**]({filename}/pages/publications.md#patent) by Analog Devices. As an undergraduate, I studied acoustics
during an exchange at the [École Centrale de Lyon](https://www.ec-lyon.fr) and [INSA-Lyon](https://www.insa-lyon.fr), France.

Before starting my graduate studies, I spent a semester teaching certifying courses
and consulting on nondestructive testing at INSACAST Formation Continue in Lyon, France,
and worked as a signal processing researcher and statistics consultant on a
[project with EMBRAER]({filename}/pages/research.md#aircraft-cabin-simulator).

For more information, you can check out my [**CV**]({static}/pdf/lfochamon_cv.pdf),
read a more [**formal bio**]({filename}/pages/bio.md),
explore my [**research projects**]({filename}/pages/research.md),
or learn more about some of my [**personal interests**]({filename}/pages/personal.md).



