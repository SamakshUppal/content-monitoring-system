# Content Monitoring & Flagging System

## Overview

This project is a backend system built using Django and Django REST Framework that monitors content based on user-defined keywords, generates flags based on matches, and supports a review workflow with suppression logic.

## Features

* Add keywords via API
* Scan content (mock dataset used)
* Keyword matching with scoring:

  * Exact match in title → 100
  * Partial match in title → 70
  * Match in body → 40
* Review workflow:

  * pending
  * relevant
  * irrelevant
* Suppression logic:

  * If a flag is marked irrelevant, it will not reappear unless the content is updated

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

## API Endpoints

| Method | Endpoint     | Description        |
| ------ | ------------ | ------------------ |
| POST   | /keywords/   | Add a keyword      |
| POST   | /scan/       | Run scan           |
| GET    | /flags/      | Get all flags      |
| PATCH  | /flags/{id}/ | Update flag status |

## Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Assumptions

* Used mock data instead of external API
* Case-insensitive keyword matching
* Avoided duplicate content using get_or_create

## Key Logic

* Matching logic implemented in service layer
* Suppression logic uses last_updated vs last_reviewed_at

## Example API Usage

### Add Keyword
POST /keywords/
{
  "name": "django"
}

### Run Scan
POST /scan/

### Get Flags
GET /flags/

### Update Flag
PATCH /flags/1/
{
  "status": "irrelevant"
}
