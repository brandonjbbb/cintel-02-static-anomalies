# cintel-02-static-anomalies

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for continuous intelligence.

Continuous intelligence systems monitor data streams, detect change, and respond in real time.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project introduces **static anomaly detection**.

The goal is to copy this repository,
set up your environment,
run the example analysis,
and explore how anomalies are identified in static data.

You will run the example pipeline, read the code,
and make small modifications to understand how
the detection logic works.

## Data

The example pipeline reads **pediatric clinic** age and height
data from: `data/clinic_data_brandon.csv`.
It creates reasonable thresholds and outputs
**anomalies** (data outside the expected threshold).

I copied the example Python file and made my own modified version
to analyze `data/clinic_data_yourname.csv`.

## Working Files

You'll work with just these areas:

- **data/** - it starts with the data
- **docs/** - tell the story
- **src/cintel/** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## My Modification

I created a modified anomaly detector based on the example pipeline.

### What I changed

- Added validation checks for missing values in `age_years` and `height_inches`
- Expanded anomaly detection to flag:
  - ages below 0 or above 16
  - heights below 0 or above 72 inches
  - heights that are unusually far from the average height for the same age group
- Added an `anomaly_reason` column to explain why each record was flagged

### Why I made the change

I wanted the anomaly detector to be more informative and realistic.
The original example only checked fixed upper thresholds.
My updated version still checks thresholds, but also compares each patient's height
to the average height of similar ages.

### What I observed

After running the modified pipeline, the project completed successfully
and produced an anomalies output file in the `artifacts/` folder.
The results were easier to interpret because each flagged row included
a reason explaining why it was marked as an anomaly.

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Pipeline executed successfully!
========================
