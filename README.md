# Playbook

Playbook is an open source project meant to programatically define abstract animations.

## Playbook class

The `Playbook` class is responsible for keeping track of all the components and transitions, and eventually rendering this into video.

## Components

Components are objects that are rendered into video. They have attributes that parameterize the component, which can be changed by transitions.

## Transitions

Transitions are objects that change the behaviour and looks of components.

## TODO

### Attributes

Currently the attributes are a big mess, we need a registration process that explains a number of meta attributes. These include whether they can be part of a transition, whether they scale with resizing (for supersampling and for resize style transitions) and if they are integer, float or color.

### Color

Currently, color cannot be transitioned yet. It is probably best to add a Color class.

### Transitions

Opacity transitions which also mean we need to add opacity.

### Better interpolators

The sigmoid interpolator is not great, we need to add parameterization and other interpolators.

### Text attribute

Needs to be factored out

### PyTest

Add pytest unit tests