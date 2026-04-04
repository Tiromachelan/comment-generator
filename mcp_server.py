from fastmcp import FastMCP


mcp = FastMCP("Comment Poster")

@mcp.tool
def post_comment(comment: str):
    return f"Posting comment: {comment}"

if __name__ == "__main__":
    mcp.run()