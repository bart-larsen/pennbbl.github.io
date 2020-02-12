---
layout: default
title: "Getting Data from Flywheel"
parent: Flywheel
nav_order: 4
---

## Requirements

These tutorials require

  * A local installation or [Python](/docs/Basics/basics/#installing-python)
  * [Logging in](/docs/flywheel/#connecting-with-the-sdk) to Flywheel using the CLI


# Getting data from Flywheel

Flywheel stores data and its accompanying metadata in a proprietary system in the cloud. This data can be downloaded manually using the web interface or through the SDK. The process of getting data from Flywheel involves two steps

  1. Finding the data's [container](/docs/flywheel/sdk_theory/#data-containers)
  2. Finding the file object and downloading it or a part of it



## Accessing data in Python

Suppose we ran FMRIPREP and would like to download some of its outputs. In this example FMRIPREP was run and attached to a session container (it could also be attached to a subject or project). The first step is to find the session container:

```python
>>> import flywheel
>>> fw = flywheel.Client()
>>> session_id = "5cd31cbc08a9960041650843"
>>> analysis = fw.get_container_analyses(
...     session_id, filter='label="fmriprep 06/03/2019 10:58:53"')[0]
>>> print(analysis.label)
fmriprep 06/03/2019 10:58:53
```

In this case we know that there is only one analysis with this name so we access it from the list that is returned by indexing at `[0]`. Now we can see which files are attached to this analysis data container:

```python
>>> print("\n".join([file_obj.name for file_obj in analysis.files]))
sub-01_5cf535cb36da2300443b2fb9.html.zip
fmriprep_work_sub-01_5cf535cb36da2300443b2fb9.zip
fmriprep_sub-01_5cf535cb36da2300443b2fb9.zip
```

These are the names of each file object attached to the container. We can get one of these by asking the client for it:

```python

```

### Data container information



### File attachments

## Downloading specific files

## Downloading BIDS

### Using the CLI

We don't recommend using this approach, but it is possible to use the Flywheel CLI
to download BIDS directly without using Python. See their documentation for
[usage](https://docs.flywheel.io/hc/en-us/articles/360008224093-Command-Line-Interface-Overview).

### Using `fw-heudiconv-export`

## Downloading analysis results

### Accessing zip members
