
# GreenTune: LLM-Based Hardware-Software Parameter Autotuning of HPC Applications to Improve Performance and Energy Consumption

GreenTune is an autotuner for optimizing hardware and software parameters of large-scale high-performance computing (HPC) applications. Leveraging OpenAI's GPT-4 language model, GreenTune iteratively refines parameter configurations to balance execution time and energy consumption, enabling sustainable and efficient computing.

## Key Features

- **Energy-Aware Optimization**: GreenTune integrates energy consumption as a key metric alongside execution time, making it ideal for environmentally conscious HPC applications.
- **LLM-Driven Tuning**: Utilizes state-of-the-art language models to generate optimized parameter configurations based on performance feedback.
- **Customizable Parameters**: Supports tuning for a wide range of hardware and software configurations.
- **Iterative Refinement**: Continuously improves performance metrics over multiple iterations.

## System Overview

GreenTune consists of the following modules:

- **Prompt Generator**: Generates optimization prompts for the LLM, incorporating both energy and execution time metrics.
- **Option Evaluator**: Parses LLM responses to extract new parameter configurations.
- **Performance Analyzer**: Measures execution time and energy consumption for given configurations.
- **Safety Enforcer**: Ensures generated parameters are within safe and valid bounds.

## Usage

1. Set up your environment by configuring the necessary parameters in `config.py`.
2. Run the main script using the command:

   ```bash
   python main.py
   ```

3. Monitor the iterative optimization process, which outputs the best configurations based on execution time and energy consumption.

## Prerequisites

- Python 3.8 or higher
- Access to OpenAI GPT-4 API
- Intel RAPL support for energy measurement (optional but recommended)

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/greentune.git
cd greentune
python3 main.py
```

## Future Work

GreenTune aims to integrate support for additional energy measurement tools and expand to other domains beyond HPC applications.
