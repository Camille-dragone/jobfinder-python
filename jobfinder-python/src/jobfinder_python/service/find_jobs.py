from jobfinder_python.api.api_model import FindJobsDto, Job
from jobfinder_python.logging.logging import app_logger
import os
import requests
from typing import List, Dict, Any


def find_jobs(find_jobs_dto: FindJobsDto):
    app_logger.info(f"Find jobs service called...")
    jobs: List[Job] = []
    try:
        # Search jobs with google jobs 
        google_jobs = search_jobs_with_google_jobs(find_jobs_dto)
        print(google_jobs)
        jobs.extend(google_jobs)
    except Exception as e:
        app_logger.error(f"Error finding jobs: {e}")
        raise e
    return jobs

def search_jobs_with_google_jobs(find_jobs_dto: FindJobsDto):
    app_logger.info(f"Searching jobs with google jobs...")

    try:
        search_text = f"{find_jobs_dto.job_title} {find_jobs_dto.job_location}"
        x = 1
        if not search_text or not search_text.strip():
            raise ValueError("Le paramètre 'text' ne peut pas être vide.")
        if x < 1:
            raise ValueError("Le paramètre 'x' doit être >= 1.")

        api_key = os.getenv("SERPAPI_API_KEY")
        if not api_key:
            raise ValueError(
                "Clé API manquante. Passe api_key=... ou définis SERPAPI_API_KEY."
            )

        url = "https://serpapi.com/search.json"
        results: List[Job] = []
        next_page_token: str | None = None

        session = requests.Session()

        while len(results) < x:
            params: Dict[str, Any] = {
                "engine": "google_jobs",
                "q": search_text,
                "api_key": api_key,
                "google_domain": "google.com",
            }

            # Paramètres optionnels
            params["gl"] = "fr"
            params["hl"] = "fr"
            if next_page_token:
                params["next_page_token"] = next_page_token

            try:
                resp = session.get(url, params=params, timeout=30)
                resp.raise_for_status()
                data = resp.json()
            except requests.RequestException as e:
                raise RuntimeError(f"Erreur HTTP SerpApi: {e}") from e
            except ValueError as e:
                raise RuntimeError("Réponse SerpApi non-JSON ou invalide.") from e

            if "error" in data:
                raise RuntimeError(f"Erreur SerpApi: {data['error']}")

            jobs = data.get("jobs_results", []) or []
            if not jobs:
                break

            for job in jobs:
                job = Job(
                    title=job["title"],
                    company=job["company_name"],
                    location=job["location"],
                    source=job["via"],
                    description=job["description"],
                    url=job["share_link"],
                    company_logo=job["thumbnail"],
                    extensions=job["extensions"],
                    raw=job
                )
                results.append(job)
                if len(results) >= x:
                    break

            next_page_token = (
                data.get("serpapi_pagination", {}) or {}
            ).get("next_page_token")

            if not next_page_token:
                break            
    except Exception as e:
        app_logger.error(f"Error searching jobs with google jobs: {e}")
        raise e

    return results