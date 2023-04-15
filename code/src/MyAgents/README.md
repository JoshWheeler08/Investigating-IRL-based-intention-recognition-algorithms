# MyAgents

## Description

This directory contains my Python classes for representing the `Assistant` and `Owner` agent, independent of the game environment they will be trained on (plug-and-play testing infrastructure). The abstract base class, `Agent`, is used to ensure the other classes follow a standardised interface and includes implementations for shared methods.

- Agent base class = `Agent.py`
- IRL-based Assistive Player = `Assistant.py`
- Owner/Human Player = `Owner.py`


## Objects/

Contains two Python classes for storing all the related information about an entity into one object. Used to make the code easier to read by reducing the number of parameters needed per function.

- `EnvObject.py` encapusulates all the information needed to create and use an environment

- `PolicyObject.py` encapsulates all the related information about a policy.