title: UNESCO
title_long: Uncertainty Estimation for Computational Pathology
finished: true 
picture: projects/unesco.png
template: project-single
groups: pathology, diag
default_group: pathology 
people: Jasper Linmans, Geert Litjens, Jeroen van der Laak
description: The aim of UNESCO is to study techniques for estimating uncertainty in computational pathology.
bibkeys: Linm20
type: normal

Research into computational pathology (i.e., the application of machine learning to digitized histopathological tissue sections) typically yields deep neural networks that can distinguish between different tissues or can detect and/or delineate specific tissue structures of interest. 

Deep neural networks are generated by using large amounts of training data. An important limitation of such networks is the fact that they are not designed to deal with patterns that which were not present in the data used for training. As a result, the neural network may classify a tissue section as entirely healthy whereas the tissue contains serious pathology. 

The current project aims to study techniques which can extend the network output with a number expressing the level of (un)certainty. This can be useful to intercept potential errors, as the network will be able to indicate how certain it is of the correctness of the produced output.
