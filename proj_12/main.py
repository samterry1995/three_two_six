__author__ = "Katelyn Harlan (4437710), Taya Nicholas (5926161), Samuel Terry (6786350)"

num_of_pegs = 20
only_leaf_states = True
starting_positions_set = set()


def main():
    start = "00100"
    generate_previous(start)

    leaf_peg_states = []
    for position in starting_positions_set:
        if position.count("1") == num_of_pegs:
            leaf_peg_states.append(position)

    set_no_mirrors = set()
    # Note the final part of the list comprehension returns None (so is evaluated to true)
    # But it also calls the function.
    [state for state in leaf_peg_states if state[::-1]
     not in set_no_mirrors and not set_no_mirrors.add(state)]

    if only_leaf_states:
        i = 0
        for final_peg_states in set_no_mirrors:
            print(f"{i} - {final_peg_states}")
            i += 1
    return set_no_mirrors


def generate_previous(current_state: list):
    if (current_state.count("1") > num_of_pegs - 1):
        return
    if not (current_state[0] == "0" and current_state[1] == "0"):
        current_state = "00" + current_state
    pattern_indicies = find_open_pattern(current_state)
    for i in pattern_indicies:
        new_state = undo_move(current_state, i)
        clean_state = get_cleaned_position(new_state)
        if clean_state in starting_positions_set:
            continue
        starting_positions_set.add(clean_state)
        generate_previous(new_state)
        generate_previous(new_state[::-1])


def get_cleaned_position(new_state: str) -> str:
    return new_state.strip('0')


def undo_move(current_state: str, i: int) -> str:
    return current_state[:i] + "110" + current_state[i+3:]


def find_open_pattern(current_state: list) -> list:
    pattern_indicies = []
    for i in range(len(current_state[:-3])):
        if current_state[i] == "0" and current_state[i+1] == "0" and current_state[i+2] == "1":
            pattern_indicies.append(i)
    return pattern_indicies


if __name__ == "__main__":
    main()
