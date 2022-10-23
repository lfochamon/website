Title: Application package
URL: applications/index.html
status: hidden
save_as: applications/index.html
template: applications


# Recent talks
<div style="float:left; margin-right:1rem;" markdown="1">
  <iframe width="280" height="160" src="https://www.youtube.com/embed/0cl35wNAfiA" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <br />
  <center>IEEE ICASSP 2020  
  **(best student paper award)**</center>
  <br />
</div>
<div style="float:left; margin-right:1rem;" markdown="1">
  <iframe width="280" height="160" src="https://www.youtube.com/embed/9e-n8lPu5S8" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <br />
  <center>IEEE CDC 2020</center>
  <br />
</div>
<div style="clear:both;"></div>
<div style="float:left; margin-right:1rem;" markdown="1">
  <iframe width="280" height="160" src="https://www.youtube.com/embed/YOo19MLVimA" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <br />
  <center>Deep Learning Theory Symposium  
  (Simons Institute, Dec. 2021)</center>
  <br />
</div>

<div style="clear:both;"></div>

&nbsp;

&nbsp;


<h1 id="research">Research<br /><div style='font-size:1.5rem;'>Learning under requirements</div></h1>

[**Research statement**]({static}/pdf/lfochamon_research.pdf)

## An animated overview

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src="https://www.youtube.com/embed/thIbfzqMX1w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## Why requirements?

![The power of learning under requirements]({static}/images/engineering_learning_requirements.svg)

Learning has the power to automate the design of complex systems and allow us to go from data to operation
with little to no human intervention. But despite their central role in engineering, learning today does not
incorporate requirements organically. This has led to data-driven solutions that are biased, prejudiced,
and prone to tampering and unsafe behaviors. Ultimately, this is due to our inability to specify
fairness, robustness, and safety requirements.

I contend that we can no longer expect learning to bring about trustworthy systems by improving existing methods.
We must advance beyond the current paradigm of minimizing costs and develop learning methods capable of satisfying requirements.

**My goal is to realize this *autonomous system engineering* vision by developing the theory and practice of *learning under requirements*.**


## Requirements as ends and means

On the one hand, **my research treats requirements as goals.** It uses tools
from optimization and learning theory to determine *when* and *how* systems
can learn to satisfy requirements. In other words, it develops tools to

- impose *demographic parity* and obtain fair models
- require *invariance* or *insensitivity* to disturbances and obtain robust systems
- avoid *dangerous behaviors* to obtain safe control policies


On the other hand, **my research treats requirements as means** and uses them to
formulate solutions to practical problems, such as

- selecting the protected groups in fairness
- trading off nominal and adversarial performance or fit and complexity
- surviving and recovering from catastrophic failures


Ultimately, I seek to shift from the current, objective-centric learning
paradigm to a **constraint-driven learning** one that enables systems to
learn both *under* requirements and *from* their requirements. This
synergistic exploitation of constraints showcases the potential of
constrained learning to be the driving force behind **autonomy**.


## Can we not already do this?

Unfortunately, no. As in classical learning, learning under requirements can be
formulated as an optimization program, albeit one with constraints. But while this
distinction may appear innocuous, we know from optimization theory
that constraints are a major source of complexity. Even linear
regression, the most benign of problems, can be made NP-hard with a
single sparsity constraint. These issues are only amplified by the
lack of convexity of modern learning problems.

The path between learning and critical, trustworthy systems is therefore obstructed
by questions that our current learning theory cannot address. These questions are
the basis for the concrete directions of my research:

