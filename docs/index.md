# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Your Files** - how to copy the example and create your version
- **Glossary** - project terms and concepts

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

## Custom Project
I created a custom anomaly detection project based on the example static clinic pipeline. I modified the logic to improve validation and make the anomaly output easier to understand.
### Dataset
I used a static clinic dataset containing patient age in years and height in inches. Each row represented one patient record, and the data was read from a CSV file.

### Signals
The main signals used were age_years and height_inches from the dataset. I also created derived signals such as age_group, average height for age, and height difference from the age-group average.

### Experiments
I tested modifications by adding validation checks for missing values and by expanding the anomaly rules beyond simple upper thresholds. I also added anomaly reasons so I could see exactly why each record was flagged.

### Results
The modified pipeline ran successfully and generated an anomalies output file in the artifacts folder. The results were more informative because flagged rows included a reason and reflected both threshold issues and unusual height patterns by age.

### Interpretation
This means the system became more useful for identifying suspicious records instead of only catching obvious extreme values. The business intelligence gained is that adding validation and context-based rules improves data quality monitoring and makes anomaly results more actionable.
