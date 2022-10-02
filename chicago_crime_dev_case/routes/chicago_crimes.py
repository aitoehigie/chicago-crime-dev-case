from typing import List, Union
import os
import json
import cachetools, functools

from fastapi import APIRouter, Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from sqlmodel import Session, or_, select

from ..db import ActiveSession
from ..models.chicago_crimes import CrimeIncoming, CrimeResponse
from ..security import AuthenticatedUser, User, get_current_user

import pandas as pd
from google.cloud import bigquery

from chicago_crime_dev_case.config import settings

router = APIRouter()

#BigQuery Client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=settings.get("GOOGLE_APPLICATION_CREDENTIALS")
client = bigquery.Client()

def async_ttl_cache(ttl: int = 3600, maxsize: int = 1):
    cache = cachetools.TTLCache(ttl=ttl, maxsize=maxsize)

    def decorator(fn):
        @functools.wraps(fn)
        async def memoize(*args, **kwargs):
            key = str((args, kwargs))
            try:
                cache[key] = cache.pop(key)
            except KeyError:
                cache[key] = await fn(*args, **kwargs)
            return cache[key]
        return memoize

    return decorator 


@router.get("/", response_model=List[CrimeResponse])
@async_ttl_cache()
async def chicago_crimes(*, session: Session = ActiveSession):
    QUERY = ('SELECT * FROM `bigquery-public-data.chicago_crime.crime`'
             'LIMIT 100'
    )
    query_job = client.query(QUERY)
    query_result = query_job.result()
    df = query_result.to_dataframe()
    crime_data = json.loads(df.to_json(orient = "records"))
    return crime_data

