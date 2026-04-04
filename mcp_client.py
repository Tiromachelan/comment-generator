import asyncio
import ollama
from fastmcp import Client


MODEL = "gemma4"

client = Client("mcp_server.py")

async def call_post_comment(comment: str):
    async with client:
        result = await client.call_tool("post_comment", {"comment": comment})
        print(result.content[0].text)

asyncio.run(call_post_comment("This is a comment from the client!"))