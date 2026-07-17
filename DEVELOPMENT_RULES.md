# Development Rules

## Rule 1

Never start implementing before requirements are frozen.

---

## Rule 2

Build in this order:

1. Project scaffold
2. Camera + overlay
3. Detector
4. Model export
5. Gesture system
6. Dashboard
7. Focus logic
8. Integration
9. Deployment
10. Polish

Never change order without reason.

---

## Rule 3

Use milestone commits.

Bad:

Initial commit

Final commit

Good:

feat: create project scaffold

feat: add camera overlay

feat: implement detector pipeline

feat: integrate gesture cursor

perf: optimize inference

build: prepare deployment

---

## Rule 4

One commit = one meaningful completed unit.

Do not commit:

* unfinished code
* temporary experiments
* datasets
* weights

---

## Rule 5

Git Structure

Branches:

main
dev

Work:

dev

Stable:

main

---

## Rule 6

Do not commit:

datasets/
weights/
cache/
outputs/
checkpoints/

Use .gitignore.

---

## Rule 7

Keep modules independent:

vision/
ui/
gesture/
logic/
deployment/

Avoid tight coupling.

---

## Rule 8

Every major milestone must include:

* commit
* screenshot
* notes

---

## Rule 9

Every completed phase updates README.

---

## Rule 10

Prioritize:

deployability

>

maintainability

>

extra features
