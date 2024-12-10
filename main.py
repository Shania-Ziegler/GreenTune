
import openai
import os
from prompt_generator import PromptGenerator
from option_evaluator import OptionEvaluator
from performance_analyzer import PerformanceAnalyzer
from safety_enforcer import SafetyEnforcer
import config

def main():
    openai.api_key = config.OPENAI_API_KEY or os.getenv('OPENAI_API_KEY')

    prompt_generator = PromptGenerator(config.APP_COMPILER_FLAGS, config.SYSTEM_PARAMS)
    safety_enforcer = SafetyEnforcer(config.PARAM_BLACKLIST, config.APP_COMPILER_FLAGS, config.SYSTEM_PARAMS)
    option_evaluator = OptionEvaluator(safety_enforcer)
    performance_analyzer = PerformanceAnalyzer()

    previous_params = {}
    previous_performance = {}
    best_performance = None
    best_params = None

    for iteration in range(config.MAX_ITERATIONS):
        print(f"Iteration {iteration + 1}")

        # Generate prompt
        prompt = prompt_generator.generate_prompt(previous_params, previous_performance)

        # Get response from LLM
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )

        # Parse new parameter values
        new_params = option_evaluator.parse_response(response.choices[0].text)

        # Evaluate performance
        execution_time, energy_consumption = performance_analyzer.compile_ffmpeg(new_params['app_params'])

        if execution_time is not None and energy_consumption is not None:
            print(f"Execution Time: {execution_time} seconds")
            print(f"Energy Consumption: {energy_consumption} joules")

            # Update performance metrics
            current_performance = {
                'execution_time': execution_time,
                'energy_consumption': energy_consumption
            }

            # Check if this is the best performance so far
            if best_performance is None or (
                current_performance['execution_time'] < best_performance['execution_time'] and
                current_performance['energy_consumption'] < best_performance['energy_consumption']
            ):
                best_performance = current_performance
                best_params = new_params

            previous_params = new_params
            previous_performance = current_performance

    print("Optimization Complete!")
    print(f"Best Performance: {best_performance}")
    print(f"Best Parameters: {best_params}")

if __name__ == "__main__":
    main()
