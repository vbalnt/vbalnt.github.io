#!/usr/bin/env python3
"""
Growing Trees with Grammar: An Introduction to L-Systems
========================================================

Auto-generated from blog post. Run this script to generate all outputs.

Requirements:
    pip install matplotlib numpy trimesh

Output:
    All images and models are saved to ./output/
"""

import os
import sys
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Create output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper to save files to output directory
def _img(filename):
    """Convert filename to output path."""
    return os.path.join(OUTPUT_DIR, filename)

def _web(filename):
    """Return web path (for blog compatibility)."""
    return f"./output/{filename}"

print(f"L-Systems Generator")
print(f"Output directory: {OUTPUT_DIR}")
print()

def apply_rules(axiom: str, rules: dict, iterations: int) -> str:
    """Apply L-system rules for n iterations."""
    current = axiom
    for _ in range(iterations):
        current = ''.join(rules.get(c, c) for c in current)
    return current

# Simple example: Algae growth
rules = {'A': 'AB', 'B': 'A'}
for i in range(8):
    result = apply_rules('A', rules, i)
    print(f"n={i}: {result}")

@dataclass
class Turtle:
    x: float = 0.0
    y: float = 0.0
    angle: float = 90.0

    def copy(self):
        return Turtle(self.x, self.y, self.angle)

def draw_lsystem(axiom: str, rules: dict, iterations: int,
                 angle: float = 25.0, step: float = 1.0,
                 figsize=(10, 10), title=None, filename=None):
    """Generate and draw an L-system."""
    instructions = apply_rules(axiom, rules, iterations)
    turtle = Turtle()
    stack = []
    lines = []

    for cmd in instructions:
        if cmd == 'F':
            rad = np.radians(turtle.angle)
            new_x = turtle.x + step * np.cos(rad)
            new_y = turtle.y + step * np.sin(rad)
            lines.append(((turtle.x, turtle.y), (new_x, new_y)))
            turtle.x, turtle.y = new_x, new_y
        elif cmd == '+':
            turtle.angle -= angle
        elif cmd == '-':
            turtle.angle += angle
        elif cmd == '[':
            stack.append(turtle.copy())
        elif cmd == ']':
            turtle = stack.pop()

    fig, ax = plt.subplots(figsize=figsize)
    for (x1, y1), (x2, y2) in lines:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    if title:
        ax.set_title(title)
    plt.tight_layout()
    if filename:
        plt.savefig(_img(filename), dpi=150, bbox_inches='tight')
    plt.close()
    return _web(filename) if filename else None

def draw_lsystem_fg(axiom, rules, iterations, angle=60, step=1.0,
                    figsize=(10, 10), title=None, filename=None):
    """L-system where both F and G draw forward (for two-symbol systems)."""
    instructions = apply_rules(axiom, rules, iterations)
    turtle = Turtle()
    lines = []

    for cmd in instructions:
        if cmd in 'FG':
            rad = np.radians(turtle.angle)
            new_x = turtle.x + step * np.cos(rad)
            new_y = turtle.y + step * np.sin(rad)
            lines.append(((turtle.x, turtle.y), (new_x, new_y)))
            turtle.x, turtle.y = new_x, new_y
        elif cmd == '+':
            turtle.angle -= angle
        elif cmd == '-':
            turtle.angle += angle

    fig, ax = plt.subplots(figsize=figsize)
    for (x1, y1), (x2, y2) in lines:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    if title:
        ax.set_title(title)
    plt.tight_layout()
    if filename:
        plt.savefig(_img(filename), dpi=150, bbox_inches='tight')
    plt.close()
    return _web(filename) if filename else None

koch_rules = {'F': 'F+F--F+F'}
draw_lsystem('F', koch_rules, iterations=4, angle=60, figsize=(12, 4),
             title='Koch Curve', filename='koch.png')

draw_lsystem('F', {'F': 'F+F-F-F+F'}, iterations=4, angle=90, figsize=(12, 6),
             title='Quadratic Koch', filename='quadratic-koch.png')

draw_lsystem_fg('F', {'F': 'F+G', 'G': 'F-G'}, iterations=12, angle=90, figsize=(10, 10),
                title='Dragon Curve', filename='dragon.png')

