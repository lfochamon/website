Title: SGM tutorial
URL: sgm/index.html
status: hidden
save_as: sgm/index.html
template: tutorial_refs
bibtex: content/csrl_tutorial.bib


# SIMPAS Group Meeting 2025 &ndash;<br>Learning under Requirements: Supervised and Reinforcement Learning with Constraints

This tutorial is geared towards researchers and practitioners interested in imposing requirements to ML systems, such as fairness, robustness, and safety. Typically, these statistical, data-driven constraints are induced by combining the learning objective and requirement violation metrics into a single training loss. To guarantee that the solution satisfies the requirements, however, this approach requires careful tuning of hyperparameters (penalty coefficients) using cross-validation, which can be computationally intensive and time consuming. Constrained learning incorporates requirements as statistical constraints rather than by modifying the training objective.

In this tutorial, we provide an overview of theoretical and algorithmic advances from the past 5 years that show when and how it is possible to learn under constraints and effectively impose constraints on ML systems, both during training and at test time. Specifically, we explore the role and impact of different types of requirements in supervised learning, robust learning, and RL:

1. [**Constrained supervised learning**](#module-1), where we show generalization guarantees for constrained supervised learning based on new non-convex duality results and then use them to derive practical algorithms;
3. [**Constrained reinforcement learning**](#module-2), where we develop a parallel theory for constrained RL, showing that it is strictly more expressive than unconstrained RL and providing guaranteed algorithms.

Throughout the tutorial, we illustrate the effectiveness and flexibility of constrained learning in a diverse set of applications, such as *fairness*, *federated learning*, *robust image classification*, *safe RL*, and *wireless communications*. Ultimately, this tutorial provides a general tool that can be used to tackle a variety of problems in ML and sequential decision-making.


**Prerequisite knowledge**: only basic understanding of optimization, ML, and RL are expected. Specifically, familiarity with the basics of convex **optimization** and its algorithms (i.e., what are convex functions, mathematics of gradients, and gradient descent); fundamentals of empirical risk minimization (ERM) and the associated **learning theory** (i.e., basic notions of generalization and sample complexity); and familiarity with **Markov decision processes** (MDPs) and basic RL algorithms (policy gradient, e.g., REINFORCE).


## Schedule

| Time | Topic |
|---|---|
| 10:00 - 10:15 | [**Introduction**](#) |
| 10:15 - 11:00 | [**Constrained supervised learning**](#module-1) ([slides]({static}/pdf/sgm_handout_1.pdf)) |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(un)constrained learning and ERM |
|             | &nbsp;&nbsp;&nbsp;&nbsp;non-convex duality and constrained learning theory |
|             | &nbsp;&nbsp;&nbsp;&nbsp;constrained learning algorithms |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(robust or resilient) learning |
| 11:00 - 11:10 | Break |
| 11:10 - 11:45 | [**Constrained reinforcement learning**](#module-2) ([slides]({static}/pdf/sgm_handout_2.pdf)) |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(C)MDPs and (C)RL |
|             | &nbsp;&nbsp;&nbsp;&nbsp;CRL duality |
|             | &nbsp;&nbsp;&nbsp;&nbsp;CRL algorithms |
| 11:45 - 12:00 | [**Q&A and discussion**](#) |

A selected bibliography for the tutorial is available [here](#bibliography).


## Content

### Constrained Supervised Learning: Duality, Generalization, and Resilience {: #module-1}

In this module, we formalize statistical learning and empirical risk minimization (ERM), discuss different types of requirements that arise in ML, and show how these requirements are imposed using constrained optimization. We then introduce constrained learning theory and proceed to show a family of generalization bounds for constrained learning using not constrained ERM, but non-convex duality. Based on these results, we develop primal-dual training algorithms, discuss practical aspects of their implementation (step sizes, stopping criteria), and elucidate their convergence properties. We explore how these duality results can be used to adapt the trade-off between objective and requirements and balance the marginal costs and benefits of relaxing constraints. We dub these techniques "resilient learning," from the ecological concept that describes the ability of a system to adapt to changes in their environment.

**Applications**: We use *fairness* as an example of rate requirement (e.g., equality of odds, churn), *adversarial examples* in image classification for robustness, and *federated learning* to illustrate how to tackle ML problems with simultaneous goals (e.g., heterogeneous data or heterogeneous performance targets). We then revisit this *heterogeneous federated learning* application to illustrate the use of resilient learning.


### Constrained Reinforcement Learning: Duality and Algorithms {: #module-2}

The final module develops a parallel constrained learning theory in the dynamic setting of sequential decision-making problems. We start by introducing the MDP formalism and RL algorithms commonly used to tackle this setting. Using a different technique, we then derive non-convex duality results similar to the supervised case and use them to put forward a primal-dual algorithm for constrained RL. We then show how this algorithm can fail even on simple tasks and describe a systematic state augmentation procedure able to provably overcome this issue.

**Applications**: We consider the task of learning *safe policies* and *wireless resource allocation* to motivate and illustrate the results of this module. We then turn to a *continuous monitoring problem* to illustrate the limitations of unconstrained RL and show the need for state augmentation.