<ul style="list-style-type: none;"  markdown="span">
  <li markdown="1">
    **Direction A.** *When* is it possible to learn *under* requirements?
    <input type="checkbox" id="expand-A" class="check-with-label" />
    <div class="smalldesc" markdown="block">

    <p>**Constrained (reinforcement) learning.** The goal of this direction
    is to study *when learning under requirements is possible*. More
    specifically, I am interested in characterizing the effect of sample
    size on feasibility. This requires pushing constrained learning
    [[CPCR ICASSP'20]({filename}/pages/publications.md#Chamon20ta) *(best student paper award)*;
    [CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p)]
    theory to new learning models&mdash;e.g., structured
    complexity and PAC-Bayes&mdash;and tasks&mdash;e.g., reinforcement learning
    [[PCCR NeurIPS'19]({filename}/pages/publications.md#Paternain19c);
    [PCCR ArXiv'19]({filename}/pages/publications.md#Paternain19s)]
    and non-convex losses. The latter is especially
    important to tackle rate-constrained problems that arise, e.g., in
    fairness.</p>

    <p>These advances provide a unique perspective for studying *when*
    requirements such as fairness or invariance are achievable without
    unnecessary performance harm by leveraging the duality between
    constrained optimization and Pareto optimality. I will exploit these
    results to develop a statistical analysis of the Pareto frontier to
    study how compromises between, e.g., performance, fairness, and
    robustness, arise when models are trained from data. This duality also
    relates constrained and minimax problems, allowing the theory developed
    in this direction to shed light on *when* minimax learning is viable.
    This has implications on the learning complexity of robustness, model
    auditing, and adversarial training&mdash;e.g., generative adversarial
    networks (GANs). Nevertheless, there are fundamental roadblocks to using
    duality in non-convex settings that I will address using non-convex
    variational results [[CER IEEE TSP'20]({filename}/pages/publications.md#Chamon20f)]
    rather than resorting to randomized
    solutions (mixed Nash equilibria). Additionally, it is not immediate
    that feasible, *deterministic* models/policies (primal solutions) can be
    recovered from minimax (dual) solutions even in the convex case.
    Preliminary results suggest that feasible policies can be obtained in
    sequential decision settings&mdash;e.g., reinforcement learning&mdash;by leveraging
    the implicit memory of primal-dual methods to build systems capable of
    compensating for their mistakes.</p>

    </div>
    <label for="expand-A" class="expand-label">
      <span class="closed">More details</span>
      <span class="open">Collapse</span>
    </label>
  </li>

  <li>
    **Direction B.** *When* is it possible to learn *from* requirements?
    <input type="checkbox" id="expand-B" class="check-with-label" />
    <div class="smalldesc" markdown="block">

    <p>**Learning from constraints.** Direction A investigates how learning
    complexity affects feasibility. In contrast, this direction explores
    *how constraints in return affect learning complexity*. Indeed, whereas
    constraints should improve sample complexity by reducing the feasible
    hypotheses class, current results show that constrained and
    unconstrained learning have essentially the *same* sample
    complexity [[CPCR ICASSP'20]({filename}/pages/publications.md#Chamon20ta) *(best student paper award)*;
    [CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p)].
    Any gains from restricting the
    hypotheses set thus appears to be offset by the fact we use data to
    determine whether a hypothesis is feasible. Understanding this trade-off
    will allow us to separate the underlying learning complexity of the task
    from that of its requirements and provide conditions under which
    learning can occur through the constraints, i.e., by using constraints
    to describe not only requirements, but also the learning problem itself.
    I am particularly interested in the impact of generalization constraints
    and the use of cross-validated versions of stochastic gradient
    descent (SGD) to impose them, given their promising results for Bayesian
    prior learning [[CPR ASILOMAR'19]({filename}/pages/publications.md#Chamon19l)].</p>

    <p>Ultimately, the goal of this research direction is to enable
    *constraint-driven learning*, a paradigm in which learning occurs not
    *under* constraints, but *from* constraints. In other words, where
    learning tasks are feasibility problems as opposed to cost minimization
    ones. This formulation is attractive since practical problems are often
    expressed as requirements rather than costs&mdash;e.g., “accuracy above 80%
    and fairness parity within 5%” rather than “minimize a combination of
    performance and fairness losses.” Additionally, it decouples conflicting
    requirements such as fit and model complexity, facilitating their
    specification, both manually or systematically using resilient
    techniques (Direction C). This approach has been beneficial in optimal
    control problems [[CPR L4DC'20]({filename}/pages/publications.md#Chamon20c);
    [CAPR CDC'20]({filename}/pages/publications.md#Chamon20r)], but remains unexplored in
    the context of learning. Naturally, it poses new algorithmic challenges
    as it leads to optimization problems with a large&mdash;on the order of the
    number of samples&mdash;or even an infinite number of constraints. I will
    address this issue by studying large-scale programs as samples from
    infinite ones (see Direction D for details).</p>

    </div>
    <label for="expand-B" class="expand-label">
      <span class="closed">More details</span>
      <span class="open">Collapse</span>
    </label>
  </li>

  <li>
    **Direction C.** *Which* requirements should be used to learn and how to specify them?
    <input type="checkbox" id="expand-C" class="check-with-label" />
    <div class="smalldesc" markdown="block">

    <p>**Resilient learning.** Directions A and B deal with the issue of
    learning under requirements once they are specified. Here, I am
    concerned with *which requirements to specify* in the first place. This
    is particularly important in the presence of conflicting objectives,
    such as fit vs. model complexity and nominal vs. adversarial
    performance, or ill-posed requirements, such as the protected groups in
    fairness&mdash;women; women and person of color; or women, person of color,
    and women&nbsp;x&nbsp;person of color. The goal is to enable
    tasks to *adapt* to their learning conditions (sample size,
    distributions, requirement difficulty) by automatically trading off
    their requirements. In ecology, this property is known as *resilience*.
    I propose to advance a mathematical formulation of resilient learning
    based on *counterfactuals* of the form “what would have been the
    performance if the requirement were relaxed/tightened?” Evaluating these
    counterfactuals, however, can be challenging, particularly in the
    non-convex setting of machine learning. Leveraging duality results from
    previous directions, I will establish conditions under which this is
    possible, determining when learning requirements can be balanced and how
    it can be done efficiently. I will then leverage other forms of duality
    to study compromise in different domains, such as discrete and
    semi-infinite optimization, and develop new statistical notions of
    duality to study the effect of uncertainty on compromises (statistical
    Pareto, Direction A).</p>

    <p>This approach to resilience has been fruitful in control
    [[CPR L4DC'20]({filename}/pages/publications.md#Chamon20c);
    [CAPR CDC'20]({filename}/pages/publications.md#Chamon20r)]
    and preliminary results show that it can be used to address
    learning issues such as outlier detection, classification confidence,
    and adversarial training. Indeed, modern parametrizations can&mdash;and
    possibly even should&mdash;interpolate training samples, making fit a poor
    measure of sample anomaly and leading to overconfident classifiers.
    Nevertheless, the credibility of a sample or prediction can still be
    assessed by balancing fit and model complexity or
    classification and perturbation magnitude
    [[CPR ArXiv'20]({filename}/pages/publications.md#Chamon20t)]. In the case of adversarial
    training, the compromise between nominal and adversarial performance can
    be used to determine the strength, type, and number of adversaries. In
    this context, resilience enables what are essentially self-learning
    adversaries. For GANs, these multiple, diverse discriminators may be
    used to address issues such as mode collapse.</p>

    </div>
    <label for="expand-C" class="expand-label">
      <span class="closed">More details</span>
      <span class="open">Collapse</span>
    </label>

  </li>
  <li>
    **Direction D.** *How* can we learn under requirements in practice?
    <input type="checkbox" id="expand-D" class="check-with-label" />
    <div class="smalldesc" markdown="block">

    <p>**Overparametrized learning.** Directions A–C primarily investigate
    *when* it is possible to learn under requirements and *which*
    requirements. This direction focuses on *how*. More specifically, how
    overparametrization affects the behavior of the primal-dual algorithms
    used to solve the dual learning problems from Directions A–C. This is
    motivated by the growing empirical and theoretical evidence that SGD
    finds good local minima for high-dimensional unconstrained learning
    problems despite their non-convexity. While there is strong empirical
    evidence that the same happens with stochastic gradient descent-ascent
    dynamics, the theory in this case remains scarce. What is more, it is
    not immediate that these methods can yield feasible models, especially
    due to fundamental roadblocks from duality to retrieving deterministic
    primal solutions.</p>

    <p>To achieve these results, I will combine classical tools, such as
    concentration of measure, with new techniques based on approaching
    *high-dimensionality from above*. Inspired by the fact that certain
    non-convex functional problems are tractable
    [[CER IEEE TSP'20]({filename}/pages/publications.md#Chamon20f)], this perspective
    proposes to tackle high dimensional phenomena not asymptotically from
    low dimensional structures, but as approximations or samples of infinite
    dimensional ones. This technique was used to quantify the
    parametrization gap in dual learning
    [[PCCR NeurIPS'19]({filename}/pages/publications.md#Paternain19c);
    [PCCR ArXiv'19]({filename}/pages/publications.md#Paternain19s);
    [CPCR ICASSP'20]({filename}/pages/publications.md#Chamon20ta) *(best student paper award)*;
    [CR NeurIPS'20]({filename}/pages/publications.md#Chamon20p)]
    and study
    transferability in graph neural networks (GNNs) by introducing their
    continuous counterparts, graphon NNs
    [[RCR NeurIPS'20]({filename}/pages/publications.md#Ruiz20ga)].
    I will use this approach
    to study both overparametrized problems&mdash;i.e., high dimensional primal
    problems&mdash;and the large-scale constrained optimization problems&mdash;i.e.,
    high dimensional dual problems&mdash;from Directions B and C. I foresee this
    method will also provide a new functional outlook on the generalization
    properties of interpolating NNs beyond neural tangent kernels (NTK).</p>

    </div>
    <label for="expand-D" class="expand-label">
      <span class="closed">More details</span>
      <span class="open">Collapse</span>
    </label>

  </li>
</ul>



![Bridging the gap between learning and critical systems]({static}/images/bridge.svg)

&nbsp;

&nbsp;



# Teaching

[**Teaching statement**]({static}/pdf/lfochamon_teaching.pdf)

## Unprompted feedback

&nbsp;


<div id="teachingQuotes" class="carousel slide" data-ride="carousel" data-interval="8000">
  <div class="carousel-inner">
    <div class="carousel-item active">
    <p>"Thanks for everything you did for us this summer! Your guidance and humor definitely made the experience even better."</p>
    <p style="line-height:100%;">Carly Staebell<br />
    <span style="font-size:75%;">Summer Undergraduate Fellowship in Sensor Technologies (SUNFEST), 2018</span></p>
    </div>
    <div class="carousel-item">
    <p>"I thought that Luiz gave an awesome lecture today.  We were pleasantly surprised, usually TAs are not that good / skilled."</p>
    <p style="line-height:100%;">Robert Mack Pierson<br />
    <span style="font-size:75%;">Stochastic Systems Analysis and Simulation (ESE 303), 2017</span></p>
    </div>
    <div class="carousel-item">
    <p>"I’m in ESE 224 and really enjoyed your lecture this morning."</p>
    <p style="line-height:100%;">Jacob Bendell<br />
    <span style="font-size:75%;">Signal and Information Processing (ESE 224), 2020</span></p>
    </div>

    <ol class="carousel-indicators">
      <li data-target="#teachingQuotes" data-slide-to="0" class="active"></li>
      <li data-target="#teachingQuotes" data-slide-to="1"></li>
      <li data-target="#teachingQuotes" data-slide-to="2"></li>
    </ol>
  </div>

</div>


## Experience

- **2009**: Instructor for non-destructive testing certification course at INSACAST, France  
    *Developed a new tutorial on ultrasound-based non-destructive testing of concrete*

- **2013&ndash;2014**: TA for undergraduate probability at the University of São Paulo, Brazil  
    *Produced instructional videos that have received over 130.000 views on [YouTube](https://www.youtube.com/user/luizchamon/videos)*

- **2016&ndash;2019**: TA for undergraduate probability at the University of Pennsylvania, USA

- **2017&ndash;2020**: TA for undergraduate signal processing (*in person and virtual*) at the University of Pennsylvania, USA

- **2018&ndash;2019**: Research mentor of [SUNFEST](https://sunfest.seas.upenn.edu/) (NSF-sponsored REU program at Penn)

- \> 7 years mentoring undergraduate and graduate research



## Recording

Highlights featured in the teaching statement to showcase my teaching philosophy:

- Day-to-day illustration of the material  
<iframe width="280" height="160" src="https://www.youtube.com/embed/BjS3FeXrOWE?start=1982" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- Fostering participation by
    * always waiting for an answer  
    <iframe width="280" height="160" src="https://www.youtube.com/embed/BjS3FeXrOWE?start=1560" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    * asking for "guesses" (hypotheses)  
    <iframe width="280" height="160" src="https://www.youtube.com/embed/BjS3FeXrOWE?start=600" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    * questioning "guesses"  
        <iframe width="280" height="160" src="https://www.youtube.com/embed/BjS3FeXrOWE?start=515" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


You can watch the whole thing on [YouTube](https://www.youtube.com/embed/BjS3FeXrOWE).

&nbsp;

&nbsp;


# Diversity

[**Diversity statement**]({static}/pdf/lfochamon_diversity.pdf)


My personal experience teaching and conducting research in different countries and
under a variety of conditions have made me realize that the challenge of building
a diverse education system goes beyond **bringing** people with different views and
backgrounds (*diversity* and *inclusion*), but must also include **supporting** them once
they come (*inclusion* and *equity*).

I plan to address these aspects through [**recruiting**](#student-recruitment),
[**mentoring**](#teaching-and-mentoring), and [**community**](#community).


## Student recruitment

First-generation students, international students, and those from groups underrepresented
in the sciences are often lead to believe that they are not fit to pursue a higher education
degree. In my case, an important factor in deciding to apply for a Ph.D. was having professors
that had studied abroad and seeing leading Brazilian scientists working in American
institutions. I aspire to also be such a role model and plan to actively reach out to a
diverse group of students with an emphasis on promoting the role of
Latin American/Latino women in engineering.

I have been involved in such recruiting efforts throughout my Ph.D.,
leveraging my close ties with universities in Brazil to help bring Luana Ruiz,
a Brazilian-American student, to Penn and participating in multiple meetings with
[Meyerhoff Scholars](https://meyerhoff.umbc.edu/), a program from the
University of Maryland, Baltimore County (UMBC) to increase diversity in STEM fields.


## Teaching and mentoring

Not all students are equally prepared for the challenges of higher education and research.
This issue is amplified by the non-technical obstacles faced by international students
and members of marginalized groups in STEM fields, such as navigating cultural and
institutional differences or dealing with a lack of relatable references.

In *mentoring*, I overcome these issues by taking the time to teach ancillary
research skills such as methodology, science communication, and peer-reviewing.
I also use personal experiences to help students navigate and cope with failure and
lack of structure. In *teaching*, I address these issues by allowing students
to resubmit homework so as to provide them with additional time and feedback
without them having to ask for it.


## Community

Support, however, must come from the whole community surrounding students.
Campus climate reports repeatedly show that the primary coping mechanism of
distressed students is to seek out their peers. It is therefore fundamental
to actively foster a welcoming and inclusive community, especially in graduate
school where the elective nature of classes can make it difficult for students
to come together.

At Penn, I ran the department Ph.D. colloquium, a seminar series where Ph.D.
students would present their recent work, practice their communication skills,
and learn about their colleagues’ research. I also lead activities such as
welcoming BBQs and the Women in ESE BBQ with the goal of fostering stronger
bonds in the department. For these initiatives, I received the 2018 ESE Good Citizen award.

Beyond the department, I also co-founded the [Philadelphia Open Soccer](https://www.philadelphiaopensoccer.org/),
a student organization that runs weekly after-school activities for public
school and refugee children.
