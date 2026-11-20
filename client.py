import asyncio
from dotenv import load_dotenv
from os import getenv

from langchain.mcp import MCPAdapter
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from langchain.messages import HumanMessage, ToolMessage

from llm import llm
from langchain.agents import create_agent
from prompt import SYSTEM_PROMPT
import utils

load_dotenv()

MCP_SERVER_URL = getenv("MCP_SERVER_URL")

async def main():
    async with AsyncSqliteSaver.from_conn_string("chats.db") as memory:
        async with MCPAdapter(MCP_SERVER_URL) as adapter:
            tools = await adapter.list_tools()
            agent = create_agent(llm, tools=tools, system_prompt=SYSTEM_PROMPT, checkpointer=memory)

            utils.init_scr()
            utils.display_mcp_tools(tools, MCP_SERVER_URL)
            await utils.list_threads(memory)
            CHAT = utils.switch_chat()
            config = utils.get_config(CHAT)

            while True:
                try:
                    user_input = input("You: ").strip()

                    if user_input == "/exit":
                        break

                    if user_input == "/clear":
                        utils.init_scr()
                        continue

                    if user_input == "/mcp":
                        utils.display_mcp_tools(tools, MCP_SERVER_URL)
                        continue

                    if user_input == "/switch":
                        CHAT = utils.switch_chat()
                        config = utils.get_config(CHAT)
                        continue

                    if user_input == "/history":
                        await utils.show_history(agent, config)
                        continue

                    if user_input == "/forget":
                        await memory.adelete_thread(CHAT)
                        print(f"Chat '{CHAT}' forgotten.\n")
                        continue

                    if user_input == "/help":
                        utils.init_scr()
                        continue

                    if not user_input:
                        continue

                    try:
                        print("\nMr. Agent: ", end="", flush=True)

                        async for chunk in agent.astream(
                            {"messages": [HumanMessage(content=user_input)]},
                            config,
                            stream_mode=["updates", "messages"],
                            version="v2"):
                            if chunk["type"] == "messages":
                                token, metadata = chunk["data"]

                                if metadata["langgraph_node"] == "model" and token.text:
                                    print(token.text, end="", flush=True)

                            elif chunk["type"] == "updates":
                                for node, update in chunk["data"].items():
                                    msg = update["messages"][-1]

                                    if node == "model" and msg.tool_calls:
                                        print()
                                        for call in msg.tool_calls:
                                            print(f"\t• [Called {call['name']}: {call['args']}]")
                                        print()

                                    # elif node == "tools":
                                    #     print(f"\n[Tool {msg.name}: {msg.content}]")

                        print("\n" + "-" * 40 + "\n")

                    except Exception as e:
                        print("\nKuch to ghalat hua hai.")
                        print(e)
                        try:
                            state = await agent.aget_state(config)
                            messages = state.values.get("messages", [])
                            if messages and getattr(messages[-1], "tool_calls", None):
                                await agent.aupdate_state(
                                    config,
                                    {
                                        "messages": [
                                            ToolMessage(
                                                content="MCP tool failed. Tell the user it could not complete and they can try again later.",
                                                tool_call_id=call["id"],
                                            )
                                            for call in messages[-1].tool_calls
                                        ]
                                    },
                                )
                        except Exception as err:
                            print("Tool call sai nahi hoski:", err)

                except (KeyboardInterrupt, EOFError):
                    break

            print("\nBye, Bhai!")

asyncio.run(main())
