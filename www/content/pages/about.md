Title: About
Date: 1001-01-01

{% from 'fragments/functions.html' import cite with context %}
{% from 'fragments/functions.html' import youtube %}

# About ([formal bio]({filename}/pages/bio.md))

I am an assistant professor of the center for applied math ([CMAP](https://cmap.ip-paris.fr)) of the
[&Eacute;cole Polytechnique](https://www.polytechnique.edu), France,
broadly interested in optimization, machine learning, signal processing, and control,
and in particular, in the intersections of these fields. Currently, the main drive of my research is
developing the theory, algorithms, and applications of
[**constrained learning**]({filename}/pages/research.md#constrained-learning),
a tool that enables the data-driven design of systems that satisfy requirements
such as robustness {{- cite('Chamon20p', 'Robey21a','Robey22p', 'Chamon23c') }},
fairness {{- cite('Chamon20p', 'Chamon23c') }},
safety {{- cite('Paternain19c', 'Paternain23s', 'Calvo-Fullana24s') }},
smoothness {{- cite('Cervino23l') }},
and invariance {{- cite('Hounie23a') }}.

For more information, you can check out my&nbsp;[**CV**]({static}/pdf/lfochamon_cv.pdf),
read a more [**formal&nbsp;bio**]({filename}/pages/bio.md),
explore my [**research&nbsp;projects**]({filename}/pages/research.md),
or learn more about some of my [**personal&nbsp;interests**]({filename}/pages/about.md#personal-interests).


### My background

I did my Ph.D. at the [University of Pennsylvania](https://www.seas.upenn.edu/)
advised by [Alejandro&nbsp;Ribeiro](https://alelab.seas.upenn.edu/), immediately followed by a postdoc at the
[Simons Institute](https://simons.berkeley.edu/) of the [University of California, Berkeley](https://www.berkeley.edu/). During this time, I developed

- [**near-optimal selection methods**]({filename}/pages/research.md#combinatorial-optimization-and-approximate-submodularity)
  for experimental design {{- cite('Chamon17a') }}, actuator scheduling {{- cite('Chamon22a') }}, and sampling {{- cite('Chamon18g', 'Chamon21a') }};
- the theoretical and algorithmic foundations of
  [**sparse functional programs**]({filename}/pages/research.md#non-convex-functional-optimization), showing that sparsity
  is tractable on the continuum {{- cite('Chamon20f') }} and can be used for
  nonlinear line spectral estimation {{- cite('Chamon20f') }},
  fitting multi-resolution kernel models {{- cite('Peifer20s') }},
  and learn Gaussian Processes from data {{- cite('Chamon19l') }};
- a [**graphon signal processing**]({filename}/pages/research.md#non-convex-functional-optimization)
  framework&nbsp;(in collaboration with [Luana&nbsp;Ruiz](https://sites.google.com/seas.upenn.edu/luanaruiz)) {{- cite('Ruiz21g') }}
  that we used to demonstrate the transferability of **graph neural networks** {{- cite('Ruiz20g', 'Ruiz21t') }};
- a new [**risk-aware estimator**]({filename}/pages/publications.md#Kalogerias20b)&nbsp;(together with
  [Dionysios&nbsp;Kalogerias](https://www.dkalogerias.org/)) that received the
  [*best paper award*](https://2020.ieeeicassp.org/general/icassp-best-paper-awards/) at ICASSP 2020.

After that, I spent two years as the [ELLIS](https://ellis.eu/)&ndash;[SimTech](https://simtech.uni-stuttgart.de/) independent research group leader of the [University of Stuttgart](https://www.uni-stuttgart.de/), Germany.

Prior to moving to the US, I received my bachelor and master degrees in electrical
engineering from the [University of São Paulo](https://www.poli.usp.br), Brazil,
where I am originally from. My masters thesis was on
[**combinations of adaptive filters**]({filename}/pages/research.md#combinations-of-adaptive-filters),
but I also worked on innovative digital design projects&nbsp;(with [David&nbsp;Lamb](https://www.linkedin.com/in/davidlamb99/)),
one of which was [**patented**]({filename}/pages/publications.md#patent) by Analog Devices. As an undergraduate, I studied acoustics
during an exchange at the [École Centrale de Lyon](https://www.ec-lyon.fr) and [INSA-Lyon](https://www.insa-lyon.fr), France.

Before starting my graduate studies, I spent a semester teaching certifying courses
and consulting on nondestructive testing at INSACAST Formation Continue in Lyon, France,
and worked as a signal processing researcher and statistics consultant on a
[project with EMBRAER]({filename}/pages/research.md#aircraft-cabin-simulator).



### Personal interests

In my spare time, I like to write and play music. Mostly the acoustic guitar and the piano, but I sometimes pretend
to play the violin, the flute, and typical Brazilian percussion instruments, such as the zabumba and the triangle.
I used to play the accordion in a *forró* band named [Quaraçá](https://soundcloud.com/luiz-chamon/sets/quaraca), meaning
sun ray or sun light in a Brazilian indigenous language. *Forró* is a folk music genre from the Northeast of Brazil that is
surprisingly widespread worldwide: I've managed to find some underground Forró dance party in almost every city I've lived in.

Back in Brazil, I worked in many recording studios&nbsp;(most small, some even smaller) and was involved in the production of
international theater and art exhibitions, notably Bob Wilson's "Quartett"&nbsp;(with Théâtre de l’Odéon, France) and
Wajdi Mouawad's "The three sisters"&nbsp;(with Théâtre du Trident, Canada). This is actually how I got interested in electrical engineering and
later, signal processing. Amidst the 2020 pandemic, I went back to recording in what served as my bedroom/office/gym/homestudio
and released my first solo EP, *Philathina*, in July&nbsp;2022. You can check it out on my [music&nbsp;website](https://www.lfochamon.com) or
any major music streaming service&nbsp;([Spotify](https://open.spotify.com/album/4dLuLYglloY8fPcuK9uNrU),
[Apple music](https://music.apple.com/gr/album/philatinha-ep/1637179028?uo=4), [Amazon music](https://music.amazon.com/albums/B0B82T289X),
[YouTube](https://www.youtube.com/watch?v=Dr22lwhElvc&list=OLAK5uy_m2dR9NIMG6BTEK_zE9UG3NSIcsLIYOPoc&index=1), [Tidal](http://www.tidal.com/album/240501656)...).

While I don't play live anymore, I've made a few guest appearances on [Tau-zeta's YouTube channel](https://www.youtube.com/@tau-zeta3461),
the first of which singing&nbsp;(if you can call that "singing") one of my favorite Greek songs.

&nbsp;

{{ youtube('3S2Jc6-n4wk') }}

&nbsp;

Besides music, I like learning languages and discovering cultures. I speak a few languages to varying degrees of success,
the latest addition being German with degree unsuccessful. I've also been pretending to speak Greek for a couple of years now.
I don't always pretend very well.

During my Ph.D., I was part of a group of soccer lovers that founded the
[Philadelphia Open Soccer](https://www.philadelphiaopensoccer.org/)&nbsp;(or on
[Facebook](https://www.facebook.com/phillyopensoccer/)), a program that taught soccer to kids in underprivileged
public schools of West Philadelphia and in a
[Northeast Philadelphia](https://www.facebook.com/pg/phillyopensoccer/photos/?tab=album&album_id=1299783973460905) community
composed largely of immigrants and refugees.

Although I don't take soccer as seriously as you'd expect from a Brazilian, I do like watching the *Seleção*&nbsp;(Brazilian national team).
And I understand if right now the thought of mentioning the&nbsp;2014 "7-1" fiasco against Germany crossed your mind.
I'll get back to you on that as soon as your national team also manages to win five World Cups...
