# Playbook

Playbook is an open source project meant to programatically define abstract animations.

## Playbook class

The `Playbook` class is responsible for keeping track of all the components and transitions, and eventually rendering this into video.

## Components

Components are objects that are rendered into video. They have attributes that parameterize the component, which can be changed by transitions.

## Transitions

Transitions are objects that change the behaviour and looks of components.

## TODO

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