from config import CREATE_DOCKER, GUIDELINES, HIERARCHY, SINGLEFILE, WRITE_CODE
from utils import llm_write_file, prompt_constructor


def create_environment(globals):
    """Create Dockerfile"""

    docker_prompt_template = prompt_constructor(HIERARCHY, GUIDELINES, WRITE_CODE, CREATE_DOCKER, SINGLEFILE)

    prompt = docker_prompt_template.format(
        targetlang=globals.targetlang,
        sourcelang=globals.sourcelang,
        sourceentry=globals.sourceentry,
        guidelines=globals.guidelines,
    )

    llm_write_file(
        prompt,
        target_path="Dockerfile",
        waiting_message="Creating your environment...",
        success_message=f"Created Docker environment for {globals.targetlang} project in directory '{globals.targetdir}'.",
        globals=globals,
    )

    with open("memory/external_dependencies", "w") as file:
        file.write("")