draw_lsystem('F', {'F': '+F--F+'}, iterations=12, angle=45, figsize=(10, 10),
             title='Lévy C Curve', filename='levy-c.png')

draw_lsystem_fg('F', {'F': 'F-G--G+F++FF+G-', 'G': '+F-GG--G-F++F+G'},
                iterations=4, angle=60, figsize=(10, 10),
                title='Gosper Curve', filename='gosper.png')

sierpinski_rules = {'F': 'F-G+F+G-F', 'G': 'GG'}
draw_lsystem_fg('F-G-G', sierpinski_rules, iterations=6, angle=120,
                figsize=(8, 8), title='Sierpinski Triangle',
                filename='sierpinski.png')

plant_rules = {'F': 'FF', 'X': 'F-[[X]+X]+F[+FX]-X'}
draw_lsystem('X', plant_rules, iterations=5, angle=25, figsize=(10, 12),
             title='Fractal Plant', filename='plant.png')

tree_rules = {'F': 'FF+[+F-F-F]-[-F+F+F]'}
draw_lsystem('F', tree_rules, iterations=4, angle=22.5, figsize=(12, 12),
             title='Organic Tree', filename='tree.png')


def draw_stochastic(axiom, rules, iterations, angle=25, angle_var=5,
                    step=1.0, step_var=0.2, figsize=(10, 10),
                    seed=None, filename=None, ax=None):
    """Draw L-system with random variations."""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    instructions = apply_rules(axiom, rules, iterations)
    turtle = Turtle()
    stack = []
    lines = []
    depths = []
    depth = 0

    for cmd in instructions:
        if cmd == 'F':
            s = step * (1 + random.uniform(-step_var, step_var))
            rad = np.radians(turtle.angle)
            new_x = turtle.x + s * np.cos(rad)
            new_y = turtle.y + s * np.sin(rad)
            lines.append(((turtle.x, turtle.y), (new_x, new_y)))
            depths.append(depth)
            turtle.x, turtle.y = new_x, new_y
        elif cmd == '+':
            a = angle + random.uniform(-angle_var, angle_var)
            turtle.angle -= a
        elif cmd == '-':
            a = angle + random.uniform(-angle_var, angle_var)
            turtle.angle += a
        elif cmd == '[':
            stack.append((turtle.copy(), depth))
            depth += 1
        elif cmd == ']':
            turtle, depth = stack.pop()

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    max_depth = max(depths) if depths else 1

    for ((x1, y1), (x2, y2)), d in zip(lines, depths):
        lw = 2.0 * (1 - d / (max_depth + 1)) + 0.3
        t = d / (max_depth + 1)
        color = (0.3 + 0.2*t, 0.2 + 0.5*t, 0.1)
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw)

    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#f5f5dc')
    return ax

organic_rules = {'F': 'FF+[+F-F-F]-[-F+F+F]'}

fig, axes = plt.subplots(1, 3, figsize=(15, 8), facecolor='#f5f5dc')
for i, ax in enumerate(axes):
    draw_stochastic('F', organic_rules, iterations=4,
                    angle=22, angle_var=8,
                    step=1.0, step_var=0.3,
                    seed=i*42, ax=ax)
plt.suptitle('Stochastic Variations', fontsize=14)
plt.tight_layout()
plt.savefig(_img('stochastic.png'), dpi=150, bbox_inches='tight', facecolor='#f5f5dc')
plt.close()
_web('stochastic.png')

import trimesh

