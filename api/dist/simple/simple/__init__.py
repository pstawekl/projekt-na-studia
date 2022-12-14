import pathlib

from open_alchemy import init_json

parent_path = pathlib.Path(__file__).parent.absolute()
init_json(parent_path / "spec.json")


"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models

Base = models.Base  # type: ignore


class _LinkDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int


class LinkDict(_LinkDictBase, total=False):
    """TypedDict for properties that are not required."""

    BeginNodeID: typing.Optional[int]
    EndNodeID: typing.Optional[int]
    Length: typing.Optional[float]


class TLink(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        BeginNodeID: none
        EndNodeID: none
        Length: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    BeginNodeID: 'sqlalchemy.Column[typing.Optional[int]]'
    EndNodeID: 'sqlalchemy.Column[typing.Optional[int]]'
    Length: 'sqlalchemy.Column[typing.Optional[float]]'

    def __init__(self, ID: int, BeginNodeID: typing.Optional[int] = None, EndNodeID: typing.Optional[int] = None, Length: typing.Optional[float] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            BeginNodeID: none
            EndNodeID: none
            Length: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, BeginNodeID: typing.Optional[int] = None, EndNodeID: typing.Optional[int] = None, Length: typing.Optional[float] = None) -> "TLink":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            BeginNodeID: none
            EndNodeID: none
            Length: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TLink":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> LinkDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Link: typing.Type[TLink] = models.Link  # type: ignore


class _MethodDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int
    MethodDefID: int
    PipelineID: int


class MethodDict(_MethodDictBase, total=False):
    """TypedDict for properties that are not required."""

    Name: typing.Optional[str]


class TMethod(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        MethodDefID: The MethodDefID of the Method.
        PipelineID: The PipelineID of the Method.
        Name: The Name of the Method.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    MethodDefID: 'sqlalchemy.Column[int]'
    PipelineID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, ID: int, MethodDefID: int, PipelineID: int, Name: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            MethodDefID: The MethodDefID of the Method.
            PipelineID: The PipelineID of the Method.
            Name: The Name of the Method.

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, MethodDefID: int, PipelineID: int, Name: typing.Optional[str] = None) -> "TMethod":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            MethodDefID: The MethodDefID of the Method.
            PipelineID: The PipelineID of the Method.
            Name: The Name of the Method.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMethod":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MethodDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Method: typing.Type[TMethod] = models.Method  # type: ignore


class _MethodDefDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int


class MethodDefDict(_MethodDefDictBase, total=False):
    """TypedDict for properties that are not required."""

    Name: typing.Optional[str]


class TMethodDef(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        Name: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, ID: int, Name: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            Name: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, Name: typing.Optional[str] = None) -> "TMethodDef":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            Name: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMethodDef":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MethodDefDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


MethodDef: typing.Type[TMethodDef] = models.MethodDef  # type: ignore


class _MethodParamDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    MethodParamDefID: int
    MethodID: int


class MethodParamDict(_MethodParamDictBase, total=False):
    """TypedDict for properties that are not required."""

    Value: typing.Optional[str]


class TMethodParam(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        MethodParamDefID: none
        MethodID: none
        Value: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    MethodParamDefID: 'sqlalchemy.Column[int]'
    MethodID: 'sqlalchemy.Column[int]'
    Value: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, MethodParamDefID: int, MethodID: int, Value: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            MethodParamDefID: none
            MethodID: none
            Value: none

        """
        ...

    @classmethod
    def from_dict(cls, MethodParamDefID: int, MethodID: int, Value: typing.Optional[str] = None) -> "TMethodParam":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            MethodParamDefID: none
            MethodID: none
            Value: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMethodParam":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MethodParamDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


MethodParam: typing.Type[TMethodParam] = models.MethodParam  # type: ignore


class _MethodParamDefDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int


class MethodParamDefDict(_MethodParamDefDictBase, total=False):
    """TypedDict for properties that are not required."""

    MethodDefID: typing.Optional[int]
    Name: typing.Optional[str]
    DataType: typing.Optional[str]


class TMethodParamDef(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        MethodDefID: none
        Name: none
        DataType: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    MethodDefID: 'sqlalchemy.Column[typing.Optional[int]]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'
    DataType: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, ID: int, MethodDefID: typing.Optional[int] = None, Name: typing.Optional[str] = None, DataType: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            MethodDefID: none
            Name: none
            DataType: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, MethodDefID: typing.Optional[int] = None, Name: typing.Optional[str] = None, DataType: typing.Optional[str] = None) -> "TMethodParamDef":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            MethodDefID: none
            Name: none
            DataType: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMethodParamDef":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MethodParamDefDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


MethodParamDef: typing.Type[TMethodParamDef] = models.MethodParamDef  # type: ignore


class _NodeDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int
    Type: str


class NodeDict(_NodeDictBase, total=False):
    """TypedDict for properties that are not required."""

    TrendID: typing.Optional[int]
    Name: typing.Optional[str]


class TNode(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        Type: none
        TrendID: none
        Name: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    Type: 'sqlalchemy.Column[str]'
    TrendID: 'sqlalchemy.Column[typing.Optional[int]]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, ID: int, Type: str, TrendID: typing.Optional[int] = None, Name: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            Type: none
            TrendID: none
            Name: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, Type: str, TrendID: typing.Optional[int] = None, Name: typing.Optional[str] = None) -> "TNode":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            Type: none
            TrendID: none
            Name: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TNode":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> NodeDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Node: typing.Type[TNode] = models.Node  # type: ignore


class _PipelineDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int


class PipelineDict(_PipelineDictBase, total=False):
    """TypedDict for properties that are not required."""

    Name: typing.Optional[str]
    BeginPos: typing.Optional[float]


class TPipeline(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        Name: none
        BeginPos: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'
    BeginPos: 'sqlalchemy.Column[typing.Optional[float]]'

    def __init__(self, ID: int, Name: typing.Optional[str] = None, BeginPos: typing.Optional[float] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            Name: none
            BeginPos: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, Name: typing.Optional[str] = None, BeginPos: typing.Optional[float] = None) -> "TPipeline":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            Name: none
            BeginPos: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TPipeline":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> PipelineDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Pipeline: typing.Type[TPipeline] = models.Pipeline  # type: ignore


class _PipelineNodeDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int
    NodeID: int


class PipelineNodeDict(_PipelineNodeDictBase, total=False):
    """TypedDict for properties that are not required."""

    First: typing.Optional[bool]


class TPipelineNode(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        NodeID: none
        First: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    NodeID: 'sqlalchemy.Column[int]'
    First: 'sqlalchemy.Column[typing.Optional[bool]]'

    def __init__(self, ID: int, NodeID: int, First: typing.Optional[bool] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            NodeID: none
            First: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, NodeID: int, First: typing.Optional[bool] = None) -> "TPipelineNode":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            NodeID: none
            First: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TPipelineNode":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> PipelineNodeDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


PipelineNode: typing.Type[TPipelineNode] = models.PipelineNode  # type: ignore


class _TrendDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int


class TrendDict(_TrendDictBase, total=False):
    """TypedDict for properties that are not required."""

    Name: typing.Optional[str]
    TrendGroupID: typing.Optional[int]
    TrendDefID: typing.Optional[int]


class TTrend(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        Name: none
        TrendGroupID: none
        TrendDefID: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'
    TrendGroupID: 'sqlalchemy.Column[typing.Optional[int]]'
    TrendDefID: 'sqlalchemy.Column[typing.Optional[int]]'

    def __init__(self, ID: int, Name: typing.Optional[str] = None, TrendGroupID: typing.Optional[int] = None, TrendDefID: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            Name: none
            TrendGroupID: none
            TrendDefID: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, Name: typing.Optional[str] = None, TrendGroupID: typing.Optional[int] = None, TrendDefID: typing.Optional[int] = None) -> "TTrend":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            Name: none
            TrendGroupID: none
            TrendDefID: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTrend":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TrendDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Trend: typing.Type[TTrend] = models.Trend  # type: ignore


class TrendDataDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    TrendID: int
    Time: int
    Data: str


class TTrendData(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        TrendID: none
        Time: none
        Data: The Data of the TrendData.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    TrendID: 'sqlalchemy.Column[int]'
    Time: 'sqlalchemy.Column[int]'
    Data: 'sqlalchemy.Column[bytes]'

    def __init__(self, TrendID: int, Time: int, Data: bytes) -> None:
        """
        Construct.

        Args:
            TrendID: none
            Time: none
            Data: The Data of the TrendData.

        """
        ...

    @classmethod
    def from_dict(cls, TrendID: int, Time: int, Data: bytes) -> "TTrendData":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            TrendID: none
            Time: none
            Data: The Data of the TrendData.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTrendData":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TrendDataDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


TrendData: typing.Type[TTrendData] = models.TrendData  # type: ignore


class TrendDefDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int
    Name: str
    TimeExponent: int
    Format: str
    SIUnitTID: str


class TTrendDef(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        Name: none
        TimeExponent: none
        Format: none
        SIUnitTID: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[str]'
    TimeExponent: 'sqlalchemy.Column[int]'
    Format: 'sqlalchemy.Column[str]'
    SIUnitTID: 'sqlalchemy.Column[str]'

    def __init__(self, ID: int, Name: str, TimeExponent: int, Format: str, SIUnitTID: str) -> None:
        """
        Construct.

        Args:
            ID: none
            Name: none
            TimeExponent: none
            Format: none
            SIUnitTID: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, Name: str, TimeExponent: int, Format: str, SIUnitTID: str) -> "TTrendDef":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            Name: none
            TimeExponent: none
            Format: none
            SIUnitTID: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTrendDef":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TrendDefDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


TrendDef: typing.Type[TTrendDef] = models.TrendDef  # type: ignore


class TrendGroupDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int
    Name: str
    AnalisisOnly: bool


class TTrendGroup(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        Name: none
        AnalisisOnly: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[str]'
    AnalisisOnly: 'sqlalchemy.Column[bool]'

    def __init__(self, ID: int, Name: str, AnalisisOnly: bool) -> None:
        """
        Construct.

        Args:
            ID: none
            Name: none
            AnalisisOnly: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, Name: str, AnalisisOnly: bool) -> "TTrendGroup":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            Name: none
            AnalisisOnly: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTrendGroup":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TrendGroupDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


TrendGroup: typing.Type[TTrendGroup] = models.TrendGroup  # type: ignore


class _TrendParamDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    TrendParamDefID: int
    TrendID: int


class TrendParamDict(_TrendParamDictBase, total=False):
    """TypedDict for properties that are not required."""

    Value: typing.Optional[str]


class TTrendParam(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        TrendParamDefID: none
        TrendID: none
        Value: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    TrendParamDefID: 'sqlalchemy.Column[int]'
    TrendID: 'sqlalchemy.Column[int]'
    Value: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, TrendParamDefID: int, TrendID: int, Value: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            TrendParamDefID: none
            TrendID: none
            Value: none

        """
        ...

    @classmethod
    def from_dict(cls, TrendParamDefID: int, TrendID: int, Value: typing.Optional[str] = None) -> "TTrendParam":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            TrendParamDefID: none
            TrendID: none
            Value: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTrendParam":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TrendParamDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


TrendParam: typing.Type[TTrendParam] = models.TrendParam  # type: ignore


class _TrendParamDefDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    ID: int
    TrendDefID: int


class TrendParamDefDict(_TrendParamDefDictBase, total=False):
    """TypedDict for properties that are not required."""

    Name: typing.Optional[str]
    DataType: typing.Optional[str]


class TTrendParamDef(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        ID: none
        TrendDefID: none
        Name: none
        DataType: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    ID: 'sqlalchemy.Column[int]'
    TrendDefID: 'sqlalchemy.Column[int]'
    Name: 'sqlalchemy.Column[typing.Optional[str]]'
    DataType: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, ID: int, TrendDefID: int, Name: typing.Optional[str] = None, DataType: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            ID: none
            TrendDefID: none
            Name: none
            DataType: none

        """
        ...

    @classmethod
    def from_dict(cls, ID: int, TrendDefID: int, Name: typing.Optional[str] = None, DataType: typing.Optional[str] = None) -> "TTrendParamDef":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            ID: none
            TrendDefID: none
            Name: none
            DataType: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTrendParamDef":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TrendParamDefDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


TrendParamDef: typing.Type[TTrendParamDef] = models.TrendParamDef  # type: ignore


class _EventDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    EventID: int
    EventDefID: int
    DeviceID: int
    BeginDate: str
    AppName: str
    DBUser: str
    HostName: str
    SentSMS: bool
    SentEmail: bool


class EventDict(_EventDictBase, total=False):
    """TypedDict for properties that are not required."""

    AckDate: typing.Optional[str]
    EndDate: typing.Optional[str]
    UserAppID: typing.Optional[int]
    ChangeDate: typing.Optional[str]
    AdditionalInfo: typing.Optional[str]


class TEvent(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        EventID: none
        EventDefID: none
        DeviceID: none
        BeginDate: none
        AckDate: none
        EndDate: none
        UserAppID: none
        AppName: none
        DBUser: none
        HostName: none
        ChangeDate: none
        SentSMS: none
        SentEmail: none
        AdditionalInfo: none

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    EventID: 'sqlalchemy.Column[int]'
    EventDefID: 'sqlalchemy.Column[int]'
    DeviceID: 'sqlalchemy.Column[int]'
    BeginDate: 'sqlalchemy.Column[datetime.datetime]'
    AckDate: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    EndDate: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    UserAppID: 'sqlalchemy.Column[typing.Optional[int]]'
    AppName: 'sqlalchemy.Column[str]'
    DBUser: 'sqlalchemy.Column[str]'
    HostName: 'sqlalchemy.Column[str]'
    ChangeDate: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    SentSMS: 'sqlalchemy.Column[bool]'
    SentEmail: 'sqlalchemy.Column[bool]'
    AdditionalInfo: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, EventID: int, EventDefID: int, DeviceID: int, BeginDate: datetime.datetime, AppName: str, DBUser: str, HostName: str, SentSMS: bool, SentEmail: bool, AckDate: typing.Optional[datetime.datetime] = None, EndDate: typing.Optional[datetime.datetime] = None, UserAppID: typing.Optional[int] = None, ChangeDate: typing.Optional[datetime.datetime] = None, AdditionalInfo: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            EventID: none
            EventDefID: none
            DeviceID: none
            BeginDate: none
            AckDate: none
            EndDate: none
            UserAppID: none
            AppName: none
            DBUser: none
            HostName: none
            ChangeDate: none
            SentSMS: none
            SentEmail: none
            AdditionalInfo: none

        """
        ...

    @classmethod
    def from_dict(cls, EventID: int, EventDefID: int, DeviceID: int, BeginDate: datetime.datetime, AppName: str, DBUser: str, HostName: str, SentSMS: bool, SentEmail: bool, AckDate: typing.Optional[datetime.datetime] = None, EndDate: typing.Optional[datetime.datetime] = None, UserAppID: typing.Optional[int] = None, ChangeDate: typing.Optional[datetime.datetime] = None, AdditionalInfo: typing.Optional[str] = None) -> "TEvent":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            EventID: none
            EventDefID: none
            DeviceID: none
            BeginDate: none
            AckDate: none
            EndDate: none
            UserAppID: none
            AppName: none
            DBUser: none
            HostName: none
            ChangeDate: none
            SentSMS: none
            SentEmail: none
            AdditionalInfo: none

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TEvent":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> EventDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Event: typing.Type[TEvent] = models.Event  # type: ignore
