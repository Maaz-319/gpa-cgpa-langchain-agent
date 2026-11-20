import os

def get_config(chat):
    return {"configurable": {"thread_id": chat}}

def init_scr():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print("          AI CHAT")
    print("=" * 40)
    print("Commands: \n\t- /clear (screen ki safai)\n\t- /exit (Agent band karo)\n\t- /switch (Naya Aghaz)\n\t- /history (chat history dekho)\n\t- /forget (current chat bhool jao)\n\t- /mcp (saray mcp tools)\n\t- /help (ye menu dispay karo)")
    print("")

def switch_chat():
    name = ""
    while not name:
        name = input("Enter Chat Name: ").strip()
    return name

def display_mcp_tools(tools, MCP_SERVER_URL):
    print("\nMCP servers and tools:")
    print(f"{MCP_SERVER_URL}")
    if tools:
        for tool in tools:
            print(f"  - {tool.name}")
    else:
        print("  No tools found.")
    print()

async def list_threads(memory):
    threads = set()
    async for checkpoint in memory.alist(None):
        thread_id = checkpoint.config.get("configurable", {}).get("thread_id")
        if thread_id:
            threads.add(thread_id)

    print("Saved chats:")
    if threads:
        for thread in sorted(threads):
            print(f"  - {thread}")
    else:
        print("  No saved chats.")
    print()

async def show_history(agent, config):
    state = await agent.aget_state(config)
    messages = state.values.get("messages", [])

    print("\nChat history:")
    if not messages:
        print("  No messages in this chat.\n")
        return

    for message in messages:
        role = "You" if message.type == "human" else "Mr. Agent"
        if message.type == "tool":
            continue
        content = message.content
        if isinstance(content, list):
            content = " ".join(
                item.get("text", str(item)) if isinstance(item, dict) else str(item)
                for item in content
            )
        print(f"{role}: {content}")
    print()
