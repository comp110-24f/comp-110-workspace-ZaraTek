def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    # base case 1 - a dog did not meet threshold
    if int(scores[idx]["score"]) < thresh:
        return False
    # base case 2 - reached end of list, every dog met threshold
    if idx == len(scores) - 1:
        return True
    # recursive case - call fn with idx incremented
    else:
        return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]
print(all_good(scores=pack, thresh=7, idx=0))
print(all_good(scores=pack, thresh=8, idx=0))
