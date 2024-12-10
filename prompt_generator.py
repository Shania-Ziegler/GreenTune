
import json

class PromptGenerator:
    def __init__(self, app_params, system_params):
        self.app_params = app_params
        self.system_params = system_params

    def generate_prompt(self, previous_params, previous_performance):
        prompt = (
            "You are an expert system tuner. Based on the previous FFmpeg parameters and performance metrics, "
            "suggest new parameter values to optimize both execution time and energy consumption. "
            "Balance reducing energy usage while maintaining or improving execution time.\n\n"
            f"Previous Application Parameters:\n{json.dumps(previous_params.get('app_params', {}), indent=2)}\n"
            f"Previous System Parameters:\n{json.dumps(previous_params.get('system_params', {}), indent=2)}\n"
            f"Previous Performance Metrics:\n"
            f"Execution Time: {previous_performance.get('execution_time', 'N/A')} seconds\n"
            f"Energy Consumption: {previous_performance.get('energy_consumption', 'N/A')} joules\n\n"
            "Available Application Parameters to Tune:\n"
            f"{json.dumps(self.app_params, indent=2)}\n\n"
            "Available System Parameters to Tune:\n"
            f"{json.dumps(self.system_params, indent=2)}\n\n"
            "Suggest new configurations that optimize for both metrics."
        )
        return prompt
