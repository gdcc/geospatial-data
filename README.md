# Data and Code for "Open Source Tools for Geospatial Data Management and Analysis with GPT-4"

## Abstract

This study investigates the challenges associated with managing high-dimensional geospatial data across various fields such as economics, biostatistics, epidemiology, environmental health, and sciences. We present the current state of geospatial data in Dataverse and introduce novel tools and advancements for enhancing data management and utilization. A significant focus is on evaluating the effectiveness of automatic metadata extraction using GPT-4 for geospatial datasets in the Harvard Dataverse repository.

The repository contains data and code for the landscape analysis of geospatial data in Dataverse and the analysis with GPT-4. 
Open source tools presented in the paper are part of the [Dataverse](https://github.com/IQSS/dataverse) and [EasyDataverse](https://github.com/gdcc/easyDataverse) repositories.


## Repository Structure

```
├── README.md                  : This file
├── data/                      : Folder containing sample datasets and metadata for analysis
├── notebooks/                 : Jupyter notebooks with analysis and code
├── scripts/                   : Python scripts for Dataverse metadata retrival
├── requirements.txt           : Required Python packages for replicating the study
└── results/                   : Generated figures 
```

## Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab

## Installation

1. Clone this repository to your local machine.
2. Install required Python packages using `pip install -r requirements.txt`.

## Data

The `data/` folder includes metadata, Dataverse statistics and GPT-4 ratings used in this study. 

## Usage

- **Metadata Retrival from Dataverse and GPT-4**: Scripts for metadata retrival and evaluation with GPT-4 are located in `scripts/`. 
- **Analysis**: Jupyter notebooks in `notebooks/` contain the exploratory data analysis (EDA) and the evaluation of the automatic metadata extraction feature.

## Contributing

Contributions to this study are welcome. Please open an issue or a pull request in the repository.

## Citation

If you use the code or data from this study, please cite it as follows:

```
TBD
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Harvard Dataverse for providing access to geospatial datasets.
- OpenAI for the GPT-4 model.
- Dataverse Geospatial Working Group