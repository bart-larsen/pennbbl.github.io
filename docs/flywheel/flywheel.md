---
layout: default
title: Flywheel
nav_order: 3
has_children: true
permalink: docs/flywheel
---

# Using UPenn's Flywheel Instance
{: .no_toc }

Data collected at UPenn research scanners is anonymized and uploaded to
[Flywheel](https://upenn.flywheel.io). You need a PennKey to log in to Flywheel and
need to be added to projects by your lab's Flywheel administrator. In addition
to storing data, Flywheel can also process your data with its "gears". You will
interact with Flywheel either through your web browser or using the Flywheel
Standard Development Kit (SDK) from Python.
{: .fs-6 .fw-300 }


## Connecting with a browser

In any browser (preferably Google Chrome), you can access Flywheel by visiting upenn.flywheel.io.


## Connecting with the SDK

The flywheel CLI allows fw-heudiconv (or any other program you write) to communicate with Flywheel’s database. Follow their instructions here:

https://docs.flywheel.io/hc/en-us/articles/360008162214

Once installed and logged in, you should see your username when you do:
```
$ fw status
$ You are currently logged in as Tinashe Tapera to https://upenn.flywheel.io
```

## Using the Python SDK

As long as you have run the `fw login` operation from the previous
