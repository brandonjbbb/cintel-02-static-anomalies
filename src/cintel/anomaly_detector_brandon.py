"""
anomaly_detector_yourname.py - Modified project script.

Author: Brandon Jean-Baptiste
Date: 2026-03-20

Modification summary
- Added validation for missing and negative values.
- Changed anomaly logic to flag:
    1) ages below 0 or above 16
    2) heights below 0 or above 72
    3) very unusual height-for-age values using age-group averages
- Added an anomaly_reason column so results are easier to interpret.

Run from repo root:

    uv run python -m cintel.anomaly_detector_brandon
"""

import logging
from pathlib import Path
from typing import Final

import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

LOG: logging.Logger = get_logger("P2", level="DEBUG")

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "clinic_data_yourname.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "anomalies_yourname.csv"


def main() -> None:
    """Run the modified anomaly detection pipeline."""
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # STEP 1: READ DATA
    df: pl.DataFrame = pl.read_csv(DATA_FILE)
    LOG.info(f"Loaded {df.height} patient records")

    # STEP 2: BASIC VALIDATION
    LOG.info("Checking for missing or invalid values...")

    missing_age = df.filter(pl.col("age_years").is_null()).height
    missing_height = df.filter(pl.col("height_inches").is_null()).height

    LOG.info(f"Missing age_years values: {missing_age}")
    LOG.info(f"Missing height_inches values: {missing_height}")

    # Remove rows with nulls before analysis
    df = df.drop_nulls(["age_years", "height_inches"])

    # STEP 3: DEFINE RULES
    LOG.info("Applying anomaly detection rules...")

    MIN_AGE: Final[float] = 0.0
    MAX_AGE: Final[float] = 16.0
    MIN_HEIGHT: Final[float] = 0.0
    MAX_HEIGHT: Final[float] = 72.0

    LOG.info(f"MIN_AGE: {MIN_AGE}")
    LOG.info(f"MAX_AGE: {MAX_AGE}")
    LOG.info(f"MIN_HEIGHT: {MIN_HEIGHT}")
    LOG.info(f"MAX_HEIGHT: {MAX_HEIGHT}")

    # Create age groups to compare patients with similar ages
    df = df.with_columns(
        pl.col("age_years").floor().alias("age_group")
    )

    # Compute average height for each age group
    age_group_stats = df.group_by("age_group").agg(
        pl.col("height_inches").mean().alias("avg_height_for_age")
    )

    # Join averages back to original data
    df = df.join(age_group_stats, on="age_group", how="left")

    # Add deviation from average
    df = df.with_columns(
        (pl.col("height_inches") - pl.col("avg_height_for_age")).abs().alias("height_diff_from_avg")
    )

    # Define anomaly reason
    df = df.with_columns(
        pl.when(pl.col("age_years") < MIN_AGE)
        .then(pl.lit("age below 0"))
        .when(pl.col("age_years") > MAX_AGE)
        .then(pl.lit("age above 16"))
        .when(pl.col("height_inches") < MIN_HEIGHT)
        .then(pl.lit("height below 0"))
        .when(pl.col("height_inches") > MAX_HEIGHT)
        .then(pl.lit("height above 72 inches"))
        .when(pl.col("height_diff_from_avg") >= 8)
        .then(pl.lit("height unusually far from age-group average"))
        .otherwise(pl.lit(None))
        .alias("anomaly_reason")
    )

    anomalies_df = df.filter(pl.col("anomaly_reason").is_not_null())

    LOG.info(f"Count of anomalies found: {anomalies_df.height}")

    # STEP 4: SAVE OUTPUT
    anomalies_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote anomalies file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


if __name__ == "__main__":
    main()
