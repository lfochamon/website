Title: Learning under Requirements
URL: csrl/index.html
status: hidden
save_as: csrl/index.html
template: tutorial_refs


# Learning under Requirements: Supervised and Reinforcement Learning with Constraints

{#
**February 20th (Tuesday), morning session (full schedule at [AAAI](https://aaai.org/aaai-conference/aaai-24-tutorial-and-lab-forum/))**
#}

This tutorial is geared towards researchers and practitioners interested in imposing requirements to ML systems, such as fairness, robustness, and safety. Typically, these statistical, data-driven constraints are induced by combining the learning objective and requirement violation metrics into a single training loss. To guarantee that the solution satisfies the requirements, however, this approach requires careful tuning of hyperparameters (penalty coefficients) using cross-validation, which can be computationally intensive and time consuming. Constrained learning incorporates requirements as statistical constraints rather than by modifying the training objective.

In this tutorial, we provide an overview of theoretical and algorithmic advances from the past 5 years that show when and how it is possible to learn under constraints and effectively impose constraints on ML systems, both during training and at test time. Specifically, we explore the role and impact of different types of requirements in supervised learning, robust learning, and RL:

1. [**Constrained supervised learning**](#module-1), where we show generalization guarantees for constrained supervised learning based on new non-convex duality results and then use them to derive practical algorithms;
2. [**Robust learning**](#module-2), where we leverage these advances to obtain robust learning algorithms capable of achieving better trade-offs between nominal and adversarial accuracy;
3. [**Constrained reinforcement learning**](#module-3), where we develop a parallel theory for constrained RL, showing that it is strictly more expressive than unconstrained RL.

Throughout the tutorial, we illustrate the effectiveness and flexibility of constrained learning in a diverse set of applications, such as *fairness*, *robust image classification*, *federated learning*, *learning under invariance*, and *safe RL*. Ultimately, this tutorial provides a general tool that can be used to tackle a variety of problems in ML and sequential decision-making.


**Prerequisite knowledge**: only basic understanding of optimization, ML, and RL are expected. Specifically, familiarity with the basics of convex **optimization** and its algorithms (i.e., what are convex functions, mathematics of gradients, and gradient descent); fundamentals of empirical risk minimization (ERM) and the associated **learning theory** (i.e., basic notions of generalization and sample complexity); and familiarity with **Markov decision processes** (MDPs) and basic RL algorithms (policy gradient, e.g., REINFORCE).


## Schedule

| Time | Topic |
|---|---|
| 8:30 - 9:30 | [**Constrained supervised learning**](#module-1) |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(un)constrained learning and ERM |
|             | &nbsp;&nbsp;&nbsp;&nbsp;non-convex duality and constrained learning theory |
|             | &nbsp;&nbsp;&nbsp;&nbsp;constrained learning algorithms |
|             | &nbsp;&nbsp;&nbsp;&nbsp;resilient learning |
| 9:30 - 10:30 | [**Robust learning**](#module-2) |
|             | &nbsp;&nbsp;&nbsp;&nbsp;robustness-constrained learning and semi-infinite optimization |
|             | &nbsp;&nbsp;&nbsp;&nbsp;sampling algorithms and MCMC |
|             | &nbsp;&nbsp;&nbsp;&nbsp;probabilistic robustness |
| 10:30 - 11:00 | Break |
| 11:00 - 12:30 | [**Constrained reinforcement learning**](#module-3) |
|             | &nbsp;&nbsp;&nbsp;&nbsp;(C)MDPs and (C)RL |
|             | &nbsp;&nbsp;&nbsp;&nbsp;duality and primal-dual algorithms |
|             | &nbsp;&nbsp;&nbsp;&nbsp;state augmented algorithm |



## Content

### Constrained Supervised Learning: Duality, Generalization, and Algorithms {: #module-1}

In this module, we formalize statistical learning and empirical risk minimization (ERM), discuss different types of requirements that arise in ML, and show how these requirements are imposed using constrained optimization. We then introduce constrained learning theory and proceed to show a family of generalization bounds for constrained learning using not constrained ERM, but non-convex duality. Based on these results, we develop primal-dual training algorithms, discuss practical aspects of their implementation (step sizes, stopping criteria), and elucidate their convergence properties.

{#
In this module, we explore the issue of specifying learning requirements to balance the trade-off between objective and requirements. To do so, we incorporate constraint relaxations as part of the optimization space and develop strategies to balance the marginal costs and benefits of these relaxation. Leveraging duality results from previous modules, we analyze these equilibria and develop algorithms to automatically find them during training. We dub these techniques "resilient learning," from the ecological concept that describes the ability of a system to adapt to changes in their environment. We then discuss the relations to robust learning and other classical ML tasks, such as soft-margin SVMs.
#}

**Applications**: We use *fairness* as an example of rate requirement (e.g., equality of odds, churn) and *federated learning* to illustrate how to tackle ML problems with simultaneous goals (e.g., heterogeneous data or heterogeneous performance targets). We also briefly mentions applications to other problems of current interest, such as *active learning* and *continual learning*.


### Robust Learning: Adversaries, Invariance, and Data Manifolds {: #module-2}

We begin this module by introducing the problem of robust learning, showing how robustness can be formulated as a constraint. In particular, we introduce epigraph formulations of adversarial robustness that feature one constraint per sample and disturbance and extend previous duality results to this semi-infinite constrained learning problem. Based on these results, we derive a practical algorithm for tackling robustness-constrained learning based on Markov Chain Monte Carlo (MCMC) and stochastic optimization, showing how it generalizes previous solutions based on adversarial training (e.g., "PGD") and penalty methods (e.g., TRADES). We then explore how constrained learning formulations achieve stronger guarantees, better compromises, and mitigate the challenges involved in computing worst-case perturbations during training.

**Applications**: We use *adversarial robustness* in image classification as a running example. We also explore how these techniques can be use to tackle "non-robustness" applications, namely *learning in the presence of invariances*, where we show a mathematical equivalence between robustness and data augmentation, and *semi-supervised learning*, where we derive connections between robustness, Lipschitz regularization of neural networks, and manifold Laplacian regularization.


### Constrained Reinforcement Learning: Duality and Algorithms {: #module-3}

The final module develops a parallel constrained learning theory in the dynamic setting of sequential decision-making problems. We start by introducing the MDP formalism and RL algorithms commonly used to tackle this setting. Using a different technique, we then derive non-convex duality results similar to the supervised case and use them to put forward a primal-dual algorithm for constrained RL. We then show how this algorithm can fail even on simple tasks and describe a systematic state augmentation procedure able to provably overcome this issue.

**Applications**: We consider the task of learning *safe policies* to motivate and illustrate the results of this module. We then turn to a *continuous monitoring problem* to illustrate the limitations of unconstrained RL and show the need for state augmentation.


## Presenters

[**Miguel Calvo-Fullana**](https://scholar.google.com/citations?user=pcwmurcAAAAJ) received the B.Sc. degree in electrical engineering from the Universitat de les Illes Balears (UIB) in 2010 and the M.Sc. and Ph.D. degrees in electrical engineering from the Universitat Polit&egrave;cnica de Catalunya (UPC) in 2013 and 2017, respectively. He joined Universitat Pompeu Fabra (UPF) in 2023, where he is a Ram&oacute;n y Cajal fellow. Prior to joining UPF, he held postdoctoral appointments at the University of Pennsylvania and the Massachusetts Institute of Technology and was a research assistant at the Centre Tecnol&ograve;gic de Telecomunicacions de Catalunya (CTTC). His research interests include learning, optimization, multi-agent systems, and wireless communication. He is the recipient of best paper awards at ICC 2015, IEEE GlobalSIP 2015, and IEEE ICASSP 2020.

[**Luiz F. O. Chamon**](https://luizchamon.com) received the B.Sc. and M.Sc. degrees in electrical engineering from the University of S&atilde;o Paulo, Brazil, in 2011 and 2015 and the Ph.D. degree in electrical and systems engineering from the University of Pennsylvania (Penn), USA, in 2020. Until 2022, he was a postdoctoral fellow at the Simons Institute of the University of California, Berkeley, USA. He is currently an independent research group leader at the University of Stuttgart, Germany. In 2009, he was an undergraduate exchange student of the Masters in Acoustics of the &Eacute;cole Centrale de Lyon, France. He received both the best student paper and the best paper awards at IEEE ICASSP 2020 and was recognized by the IEEE Signal Processing Society for his distinguished work for the editorial board of the IEEE Transactions on Signal Processing in 2018. His research interests include optimization, signal processing, machine learning, statistics, and control.

[**Santiago Paternain**](https://sites.ecse.rpi.edu/ paters) received the B.Sc. degree in electrical engineering from Universidad de la Rep&uacute;blica Oriental del Uruguay, Montevideo, Uruguay in 2012, the M.Sc. in Statistics from the Wharton School in 2018, and the Ph.D. in Electrical and Systems Engineering from the University of Pennsylvania in 2018. He is currently an Assistant Professor at the Rensselaer Polytechnic Institute (RPI). Prior to joining RPI, Dr. Paternain was a postdoctoral researcher at the University of Pennsylvania. His research interests lie at the intersection of machine learning and control of dynamical systems. Dr. Paternain was the recipient of the 2017 CDC Best Student Paper Award and the 2019 Joseph and Rosaline Wolfe Best Doctoral Dissertation Award from the Electrical and Systems Engineering Department at the University of Pennsylvania.

[**Alejandro Ribeiro**](https://alelab.seas.upenn.edu/) received the B.Sc. degree in electrical engineering from the Universidad de la Rep&uacute;blica Oriental del Uruguay in 1998 and the M.Sc. and Ph.D. degrees in electrical engineering from the University of Minnesota in 2005 and 2007. He joined the University of Pennsylvania (Penn) in 2008 where he is currently Professor of Electrical and Systems Engineering. His research is in wireless autonomous networks, machine learning on network data and distributed collaborative learning. Papers coauthored by Dr. Ribeiro received the 2022 IEEE Signal Processing Society Best Paper Award, the 2022 IEEE Brain Initiative Student Paper Award, the 2021 Cambridge Ring Publication of the Year Award, the 2020 IEEE Signal Processing Society Young Author Best Paper Award, the 2014 O. Hugo Schuck best paper award, and paper awards at EUSIPCO, IEEE ICASSP, IEEE CDC, IEEE SSP, IEEE SAM, Asilomar SSC Conference, and ACC. His teaching has been recognized with the 2017 Lindback award for distinguished teaching and the 2012 S. Reid Warren, Jr. Award presented by Penn’s undergraduate student body for outstanding teaching. Dr. Ribeiro received an Outstanding Researcher Award from Intel University Research Programs in 2019. He is a Penn Fellow class of 2015 and a Fulbright scholar class of 2003.