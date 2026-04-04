import asyncio
import ollama
from fastmcp import Client


MODEL = "qwen3.5"

client = Client("mcp_server.py")

async def chat():
    async with client:
        mcp_tools = await client.list_tools()
        ollama_tools = [ # Format tools for Ollama
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description or "",
                    "parameters": tool.inputSchema,
                },
            }
            for tool in mcp_tools
        ]

        messages = []
        print("Chat started, type \"/quit\" to exit\n")

        while True: # Take input from user
            user_input = input("You: ").strip()
            if user_input.lower() == "/quit":
                break
            if not user_input:
                continue

            messages.append({"role": "user", "content": user_input})

            while True: # Agentic loop for this turn
                response = ollama.chat(model=MODEL, messages=messages, tools=ollama_tools, think=False)
                messages.append(response.message)

                if not response.message.tool_calls: # No tool calls made
                    break

                for tool_call in response.message.tool_calls: # Run tools calls
                    result = await client.call_tool(
                        tool_call.function.name,
                        dict(tool_call.function.arguments)
                    )
                    messages.append({
                        "role": "tool",
                        "content": result.content[0].text,
                    })
            print(f"Assistant: {response.message.content}\n")
        #print(f"MCP tools: {mcp_tools}")

#asyncio.run(chat())
    

# async def call_post_comment(comment: str):
#     async with client:
#         result = await client.call_tool("post_comment", {"comment": comment})
#         print(result.content[0].text)

# asyncio.run(call_post_comment("This is a comment from the client!"))