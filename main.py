import asyncio

from semantic_kernel import Kernel
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.functions import kernel_function
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions.kernel_arguments import KernelArguments

from plugins import userInitPlugin;

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings)

async def main():
    kernel = Kernel();    

    chat_completion = AzureChatCompletion(
            deployment_name="gpt-4o-mini",
            api_key="xxx",
            base_url="xxx",
    )
    kernel.add_service(chat_completion)
    
    # location -> your in korea
    # plugin (korea) -> location -> korea
    kernel.add_plugin(
        userInitPlugin(),
        plugin_name="userInit",
    )
    
    execution_settings = AzureChatPromptExecutionSettings()
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
    
    history = ChatHistory()
    
    userInput = None
    while True:
        userInput = input("User > ")
        
        if userInput == "exit":
            break
        
        history.add_user_message(userInput)
        
        result = await chat_completion.get_chat_message_content(
            chat_history=history,
            settings=execution_settings,
            kernel=kernel
        )
        
        print("Bot >", str(result))     
        history.add_message(result)

if __name__ == "__main__":
    asyncio.run(main())
