# from openai import OpenAI
# from rich.console import Console
# from rich.panel import Panel
# from rich.spinner import Spinner
# from rich.prompt import Prompt
# from rich.status import Status
# import subprocess
# from rich import print as rprint
# import json 
# import ast
# import os

# """
# Here is the general flow:

# 1. User enters an objective
# 2. Brybot breaks goal down into steps, each consisting of a terminal command.
# 4. For each step, Brybot asks for confirmation to run the command on a subprocess.
# 5. Brybot runs the command.
# - 4.1 If the command fails, Brybot stops and reports the error.
# - 4.2 If the command succeeds, Brybot moves on to the next step.
# 5. Brybot repeats this process until all steps are completed or the user stops the process.

# """




# class BryBot:
#     def __init__(self, api_key):
#         self.client = OpenAI(
#             organization='org-sFsNcKYiRz6GM7yvA2UBG3uQ',
#             project='proj_kTb24nqx1zFjTWLpVJFG0AjA',
#             api_key=api_key
#         )
#         self.model="gpt-4"
#         self.messages = []
#         self.objective = None

#         self.console = Console()

#     def get_user_request(self) -> str:

#         try:
#             self.console.print(
#                 Panel("[bold cyan]\nHi! I'm BryBot, Bryan's terminal assistant\n[/]", subtitle="Press Ctrl+C to exit"
#                       ))

#             user_request = Prompt.ask(
#                 "\n[bold green]What can I help you with?[/]",
#                 console=self.console
#             )

#             return user_request
        
#         except Exception as e:
#             print(f"Error: {e}")

#     # Calls GPT-4o to parse the user request
#     # Returns a list of broken-down commands for completing the objective
#     def parse_user_request(self, user_request) -> list:

#         # System prompt for breaking down goals 
#         system_instruction = """You are BryBot, a terminal command expert. Convert user requests into step-by-step, human-readable instructions.

#         Rules:
#         - Your response must be a valid Python list of strings.
#         - Each step should consist of a short description of that step.
#         - Use macOS terminal commands.
#         - Keep explanations minimal.

#         Examples:

#         Q: How do I commit my changes?
#         A:
#         [
#             "git add .",
#             "git commit -m 'your message'",
#             "git push origin main"
#         ]

#         Q: How do I check the current directory?
#         A:
#         [
#             "pwd",
#             "ls -la"
#         ]

#         Q: Create a new directory and add a file to it.
#         A:
#         [
#             "mkdir new_folder",
#             "cd new_folder",
#         ]
#         """

#         # Break down the user request into steps
#         response = self.client.chat.completions.create(
#             model=self.model,
#             messages=[
#                 {"role": "system", "content": system_instruction},
#                 {"role": "user", "content": f"{user_request}"}
#             ]
#         )

#         self.objective = user_request
#         response = response.choices[0].message.content

#         # Convert to list    
#         try:
#             command_list = ast.literal_eval(response.strip())
#         except Exception as e:
#             raise ValueError("Invalid response from GPT-4")

#         for i, cmd in enumerate(command_list, 1):
#             rprint(f"[bold blue]{i}. [white]{cmd}[/]")
        
#         return command_list
    
#     def confirm_command(self, command) -> bool:

#         rprint(f"\n[bold yellow]Command:[/] {command}")
#         confirm = Prompt.ask("Run this command?", choices=["y", "n"], console=self.console)
#         return confirm.strip().lower() == "y"

#     def execute_command(self, command) -> tuple:
#         try:
#             result = subprocess.run(
#                 command,
#                 shell=True,
#                 capture_output=True,
#                 text=True
#             )
            
#             if result.returncode == 0:
#                 rprint(f"[green]Success![/] {result.stdout}")
#                 return (True, result.stdout)
                
#             else:
#                 rprint(f"[red]Error:[/] {result.stderr}")
#                 return (False, result.stderr)
#         except Exception as e:
#             rprint(f"[red]Error:[/] {str(e)}")
#             return (False, str(e))

        

#     # Executes command
#     # If fail, query GPT for a solution w/ command and error message and retry
#     # If fails x3, break and report error
#     def pursue_objective(self, command) -> bool:

#         # Define 
#         self.messages.append({"role": "system", "content": f'You are BryBot, a terminal command expert. Your goal is to accomplish this task: "{self.objective}" using terminal commands. '})

        
#         try:
#             success = False

#             # Repeat until the command successfully executes
#             while not success:
#                 success, message = self.execute_command(command)

#                 if not success:
#                     response = self.client.chat.completions.create(
#                         model=self.model,
#                         messages=self.messages.append(
#                             {"role": "system", "content": f"Command: <{command}> Error message: {message}"}
#                         )
#                     )



                    
#         except Exception as e:
#             self.console.print(f"[red]Error:[/] {str(e)}")

#     def run(self):


#         loop = True
#         while loop:
#             try:
#                 request = self.get_user_request()

#                 commands = self.parse_user_request(request)
#                 for command in commands:

#                     # User doesn't confirm command
#                     if not self.confirm_command(command):
#                         loop = False
#                         break

#                     self.pursue_objective(command)

#             except KeyboardInterrupt:
#                 print('\nExiting...')
#                 break
#             except Exception as e:
#                 print(f"Error: {e}")

    
# if __name__ == '__main__':
#     with open('secrets.json') as f:
#         api_key = json.load(f)['api_key']
#     bot = BryBot(api_key=api_key)
#     bot.run()



