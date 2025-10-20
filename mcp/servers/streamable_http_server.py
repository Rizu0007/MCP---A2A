from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel , Field


class ArithmeticInput(BaseModel):
    a: float = Field(..., description="first number ")
    b: float = Field(..., description="second number")


class ArithmeticOutput(BaseModel):
    result: float = Field(..., description="result of the arithmetic operation")
    expression: str = Field(..., description="string representation of the operation performed")