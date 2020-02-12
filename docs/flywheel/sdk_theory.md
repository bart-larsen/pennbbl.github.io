---
layout: default
title: Flywheel SDK Theory
parent: Flywheel
nav_order: 3
---

# Using the SDK: Theory


## Client objects

Whenever you use the Flywheel SDK, you communicate with Flywheel using a *client*. All actions that use the SDK begin with creating a client, which looks like this

```python
>>> import flywheel
>>> fw = flywheel.Client()
```

where the `fw` object is the client. In order to connect to flywheel using the `Client()` function, you need to have [logged in](https://docs.flywheel.io/hc/en-us/articles/360008162214) to flywheel using the commandline tool.

Under the hood, the client object translates your interactions with it into http requests that are sent back and forth with the Flywheel server. In this way, you are able to tell the Flywheel server to change metadata, add or delete files, or run gears.

## Data containers
Analysis gears store their results in a Flywheel data *container*. This terminology can be confusing, because gears are [containerized](https://en.wikipedia.org/wiki/OS-level_virtualization) pipelines. To disambiguate between software containers and the entities Flywheel uses to store data, we will refer to these as *data containers*. A data container could be a Acquisition, Analysis, Subject, Session or Project. Files stored in Flywheel all exist inside a container. When [downloading data](/docs/flywheel/sdk_getting) or [uploading data](https://docs.flywheel.io/hc/en-us/articles/360019252953-CLI-reference-guide-fw-upload), you will need to specify which container will house the file(s).
