Network
===

<!-- MarkdownTOC -->

- [Nodes](#nodes)
	- [Race](#race)
	- [Geography](#geography)
	- [Actors](#actors)
		- [Group](#group)
		- [Entity](#entity)
- [Data Structure](#data-structure)
- [Features](#features)
- [Questions](#questions)
- [Implementation Details](#implementation-details)
- [Flow](#flow)

<!-- /MarkdownTOC -->


<a id="nodes"></a>
## Nodes

<a id="race"></a>
### Race

<a id="geography"></a>
### Geography
- Resources
- Accessability
- Size
- Bio diversity (flora - fauna)
- Entity diversity (homogenous - heterogenous)

<a id="actors"></a>
### Actors
- Wealth (low - high)
- Position  (low - high)
- Connections (low - high)

<a id="group"></a>
#### Group
eg. Family, Guild, Kingdom

- Number of members (low - high)
- Wealth - include sum of members?

<a id="entity"></a>
#### Entity
- [Race](#race)
- Race variant?

<a id="data-structure"></a>
## Data Structure
- Seperate information from history
	- Information (name) in .yaml - history in git

<a id="features"></a>
## Features
- Lock nodes from being processed (eg. PCs). Incoming edges can be updated - but not outgoing ones

<a id="questions"></a>
## Questions
- What to calculate where?
- How to save history?
- How to calculate statistics like "number of members"?
- Seperate "belongs-to" tree from network representation?


<a id="implementation-details"></a>
## Implementation Details
- List of all Nodes
	- Use to randomly create new Nodes & Edges
	- Use to make sure every Node got updates  
- List of all Edges
	- Visual representation
- Register callbacks for edge updating
	- Callback returns int (-100 - 100)
	- Update with mean of callbacks
- Callbacks as plugins
	- Define node type to apply to
	- Define chance to apply to node type
- Thread Pool for Node processing
	- Start with one Node
	- When done, use Thread Pool to process connected Nodes
- "Action" = static input Callback
	- User defines input, eg. +20 for completed quest
	- Random input for automated action
	- Support multiple inputs at the same time


<a id="flow"></a>
## Flow
- Action (manual - generated) triggers ripple (backprop) through network
