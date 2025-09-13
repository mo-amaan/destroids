# AGENTS.md - Destroids Game Development Guide

## Commands
- **Run game**: `python main.py`
- **Run tests**: `python -m unittest discover` or `python -m unittest test_module.py`
- **Run single test**: `python -m unittest module.TestClass.test_method`
- **Install dependencies**: `uv sync` or `pip install -e .`

## Code Style
- **Imports**: Use wildcard imports from local modules (`from constants import *`), standard imports for external libraries
- **Classes**: PascalCase (Player, CircleShape, Asteroid)
- **Variables/functions**: snake_case with descriptive names (player_speed, screen_width)
- **Constants**: UPPER_SNAKE_CASE in constants.py file
- **Spacing**: No spaces around assignment in function parameters (`def __init__(self,x,y)`)
- **Methods**: Include draw(screen) and update(dt) methods for game objects
- **Inheritance**: Use super().__init__() for parent class initialization
- **Game objects**: Inherit from CircleShape base class, use pygame.sprite.Group containers
- **Screen drawing**: Use pygame.draw functions with "white" color and 2px line width
- **Error handling**: Simple, direct approach without extensive try/catch blocks
- **Comments**: Minimal inline comments, focus on clear variable names

## Architecture
- Game uses pygame with sprite groups (updatable, drawable)
- Base CircleShape class for all game objects with position, velocity, radius
- Constants defined in separate constants.py file
- Main game loop handles events, updates, and drawing in main.py