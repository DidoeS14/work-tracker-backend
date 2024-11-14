
# Work Tracker Backend

This is a really simple backend server for a small project for tracking worked hours and daily reports in presumably a company or some organization.


## About the project

The frontend for this project can be found [here](https://github.com/DidoeS14/work-tracker-frontend?tab=readme-ov-file). It is needed since you need to either run it while the backend is running or build it place the produced "dist" folder inside of the root folder of this project.

The server will generate a file data/time_and_reports.csv where all user logs for hours and reports are stored. It can be loaded in Excel or it can be used all sorts of analytics.

Changelog can be found [here](changelog.txt). 
## Run Locally

Clone the project

```bash
  git clone https://github.com/DidoeS14/work-tracker-backend
```

Go to the project directory

```bash
  cd work-tracker-backend
```

Activate the virtual environment and install the requirements

```bash
  venv\Scripts\activate 
  pip install -r req.txt
```
Run the project

```bash
  py main.py
```

## Related

Frontend project:

[Work Tracker Frontend](https://github.com/DidoeS14/work-tracker-frontend?tab=readme-ov-file)

