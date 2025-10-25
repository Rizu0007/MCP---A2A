import asyncio
import logging
import signal
import sys
from contextlib import asynccontextmanager
from utilities.mcp.mcp_discovery import MCPDiscovery
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from mcp import StdioServerParameters


class MCPConnect:
    """
      Discovers the MCP servers from the config.
      Config will be loaded by the MCP discovery class
      Then it lists each server's tools
      and then caches them as MCPToolsets that are compatible with 
      Google's Agent Development Kit
    """
    
    def __init__(self , config_file , str=None):
        self.discovery = MCPDiscovery(config_file=config_file)
        self.tool:list[MCPToolset] =[]
        
        
    async  def _load_all_tools(self):
        """
          Loads all the tools from each discovered MCP server
        """
        tools=[]
        try:
             for name , server in self.discovery.list_servers().item():
                if server.get("command") == "streamable_http":
                    con=StreamableHTTPServerParams(url=server["arg"][0])
                else:
                    conn = StdioConnectionParams(
                    server_params=StdioServerParameters(
                        command=server["command"],
                        args=server["args"]
                    ),
                    timeout=5
                    )
                    
                    
                    
                    toolset = MCPToolset(connection_params=conn)
                    tools=await toolset.load_tools()
                    tool_names = [tool.name for tool in toolset]
                    print(f"[bold green]Loaded tools from server [cyan]'{name}'[/cyan]:[/bold green] {', '.join(tool_names)}")
                    tools.append(toolset)
            
        except Exception as e:
            print(f"[bold red]Error loading tools from server [cyan]'{name}'[/cyan]: {e}[/bold red]")
            return tools
        
    def get_tools(self)->list[MCPToolset]:
        
        return self.tool.copy()
    