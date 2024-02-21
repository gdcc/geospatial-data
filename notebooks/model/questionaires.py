"""
This file contains Pydantic models that are used as schemas to parse data into using GPT4.

The models defined in this file are:

- TemporalCoverage: Represents the start and end date/time of the data collection period.

- SpatialCoverage:  Represents the spatial coverage of the data collection period, including 
                    coordinates, bounding box, locations, longitude, and latitude.
                    
- Variable: Represents a variable in the data collection period, including its name and unit.

- Issue: Represents known inaccuracies and missing values in the data.

- ResponseModel: Represents the overall response model, including temporal coverage, 
                 spatial coverage, time frequency, variable names, convention, spatial resolution, 
                 coordinate system, accuracy issues, timestamp format, data collection method, 
                 software, and data sources.
"""

from typing import Optional
from pydantic import BaseModel, Field


class TemporalCoverage(BaseModel):
    start: Optional[str] = Field(
        default=None,
        description="The start date/time of the data collection period.",
    )

    end: Optional[str] = Field(
        default=None,
        description="The end date/time of the data collection period.",
    )


class SpatialCoverage(BaseModel):
    coordinates: Optional[list[float]] = Field(
        default=None,
        description="The coordinates of the data collection period.",
    )

    bounding_box: Optional[list[float]] = Field(
        default=None,
        description="The bounding box of the data collection period.",
    )

    locations: Optional[list[str]] = Field(
        default=None,
        description="The locations of the data collection period.",
    )

    longitude: Optional[list[float]] = Field(
        default=None,
        description="The longitude of the data collection period.",
    )

    latitude: Optional[list[float]] = Field(
        default=None,
        description="The latitude of the data collection period.",
    )

    start_location: Optional[str] = Field(
        default=None,
        description="The start location of the data collection period.",
    )

    end_location: Optional[str] = Field(
        default=None,
        description="The end location of the data collection period.",
    )


class Variable(BaseModel):
    name: Optional[str] = Field(
        default=None,
        description="The name of the variable.",
    )

    unit: Optional[str] = Field(
        default=None,
        description="The unit of the variable.",
    )


class Issue(BaseModel):
    known_inaccuracies: Optional[bool] = Field(
        default=None,
        description="The data has known inaccuracies.",
    )

    missing_values: Optional[bool] = Field(
        default=None,
        description="The data has missing values.",
    )


class ResponseModel(BaseModel):
    temporal_coverage: Optional[TemporalCoverage] = Field(
        default=None,
        description="The start and end date of the data collection period.",
    )

    spatial_coverage: Optional[SpatialCoverage] = Field(
        default=None,
        description="The spatial coverage (coordinates, bounding box, locations, longitude, latitude) of the data collection period.",
    )

    time_frequency: Optional[float] = Field(
        default=None,
        description="The time frequency (hourly, daily, weekly) of the data collection period.",
    )

    variable_names: list[Variable] = Field(
        default_factory=list, description="The variables of the data collection period."
    )

    convention: Optional[str] = Field(
        default=None,
        description="The data encoding (CF, EPSG, etc) of the data collection period.",
    )

    spatial_resolution: Optional[float] = Field(
        default=None,
        description="The spatial resolution (e.g., scale, grid, city-level, street-level, state-level) of the data collection period.",
    )

    coordinate_system: Optional[str] = Field(
        default=None,
        description="The coordinate system (e.g., WGS84, EPSG:4326) of the data collection period.",
    )

    accuracy_issues: Optional[Issue] = Field(
        default=None,
        description="The accuracy issues (e.g., missing values, outliers, etc) of the data collection period.",
    )

    timestamp_format: Optional[str] = Field(
        default=None,
        description="The timestamp format (e.g., ISO 8601, UNIX, etc) of the data collection period.",
    )

    data_collection_method: Optional[str] = Field(
        default=None,
        description="How was the location or time data collected (e.g., sensor readings, satellite, manual input)",
    )

    software: list[str] = Field(
        default_factory=list,
        description="Software used to capture, produce or analyze the data (version)",
    )

    data_sources: list[str] = Field(
        default_factory=list,
        description="Who provisioned/gathered the data (e.g., institution, university, organization, company, etc)",
    )
