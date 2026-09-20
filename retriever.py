def retrieve_theorem(problem):
    problem = problem.lower()

    with open("theorem_index.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    results = []

    for line in lines:
        theorem, description = line.strip().split("|")
        description_lower = description.lower()

        score = 0

        # AND problems
        if "∧" in problem:
            if "∧" in description:
                score += 10
            else:
                score -= 5

        # OR problems
        if "∨" in problem:
            if "∨" in description:
                score += 10
            else:
                score -= 5

        # IFF problems
        if "↔" in problem:
            if "↔" in description:
                score += 10
            else:
                score -= 5

        # Implication problems
        if "→" in problem:
            if "→" in description or "implication" in description_lower:
                score += 10

        # Modus ponens specifically
        if "prove q" in problem and "p → q" in problem:
            if "modus ponens" in description_lower:
                score += 15

        # Left / right
        if "prove p" in problem and "left" in description_lower:
            score += 10

        if "prove q" in problem and "right" in description_lower:
            score += 10

        if score > 0:
            results.append((score, theorem, description))

    results.sort(reverse=True)

    return results[:3]