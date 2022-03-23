# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.config import settings
from app.database import get_db
from app.database import Base
from .database import client, session


def test_create_user(client, session):
    res = client.post('/users/', json={'email':'asda@sdf.ff','password':'sdfsd'})

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'asda@sdf.ff'
    assert res.status_code == 201


def test_hello(client):
    response = client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'message':'Hello world'}
