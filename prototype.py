from openai import OpenAI
import subprocess
from retriever import retrieve_theorem

client = OpenAI()


problem = """
Given h : P ∧ Q, prove P.
"""

problem = """
Given h : P ∧ Q, prove Q.
"""

problem = """
Given h1 : P → Q and h2 : P, prove Q.
"""

results = retrieve_theorem(problem)

retrieval_hint = ""

for score, theorem, description in results:
    retrieval_hint += f"{theorem} - {description}\n"

print("\nRetrieved theorems:")
print(retrieval_hint)


MAX_RETRIES = 3

response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
Solve this Lean 4 problem:

{problem}

Useful retrieved information:
{retrieval_hint}

Return a complete Lean 4 theorem.
Return only the Lean code.
"""
)

lean_code = response.output_text

for attempt in range(1, MAX_RETRIES + 1):

    print(f"\nAttempt {attempt}")

    with open("generated.lean", "w", encoding="utf-8") as file:
        file.write(lean_code)

    result = subprocess.run(
        ["lake", "env", "lean", "generated.lean"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("PASS - Lean proof is valid!")
        print(lean_code)
        break

    print("FAIL - Lean proof has an error!")
    print(result.stderr)

    if attempt == MAX_RETRIES:
        print("Maximum retries reached.")
        break

    retry_prompt = f"""
Fix this Lean 4 proof.

Problem:
{problem}

Current Lean code:
{lean_code}

Lean error:
{result.stderr}

Return only the corrected complete Lean code.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=retry_prompt
    )

    lean_code = response.output_text