# ScoreSheets
### A tool for calculating activity points from certificates of co-curricular activities for colleges under KTU university.
![Logo](https://user-images.githubusercontent.com/36796068/216495907-bacfde09-d0e4-405b-ace6-2b9e37c5bc35.png)

## Installing Conda

For using this application we recommend running it in a conda environment.
Refer the official documentation on how to install conda: https://docs.anaconda.com/free/miniconda/#latest-miniconda-installer-links

## Setting Up a Conda Enviroment

1. Create a conda environment:
```bash
conda create -n ScoreSheets python=3.10.12
```
2. Activate the environment:
```bash
conda activate ScoreSheets
```

## Setting Up
1.  Clone the [repository](https://github.com/henokjackson/ScoreSheets):
```bash
git clone https://github.com/henokjackson/ScoreSheets.git
```
2. Open the directory:
```bash
cd ScoreSheets
```
3. Install the required python packages:
```bash
pip install -r requirements.txt
```
4. Install fonts:
```bash
sh install_fonts.sh
```
5. Download SpaCy packages
```bash
python3 download_spacy_packages.py
```

## Running ScoreSheets
To run the application:
```bash
python3 main.py
```