@dataclass
class Turtle3D:
    """3D turtle with position and orientation."""
    pos: np.ndarray = None
    heading: np.ndarray = None
    left: np.ndarray = None
    up: np.ndarray = None

    def __post_init__(self):
        if self.pos is None:
            self.pos = np.array([0.0, 0.0, 0.0])
        if self.heading is None:
            self.heading = np.array([0.0, 0.0, 1.0])  # +Z is up
        if self.left is None:
            self.left = np.array([-1.0, 0.0, 0.0])
        if self.up is None:
            self.up = np.array([0.0, 1.0, 0.0])

    def copy(self):
        return Turtle3D(
            self.pos.copy(), self.heading.copy(),
            self.left.copy(), self.up.copy()
        )

    def forward(self, distance):
        start = self.pos.copy()
        self.pos = self.pos + self.heading * distance
        return start, self.pos.copy()

    def rotate(self, axis, angle_deg):
        angle = np.radians(angle_deg)
        def rotate_vec(v, k, theta):
            c, s = np.cos(theta), np.sin(theta)
            return v * c + np.cross(k, v) * s + k * np.dot(k, v) * (1 - c)
        self.heading = rotate_vec(self.heading, axis, angle)
        self.left = rotate_vec(self.left, axis, angle)
        self.up = rotate_vec(self.up, axis, angle)

    def yaw(self, angle):
        self.rotate(self.up, angle)

    def pitch(self, angle):
        self.rotate(self.left, angle)

    def roll(self, angle):
        self.rotate(self.heading, angle)


def generate_3d_lsystem(axiom, rules, iterations, angle=25.0, step=1.0):
    """Generate 3D L-system, return list of (start, end, depth) segments."""
    instructions = apply_rules(axiom, rules, iterations)
    turtle = Turtle3D()
    stack = []
    segments = []
    depth = 0

    for cmd in instructions:
        if cmd == 'F':
            start, end = turtle.forward(step)
            segments.append((start, end, depth))
        elif cmd == '+':
            turtle.yaw(angle)
        elif cmd == '-':
            turtle.yaw(-angle)
        elif cmd == '&':
            turtle.pitch(angle)
        elif cmd == '^':
            turtle.pitch(-angle)
        elif cmd == '\\':
            turtle.roll(angle)
        elif cmd == '/':
            turtle.roll(-angle)
        elif cmd == '[':
            stack.append((turtle.copy(), depth))
            depth += 1
        elif cmd == ']':
            turtle, depth = stack.pop()

    return segments

def create_branch_mesh(start, end, radius, segments=6):
    """Create a cylinder mesh between two points."""
    direction = end - start
    length = np.linalg.norm(direction)
    if length < 1e-6:
        return None

    cylinder = trimesh.creation.cylinder(radius=radius, height=length, sections=segments)

    direction_norm = direction / length
    z_axis = np.array([0, 0, 1])

    if np.allclose(direction_norm, z_axis):
        rotation_matrix = np.eye(4)
    elif np.allclose(direction_norm, -z_axis):
        rotation_matrix = trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0])
    else:
        axis = np.cross(z_axis, direction_norm)
        axis = axis / np.linalg.norm(axis)
        angle = np.arccos(np.clip(np.dot(z_axis, direction_norm), -1, 1))
        rotation_matrix = trimesh.transformations.rotation_matrix(angle, axis)

    center = (start + end) / 2
    translation = trimesh.transformations.translation_matrix(center)

    cylinder.apply_transform(rotation_matrix)
    cylinder.apply_transform(translation)
    return cylinder


def lsystem_to_mesh(segments, base_radius=0.1, taper=0.7):
    """Convert L-system segments to a combined mesh."""
    meshes = []
    max_depth = max(d for _, _, d in segments) if segments else 0

    for start, end, depth in segments:
        radius = base_radius * (taper ** depth)
        mesh = create_branch_mesh(start, end, radius)
        if mesh is not None:
            t = depth / (max_depth + 1)
            color = [int(80 + 40*t), int(50 + 150*t), int(30), 255]
            mesh.visual.vertex_colors = color
            meshes.append(mesh)

    if meshes:
        return trimesh.util.concatenate(meshes)
    return None

tree_3d_rules = {
    'F': 'FF',
    'X': 'F[&+X][&-X][^X]'
}

segments = generate_3d_lsystem('X', tree_3d_rules, iterations=5, angle=28, step=0.5)
mesh = lsystem_to_mesh(segments, base_radius=0.08, taper=0.72)
mesh.export(_img('tree-3d.glb'))
_web('tree-3d.glb')

# 3D preview as 2D image
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

max_depth = max(d for _, _, d in segments)
for start, end, depth in segments:
    t = depth / (max_depth + 1)
    color = (0.3 + 0.2*t, 0.2 + 0.5*t, 0.1)
    lw = 2.0 * (0.75 ** depth)
    ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
            color=color, linewidth=lw)

