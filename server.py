from fastmcp import FastMCP
from tools import TOOLS

mcp = FastMCP("cgpa-cal")
for tool in TOOLS:
    mcp.tool(tool)

if __name__ == "__main__":
    mcp.run()