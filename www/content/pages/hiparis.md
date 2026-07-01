Title: Hi!PARIS tutorial
URL: hiparis/index.html
status: hidden
save_as: hiparis/index.html
template: tutorial_refs
bibtex: content/csrl_tutorial.bib


# Hi!PARIS 2026 Tutorial &ndash;<br>Learning under Requirements: Supervised and Reinforcement Learning with Constraints

**July 1st (Wednesday), 9:00-12:30**

This tutorial is geared towards researchers and practitioners interested in imposing requirements to ML systems, such as fairness, robustness, and safety. Typically, these statistical, data-driven constraints are induced by combining the learning objective and requirement violation metrics into a single training loss. To guarantee that the solution satisfies the requirements, however, this approach requires careful tuning of hyperparameters (penalty coefficients) using cross-validation, which can be computationally intensive and time consuming. Constrained learning incorporates requirements as statistical constraints rather than by modifying the training objective.

In this tutorial, we provide an overview of theoretical and algorithmic advances from the past 5 years that show when and how it is possible to learn under constraints and effectively impose constraints on ML systems, both during training and at test time. Specifically, we explore the role and impact of different types of requirements in supervised learning, sampling, and RL:

1. **Constrained supervised learning**, where we show generalization guarantees for constrained supervised learning based on new non-convex duality results and then use them to derive practical algorithms;
2. **Stranger things**, where we use constraints to achieve not-so-average goals, such as robust learning, constraint adaptation, and adaptive "annealing";
2. **Constrained sampling/generation**, where we leverage these duality advances to tackle problems in sampling and generative modeling;
3. **Constrained reinforcement learning**, where we develop a parallel theory for constrained RL, showing that it is strictly more expressive than unconstrained RL and providing guaranteed algorithms.

Throughout the tutorial, we illustrate the effectiveness and flexibility of constrained learning in a diverse set of applications, such as *fairness*, *federated learning*, *robust image classification*, *constrained generation*, *safe RL*, and *wireless communications*. Ultimately, this tutorial provides a general tool that can be used to tackle a variety of problems in ML and sequential decision-making.


**Prerequisite knowledge**: only basic understanding of optimization, ML, and RL are expected. Specifically, familiarity with the basics of convex **optimization** and its algorithms (i.e., what are convex functions, mathematics of gradients, and gradient descent); fundamentals of empirical risk minimization (ERM) and the associated **learning theory** (i.e., basic notions of generalization and sample complexity); and familiarity with **Markov decision processes** (MDPs) and basic RL algorithms (policy gradient, e.g., REINFORCE).


## Schedule

| Time | Topic |
|---|---|
| 9:00 - 9:15 | **Introduction** ([slides]({static}/pdf/hiparis_handout_1.pdf)) |
| 9:15 - 10:00 | **Constrained supervised learning** |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(un)constrained learning and ERM |
|             | &nbsp;&nbsp;&nbsp;&nbsp;non-convex duality and constrained learning theory |
|             | &nbsp;&nbsp;&nbsp;&nbsp;constrained learning algorithms |
| 10:00 - 10:30 | **Stranger things** |
|             | &nbsp;&nbsp;&nbsp;&nbsp;robustness-constrained learning and semi-infinite optimization |
|             | &nbsp;&nbsp;&nbsp;&nbsp;resilient learning |
|             | &nbsp;&nbsp;&nbsp;&nbsp;adaptive "annealing" |
| 10:30 - 11:00 | Break |
| 11:00 - 12:15 | **Constrained sampling and generation** ([slides]({static}/pdf/hiparis_handout_2.pdf)) |
|             | &nbsp;&nbsp;&nbsp;&nbsp;Primal-dual Langevin Monte Carlo |
|             | &nbsp;&nbsp;&nbsp;&nbsp;Constrained diffusion models |
| 11:00 - 12:15 | **Constrained reinforcement learning** |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(C)MDPs and (C)RL |
|             | &nbsp;&nbsp;&nbsp;&nbsp;CRL duality |
|             | &nbsp;&nbsp;&nbsp;&nbsp;CRL algorithms |
| 12:15 - 12:30 | **Q&A and discussion** |