ax.set_box_aspect([1, 1, 1.5])
ax.axis('off')
ax.view_init(elev=10, azim=45)

plt.savefig(_img('tree-3d-preview.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
_web('tree-3d-preview.png')

bush_rules = {
    'F': 'FF',
    'X': 'F[-X][+X][&X][^X]'
}

segments = generate_3d_lsystem('X', bush_rules, iterations=5, angle=25, step=0.4)
mesh = lsystem_to_mesh(segments, base_radius=0.05, taper=0.78)
mesh.export(_img('bush-3d.glb'))
_web('bush-3d.glb')

# Tree Species Gallery
TREE_SPECIES = {
    'oak': {
        'axiom': 'X',
        'rules': {'F': 'FF', 'X': 'F[+X]F[-X]+X'},
        'angle': 30,
        'iterations': 6,
        'description': 'Broad, spreading crown'
    },
    'pine': {
        'axiom': 'X',
        'rules': {'F': 'FF', 'X': 'F[+X][-X]FX'},
        'angle': 25,
        'iterations': 7,
        'description': 'Conical, layered branches'
    },
    'willow': {
        'axiom': 'X',
        'rules': {'F': 'FF', 'X': 'F-[[X]+X]+F[+FX]-X'},
        'angle': 35,
        'iterations': 5,
        'description': 'Drooping, flowing branches'
    },
    'baobab': {
        'axiom': 'X',
        'rules': {'F': 'FFF', 'X': 'F[+X][-X]F[+X][-X]'},
        'angle': 50,
        'iterations': 4,
        'description': 'Thick trunk, wide crown'
    },
    'cypress': {
        'axiom': 'X',
        'rules': {'F': 'FF', 'X': 'F[+X]F[-X]FX'},
        'angle': 12,
        'iterations': 6,
        'description': 'Tall, columnar shape'
    },
    'bonsai': {
        'axiom': 'X',
        'rules': {'F': 'F', 'X': 'F[-X][+X]'},
        'angle': 40,
        'iterations': 8,
        'description': 'Compact, windswept'
    },
}

def draw_species(species_name, params, ax, seed=None):
    """Draw a tree species with optional randomness."""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    instructions = apply_rules(params['axiom'], params['rules'], params['iterations'])
    turtle = Turtle()
    stack = []
    lines = []
    depths = []
    depth = 0
    angle = params['angle']

    for cmd in instructions:
        if cmd == 'F':
            step = 1.0 * (0.85 ** depth)
            rad = np.radians(turtle.angle)
            new_x = turtle.x + step * np.cos(rad)
            new_y = turtle.y + step * np.sin(rad)
            lines.append(((turtle.x, turtle.y), (new_x, new_y)))
            depths.append(depth)
            turtle.x, turtle.y = new_x, new_y
        elif cmd == '+':
            turtle.angle -= angle + random.uniform(-5, 5)
        elif cmd == '-':
            turtle.angle += angle + random.uniform(-5, 5)
        elif cmd == '[':
            stack.append((turtle.copy(), depth))
            depth += 1
        elif cmd == ']':
            turtle, depth = stack.pop()

    if not lines:
        return

    max_depth = max(depths) if depths else 1
    for ((x1, y1), (x2, y2)), d in zip(lines, depths):
        lw = 3.0 * (0.7 ** d) + 0.2
        t = d / (max_depth + 1)
        color = (0.35 + 0.15*t, 0.25 + 0.35*t, 0.1)
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, solid_capstyle='round')

    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f"{species_name.replace('_', ' ').title()}\n{params['description']}", fontsize=10)

# Generate Tree Species Gallery
fig, axes = plt.subplots(2, 3, figsize=(15, 12), facecolor='#f9f9f9')
axes = axes.flatten()

for idx, (species, params) in enumerate(TREE_SPECIES.items()):
    draw_species(species, params, axes[idx], seed=42)

plt.suptitle('Tree Species Gallery', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(_img('tree-species.png'), dpi=150, bbox_inches='tight', facecolor='#f9f9f9')
plt.close()
_web('tree-species.png')

if __name__ == '__main__':
    print()
    print(f"Done! Check the '{OUTPUT_DIR}' folder for generated files.")
