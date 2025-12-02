from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add(a:int, b:int) -> int:
    """Add two numbers a, b and return the result

    Args:
        a (int): a number
        b (int): a number

    Returns:
        int: result
    """
    return a + b