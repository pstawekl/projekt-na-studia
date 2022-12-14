# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Information(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Information - a model defined in OpenAPI

        status: The status of this Information.
        affected: The affected of this Information.
        message: The message of this Information.
    """

    status: int = Field(alias="status")
    affected: int = Field(alias="affected")
    message: str = Field(alias="message")

Information.update_forward_refs()