A selected bibliography for the tutorial can be found [here](#bibliography).


<!--
## Content

### Constrained Supervised Learning: Duality, Generalization, and Resilience {: #module-1}

In this module, we formalize statistical learning and empirical risk minimization (ERM), discuss different types of requirements that arise in ML, and show how these requirements are imposed using constrained optimization. We then introduce constrained learning theory and proceed to show a family of generalization bounds for constrained learning using not constrained ERM, but non-convex duality. Based on these results, we develop primal-dual training algorithms, discuss practical aspects of their implementation (step sizes, stopping criteria), and elucidate their convergence properties. We explore how these duality results can be used to adapt the trade-off between objective and requirements and balance the marginal costs and benefits of relaxing constraints. We dub these techniques "resilient learning," from the ecological concept that describes the ability of a system to adapt to changes in their environment.


**Applications**: We use *fairness* as an example of rate requirement (e.g., equality of odds, churn) and *federated learning* to illustrate how to tackle ML problems with simultaneous goals (e.g., heterogeneous data or heterogeneous performance targets). We then revisit this *heterogeneous federated learning* application to illustrate the use of resilient learning.


### Robust learning: Adversaries, Invariance, and Data Manifolds {: #module-2}

This is in contrast to robustness, which seeks to resist rather than adapt to disturbances. To tackle this problem, we introduce epigraph formulations of robustness that feature one constraint per sample and disturbance and extend previous duality results to this semi-infinite constrained learning problem. We then derive a practical algorithm for tackling robustness-constrained learning based on Markov Chain Monte Carlo (MCMC) and stochastic optimization, showing how it generalizes previous solutions based on adversarial training (e.g., "PGD") and penalty methods (e.g., TRADES). Additionally, we showcase how it achieves stronger guarantees, better compromises, and mitigate the challenges involved in computing worst-case perturbations during training.

**Applications**: We consider the issue of *adversarial examples* in image classification. We also explore how semi-infinite constrained learning can be use to tackle "non-robustness" applications, namely *learning in the presence of invariances*, where we show a mathematical equivalence between robustness and data augmentation, and *semi-supervised learning*, where we derive connections between robustness, Lipschitz regularization of neural networks, and manifold Laplacian regularization. We illustrate the latter in a *navigation* example.


### Constrained Reinforcement Learning: Duality and Algorithms {: #module-3}

The final module develops a parallel constrained learning theory in the dynamic setting of sequential decision-making problems. We start by introducing the MDP formalism and RL algorithms commonly used to tackle this setting. Using a different technique, we then derive non-convex duality results similar to the supervised case and use them to put forward a primal-dual algorithm for constrained RL. We then show how this algorithm can fail even on simple tasks and describe a systematic state augmentation procedure able to provably overcome this issue.

**Applications**: We consider the task of learning *safe policies* and *wireless resource allocation* to motivate and illustrate the results of this module. We then turn to a *continuous monitoring problem* to illustrate the limitations of unconstrained RL and show the need for state augmentation.
-->

## Presenters

[**Luiz F. O. Chamon**](https://luizchamon.com) is an assistant professor (tenure-track) and Hi! PARIS chair holder in the center for applied mathematics (CMAP) of École polytechnique, France.
He received the B.Sc. and M.Sc. degrees in electrical engineering from the University of São Paulo, Brazil, in 2011 and 2015 and the Ph.D. degree in electrical and systems engineering from the University of Pennsylvania (Penn), USA, in 2020. Until 2022, he was a postdoctoral fellow at the Simons Institute of the University of California, Berkeley, and until 2024, he was an independent research group leader at the University of Stuttgart, Germany.
In 2009, he was an undergraduate exchange student of the Masters in Acoustics of the École Centrale de Lyon, France, and worked as an Assistant Instructor and Consultant on nondestructive testing at INSACAST Formation Continue. From 2010 to 2014, he worked as a Signal Processing and Statistics Consultant on a research project with EMBRAER.

He received both the best student paper and the best paper awards at IEEE ICASSP 2020 and was recognized by the IEEE Signal Processing Society for his distinguished work for the editorial board of the IEEE Transactions on Signal Processing in 2018. In 2022, he received the Young Investigators award from the Division of Engineering and Applied Sciences, Caltech. In 2025, he received the S.S. Chern Young Faculty Award, a recognition for talented young mathematicians from École polytechnique. He is currently an ELLIS Scholar of the European Laboratory for Learning and Intelligent Systems (ELLIS).

His research interests include optimization, signal processing, machine learning, statistics, and control.