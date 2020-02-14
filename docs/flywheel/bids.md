---
layout: default
title: BIDS Curation
parent: Flywheel
nav_order: 2
---

# BIDS Curation

## Introduction

[Brain Imaging Data Structure (or BIDS)](https://bids.neuroimaging.io) is an important recent development in the neuroimaging field that provides guidelines on how to structure, name, and share neuroimaging data. By adhering to the BIDS specifications, you can:

- Save time trying to understand and reuse data acquired by other scientists
- Jump right in to using a plethora of data analysis tools (BIDS apps) that understand BIDS data with little to no hassle
- Export and share neuroimaging datasets with ease
- Quickly validate and identify problems with your data before putting them through processing or analysis pipelines

Flywheel supports BIDS and BIDS apps primarily as its means of curation. They have an out-of-the-box utility gear for curation (`curate-bids`) that is available to all users; unfortunately, for some of our legacy data we found that this tool was somewhat inflexible to our needs. In lieu of this, we developed `fw-heudiconv` (pronounced /f wu di kɑ n(v)/) — a Python driven toolkit for BIDS curation on Flywheel. As the name suggests, it is in many ways a port of the common neuroimaging tool [`heudiconv`](https://heudiconv.readthedocs.io/en/latest/) developed by NiPy. Our tool allows us to build on their work and implement BIDS curation on Flywheel.

In this tutorial we will discuss more about BIDS, and then go through how to use `fw-heudiconv` to curate your data. We've found that this is most useful in cases where one is curating legacy data, so we will start there.


## Curating a legacy project

### Writing a heuristic



## Preparing sequences for a new project

### Automatically curating ReproIn
